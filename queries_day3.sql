-- ============================================
-- SQL AGGREGATIONS - WEEK 1 DAY 3
-- ============================================

-- Create sales table
CREATE TABLE sales (
    sale_id INT PRIMARY KEY,
    sale_date DATE,
    region VARCHAR(50),
    category VARCHAR(50),
    product VARCHAR(100),
    quantity INT,
    sales_amount DECIMAL(10,2)
);

-- Insert sample data
INSERT INTO sales
(sale_id, sale_date, region, category, product, quantity, sales_amount)
VALUES
(1, '2026-01-05', 'South', 'Electronics', 'Laptop', 2, 100000),
(2, '2026-01-10', 'South', 'Furniture', 'Chair', 5, 25000),
(3, '2026-01-15', 'North', 'Electronics', 'Phone', 4, 80000),
(4, '2026-02-05', 'North', 'Furniture', 'Table', 3, 45000),
(5, '2026-02-12', 'South', 'Electronics', 'Headphones', 10, 20000),
(6, '2026-02-20', 'West', 'Clothing', 'Shirt', 8, 16000),
(7, '2026-03-03', 'West', 'Electronics', 'Laptop', 1, 50000),
(8, '2026-03-15', 'East', 'Clothing', 'Shoes', 6, 30000);


-- ============================================
-- 1. COUNT
-- Count total number of sales
-- ============================================

SELECT COUNT(*) AS total_sales
FROM sales;


-- ============================================
-- 2. SUM
-- Calculate total sales amount
-- ============================================

SELECT SUM(sales_amount) AS total_revenue
FROM sales;


-- ============================================
-- 3. AVG
-- Calculate average sale amount
-- ============================================

SELECT AVG(sales_amount) AS average_sale
FROM sales;


-- ============================================
-- 4. MAX
-- Find the highest sale
-- ============================================

SELECT MAX(sales_amount) AS highest_sale
FROM sales;


-- ============================================
-- 5. MIN
-- Find the lowest sale
-- ============================================

SELECT MIN(sales_amount) AS lowest_sale
FROM sales;


-- ============================================
-- 6. GROUP BY REGION
-- Calculate sales for each region
-- ============================================

SELECT
    region,
    SUM(sales_amount) AS total_sales
FROM sales
GROUP BY region;


-- ============================================
-- 7. GROUP BY CATEGORY
-- Calculate sales for each category
-- ============================================

SELECT
    category,
    SUM(sales_amount) AS total_sales
FROM sales
GROUP BY category;


-- ============================================
-- 8. GROUP BY MONTH
-- Calculate sales for each month
-- ============================================

SELECT
    MONTH(sale_date) AS sale_month,
    SUM(sales_amount) AS total_sales
FROM sales
GROUP BY MONTH(sale_date);


-- ============================================
-- 9. HAVING
-- Show regions with sales greater than 50000
-- ============================================

SELECT
    region,
    SUM(sales_amount) AS total_sales
FROM sales
GROUP BY region
HAVING SUM(sales_amount) > 50000;


-- ============================================
-- 10. WINDOW FUNCTION
-- Calculate running total of sales
-- ============================================

SELECT
    sale_id,
    sale_date,
    sales_amount,
    SUM(sales_amount) OVER (
        ORDER BY sale_date
    ) AS running_total
FROM sales;