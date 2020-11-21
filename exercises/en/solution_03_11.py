import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.model_selection import cross_val_score

# Loading in the data
pokemon = pd.read_csv('data/pokemon.csv')

# Define X and y
X = pokemon.loc[:, 'attack':'capture_rt']
y = pokemon['legendary']

# Split the dataset
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=33)

# Create a model
model = DecisionTreeClassifier()

# Cross validate
cv_scores = cross_val_score(model, X_train, y_train, cv=6)
cv_scores



