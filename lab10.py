# 🧭 PART 3: HANDLE DUPLICATES AND INCONSISTENT FORMATTING
import pandas as pd
import numpy as np
# Load dataset (if not already loaded)
df = pd.read_csv("titanic.csv")
# Step 9: Detect and remove duplicate records
duplicate_count = df.duplicated().sum()
print(f"\nFound {duplicate_count} duplicate rows.")
df = df.drop_duplicates()
print("✅ Duplicates removed.")
# Step 10: Identify inconsistent categorical entries and standardize
cat_cols = df.select_dtypes(include=['object']).columns
for col in cat_cols:
    df[col] = df[col].astype(str).str.lower().str.strip()
print("\n✅ Standardized categorical columns (to lowercase and stripped whitespace).")
# Step 11: Standardize name/title columns — remove leading/trailing spaces
df[cat_cols] = df[cat_cols].apply(lambda x: x.str.strip())
print("✅ Removed leading/trailing spaces from text columns.")
# Step 12: Detect and remove outliers using the IQR method
num_cols = df.select_dtypes(include=['int64', 'float64']).columns
outlier_summary = {}
for col in num_cols:
    Q1 = df[col].quantile(0.25)
    Q3 = df[col].quantile(0.75)
    IQR = Q3 - Q1
    lower_limit = Q1 - 1.5 * IQR
    upper_limit = Q3 + 1.5 * IQR
    # Count outliers before removal
    outliers = df[(df[col] < lower_limit) | (df[col] > upper_limit)].shape[0]
    outlier_summary[col] = outliers
    # Remove outliers
    df = df[(df[col] >= lower_limit) & (df[col] <= upper_limit)]
print("\n✅ Outliers removed using IQR method.")
print("\nOutlier summary before removal:")
for k, v in outlier_summary.items():
    print(f" - {k}: {v} outliers detected")
# Final check
print(f"\nRemaining rows after cleaning: {df.shape[0]}")
print(f"Remaining columns: {df.shape[1]}")
print("\nPreview cleaned data:")
print(df.head())






