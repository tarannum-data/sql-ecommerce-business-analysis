from pathlib import Path

import pandas as pd
import matplotlib.pyplot as plt


DATA_PATH = Path("ecommerce_sales_data.csv")
OUTPUT_DIR = Path("outputs/charts")


def save_chart(filename: str) -> Path:
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    return OUTPUT_DIR / filename


def main():
    df = pd.read_csv(DATA_PATH)
    df["Order Date"] = pd.to_datetime(df["Order Date"])

    monthly_sales = df.groupby(df["Order Date"].dt.to_period("M"))["Sales"].sum()
    monthly_sales.index = monthly_sales.index.astype(str)

    plt.figure(figsize=(10, 5))
    monthly_sales.plot()
    plt.title("Monthly Sales Trends")
    plt.xlabel("Month")
    plt.ylabel("Sales")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig(save_chart("monthly_sales_trends.png"))
    plt.close()

    category_sales = df.groupby("Category")["Sales"].sum().sort_values(ascending=False)

    plt.figure(figsize=(8, 5))
    category_sales.plot(kind="bar")
    plt.title("Sales by Category")
    plt.xlabel("Category")
    plt.ylabel("Sales")
    plt.tight_layout()
    plt.savefig(save_chart("sales_by_category.png"))
    plt.close()

    region_profit = df.groupby("Region")["Profit"].sum().sort_values(ascending=False)

    plt.figure(figsize=(8, 5))
    region_profit.plot(kind="bar")
    plt.title("Profit by Region")
    plt.xlabel("Region")
    plt.ylabel("Profit")
    plt.tight_layout()
    plt.savefig(save_chart("profit_by_region.png"))
    plt.close()

    top_products = df.groupby("Product Name")["Sales"].sum().sort_values(ascending=False).head(10)

    plt.figure(figsize=(10, 5))
    top_products.plot(kind="bar")
    plt.title("Top 10 Products by Sales")
    plt.xlabel("Product")
    plt.ylabel("Sales")
    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()
    plt.savefig(save_chart("top_products.png"))
    plt.close()


if __name__ == "__main__":
    main()
