import time
import pandas as pd
import duckdb
import polars as pl

CSV_FILE = "data/sales_100k.csv"


def benchmark(name, function):
    start = time.perf_counter()
    result = function()
    end = time.perf_counter()

    elapsed = end - start

    print(f"{name:<35} {elapsed:.6f} seconds")

    return result, elapsed


print("W5D3 - Pandas vs DuckDB vs Polars Benchmark")
print("=" * 60)


# --------------------------------------------------
# Load data
# --------------------------------------------------

pandas_df = pd.read_csv(CSV_FILE)
polars_df = pl.read_csv(CSV_FILE)

duckdb_con = duckdb.connect()


# --------------------------------------------------
# Pandas operations
# --------------------------------------------------

print("\nPANDAS")
print("-" * 60)

pandas_times = []

_, t = benchmark(
    "1. Total Rows",
    lambda: len(pandas_df)
)
pandas_times.append(t)

_, t = benchmark(
    "2. Average Order Amount",
    lambda: pandas_df["amount"].mean()
)
pandas_times.append(t)

_, t = benchmark(
    "3. Orders by Category",
    lambda: pandas_df.groupby("category").size()
)
pandas_times.append(t)

_, t = benchmark(
    "4. Total Sales by Region",
    lambda: pandas_df.groupby("region")["amount"].sum()
)
pandas_times.append(t)

_, t = benchmark(
    "5. Top 10 Orders",
    lambda: pandas_df.nlargest(10, "amount")
)
pandas_times.append(t)


# --------------------------------------------------
# DuckDB operations
# --------------------------------------------------

print("\nDUCKDB")
print("-" * 60)

duckdb_times = []

_, t = benchmark(
    "1. Total Rows",
    lambda: duckdb_con.execute(
        f"SELECT COUNT(*) FROM read_csv_auto('{CSV_FILE}')"
    ).fetchone()
)
duckdb_times.append(t)

_, t = benchmark(
    "2. Average Order Amount",
    lambda: duckdb_con.execute(
        f"SELECT AVG(amount) FROM read_csv_auto('{CSV_FILE}')"
    ).fetchone()
)
duckdb_times.append(t)

_, t = benchmark(
    "3. Orders by Category",
    lambda: duckdb_con.execute(
        f"""
        SELECT category, COUNT(*)
        FROM read_csv_auto('{CSV_FILE}')
        GROUP BY category
        """
    ).fetchall()
)
duckdb_times.append(t)

_, t = benchmark(
    "4. Total Sales by Region",
    lambda: duckdb_con.execute(
        f"""
        SELECT region, SUM(amount)
        FROM read_csv_auto('{CSV_FILE}')
        GROUP BY region
        """
    ).fetchall()
)
duckdb_times.append(t)

_, t = benchmark(
    "5. Top 10 Orders",
    lambda: duckdb_con.execute(
        f"""
        SELECT order_id, category, region, amount
        FROM read_csv_auto('{CSV_FILE}')
        ORDER BY amount DESC
        LIMIT 10
        """
    ).fetchall()
)
duckdb_times.append(t)


# --------------------------------------------------
# Polars operations
# --------------------------------------------------

print("\nPOLARS")
print("-" * 60)

polars_times = []

_, t = benchmark(
    "1. Total Rows",
    lambda: polars_df.height
)
polars_times.append(t)

_, t = benchmark(
    "2. Average Order Amount",
    lambda: polars_df.select(
        pl.col("amount").mean()
    )
)
polars_times.append(t)

_, t = benchmark(
    "3. Orders by Category",
    lambda: polars_df.group_by("category").len()
)
polars_times.append(t)

_, t = benchmark(
    "4. Total Sales by Region",
    lambda: polars_df.group_by("region").agg(
        pl.col("amount").sum()
    )
)
polars_times.append(t)

_, t = benchmark(
    "5. Top 10 Orders",
    lambda: polars_df.sort(
        "amount",
        descending=True
    ).head(10)
)
polars_times.append(t)


# --------------------------------------------------
# Summary
# --------------------------------------------------

print("\n" + "=" * 60)
print("BENCHMARK SUMMARY")
print("=" * 60)

print(f"{'Operation':<25} {'Pandas':>12} {'DuckDB':>12} {'Polars':>12}")
print("-" * 65)

operations = [
    "Total Rows",
    "Average Amount",
    "Orders by Category",
    "Sales by Region",
    "Top 10 Orders"
]

for i, operation in enumerate(operations):
    print(
        f"{operation:<25} "
        f"{pandas_times[i]:>12.6f} "
        f"{duckdb_times[i]:>12.6f} "
        f"{polars_times[i]:>12.6f}"
    )


duckdb_con.close()