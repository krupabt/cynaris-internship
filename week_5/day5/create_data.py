import pandas as pd
import random

random.seed(42)

cities = [
    "Bengaluru", "Mumbai", "Delhi", "Hyderabad",
    "Chennai", "Pune", "Kolkata", "Ahmedabad"
]

categories = [
    "Retail", "Restaurant", "Technology",
    "Healthcare", "Manufacturing", "Finance"
]

data = {
    "business_id": range(1, 100001),
    "business_name": [f"Business_{i}" for i in range(1, 100001)],
    "city": [random.choice(cities) for _ in range(100000)],
    "category": [random.choice(categories) for _ in range(100000)],
    "revenue": [round(random.uniform(50000, 5000000), 2) for _ in range(100000)],
    "employees": [random.randint(5, 500) for _ in range(100000)],
    "rating": [round(random.uniform(2.5, 5.0), 1) for _ in range(100000)]
}

df = pd.DataFrame(data)

df.to_csv("indian_business_data.csv", index=False)

print("Dataset created successfully!")
print("Rows:", len(df))
print("Columns:", len(df.columns))