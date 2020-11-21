import pandas as pd
from sklearn.tree import ____

# Loading in the data
candybar_df = pd.read_csv('data/candybars.csv')

# Define X and y
X = candybar_df.loc[:, 'chocolate':'multi']
y = candybar_df['availability']

# Create a model
____ = ____

# Fit your data 
____.____

# Predict the labels of X
____ = ____.____

# Compare 
pd.concat([candybar_df.loc[:, ['candy bar', 'availability']],
        pd.Series(predicted, name='predicted')], axis=1)
