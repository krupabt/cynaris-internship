-- ============================================
-- SQL JOINS - WEEK 1 DAY 2
-- ============================================

-- Create Departments table
CREATE TABLE departments (
    dept_id INT PRIMARY KEY,
    department_name VARCHAR(50)
);

-- Insert department data
INSERT INTO departments (dept_id, department_name)
VALUES
(10, 'IT'),
(20, 'HR'),
(30, 'Finance'),
(40, 'Marketing');


-- Create Employees table
CREATE TABLE employees (
    employee_id INT PRIMARY KEY,
    name VARCHAR(50),
    dept_id INT,
    manager_id INT
);

-- Insert employee data
INSERT INTO employees (employee_id, name, dept_id, manager_id)
VALUES
(1, 'Ravi', 10, NULL),
(2, 'Priya', 20, 1),
(3, 'Arun', 10, 1),
(4, 'Sneha', 30, 2),
(5, 'Kiran', 50, 2);


-- ============================================
-- 1. INNER JOIN
-- Returns only matching records
-- ============================================

SELECT
    e.employee_id,
    e.name,
    d.department_name
FROM employees e
INNER JOIN departments d
    ON e.dept_id = d.dept_id;


-- ============================================
-- 2. LEFT JOIN
-- Returns all employees and matching departments
-- ============================================

SELECT
    e.employee_id,
    e.name,
    d.department_name
FROM employees e
LEFT JOIN departments d
    ON e.dept_id = d.dept_id;


-- ============================================
-- 3. RIGHT JOIN
-- Returns all departments and matching employees
-- ============================================

SELECT
    e.employee_id,
    e.name,
    d.department_name
FROM employees e
RIGHT JOIN departments d
    ON e.dept_id = d.dept_id;


-- ============================================
-- 4. FULL OUTER JOIN
-- MySQL does not directly support FULL OUTER JOIN.
-- UNION is used to achieve the same result.
-- ============================================

SELECT
    e.employee_id,
    e.name,
    d.department_name
FROM employees e
LEFT JOIN departments d
    ON e.dept_id = d.dept_id

UNION

SELECT
    e.employee_id,
    e.name,
    d.department_name
FROM employees e
RIGHT JOIN departments d
    ON e.dept_id = d.dept_id;


-- ============================================
-- 5. DUPLICATE ROWS CAUSED BY JOIN
-- A department can have multiple employees.
-- Therefore, the department information appears
-- multiple times.
-- ============================================

SELECT
    d.department_name,
    e.name AS employee_name
FROM departments d
JOIN employees e
    ON d.dept_id = e.dept_id;


-- Remove duplicate department names
-- when only unique departments are required

SELECT DISTINCT
    d.department_name
FROM departments d
JOIN employees e
    ON d.dept_id = e.dept_id;


-- ============================================
-- 6. SELF JOIN
-- Find each employee and their manager
-- ============================================

SELECT
    e.name AS employee,
    m.name AS manager
FROM employees e
LEFT JOIN employees m
    ON e.manager_id = m.employee_id;


-- ============================================
-- 7. SELF JOIN WITH CONDITION
-- Find employees who have a manager
-- ============================================

SELECT
    e.name AS employee,
    m.name AS manager
FROM employees e
INNER JOIN employees m
    ON e.manager_id = m.employee_id;


-- ============================================
-- 8. USING TABLE ALIASES
-- e = employees
-- d = departments
-- ============================================

SELECT
    e.name AS employee_name,
    d.department_name
FROM employees e
LEFT JOIN departments d
    ON e.dept_id = d.dept_id;