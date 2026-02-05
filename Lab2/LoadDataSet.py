import pandas as pd
df = pd.read_csv('US_Covid_Mobility_2021.csv')
rows, columns = df.shape
print(f"Number of Rows: {rows:,}")
print(f"Number of Columns: {columns}")
print("-" * 30)
print(f"Dataset Shape (Tuple): {df.shape}")
print("-" * 30)
print("First 5 rows:")
print(df.head())
print("-" * 30)
print("Dataset Info:")
df.info()
