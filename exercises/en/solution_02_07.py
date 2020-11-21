import pandas as pd
from sklearn.tree import DecisionTreeClassifier

# Loading in the data
candybar_df = pd.read_csv('data/candybars.csv')

# Define X and y
X = candybar_df.loc[:, 'chocolate':'multi']
y = candybar_df['availability']

# Create a model
model = DecisionTreeClassifier(random_state=1)

# Fit your data 
model.fit(X,y)

# Predict the labels of X
predicted = model.predict(X)

# Compare
pd.concat([candybar_df.loc[:, ['candy bar', 'availability']],
        pd.Series(predicted, name='predicted')], axis=1)
