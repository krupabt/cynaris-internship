import pandas as pd
import logging
from pandasai import SmartDataframe

# -----------------------------
# Logging setup
# -----------------------------
logging.basicConfig(
    filename="w5d1_errors.log",
    level=logging.ERROR,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# -----------------------------
# Load dataset
# -----------------------------
df = pd.read_csv("data/indian_sales.csv")

print("Dataset loaded successfully")
print(df.head())

# -----------------------------
# Create PandasAI DataFrame
# -----------------------------
smart_df = SmartDataframe(df)

# -----------------------------
# Natural Language Queries
# -----------------------------
queries = [
    "What is the total sales?",
    "What is the average sales?",
    "Which city has the highest sales?",
    "Which product has the highest quantity sold?",
    "How many orders are there?",
    "What is the average order value?",
    "Which category has the highest sales?",
    "Show the top 5 products by sales.",
    "Which city has the most orders?",
    "What is the total quantity sold?"
]

# -----------------------------
# Run queries with error handling
# -----------------------------
for i, query in enumerate(queries, start=1):
    print(f"\nQuery {i}: {query}")

    try:
        result = smart_df.chat(query)
        print("Answer:", result)

    except Exception as e:
        logging.error("Query failed: %s | Error: %s", query, e)
        print("Query failed. Error logged.")