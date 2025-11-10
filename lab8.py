import pandas as pd
import re
# Load dataset
df = pd.read_csv('sales_data.csv')
# Drop duplicates
df.drop_duplicates(inplace=True)
# Fill missing values with appropriate defaults or forward fill
df.fillna(method='ffill', inplace=True)
# Standardize case (e.g., for name and city columns)
df['Customer_Name'] = df['Customer_Name'].str.title()
df['City'] = df['City'].str.title()
# Remove special characters from name and address
df['Customer_Name'] = df['Customer_Name'].str.replace(r'[^A-Za-z0-9 ]+', '', regex=True)
df['Address'] = df['Address'].str.replace(r'[^A-Za-z0-9 ,.-]+', '', regex=True)
# Save cleaned data
df.to_csv('customers_cleaned.csv', index=False)