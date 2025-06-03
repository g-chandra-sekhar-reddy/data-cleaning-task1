import pandas as pd

df = pd.read_csv("Mall_Customers.csv")
print("Original Dataset:\n", df.head())

print("\nMissing Values:\n", df.isnull().sum())
df = df.dropna()

df = df.drop_duplicates()

df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_')

if 'age' in df.columns:
    df['age'] = df['age'].astype(int)

if 'gender' in df.columns:
    df['gender'] = df['gender'].str.lower().str.strip()

# df['date_of_birth'] = pd.to_datetime(df['date_of_birth'], format='%d-%m-%Y')

df.to_csv("cleaned_mall_customers.csv", index=False)

print("\nCleaned Dataset Sample:\n", df.head())
