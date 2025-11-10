# ===============================================================
# SECTION 2.4 - AGGREGATE DATA USING PYTHON
# Goal: Summarize and combine data for insights
# ===============================================================
import pandas as pd
# Load cleaned datasets (replace with your file paths if needed)
iris = pd.read_csv("iris_cleaned.csv")
netflix = pd.read_csv("netflix_dataset.csv")
# ---------------------------------------------------------------
# 1️⃣ Group the Iris dataset by flower species and compute averages
# ---------------------------------------------------------------
iris_grouped = iris.groupby('flower_species').agg({
    'sepal_length': 'mean',
    'sepal_width': 'mean',
    'petal_length': 'mean',
    'petal_width': 'mean'
}).reset_index()
print("Average Sepal and Petal Dimensions by Flower Species:\n")
print(iris_grouped)
print("\n" + "-"*60 + "\n")
# ---------------------------------------------------------------
# 2️⃣ Count number of Movies and TV Shows by country
# ---------------------------------------------------------------
movie_tv_count = netflix.groupby(['country', 'show_type']).size().reset_index(name='count')
print("Number of Movies and TV Shows by Country:\n")
print(movie_tv_count.head(10))  # show first 10 for preview
print("\n" + "-"*60 + "\n")
# ---------------------------------------------------------------
# 3️⃣ Merge two small DataFrames (example)
# ---------------------------------------------------------------
# Create two small sample DataFrames for demonstration
df1 = pd.DataFrame({
    'ID': [1, 2, 3],
    'Value': ['A', 'B', 'C']
})
df2 = pd.DataFrame({
    'ID': [3, 4, 5],
    'Value': ['C', 'D', 'E']
})
merged_df = pd.merge(df1, df2, on='ID', how='outer', suffixes=('_df1', '_df2'))
print("Merged DataFrame Example:\n")
print(merged_df)
print("\n" + "-"*60 + "\n")
# ---------------------------------------------------------------
# 4️⃣ Create a pivot table showing how many Netflix titles exist per rating
# ---------------------------------------------------------------
pivot_table = netflix.pivot_table(
    index='rating',
    values='show_type',
    aggfunc='count'
).sort_values(by='show_type', ascending=False)
print("Number of Netflix Titles per Rating:\n")
print(pivot_table)
print("\n" + "-"*60 + "\n")
# ---------------------------------------------------------------
# 5️⃣ Optional: Save aggregated data for reporting
# ---------------------------------------------------------------
iris_grouped.to_csv("iris_aggregated.csv", index=False)
movie_tv_count.to_csv("netflix_aggregated.csv", index=False)
pivot_table.to_csv("netflix_pivot.csv")
print("Aggregated data saved as CSV files.")
