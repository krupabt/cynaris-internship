import polars as pl

CSV_FILE = "data/sales_100k.csv"

print("W5D3 - Polars Analytics")
print("=" * 50)

# Load CSV
df = pl.read_csv(CSV_FILE)

print(f"\nDataset loaded: {df.height} rows")


# Query 1: Count total rows
print("\n1. Total Rows")
print(df.height)


# Query 2: Average order amount
result = df.select(
    pl.col("amount").mean().round(2)
)

print("\n2. Average Order Amount")
print(result)


# Query 3: Orders by category
result = (
    df.group_by("category")
    .len()
    .sort("len", descending=True)
)

print("\n3. Orders by Category")
print(result)


# Query 4: Total sales by region
result = (
    df.group_by("region")
    .agg(
        pl.col("amount").sum().round(2).alias("total_sales")
    )
    .sort("total_sales", descending=True)
)

print("\n4. Total Sales by Region")
print(result)


# Query 5: Top 10 orders by amount
result = (
    df.sort("amount", descending=True)
    .select(["order_id", "category", "region", "amount"])
    .head(10)
)

print("\n5. Top 10 Orders by Amount")
print(result)