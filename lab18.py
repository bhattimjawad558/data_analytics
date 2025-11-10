# Task 1: Load dataset using pandas
import pandas as pd
# Load dataset (adjust path if needed)
df = pd.read_csv('Global_Superstore.csv', encoding='ISO-8859-1')
# Display basic info
print("Dataset Shape:", df.shape)
print("Columns:", df.columns.tolist())
print("\nPreview of Dataset:")
print(df.head())
# Task 2: Display unique categorical values
print("Unique Categories:", df['Category'].unique())
print("Unique Regions:", df['Region'].unique())
print("Unique Segments:", df['Segment'].unique())
# Task 3: Filtering / Searching
# Example: Filter all 'Office Supplies' sold in 'West' region
filtered_data = df[(df['Category'] == 'Office Supplies') & (df['Region'] == 'West')]
print("Filtered Rows:", len(filtered_data))
print(filtered_data[['Category', 'Region', 'Sales', 'Profit', 'Customer.Name']].head())
# Task 4: Compute aggregation metrics
sales = df['Sales']
profit = df['Profit']
print("=== Sales Metrics ===")
print("Count:", sales.count())
print("Total Sales:", round(sales.sum(), 2))
print("Mean:", round(sales.mean(), 2))
print("Median:", round(sales.median(), 2))
print("Mode:", round(sales.mode()[0], 2))
print("Standard Deviation:", round(sales.std(), 2))
print("Min:", round(sales.min(), 2))
print("Max:", round(sales.max(), 2))
print("\n=== Profit Metrics ===")
print("Total Profit:", round(profit.sum(), 2))
print("Average Profit:", round(profit.mean(), 2))
print("Standard Deviation:", round(profit.std(), 2))
# Task 5: Compare metrics between groups (e.g., Region)
region_comparison = df.groupby('Region')[['Sales', 'Profit']].agg(['count', 'sum', 'mean', 'median', 'std'])
print("Sales and Profit Comparison by Region:")
print(region_comparison)
# Focus on West vs East regions
subset_comparison = region_comparison.loc[['West', 'East']]
print("\nWest vs East Comparison:")
print(subset_comparison)
