import pandas as pd
import sweetviz as sv

# Load dataset
df = pd.read_csv("week5/data/sales_data.csv")

# Display basic information
print("Dataset Shape:", df.shape)
print("\nDataset Columns:")
print(df.columns.tolist())

print("\nFirst 5 Rows:")
print(df.head())

# -----------------------------
# SweetViz Automated EDA Report
# -----------------------------

sweetviz_report = sv.analyze(df)

sweetviz_report.show_html(
    "week5/reports/sweetviz_report.html",
    open_browser=False
)

print("\nSweetViz report generated successfully.")