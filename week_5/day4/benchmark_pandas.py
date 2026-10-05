import time
import pandas as pd

CSV_FILE = "sales_100k.csv"

print("W5D4 - Pandas Performance Benchmark")
print("=" * 60)

# Load dataset
start = time.perf_counter()

df = pd.read_csv(CSV_FILE)

load_time = time.perf_counter() - start

print(f"\nDataset loading time: {load_time:.6f} seconds")


# 1. Filter high-value orders
start = time.perf_counter()

df[df["amount"] > 40000]

filter_time = time.perf_counter() - start

print(f"1. Filter high-value orders: {filter_time:.6f} seconds")


# 2. Create calculated column
start = time.perf_counter()

df["revenue_category"] = df["amount"].apply(
    lambda x: "High" if x >= 25000 else "Normal"
)

column_time = time.perf_counter() - start

print(f"2. Create calculated column: {column_time:.6f} seconds")


# 3. Group by category
start = time.perf_counter()

df.groupby("category").agg(
    total_sales=("amount", "sum"),
    average_sales=("amount", "mean"),
    order_count=("amount", "count")
)

category_time = time.perf_counter() - start

print(f"3. Group by category: {category_time:.6f} seconds")


# 4. Group by region
start = time.perf_counter()

df.groupby("region").agg(
    total_sales=("amount", "sum"),
    total_quantity=("quantity", "sum")
)

region_time = time.perf_counter() - start

print(f"4. Group by region: {region_time:.6f} seconds")


# 5. Top 10 orders
start = time.perf_counter()

df.sort_values(
    "amount",
    ascending=False
).head(10)

top10_time = time.perf_counter() - start

print(f"5. Top 10 orders: {top10_time:.6f} seconds")


print("\n" + "=" * 60)
print("Benchmark completed successfully.")