import polars as pl
import seaborn as sns
# ==========================================
# Task 1: Import and Explore Data
# ==========================================
# Load seaborn dataset and convert to Polars DataFrame
flights = pl.DataFrame(sns.load_dataset("flights"))
print("=== Head ===")
print(flights.head(), "\n")
print("=== Schema / Info ===")
print(flights.schema, "\n")
print("=== Describe Summary ===")
print(flights.describe(), "\n")
# ==========================================
# Task 2: Sorting and Filtering
# ==========================================
# Sort by passengers descending
flights_sorted = flights.sort("passengers", descending=True)
print("=== Sorted by passengers (desc) ===")
print(flights_sorted.head(), "\n")
# Filter where year > 1955
flights_recent = flights.filter(pl.col("year") > 1955)
print("=== Filtered where year > 1955 ===")
print(flights_recent.head(), "\n")
# Filter flights for month == 'July'
flights_july = flights.filter(pl.col("month") == "July")
print("=== Flights in July ===")
print(flights_july.head(), "\n")
# ==========================================
# Task 3: Slicing and Transposing
# ==========================================
# Select first 10 rows and specific columns
flights_slice = flights.select(["year", "month", "passengers"]).head(10)
print("=== First 10 rows (selected columns) ===")
print(flights_slice, "\n")
# Polars requires same data type for transpose → cast all to Utf8
flights_slice_str = flights_slice.select([
    pl.col("year").cast(pl.Utf8),
    pl.col("month").cast(pl.Utf8),
    pl.col("passengers").cast(pl.Utf8)
])
# Transpose safely
flights_transposed = flights_slice_str.transpose(column_names=True)
print("=== Transposed dataset ===")
print(flights_transposed, "\n")
# ==========================================
# Task 4: Appending and Truncating
# ==========================================
# Create dummy data for year 1961
dummy_data = pl.DataFrame({
    "year": [1961, 1961, 1961, 1961, 1961],
    "month": ["January", "February", "March", "April", "May"],
    "passengers": [360, 370, 400, 420, 390]
})
# Make sure schema matches original flights DataFrame
dummy_data = dummy_data.cast(flights.schema)
# Append using pl.concat
flights_appended = pl.concat([flights, dummy_data])
# Truncate to first 120 rows
flights_truncated = flights_appended.head(120)
print("=== Appended and Truncated Dataset (first 120 rows) ===")
print(flights_truncated.tail(), "\n")
# ==========================================
# Task 5: Final Sanity Checks
# ==========================================
print("Original row count:", flights.height)
print("After append:", flights_appended.height)
print("After truncation:", flights_truncated.height)


