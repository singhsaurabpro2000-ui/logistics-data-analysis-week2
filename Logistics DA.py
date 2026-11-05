# import pandas as pd
# import numpy as np
#
# # # 1. Excel file load karein
# file_path = 'Logistics_Analytics_Practice_Dataset.xlsx'
# df = pd.read_excel(r"C:\Users\singh\Downloads\Logistics_Analytics_Practice_Dataset.xlsx", sheet_name='Raw_Data')
#
# # # 2. Missing values check karein
# # print("Missing Values before cleaning:\n", df.isnull().sum())
#
# # Numerical columns mein median bharna
# df['Weight_kg'] = df['Weight_kg'].fillna(df['Weight_kg'].median())
# df['Shipping_Cost_INR'] = df['Shipping_Cost_INR'].fillna(df['Shipping_Cost_INR'].median())
# df['Customer_Rating'] = df['Customer_Rating'].fillna(df['Customer_Rating'].median())
#
# # Categorical column ('Weather') mein mode ya default value bharna
# df['Weather'] = df['Weather'].fillna(df['Weather'].mode()[0])

import pandas as pd
import numpy as np

# 1. Dataset load karein
file_path = r"C:\Users\singh\Downloads\Logistics Data Analyst\Logistics_Analytics_Practice_Dataset.xlsx"
df = pd.read_excel(file_path, sheet_name='Raw_Data')

# 2. Missing values check karein (Cleaning se pehle)
print("Missing Values before cleaning:\n", df.isnull().sum())

# 3. Numerical columns mein missing values ko median se bharna
df['Weight_kg'] = df['Weight_kg'].fillna(df['Weight_kg'].median())
df['Shipping_Cost_INR'] = df['Shipping_Cost_INR'].fillna(df['Shipping_Cost_INR'].median())
df['Customer_Rating'] = df['Customer_Rating'].fillna(df['Customer_Rating'].median())

# 4. Categorical column ('Weather') mein missing values ko mode se bharna
df['Weather'] = df['Weather'].fillna(df['Weather'].mode()[0])

# 5. Missing values check karein (Cleaning ke baad)
print("\nMissing Values after cleaning:\n", df.isnull().sum())

# 6. Cleaned data ko naye Excel file mein save karna (Week 2 submission ke liye)
df.to_excel('Cleaned_Logistics_Dataset.xlsx', index=False)
print("\nData cleaning completed and saved successfully!")