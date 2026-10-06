# W5D4: Pandas vs DuckDB vs Polars

## Performance Comparison

| Criteria | Pandas | DuckDB | Polars |
|---|---|---|---|
| Main Use | Python Data Analysis | Analytical SQL | High-performance DataFrames |
| Syntax | Python | SQL | Python/DataFrame API |
| Performance | Good | Very Fast | Very Fast |
| Large CSV Processing | Good | Excellent | Excellent |
| Ease of Use | Very Easy | Easy for SQL users | Easy after learning expressions |

## Conclusion

Pandas is easy to use for general data analysis and Python workflows.

DuckDB is powerful for analytical SQL queries directly on files such as CSV.

Polars provides high-performance DataFrame operations and is useful for processing large datasets efficiently.

Overall, Pandas is convenient, while DuckDB and Polars are strong choices for high-performance analytical workloads

## Benchmark Observation

For this 100,000-row dataset, Pandas performed well for the tested operations. Polars showed strong performance in several aggregation operations, while DuckDB provided a convenient SQL-based approach for analytical queries.

Performance can vary depending on dataset size, query complexity, hardware, and whether data loading time is included.