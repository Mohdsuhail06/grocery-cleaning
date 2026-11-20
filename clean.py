import pandas as pd

df = pd.read_csv("groceries_raw.csv")
rows_before = len(df)

# 1. Remove exact duplicate rows
df = df.drop_duplicates()

# 2. Category: remove extra spaces, make all lowercase
df["category"] = df["category"].str.strip().str.lower()

# 3. Price: remove "JD", then turn the text into a number
df["price"] = df["price"].str.replace("JD", "").str.strip().astype(float)

# 4. Rows with no price are useless, so drop them
df = df.dropna(subset=["price"])

# 5. Missing quantity: assume 1 item
df["quantity"] = df["quantity"].fillna(1)

# 6. Negative quantity is a typo: make it positive
df["quantity"] = df["quantity"].abs().astype(int)

# 7. New column: how much each line cost
df["total"] = df["price"] * df["quantity"]

df.to_csv("groceries_clean.csv", index=False)

print(f"Rows before: {rows_before}, rows after: {len(df)}")
print(df)
print(f"\nTotal spent: {df['total'].sum():.2f} JD")
print(df["category"].value_counts())