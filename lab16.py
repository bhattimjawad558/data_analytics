import pandas as pd
from mlxtend.frequent_patterns import apriori, association_rules

# === Step 1: Load and clean data ===
df = pd.read_csv("OnlineRetail.csv", encoding="ISO-8859-1")
df.columns = df.columns.str.strip()
required = {'InvoiceNo', 'StockCode', 'Description', 'Quantity', 'InvoiceDate', 'UnitPrice', 'CustomerID', 'Country'}
missing = required - set(df.columns)
if missing:
    raise ValueError(f"❌ Missing columns: {missing}")

df = df.dropna(subset=['CustomerID'])
df = df[~df['InvoiceNo'].astype(str).str.startswith('C') & (df['Quantity'] > 0)]

# === Step 2: Filter for UK and create basket matrix ===
basket = (df[df['Country'] == "United Kingdom"]
          .groupby(['InvoiceNo', 'Description'])['Quantity']
          .sum().unstack().fillna(0)
          .apply(lambda col: col.map(lambda x: 1 if x > 0 else 0)))

# === Step 3: Apply Apriori and generate rules ===
frequent_items = apriori(basket, min_support=0.02, use_colnames=True)
rules = association_rules(frequent_items, metric="lift", min_threshold=1)

# === Step 4: Display and save results ===
print("\n===== PRESCRIPTIVE RULES (TOP 10) =====")
if rules.empty:
    print("⚠️ No strong rules found. Try lowering min_support.")
else:
    print(rules[['antecedents', 'consequents', 'support', 'confidence', 'lift']].head(10))
    rules.to_excel("prescriptive_rules_output.xlsx", index=False)
    print("✅ Rules saved to 'prescriptive_rules_output.xlsx'")






