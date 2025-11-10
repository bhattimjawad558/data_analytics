import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# ==========================================
# Step 1: Load Dataset
# ==========================================
hospital = pd.read_csv("hospital data analysis.csv")

print("=== Dataset Loaded ===")
print(hospital.head(), "\n")
print("Columns:", hospital.columns.tolist(), "\n")

# ==========================================
# Step 2: Check Missing / Invalid Data
# ==========================================
print("=== Missing Values ===")
print(hospital.isna().sum(), "\n")

# Drop rows with critical missing info
hospital = hospital.dropna(subset=["Patient_ID", "Age", "Gender", "Condition", "Cost", "Length_of_Stay"])

# Ensure numeric columns
hospital["Cost"] = pd.to_numeric(hospital["Cost"], errors="coerce")
hospital["Length_of_Stay"] = pd.to_numeric(hospital["Length_of_Stay"], errors="coerce")

# ==========================================
# Step 3: Group by Condition
# ==========================================
condition_summary = (
    hospital.groupby("Condition")
    .agg(
        avg_stay=("Length_of_Stay", "mean"),
        total_cost=("Cost", "sum"),
        patient_count=("Patient_ID", "count")
    )
    .reset_index()
    .sort_values("total_cost", ascending=False)
)

print("=== Condition Summary ===")
print(condition_summary.head(), "\n")

# ==========================================
# Step 4: Group by Age Group & Gender
# ==========================================
bins = [0, 18, 35, 50, 65, 120]
labels = ["0-18", "19-35", "36-50", "51-65", "65+"]
hospital["Age_Group"] = pd.cut(hospital["Age"], bins=bins, labels=labels)

age_gender_summary = (
    hospital.groupby(["Age_Group", "Gender"])
    .agg(
        avg_stay=("Length_of_Stay", "mean"),
        avg_cost=("Cost", "mean"),
        total_patients=("Patient_ID", "count")
    )
    .reset_index()
)

print("=== Age & Gender Summary ===")
print(age_gender_summary.head(), "\n")

# ==========================================
# Step 5: Department Analysis (if provided)
# ==========================================
if "Department" in hospital.columns:
    dept_summary = (
        hospital.groupby("Department")
        .agg(
            avg_stay=("Length_of_Stay", "mean"),
            total_cost=("Cost", "sum"),
            patient_count=("Patient_ID", "count")
        )
        .reset_index()
        .sort_values("total_cost", ascending=False)
    )
    print("=== Department Summary ===")
    print(dept_summary.head(), "\n")
else:
    dept_summary = None

# ==========================================
# Step 6: Readmission & Outcome Analysis
# ==========================================
readmission_rate = (
    hospital["Readmission"].value_counts(normalize=True) * 100
).reset_index().rename(columns={"index": "Readmission", "Readmission": "Percentage"})

outcome_summary = (
    hospital["Outcome"].value_counts(normalize=True) * 100
).reset_index().rename(columns={"index": "Outcome", "Outcome": "Percentage"})

# ==========================================
# Step 7: Visualizations
# ==========================================
# Set Seaborn style
sns.set(style="whitegrid")

# --------------------------
# Top 10 Conditions by Total Cost
# --------------------------
plt.figure(figsize=(10,5))
sns.barplot(
    data=condition_summary.head(10),
    x="Condition",
    y="total_cost"
)
plt.title("Top 10 Conditions by Total Cost")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# --------------------------
# Average Treatment Cost by Age Group & Gender
# --------------------------
plt.figure(figsize=(8,5))
sns.barplot(
    data=age_gender_summary,
    x="Age_Group",
    y="avg_cost",
    hue="Gender"   # hue is now assigned properly
)
plt.title("Average Treatment Cost by Age Group and Gender")
plt.tight_layout()
plt.show()

# --------------------------
# Readmission Rate
# --------------------------
readmission_rate = hospital["Readmission"].value_counts(normalize=True).mul(100).reset_index()
readmission_rate.columns = ["Readmission", "Percentage"]

plt.figure(figsize=(6,4))
sns.barplot(
    data=readmission_rate,
    x="Readmission",
    y="Percentage"
)
plt.title("Readmission Rate (%)")
plt.tight_layout()
plt.show()

# --------------------------
# Outcome Distribution
# --------------------------
outcome_summary = hospital["Outcome"].value_counts(normalize=True).mul(100).reset_index()
outcome_summary.columns = ["Outcome", "Percentage"]

plt.figure(figsize=(6,4))
sns.barplot(
    data=outcome_summary,
    x="Outcome",
    y="Percentage"
)
plt.title("Patient Outcome Distribution (%)")
plt.tight_layout()
plt.show()

# ==========================================
# Step 8: Pivot Table - Top Conditions by Age Group
# ==========================================
top_conditions = condition_summary.head(5)["Condition"].tolist()
pivot_table = hospital[hospital["Condition"].isin(top_conditions)].pivot_table(
    index="Age_Group",
    columns="Condition",
    values="Patient_ID",
    aggfunc="count",
    fill_value=0
)
print("=== Pivot Table: Top Conditions by Age Group ===")
print(pivot_table, "\n")

# Heatmap of top conditions by age group
plt.figure(figsize=(8,5))
sns.heatmap(pivot_table, annot=True, fmt="d", cmap="YlGnBu")
plt.title("Patient Count: Top Conditions by Age Group")
plt.show()

# ==========================================
# Step 9: Export Summaries to Excel
# ==========================================
with pd.ExcelWriter("Hospital_Analysis_Summary.xlsx") as writer:
    condition_summary.to_excel(writer, sheet_name="Condition_Summary", index=False)
    age_gender_summary.to_excel(writer, sheet_name="Age_Gender_Summary", index=False)
    readmission_rate.to_excel(writer, sheet_name="Readmission_Rate", index=False)
    outcome_summary.to_excel(writer, sheet_name="Outcome_Summary", index=False)
    pivot_table.to_excel(writer, sheet_name="Pivot_Top_Conditions")
    if dept_summary is not None:
        dept_summary.to_excel(writer, sheet_name="Department_Summary", index=False)
print("✅ Analysis complete. Summaries exported to Hospital_Analysis_Summary.xlsx")



