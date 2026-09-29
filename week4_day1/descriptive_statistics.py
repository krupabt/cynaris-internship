import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
data = pd.read_csv("dataset.csv")

sales = data["Monthly_Sales"]

# 1. Mean
print("Mean:", sales.mean())

# 2. Median
print("Median:", sales.median())

# 3. Mode
print("Mode:", sales.mode().tolist())

# 4. Variance
print("Variance:", sales.var())

# 5. Standard Deviation
print("Standard Deviation:", sales.std())

# 6. Percentiles
print("25th Percentile:", sales.quantile(0.25))
print("50th Percentile:", sales.quantile(0.50))
print("75th Percentile:", sales.quantile(0.75))

# 7. Quartiles
print("Q1:", sales.quantile(0.25))
print("Q2:", sales.quantile(0.50))
print("Q3:", sales.quantile(0.75))

# 8. Frequency Distribution
plt.figure(figsize=(8, 5))
plt.hist(sales, bins=6, edgecolor="black")

plt.title("Frequency Distribution of Monthly Sales")
plt.xlabel("Monthly Sales")
plt.ylabel("Frequency")

plt.show()

# 9. Side-by-side Box Plot

sales_group = data[data["Department"] == "Sales"]["Monthly_Sales"]
support_group = data[data["Department"] == "Support"]["Monthly_Sales"]

plt.figure(figsize=(8, 5))

plt.boxplot(
    [sales_group, support_group],
    labels=["Sales", "Support"]
)

plt.title("Sales vs Support Monthly Sales")
plt.ylabel("Monthly Sales")

plt.show()