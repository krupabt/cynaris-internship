import polars as pl

CSV_FILE = "sales_100k.csv"

print("W5D4 - Polars High-Performance DataFrame Operations")
print("=" * 60)

# Load dataset
df = pl.read_csv(CSV_FILE)

print("\nDataset loaded successfully")
print("Rows:", df.height)
print("Columns:", df.columns)


# 1. Filter high-value orders
print("\n1. High-Value Orders")

high_value_orders = df.filter(
    pl.col("amount") > 40000
)

print(high_value_orders.head(5))


# 2. Create a calculated column
print("\n2. Revenue Category")

df_with_category = df.with_columns(
    pl.when(pl.col("amount") >= 25000)
    .then(pl.lit("High"))
    .otherwise(pl.lit("Normal"))
    .alias("revenue_category")
)

print(
    df_with_category
    .select([
        "order_id",
        "amount",
        "revenue_category"
    ])
    .head(5)
)


# 3. Group by category
print("\n3. Sales by Category")

category_sales = (
    df.group_by("category")
    .agg(
        pl.col("amount")
        .sum()
        .round(2)
        .alias("total_sales"),

        pl.col("amount")
        .mean()
        .round(2)
        .alias("average_sales"),

        pl.len()
        .alias("order_count")
    )
    .sort("total_sales", descending=True)
)

print(category_sales)


# 4. Group by region
print("\n4. Sales by Region")

region_sales = (
    df.group_by("region")
    .agg(
        pl.col("amount")
        .sum()
        .round(2)
        .alias("total_sales"),

        pl.col("quantity")
        .sum()
        .alias("total_quantity")
    )
    .sort("total_sales", descending=True)
)

print(region_sales)


# 5. Top 10 orders
print("\n5. Top 10 Orders")

top_orders = (
    df.sort("amount", descending=True)
    .select([
        "order_id",
        "category",
        "region",
        "amount"
    ])
    .head(10)
)

print(top_orders)


print("\n" + "=" * 60)
print("W5D4 Polars operations completed successfully.")