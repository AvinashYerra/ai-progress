import pandas as pd

sales = pd.Series([
    1200,
    800,
    1500,
    2300,
    900,
    3100,
    1700
])
print(sales)


data = {
    "name": ["John", "Sarah", "Mike"],
    "city": ["Pune", "Delhi", "Mumbai"],
    "salary": [80000, 90000, 75000]
}

df = pd.DataFrame(data)

print(df)