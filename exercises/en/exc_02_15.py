import pandas as pd
from sklearn.tree import ____

# Loading in the data
candybar_df = pd.read_csv('data/candybars.csv')

# Define X and y
X = candybar_df.loc[:, 'chocolate':'multi']
y = candybar_df['availability']

# Create the model
____ = ____

# Fit your data 
____.____

# Score the model
____ = ____.____

