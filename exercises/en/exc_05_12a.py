import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import ____


# Loading in the data
bball_df = pd.read_csv('data/bball.csv')
bball_df = bball_df[(bball_df['position'] =='G') | (bball_df['position'] =='F')]

# Define X and y
X = bball_df.loc[:, ['height', 'weight', 'salary']]
y = bball_df['position']

# Split the dataset
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=7)

# Build the transformer and name it bb_scaler
____ = ____

# Fit and transform the data X_train
# Save the transformed feature vectors in objects named X_train_scaled
____ = ____

# Transform X_test and save it in an object named X_test_scaled
____ = ____

# Build a KNN classifier and name it knn
____ = ____

# Fit your model on the newly scaled training data
____.____

# Save the training score to 3 decimal places in an object named ss_score
____ = ____
____