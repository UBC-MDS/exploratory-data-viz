import pandas as pd
from sklearn.model_selection import train_test_split

# Loading in the data
bball_df = pd.read_csv('data/bball_imp.csv')
bball_df = bball_df[(bball_df['position'] =='G') | (bball_df['position'] =='F')]

# Define X and y
X = bball_df.loc[:, ['height', 'weight', 'salary']]
y = bball_df['position']

# Split the dataset
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=7)

# Explore the missing data in the training features 
X_train.info()

# Calculate the number of examples with missing values
num_nan = X_train.isnull().any(axis=1).sum()
num_nan