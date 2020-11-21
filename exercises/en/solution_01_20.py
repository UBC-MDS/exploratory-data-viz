import pandas as pd
from sklearn.dummy import DummyRegressor


# Loading in the data
canucks = pd.read_csv('data/canucks_subbed.csv')

# Define X and y
X = canucks.loc[:, ['No.', 'Age', 'Height',	'Weight', 'Experience']]
y = canucks['Salary']

# Create a model
model = DummyRegressor(strategy="mean")

# Fit your data 
model.fit(X,y)

# Predict the labels of X
model.predict(X)

# The model accuracy
accuracy = round(model.score(X,y), 2)

accuracy
