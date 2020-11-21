import pandas as pd
from sklearn.tree import DecisionTreeClassifier

# Loading in the data
canucks = pd.read_csv('data/canucks_subbed.csv')

# Define X and y
X = canucks.loc[:, ['No.', 'Age', 'Height', 'Weight', 'Experience']]
y = canucks['Salary']

# Create a model
reg_tree = DecisionTreeClassifier(random_state=1, max_depth=8)

# Fit your data 
reg_tree.fit(X,y)

# Score the model
reg_score = reg_tree.score(X, y)
reg_score