#Task 8
import pandas as pd
data = {
    'Name': ['Alex', 'Beth', 'Cathy', 'Dan', 'Ella'],
    'Age': [20, 19, 21, 20, 22],
    'Passed': [True, False, True, True, False],
    'Enrollment_Date': ['2023-09-01', '2023-08-15', '2023-10-01', '2023-09-10', '2023-08-20'],
    'Feedback': ['Excellent', 'Needs Improvement', 'Good', 'Outstanding', 'Fair'],
}
df_students = pd.DataFrame(data)
# Convert Enrollment_Date column from string (object) to a proper datetime type
df_students['Enrollment_Date'] = pd.to_datetime(df_students['Enrollment_Date'])
print("--- 1. Initial DataFrame ---")
print(df_students)
# --- Metadata Exploration ---
## 2. Identify and print Variable Types (Dtypes)
print("--- 2. Variable Types (df.dtypes) ---")
print(df_students.dtypes)
## 3. Print Structure Summary and Metadata (df.info())
print("\n--- 3. Structure Summary and Metadata (df.info()) ---")
# .info() provides non-null counts, Dtypes, and memory usage
df_students.info()
df_students.describe()
## 4. Print Shape (Dimensions)
print("\n--- 4. Shape (Rows, Columns) ---")
# .shape returns a tuple: (number of rows, number of columns)
print(df_students.shape)