# Week 2 Day 4 — Data Cleaning Log

## Cleaning Steps

### Missing Values

Missing values were identified using `isnull().sum()`.

Numeric missing values were handled using median imputation because the median is less sensitive to extreme values.

### Duplicates

Duplicate records were identified using `duplicated()` and removed using `drop_duplicates()`.

### Outliers

Outliers were detected using the Interquartile Range (IQR) method.

Extreme numeric values were capped using the calculated IQR boundaries instead of removing complete records.

### String Standardisation

String columns were standardised by removing leading/trailing whitespace and converting values to lowercase.

### Before and After

The notebook contains a data quality comparison showing rows, columns, missing values, and duplicate records before and after cleaning.

### Output

The cleaned data was exported to:

`cleaned_dataset.csv`
