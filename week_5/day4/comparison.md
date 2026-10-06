# W5D4 - Pandas vs DuckDB vs Polars Comparison

## 1. Project Overview

This project compares Pandas, DuckDB, and Polars using the same
100,000-row sales dataset.

The following operations were performed:

1. Filter high-value orders
2. Create a calculated column
3. Group by category
4. Group by region
5. Find top 10 orders

Performance was measured using Python's `time.perf_counter()`.

---

## 2. Performance Benchmark

| Operation | Pandas (seconds) | DuckDB (seconds) | Polars (seconds) |
|---|---:|---:|---:|
| Load CSV | 0.193331 | 0.379938 | 0.213845 |
| Filter high-value orders | 0.002873 | 0.207430 | 0.007452 |
| Create calculated column | 0.081306 | 0.424115 | 0.003582 |
| Group by category | 0.040264 | 0.220266 | 0.014351 |
| Group by region | 0.023902 | 0.227572 | 0.005913 |
| Top 10 orders | 0.037004 | 0.202695 | 0.014866 |

---

## 3. Performance Observations

### Pandas

Pandas was the fastest for CSV loading and simple filtering in this
benchmark.

It also provided good performance for grouping and sorting operations.

### Polars

Polars performed very well for computational DataFrame operations.

It was faster than Pandas for:

- Creating the calculated column
- Grouping by category
- Grouping by region
- Finding the top 10 orders

### DuckDB

DuckDB provides a SQL-based approach to analytical data processing.

In this benchmark, DuckDB was slower than Pandas and Polars for the
tested operations because each query scanned the CSV file independently.

Performance can vary depending on dataset size, hardware, query design,
file format, and whether data is loaded into memory or stored in an
analytical database.

---

## 4. Syntax Comparison

### Pandas

Filtering:

```python
df[df["amount"] > 40000]