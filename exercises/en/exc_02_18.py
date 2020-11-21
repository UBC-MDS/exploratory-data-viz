import pandas as pd
from sklearn.tree import ____

# Loading in the data
canucks = pd.read_csv('data/canucks_subbed.csv')

# Define X and y
X = canucks.loc[:, ['No.', 'Age', 'Height', 'Weight', 'Experience']]
y = canucks['Salary']

# Create a model
____ = ____(____)

# Fit your data 
____.____

# Score the model
____ = ____
____