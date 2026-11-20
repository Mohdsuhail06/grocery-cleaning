import pandas as pd

df = pd.read_csv("groceries_raw.csv")

print("--- First 5 rows ---")
print(df.head())

print("\n--- Columns and types ---")
df.info()

print("\n--- Missing values per column ---")
print(df.isna().sum())

print("\n--- Duplicate rows ---")
print(df.duplicated().sum())

print("\n--- Category values ---")
print(df["category"].unique())