import time
import duckdb

CSV_FILE = "sales_100k.csv"

print("W5D4 - DuckDB Performance Benchmark")
print("=" * 60)

# Connect to DuckDB
con = duckdb.connect()

# 1. Load / scan dataset
start = time.perf_counter()

con.execute(f"""
    SELECT *
    FROM read_csv_auto('{CSV_FILE}')
""").fetchall()

load_time = time.perf_counter() - start

print(f"\nDataset loading time: {load_time:.6f} seconds")


# 2. Filter high-value orders
start = time.perf_counter()

con.execute(f"""
    SELECT *
    FROM read_csv_auto('{CSV_FILE}')
    WHERE amount > 40000
""").fetchall()

filter_time = time.perf_counter() - start

print(f"1. Filter high-value orders: {filter_time:.6f} seconds")


# 3. Create calculated column
start = time.perf_counter()

con.execute(f"""
    SELECT *,
        CASE
            WHEN amount >= 25000 THEN 'High'
            ELSE 'Normal'
        END AS revenue_category
    FROM read_csv_auto('{CSV_FILE}')
""").fetchall()

column_time = time.perf_counter() - start

print(f"2. Create calculated column: {column_time:.6f} seconds")


# 4. Group by category
start = time.perf_counter()

con.execute(f"""
    SELECT
        category,
        SUM(amount) AS total_sales,
        AVG(amount) AS average_sales,
        COUNT(*) AS order_count
    FROM read_csv_auto('{CSV_FILE}')
    GROUP BY category
    ORDER BY total_sales DESC
""").fetchall()

category_time = time.perf_counter() - start

print(f"3. Group by category: {category_time:.6f} seconds")


# 5. Group by region
start = time.perf_counter()

con.execute(f"""
    SELECT
        region,
        SUM(amount) AS total_sales,
        SUM(quantity) AS total_quantity
    FROM read_csv_auto('{CSV_FILE}')
    GROUP BY region
    ORDER BY total_sales DESC
""").fetchall()

region_time = time.perf_counter() - start

print(f"4. Group by region: {region_time:.6f} seconds")


# 6. Top 10 orders
start = time.perf_counter()

con.execute(f"""
    SELECT
        order_id,
        category,
        region,
        amount
    FROM read_csv_auto('{CSV_FILE}')
    ORDER BY amount DESC
    LIMIT 10
""").fetchall()

top10_time = time.perf_counter() - start

print(f"5. Top 10 orders: {top10_time:.6f} seconds")


con.close()

print("\n" + "=" * 60)
print("DuckDB benchmark completed successfully.")