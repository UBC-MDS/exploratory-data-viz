import pandas as pd
from sklearn.dummy import DummyClassifier


# Loading in the data
candybar_df = pd.read_csv('data/candybars.csv')

# Define X and y
X = candybar_df.loc[:, 'chocolate':'multi']
y = candybar_df['availability']

# Create a model
model = ____

# Fit your data 
____

# Predict the labels of X
____

# The model accuracy
accuracy = round(____, 2)

accuracy