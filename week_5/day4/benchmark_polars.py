import time
import polars as pl

CSV_FILE = "sales_100k.csv"

print("W5D4 - Polars Performance Benchmark")
print("=" * 60)

# Load dataset
start = time.perf_counter()

df = pl.read_csv(CSV_FILE)

load_time = time.perf_counter() - start

print(f"\nDataset loading time: {load_time:.6f} seconds")


# 1. Filter high-value orders
start = time.perf_counter()

df.filter(
    pl.col("amount") > 40000
)

filter_time = time.perf_counter() - start

print(f"1. Filter high-value orders: {filter_time:.6f} seconds")


# 2. Create calculated column
start = time.perf_counter()

df.with_columns(
    pl.when(pl.col("amount") >= 25000)
    .then(pl.lit("High"))
    .otherwise(pl.lit("Normal"))
    .alias("revenue_category")
)

column_time = time.perf_counter() - start

print(f"2. Create calculated column: {column_time:.6f} seconds")


# 3. Group by category
start = time.perf_counter()

df.group_by("category").agg(
    pl.col("amount").sum().alias("total_sales"),
    pl.col("amount").mean().alias("average_sales"),
    pl.len().alias("order_count")
)

category_time = time.perf_counter() - start

print(f"3. Group by category: {category_time:.6f} seconds")


# 4. Group by region
start = time.perf_counter()

df.group_by("region").agg(
    pl.col("amount").sum().alias("total_sales"),
    pl.col("quantity").sum().alias("total_quantity")
)

region_time = time.perf_counter() - start

print(f"4. Group by region: {region_time:.6f} seconds")


# 5. Top 10 orders
start = time.perf_counter()

df.sort(
    "amount",
    descending=True
).head(10)

top10_time = time.perf_counter() - start

print(f"5. Top 10 orders: {top10_time:.6f} seconds")


print("\n" + "=" * 60)
print("Benchmark completed successfully.")