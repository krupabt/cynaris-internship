"""
ai_eda.py - AI-Powered Exploratory Data Analysis

W5D5 Data Analyst Intern Project
- Loads indian_business_data.csv
- Performs basic data cleaning
- Generates business insights
- Creates three visualizations
- Generates an EDA markdown report
"""

import pathlib
import sys

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns


DATA_FILE = pathlib.Path("indian_business_data.csv")
REPORT_FILE = pathlib.Path("eda_report.md")


def load_data(path: pathlib.Path) -> pd.DataFrame:
    """Load the CSV dataset safely."""
    if not path.is_file():
        sys.exit(f"Data file not found: {path.resolve()}")

    try:
        return pd.read_csv(path)
    except Exception as error:
        sys.exit(f"Failed to read CSV: {error}")


def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    """Clean required columns and convert numeric fields."""
    required_columns = [
        "city",
        "category",
        "revenue",
        "rating",
    ]

    df = df.dropna(subset=required_columns).copy()

    df["revenue"] = pd.to_numeric(
        df["revenue"],
        errors="coerce",
    )

    df["rating"] = pd.to_numeric(
        df["rating"],
        errors="coerce",
    )

    df = df.dropna(
        subset=["revenue", "rating"]
    )

    return df


def print_overview(df: pd.DataFrame) -> None:
    """Print basic information about the dataset."""
    print("\n=== DATASET OVERVIEW ===")
    print(f"Rows: {df.shape[0]}")
    print(f"Columns: {df.shape[1]}")

    print("\nColumns:")
    print(df.columns.tolist())

    print("\n=== DATA TYPES ===")
    print(df.dtypes)

    print("\n=== MISSING VALUES ===")
    print(df.isnull().sum())

    print("\n=== STATISTICAL SUMMARY ===")
    print(df.describe())


def business_insights(df: pd.DataFrame) -> dict:
    """Calculate important business insights."""
    insights = {}

    insights["top_cities"] = (
        df.groupby("city")["revenue"]
        .sum()
        .sort_values(ascending=False)
        .head(5)
    )

    insights["rev_by_category"] = (
        df.groupby("category")["revenue"]
        .sum()
        .sort_values(ascending=False)
    )

    insights["rating_by_category"] = (
        df.groupby("category")["rating"]
        .mean()
        .sort_values(ascending=False)
    )

    insights["total_revenue"] = round(
        df["revenue"].sum(),
        2,
    )

    insights["average_revenue"] = round(
        df["revenue"].mean(),
        2,
    )

    print("\n=== BUSINESS INSIGHTS ===")

    print("\nTop 5 Cities by Revenue:")
    print(insights["top_cities"])

    print("\nRevenue by Business Category:")
    print(insights["rev_by_category"])

    print("\nAverage Rating by Category:")
    print(insights["rating_by_category"])

    print(
        f"\nTotal Revenue: "
        f"{insights['total_revenue']}"
    )

    print(
        f"Average Revenue: "
        f"{insights['average_revenue']}"
    )

    return insights


def make_plots(df: pd.DataFrame) -> None:
    """Create and save the required visualizations."""
    sns.set_style("whitegrid")

    # Revenue by city
    top_cities = (
        df.groupby("city")["revenue"]
        .sum()
        .sort_values(ascending=False)
        .head(15)
    )

    plt.figure(figsize=(10, 6))

    top_cities.plot(kind="bar")

    plt.title("Total Revenue by City (Top 15)")
    plt.xlabel("City")
    plt.ylabel("Revenue")
    plt.tight_layout()

    plt.savefig(
        "revenue_by_city.png",
        dpi=150,
    )

    plt.close()

    # Revenue distribution and outliers
    plt.figure(figsize=(10, 3))

    sns.boxplot(
        x=df["revenue"]
    )

    plt.title("Revenue Distribution and Outliers")
    plt.xlabel("Revenue")
    plt.tight_layout()

    plt.savefig(
        "revenue_outliers.png",
        dpi=150,
    )

    plt.close()

    # Revenue by business category
    plt.figure(figsize=(10, 6))

    sns.barplot(
        data=df,
        x="category",
        y="revenue",
        estimator=sum,
    )

    plt.title("Revenue by Business Category")
    plt.xlabel("Business Category")
    plt.ylabel("Revenue")
    plt.xticks(
        rotation=30,
        ha="right",
    )
    plt.tight_layout()

    plt.savefig(
        "revenue_by_category.png",
        dpi=150,
    )

    plt.close()


def generate_report(
    df: pd.DataFrame,
    insights: dict,
) -> None:
    """Generate a markdown report containing EDA findings."""
    with open(
        REPORT_FILE,
        "w",
        encoding="utf-8",
    ) as file:

        file.write("# AI-Powered EDA Report\n\n")

        file.write(
            f"**Rows:** {df.shape[0]}  \n"
        )

        file.write(
            f"**Columns:** {df.shape[1]}\n\n"
        )

        file.write("## Key Business Insights\n\n")

        file.write(
            "### Top 5 Cities by Revenue\n\n"
        )

        file.write(
            insights["top_cities"].to_markdown()
        )

        file.write("\n\n")

        file.write(
            "### Revenue by Business Category\n\n"
        )

        file.write(
            insights["rev_by_category"].to_markdown()
        )

        file.write("\n\n")

        file.write(
            "### Average Rating by Category\n\n"
        )

        file.write(
            insights["rating_by_category"].to_markdown()
        )

        file.write("\n\n")

        file.write(
            f"**Total Revenue:** "
            f"{insights['total_revenue']}\n\n"
        )

        file.write(
            f"**Average Revenue:** "
            f"{insights['average_revenue']}\n\n"
        )

        file.write("## Visualisations\n\n")

        file.write(
            "![Revenue by City]"
            "(revenue_by_city.png)\n\n"
        )

        file.write(
            "![Revenue Distribution]"
            "(revenue_outliers.png)\n\n"
        )

        file.write(
            "![Revenue by Category]"
            "(revenue_by_category.png)\n"
        )


def main() -> None:
    """Run the complete EDA workflow."""
    df = load_data(DATA_FILE)

    df = clean_data(df)

    print_overview(df)

    insights = business_insights(df)

    make_plots(df)

    generate_report(
        df,
        insights,
    )

    print("\n=== EDA COMPLETED SUCCESSFULLY ===")

    print(
        "Charts saved:"
        " revenue_by_city.png,"
        " revenue_outliers.png,"
        " revenue_by_category.png"
    )

    print(
        f"Report generated: {REPORT_FILE}"
    )


if __name__ == "__main__":
    main()