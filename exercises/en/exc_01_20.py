import pandas as pd
from sklearn.dummy import ____


# Loading in the data
canucks = pd.read_csv('data/canucks_subbed.csv')

# Define X and y
X = canucks.loc[:, ['No.', 'Age', 'Height',	'Weight', 'Experience']]
y = canucks['Salary']

# Create a model
model = ____

# Fit your data 
____

# Predict the labels of X
____

# The model accuracy
accuracy = round(____, 2)

accuracy