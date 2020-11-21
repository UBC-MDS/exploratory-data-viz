import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split

# Loading in the data
candybar_df = pd.read_csv('data/candybars.csv')

# Define X and y
X = candybar_df.loc[:, 'chocolate':'multi']
y = candybar_df['availability']

# Split the dataset
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=7)

# Create a model
model = DecisionTreeClassifier()

# Fit your data 
model.fit(X_train,y_train)

# Score the model
train_score = model.score(X_train, y_train)
test_score = model.score(X_test, y_test)

print("The train score: " + str(round(train_score, 2)))
print("The test score: " + str(round(test_score, 2)))


