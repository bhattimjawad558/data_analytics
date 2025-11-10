# ==============================
# Part 6: Transposing and Reshaping
# ==============================
import seaborn as sns
import pandas as pd
titanic = sns.load_dataset('titanic')
# Transpose first 5 rows
print(titanic.head().T)
# Create pivot table: average fare by class and gender
pivot_table = titanic.pivot_table(values='fare', index='class', columns='sex', aggfunc='mean')
print("Pivot Table:\n", pivot_table)
# Unpivot (melt) pivot table
melted = pivot_table.reset_index().melt(id_vars='class', value_name='avg_fare')
print("Melted Pivot Table:\n", melted)




