

import pandas as pd
import numpy as np


file_path = r"C:\Users\singh\Downloads\Logistics Data Analyst\Logistics_Analytics_Practice_Dataset.xlsx"
df = pd.read_excel(file_path, sheet_name='Raw_Data')


print("Missing Values before cleaning:\n", df.isnull().sum())


df['Weight_kg'] = df['Weight_kg'].fillna(df['Weight_kg'].median())
df['Shipping_Cost_INR'] = df['Shipping_Cost_INR'].fillna(df['Shipping_Cost_INR'].median())
df['Customer_Rating'] = df['Customer_Rating'].fillna(df['Customer_Rating'].median())


df['Weather'] = df['Weather'].fillna(df['Weather'].mode()[0])


print("\nMissing Values after cleaning:\n", df.isnull().sum())


df.to_excel('Cleaned_Logistics_Dataset.xlsx', index=False)
print("\nData cleaning completed and saved successfully!")
