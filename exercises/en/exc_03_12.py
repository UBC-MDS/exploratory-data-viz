import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.model_selection import ____

# Loading in the data
pokemon = pd.read_csv('data/pokemon.csv')

X = pokemon.loc[:, 'speed':'capture_rt']
y = pokemon['legendary']

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=7)

# Create a model
____ = ____

# Cross validate
____ = ____

# Convert scores into a dataframe
____ = ____

# Calculate the mean value of each column
____ = ____

# Display each score mean value
____