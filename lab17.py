# Market Basket Analysis on Superstore Sales Dataset
# Using Apriori algorithm and generating association rules (Customer-level)
import pandas as pd
from mlxtend.frequent_patterns import apriori, association_rules
import matplotlib.pyplot as plt
import seaborn as sns
# -----------------------------
# Step 1: Load the Dataset
# -----------------------------
df = pd.read_csv('Superstore.csv', encoding='ISO-8859-1')
print("Dataset Shape:", df.shape)
print("Columns:", df.columns.tolist())
print(df.head())
# -----------------------------
# Step 2: Data Preprocessing (Group by Customer ID)
# -----------------------------
# Keep relevant columns
df_basket = df[['Customer ID', 'Product Name', 'Quantity']]
# Group by Customer ID to treat all purchases by the same customer as one basket
basket = df_basket.groupby(['Customer ID', 'Product Name'])['Quantity'].sum().unstack().fillna(0)
# Convert quantities to boolean (1 = purchased, 0 = not purchased)
basket_sets = (basket > 0).astype(bool)
print("\nTransaction-Product Matrix Shape:", basket_sets.shape)
print("Memory Usage (MB):", basket_sets.memory_usage(deep=True).sum() / (1024 ** 2))
# -----------------------------
# Step 3: Apply Apriori Algorithm
# -----------------------------
# Use a moderate support threshold to start
frequent_itemsets = apriori(basket_sets, min_support=0.005, use_colnames=True, low_memory=True)
frequent_itemsets = frequent_itemsets.sort_values(by='support', ascending=False)
print("\nFrequent Itemsets Found:", len(frequent_itemsets))
multi_item_sets = frequent_itemsets[frequent_itemsets['itemsets'].apply(lambda x: len(x) > 1)]
print("Multi-item frequent sets:", len(multi_item_sets))
print(frequent_itemsets.head(10))
# -----------------------------
# Step 4: Generate Association Rules
# -----------------------------
if not frequent_itemsets.empty:
    rules = association_rules(frequent_itemsets, metric="confidence", min_threshold=0.05)
    if not rules.empty:
        rules = rules.sort_values(by='lift', ascending=False)
        print("\nTop 10 Association Rules:")
        print(rules[['antecedents', 'consequents', 'support', 'confidence', 'lift']].head(10))
    else:
        print("⚠️ No association rules found. Try lowering confidence or support thresholds.")
else:
    print("⚠️ No frequent itemsets found. Try lowering min_support.")
# -----------------------------
# Step 5: Visualization
# -----------------------------
if not rules.empty:
    plt.figure(figsize=(10,6))
    sns.scatterplot(x='support', y='confidence', size='lift', data=rules, legend=False, alpha=0.6)
    plt.title('Association Rules (Support vs Confidence, size=Lift)')
    plt.xlabel('Support')
    plt.ylabel('Confidence')
    plt.tight_layout()
    plt.savefig('association_rules_plot_customer.png')
    plt.show()
# -----------------------------
# Step 6: Insights
# -----------------------------
print("\nInsights:")
print("- Each 'basket' now represents a customer's overall purchasing behavior.")
print("- Multi-item sets indicate products commonly bought by the same customers.")
print("- High-confidence, high-lift rules can be used for product recommendations or cross-selling.")
if not rules.empty:
    top_lift_rules = rules.sort_values(by='lift', ascending=False).head(10)
    print("\nTop 10 Rules by Lift:")
    print(top_lift_rules[['antecedents', 'consequents', 'support', 'confidence', 'lift']])
