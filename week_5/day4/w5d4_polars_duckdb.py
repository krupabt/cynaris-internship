import time
import pandas as pd
import duckdb
import polars as pl

CSV_FILE = "sales_100k.csv"

# Load dataset
df_pandas = pd.read_csv(CSV_FILE)

print("Rows loaded:", len(df_pandas))


# -----------------------------
# DuckDB - 5 analytical queries
# -----------------------------
con = duckdb.connect()

duckdb_times = []

queries = [
    """
    SELECT category, SUM(sales) AS total_sales
    FROM read_csv_auto('sales_100k.csv')
    GROUP BY category
    ORDER BY total_sales DESC
    """,
    """
    SELECT category, AVG(sales) AS average_sales
    FROM read_csv_auto('sales_100k.csv')
    GROUP BY category
    """,
    """
    SELECT region, SUM(sales) AS total_sales
    FROM read_csv_auto('sales_100k.csv')
    GROUP BY region
    ORDER BY total_sales DESC
    """,
    """
    SELECT category, COUNT(*) AS transaction_count
    FROM read_csv_auto('sales_100k.csv')
    GROUP BY category
    """,
    """
    SELECT region, SUM(profit) AS total_profit
    FROM read_csv_auto('sales_100k.csv')
    GROUP BY region
    ORDER BY total_profit DESC
    """
]

print("\n--- DuckDB ---")

for i, query in enumerate(queries, 1):
    start = time.perf_counter()
    result = con.execute(query).fetchdf()
    elapsed = time.perf_counter() - start

    duckdb_times.append(elapsed)

    print(f"\nQuery {i}: {elapsed:.4f} seconds")
    print(result)


# -----------------------------
# Pandas - same operations
# -----------------------------
pandas_times = []

operations = [
    lambda: df_pandas.groupby("category")["sales"].sum(),
    lambda: df_pandas.groupby("category")["sales"].mean(),
    lambda: df_pandas.groupby("region")["sales"].sum(),
    lambda: df_pandas.groupby("category").size(),
    lambda: df_pandas.groupby("region")["profit"].sum()
]

print("\n--- Pandas ---")

for i, operation in enumerate(operations, 1):
    start = time.perf_counter()
    operation()
    elapsed = time.perf_counter() - start

    pandas_times.append(elapsed)
    print(f"Query {i}: {elapsed:.4f} seconds")


# -----------------------------
# Polars
# -----------------------------
print("\n--- Polars ---")

df_polars = pl.read_csv(CSV_FILE)

polars_times = []

operations = [
    lambda: df_polars.group_by("category").agg(
        pl.col("sales").sum()
    ),
    lambda: df_polars.group_by("category").agg(
        pl.col("sales").mean()
    ),
    lambda: df_polars.group_by("region").agg(
        pl.col("sales").sum()
    ),
    lambda: df_polars.group_by("category").agg(
        pl.len()
    ),
    lambda: df_polars.group_by("region").agg(
        pl.col("profit").sum()
    )
]

for i, operation in enumerate(operations, 1):
    start = time.perf_counter()
    operation()
    elapsed = time.perf_counter() - start

    polars_times.append(elapsed)
    print(f"Query {i}: {elapsed:.4f} seconds")


# -----------------------------
# Comparison
# -----------------------------
comparison = pd.DataFrame({
    "Operation": [
        "Category SUM sales",
        "Category AVG sales",
        "Region SUM sales",
        "Category COUNT",
        "Region SUM profit"
    ],
    "Pandas": pandas_times,
    "DuckDB": duckdb_times,
    "Polars": polars_times
})

print("\n--- Performance Comparison ---")
print(comparison.to_string(index=False))

comparison.to_csv("w5d4_benchmark_results.csv", index=False)

con.close()

print("\nW5D4 completed successfully!")