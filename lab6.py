#Task 3
import pandas as pd
# A list is an ordered collection that can be changed (mutable)
fruits = ['apple', 'banana']  # You can add/remove items later
# A tuple is also ordered but cannot be changed (immutable)
colors = ('red', 'green')  # Fixed values
# A dictionary stores data in key-value pairs
person = {
    'name': 'Alice',
    'age': 30,
    'city': 'Lahore'
}
# This is useful for representing structured data like a person's profile
# 2. Convert Dictionary to DataFrame
# A DataFrame is like a table with rows and columns
# We wrap the dictionary in a list to make it a single-row table
df = pd.DataFrame([person])
# Print the initial DataFrame
print("Initial DataFrame:")
print(df)
# Add a new column called 'country' and set its value to 'Pakistan' for all rows
df['country'] = 'Pakistan'
# Print the updated DataFrame
print("\nAfter adding 'country' column:")
print(df)
# Use .loc to add a new row at index 1
# The order of values must match the column order: name, age, city, country
df.loc[1] = ['Bob', 25, 'Karachi', 'Pakistan']
# Print the final DataFrame
print("\nAfter adding a new row:")
print(df)