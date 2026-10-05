# W5D3 - Pandas vs DuckDB vs Polars Comparison

| Criteria | Pandas | DuckDB | Polars |
|---|---|---|---|
| Ease of use | Very easy for Python data analysis | Easy for SQL users | Easy after learning Polars syntax |
| Query syntax | Python/DataFrame operations | SQL | DataFrame expressions |
| Performance | Good for medium-sized datasets | Very fast for analytical SQL queries | Very fast for DataFrame operations |
| Memory usage | Can use more memory for large datasets | Efficient for analytical workloads | Generally memory efficient |
| Best use case | Data cleaning, analysis, visualization | SQL analytics and querying large datasets | Fast DataFrame processing |

## Summary

Pandas is beginner-friendly and widely used for data analysis.

DuckDB is useful when working with analytical SQL queries directly on files such as CSV.

Polars provides fast DataFrame operations and is a strong alternative to Pandas for performance-focused data processing.

For this 100,000-row dataset, all three tools successfully performed the same five analytical operations.
## Benchmark Note

The benchmark measures the execution time of the five analytical operations after the datasets have been loaded. Results can vary between runs depending on the computer and system load.