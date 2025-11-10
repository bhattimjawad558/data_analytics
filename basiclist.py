# Task 5
import pandas as pd
data = pd.read_csv('https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv')
print(data.head())
data.info()
data.describe()
data2 = {
    'Customer': ['Ali', 'Sara', 'John'],
    'Rating': [5, 3, 1],
    'Review': ['Excellent!', 'Okay', 'Bad']
}
df = pd.DataFrame(data2)
print(df)
feedback = ['Great service!', 'Average experience', 'Very poor quality']
for review in feedback:
    print(review)
