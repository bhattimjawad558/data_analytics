import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from scipy.stats import chi2_contingency
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix
data = pd.read_csv('titanic.csv')
# Prepare data
X = data[['Pclass','Age','Fare']].fillna(data['Age'].mean())
y = data['Survived']
# Split dataset
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
# Train model
model = LogisticRegression()
model.fit(X_train, y_train)
# Evaluate
predictions = model.predict(X_test)
print('Accuracy:', accuracy_score(y_test, predictions))
print('Confusion Matrix:\n', confusion_matrix(y_test, predictions))

