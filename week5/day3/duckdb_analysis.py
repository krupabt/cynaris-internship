import duckdb

CSV_FILE = "data/sales_100k.csv"

con = duckdb.connect()

print("W5D3 - DuckDB Analytics")
print("=" * 50)

# Query 1: Count total rows
result = con.execute(f"""
    SELECT COUNT(*) AS total_rows
    FROM read_csv_auto('{CSV_FILE}')
""").fetchone()

print("\n1. Total Rows")
print(result[0])


# Query 2: Average order amount
result = con.execute(f"""
    SELECT ROUND(AVG(amount), 2) AS average_amount
    FROM read_csv_auto('{CSV_FILE}')
""").fetchone()

print("\n2. Average Order Amount")
print(result[0])


# Query 3: Orders by category
result = con.execute(f"""
    SELECT
        category,
        COUNT(*) AS order_count
    FROM read_csv_auto('{CSV_FILE}')
    GROUP BY category
    ORDER BY order_count DESC
""").fetchall()

print("\n3. Orders by Category")
for row in result:
    print(row)


# Query 4: Total sales by region
result = con.execute(f"""
    SELECT
        region,
        ROUND(SUM(amount), 2) AS total_sales
    FROM read_csv_auto('{CSV_FILE}')
    GROUP BY region
    ORDER BY total_sales DESC
""").fetchall()

print("\n4. Total Sales by Region")
for row in result:
    print(row)


# Query 5: Top 10 orders by amount
result = con.execute(f"""
    SELECT
        order_id,
        category,
        region,
        amount
    FROM read_csv_auto('{CSV_FILE}')
    ORDER BY amount DESC
    LIMIT 10
""").fetchall()

print("\n5. Top 10 Orders by Amount")
for row in result:
    print(row)


con.close()