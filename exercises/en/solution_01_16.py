import pandas as pd
from sklearn.dummy import DummyClassifier


# Loading in the data
candybar_df = pd.read_csv('data/candybars.csv')

# Define X and y
X = candybar_df.loc[:, 'chocolate':'multi']
y = candybar_df['availability']

# Create a model
model = DummyClassifier(strategy="most_frequent")

# Fit your data 
model.fit(X,y)

# Predict the labels of X
model.predict(X)

# The model accuracy
accuracy = round(model.score(X,y), 2)

accuracy
