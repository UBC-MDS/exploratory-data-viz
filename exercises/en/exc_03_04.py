import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import ____

# Loading in the data
candybar_df = pd.read_csv('data/candybars.csv')

# Define X and y
X = candybar_df.loc[:, 'chocolate':'multi']
y = candybar_df['availability']

# Split the dataset
____, ____, ____, ____ = ____(
    ____, ____, ____, ____)

# Create a model
____ = ____

# Fit your data 
____.____

# Score the model
____ = ____.score(____, ____)
____ = ____.score(____, ____)

print("The train score: " + str(round(train_score, 2)))
print("The test score: " + str(round(test_score, 2)))
