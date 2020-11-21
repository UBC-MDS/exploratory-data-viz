import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.model_selection import ____

# Loading in the data
pokemon = pd.read_csv('data/pokemon.csv')

# Define X and y
X = pokemon.loc[:, 'attack':'capture_rt']
y = pokemon['legendary']

# Split the dataset
____, ____, ____, ____ = ____(
    ____, ____, test_size=____, random_state=33)

# Create a model
____ = ____

# Cross validate
____ = ____
____