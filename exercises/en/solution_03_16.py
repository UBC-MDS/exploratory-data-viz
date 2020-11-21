import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split, cross_validate

# Loading in the data
bball_df = pd.read_csv('data/bball.csv')
bball_df = bball_df[(bball_df['position'] =='G') | (bball_df['position'] =='F')]

# Define X and y
X = bball_df.loc[:, ['height', 'weight', 'salary']]
y = bball_df['position']

# Split the dataset
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=31)

# Create a model
model = DecisionTreeClassifier()

# Cross validate
scores = cross_validate(model, X_train, y_train, cv=10, return_train_score=True)

# Covert scores into a dataframe
scores_df = pd.DataFrame(scores)

# Calculate the mean value of each column
mean_scores = scores_df.mean()

# Display each score mean value 
# Remember that in this case "test_score" is actually "validation" score

mean_scores
