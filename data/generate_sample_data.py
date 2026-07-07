"""
Generates a synthetic retail sales dataset for the analysis project.
Run this once to create data/raw_sales.csv, or replace it with a real
dataset (e.g. Kaggle 'Superstore Sales' or 'Online Retail').
"""
import numpy as np
import pandas as pd
from datetime import datetime, timedelta

np.random.seed(42)

n_rows = 8000
products = ["Laptop", "Headphones", "Keyboard", "Monitor", "Mouse",
            "Webcam", "Printer", "Tablet", "Speaker", "Charger"]
categories = {
    "Laptop": "Electronics", "Headphones": "Accessories", "Keyboard": "Accessories",
    "Monitor": "Electronics", "Mouse": "Accessories", "Webcam": "Electronics",
    "Printer": "Office", "Tablet": "Electronics", "Speaker": "Accessories",
    "Charger": "Accessories"
}
regions = ["North", "South", "East", "West"]

start_date = datetime(2024, 1, 1)
dates = [start_date + timedelta(days=int(x)) for x in np.random.randint(0, 540, n_rows)]

df = pd.DataFrame({
    "order_id": range(1, n_rows + 1),
    "order_date": dates,
    "customer_id": np.random.randint(1000, 1300, n_rows),
    "product": np.random.choice(products, n_rows),
    "region": np.random.choice(regions, n_rows),
    "quantity": np.random.randint(1, 6, n_rows),
    "unit_price": np.round(np.random.uniform(10, 800, n_rows), 2),
})
df["category"] = df["product"].map(categories)
df["revenue"] = df["quantity"] * df["unit_price"]

# Inject realistic messiness so cleaning has something to do
dupe_idx = np.random.choice(df.index, 150, replace=False)
df = pd.concat([df, df.loc[dupe_idx]], ignore_index=True)

null_idx = np.random.choice(df.index, 200, replace=False)
df.loc[null_idx, "unit_price"] = np.nan

date_str_idx = np.random.choice(df.index, 300, replace=False)
df["order_date"] = df["order_date"].astype(object)
df.loc[date_str_idx, "order_date"] = df.loc[date_str_idx, "order_date"].apply(
    lambda d: d.strftime("%d/%m/%Y")
)

df = df.sample(frac=1, random_state=1).reset_index(drop=True)
df.to_csv("data/raw_sales.csv", index=False)
print(f"Generated data/raw_sales.csv with {len(df)} rows")
