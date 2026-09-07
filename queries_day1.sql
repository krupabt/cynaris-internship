USE cynaris_sales;

-- 1. Display all sales records
SELECT * FROM sales;

-- 2. Display customer names and products
SELECT customer_name, product
FROM sales;

-- 3. Find sales from Bangalore
SELECT *
FROM sales
WHERE city = 'Bangalore';

-- 4. Find electronics sales with price greater than 5000
SELECT *
FROM sales
WHERE category = 'Electronics'
  AND price > 5000;

-- 5. Find sales from Bangalore OR Chennai
SELECT *
FROM sales
WHERE city = 'Bangalore'
   OR city = 'Chennai';

-- 6. Find sales that are NOT from Bangalore
SELECT *
FROM sales
WHERE NOT city = 'Bangalore';

-- 7. Find customers whose name starts with 'A'
SELECT *
FROM sales
WHERE customer_name LIKE 'A%';

-- 8. Find sales from Bangalore or Delhi
SELECT *
FROM sales
WHERE city IN ('Bangalore', 'Delhi');

-- 9. Find products with price between 1000 and 15000
SELECT *
FROM sales
WHERE price BETWEEN 1000 AND 15000;

-- 10. Find records where city is NULL
SELECT *
FROM sales
WHERE city IS NULL;