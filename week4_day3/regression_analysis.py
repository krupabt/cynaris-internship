import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score, mean_absolute_error, mean_squared_error

import numpy as np


# -------------------------------------------------
# 1. CREATE DATASET
# -------------------------------------------------

data = {
    "Advertising_Spend": [
        10, 12, 15, 18, 20,
        22, 25, 28, 30, 32,
        35, 38, 40, 42, 45,
        48, 50, 52, 55, 58
    ],

    "Sales": [
        25, 28, 30, 35, 38,
        40, 45, 48, 50, 53,
        55, 60, 62, 65, 68,
        70, 73, 76, 80, 84
    ],

    "Customer_Rating": [
        3.1, 3.2, 3.3, 3.5, 3.6,
        3.7, 3.8, 4.0, 4.1, 4.0,
        4.2, 4.3, 4.4, 4.5, 4.4,
        4.6, 4.7, 4.8, 4.8, 4.9
    ]
}

df = pd.DataFrame(data)

print("DATASET")
print(df)


# -------------------------------------------------
# 2. PEARSON CORRELATION
# -------------------------------------------------

pearson_correlation = df["Advertising_Spend"].corr(
    df["Sales"],
    method="pearson"
)

print("\nPEARSON CORRELATION")
print("-------------------")
print("Advertising Spend vs Sales:", pearson_correlation)


# -------------------------------------------------
# 3. SPEARMAN CORRELATION
# -------------------------------------------------

spearman_correlation = df["Advertising_Spend"].corr(
    df["Sales"],
    method="spearman"
)

print("\nSPEARMAN CORRELATION")
print("--------------------")
print("Advertising Spend vs Sales:", spearman_correlation)


# -------------------------------------------------
# 4. CORRELATION HEATMAP
# -------------------------------------------------

correlation_matrix = df.corr()

plt.figure(figsize=(8, 5))

sns.heatmap(
    correlation_matrix,
    annot=True,
    cmap="coolwarm",
    fmt=".2f"
)

plt.title("Correlation Heatmap")
plt.tight_layout()
plt.show()


# -------------------------------------------------
# 5. SCATTER MATRIX
# -------------------------------------------------

pd.plotting.scatter_matrix(
    df,
    figsize=(10, 8),
    diagonal="hist"
)

plt.suptitle("Scatter Matrix")
plt.tight_layout()
plt.show()


# -------------------------------------------------
# 6. SIMPLE LINEAR REGRESSION
# -------------------------------------------------

X = df[["Advertising_Spend"]]
y = df["Sales"]

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

model = LinearRegression()

model.fit(X_train, y_train)

y_pred = model.predict(X_test)


# -------------------------------------------------
# 7. REGRESSION RESULTS
# -------------------------------------------------

r2 = r2_score(y_test, y_pred)

mae = mean_absolute_error(
    y_test,
    y_pred
)

rmse = np.sqrt(
    mean_squared_error(y_test, y_pred)
)

print("\nREGRESSION RESULTS")
print("------------------")

print("R² Score:", r2)
print("MAE:", mae)
print("RMSE:", rmse)

print("\nRegression Equation:")
print(
    "Sales =",
    model.intercept_,
    "+",
    model.coef_[0],
    "* Advertising Spend"
)


# -------------------------------------------------
# 8. ACTUAL VS PREDICTED VALUES
# -------------------------------------------------

results = pd.DataFrame({
    "Actual Sales": y_test.values,
    "Predicted Sales": y_pred
})

print("\nACTUAL VS PREDICTED")
print("-------------------")
print(results)


# -------------------------------------------------
# 9. REGRESSION LINE
# -------------------------------------------------

plt.figure(figsize=(8, 5))

plt.scatter(
    df["Advertising_Spend"],
    df["Sales"],
    label="Actual Data"
)

plt.plot(
    df["Advertising_Spend"],
    model.predict(df[["Advertising_Spend"]]),
    label="Regression Line"
)

plt.xlabel("Advertising Spend")
plt.ylabel("Sales")

plt.title("Advertising Spend vs Sales")

plt.legend()

plt.tight_layout()
plt.show()


# -------------------------------------------------
# 10. RESIDUAL PLOT
# -------------------------------------------------

residuals = y_test - y_pred

plt.figure(figsize=(8, 5))

plt.scatter(
    y_pred,
    residuals
)

plt.axhline(
    y=0,
    linestyle="--"
)

plt.xlabel("Predicted Sales")
plt.ylabel("Residuals")

plt.title("Residual Plot")

plt.tight_layout()
plt.show()


# -------------------------------------------------
# 11. BASIC MODEL INTERPRETATION
# -------------------------------------------------

print("\nMODEL INTERPRETATION")
print("--------------------")

if r2 >= 0.7:
    print("The model explains a large proportion of the variation in Sales.")

else:
    print("The model explains a smaller proportion of the variation in Sales.")

print(
    "MAE shows the average absolute prediction error."
)

print(
    "RMSE gives more importance to larger prediction errors."
)

print(
    "Residuals should generally be randomly scattered around zero."
)