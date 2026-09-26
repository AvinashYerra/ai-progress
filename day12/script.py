import csv
import pandas as pd

df = pd.read_csv(
    "employees.csv",
    na_values = ["?"]
)
print(df.head())
print("Shape:", df.shape)
print("\nData types:\n", df.dtypes)
print("\nMissing values:\n", df.isna().sum())
print("\nDuplicate rows:\n", df.duplicated().sum())

df = df.drop_duplicates()
print("Shape after cleaning:", df.shape)

df["age"] = pd.to_numeric(
    df["age"], errors = "coerce"
)

df["salary"] = pd.to_numeric(
    df["salary"], errors = "coerce"
)

df["age"] = df["age"].fillna(df["age"].median())
df["salary"] = df["salary"].fillna(df["salary"].median())
df["city"] = df["city"].fillna("Unknown")



df["salary_category"] = df["salary"].apply(
    lambda x : "High" if x > 100000 else "Medium" if x > 50000 else "Low"
)

print("\nSUMMARY")
print("Employees:", len(df))
print("Average age:", df["age"].mean())
print("Average salary:", df["salary"].mean())
print("Total salary:", df["salary"].sum())
print("Minimum salary:", df["salary"].min())
print("Maximum salary:", df["salary"].max())

print("\nEmployees by city:")
print(df.groupby("city").size())

print("\nAverage salary by city:")
print(df.groupby("city")["salary"].mean())




print("\n Data quality checks")
print("missing values:")
print(df.isna().sum())
print("duplicate rows:", df.duplicated().sum())

df.to_csv("employees_cleaned.csv", index=False)