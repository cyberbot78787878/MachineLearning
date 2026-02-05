import pandas as pd
df = pd.read_csv('US_Covid_Mobility_2021.csv')
print(f"Dataset Shape: {df.shape}")
print("-" * 30)
print("First 5 rows:")
print(df.head())
print("-" * 30)
print("Dataset Info:")
df.info()
