-- Week 1 Day 4: Subqueries and CTEs


-- 1. Non-correlated subquery:
-- Find sales records where the sales amount is above the average sales.

SELECT *
FROM sales
WHERE sales_amount > (
    SELECT AVG(sales_amount)
    FROM sales
);


-- 2. Correlated subquery:
-- Find the top performer in each region.

SELECT s1.*
FROM sales s1
WHERE s1.sales_amount = (
    SELECT MAX(s2.sales_amount)
    FROM sales s2
    WHERE s2.region = s1.region
);


-- 3. Rewrite a nested subquery as a CTE using WITH.

-- Nested subquery version
SELECT *
FROM sales
WHERE sales_amount > (
    SELECT AVG(sales_amount)
    FROM sales
);


-- CTE version
WITH average_sales AS (
    SELECT AVG(sales_amount) AS avg_sales
    FROM sales
)
SELECT s.*
FROM sales s
CROSS JOIN average_sales a
WHERE s.sales_amount > a.avg_sales;


-- 4. Chain two CTEs in a single query.

WITH regional_sales AS (
    SELECT
        region,
        SUM(sales_amount) AS total_sales
    FROM sales
    GROUP BY region
),
above_average_regions AS (
    SELECT
        region,
        total_sales
    FROM regional_sales
    WHERE total_sales > (
        SELECT AVG(total_sales)
        FROM regional_sales
    )
)
SELECT *
FROM above_average_regions
ORDER BY total_sales DESC;