import pandas as pd
import random
from datetime import datetime, timedelta

random.seed(42)

categories = ["Electronics", "Clothing", "Home", "Books", "Sports"]
regions = ["North", "South", "East", "West"]

start_date = datetime(2025, 1, 1)

data = []

for i in range(1, 100001):
    category = random.choice(categories)
    region = random.choice(regions)
    quantity = random.randint(1, 10)
    unit_price = round(random.uniform(100, 5000), 2)

    date = start_date + timedelta(days=random.randint(0, 364))

    amount = round(quantity * unit_price, 2)

    data.append({
        "order_id": i,
        "date": date.strftime("%Y-%m-%d"),
        "category": category,
        "region": region,
        "quantity": quantity,
        "unit_price": unit_price,
        "amount": amount
    })

df = pd.DataFrame(data)

df.to_csv("data/sales_100k.csv", index=False)

print(f"Dataset created successfully: {len(df)} rows")
print(df.head())