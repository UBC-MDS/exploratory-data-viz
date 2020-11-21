import pandas as pd
from sklearn.tree import DecisionTreeClassifier

# Loading in the data
candybar_df = pd.read_csv('data/candybars.csv')

# Define X and y
X = candybar_df.loc[:, 'chocolate':'multi']
y = candybar_df['availability']

# Creating a model
hyper_tree = DecisionTreeClassifier(random_state=1, max_depth=8, min_samples_split=4)

# Fit your data 
hyper_tree.fit(X,y)

# Score the model
tree_score = hyper_tree.score(X, y)
tree_score

