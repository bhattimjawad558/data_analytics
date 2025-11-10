#task 12
import pandas as pd
import openpyxl
# 1. Create sample sales data
sales_data = {
    'Region': ['North', 'South', 'East', 'West', 'North', 'South', 'East', 'West'],
    'Salesperson': ['Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Frank', 'Grace', 'Hank'],
    'SalesAmount': [200, 150, 300, 250, 400, 350, 500, 450]
}
sales_df = pd.DataFrame(sales_data)
# 2. Calculate region-wise totals
region_totals_df = sales_df.groupby('Region', as_index=False)['SalesAmount'].sum()
region_totals_df = region_totals_df.rename(columns={'SalesAmount': 'TotalSales'})
# 3. Write to Excel with multiple sheets
with pd.ExcelWriter('sales_report.openpyxl', engine='openpyxl') as writer:
    sales_df.to_excel(writer, sheet_name='Sales Data', index=False)
    region_totals_df.to_excel(writer, sheet_name='Region Totals', index=False)
print("Excel file 'sales_report.xlsx' created with two sheets:")
print("   • 'Sales Data' — raw sales records")
print("   • 'Region Totals' — total sales per region")
