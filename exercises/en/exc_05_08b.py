import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.impute import ____

# Loading in the data
bball_df = pd.read_csv('data/bball_imp.csv')
bball_df = bball_df[(bball_df['position'] =='G') | (bball_df['position'] =='F')]

# Define X and y
X = bball_df.loc[:, ['height', 'weight', 'salary']]
y = bball_df['position']

# Split the dataset
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=7)

# Fill in the missing values using imputation
____ = ____
____.____
____ = ____
____ = ____

# Transform X_train_imp into a dataframe using the column and index labels from X_train
____ = ____

# Check if your training set still has missing values 
____
