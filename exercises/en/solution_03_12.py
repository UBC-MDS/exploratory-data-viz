import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.model_selection import cross_validate

# Loading in the data
pokemon = pd.read_csv('data/pokemon.csv')

X = pokemon.loc[:, 'speed':'capture_rt']
y = pokemon['legendary']

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=7)

# Create a model
model = DecisionTreeClassifier()

# Cross validate
scores = cross_validate(model, X, y, cv=10, return_train_score=True)

# Convert scores into a dataframe
scores_df = pd.DataFrame(scores)

# Calculate the mean value of each column
mean_scores = scores_df.mean()

# Display each score mean value
mean_scores