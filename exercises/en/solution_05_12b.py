import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import MinMaxScaler


# Loading in the data
bball_df = pd.read_csv('data/bball.csv')
bball_df = bball_df[(bball_df['position'] =='G') | (bball_df['position'] =='F')]

# Define X and y
X = bball_df.loc[:, ['height', 'weight', 'salary']]
y = bball_df['position']

# Split the dataset
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=7)

# Build the transformer and name it mm_scaler
mm_scaler = MinMaxScaler()

# Fit and transform the data X_train
# Save the transformed feature vectors in objects named X_train_scaled
X_train_scaled = mm_scaler.fit_transform(X_train)


# Transform X_test and save it in an object named X_test_scaled
X_test_scaled = mm_scaler.transform(X_test)

# Build a KNN classifier and name it knn
knn = KNeighborsClassifier()

# Fit your model on the newly scaled training data
knn.fit(X_train_scaled, y_train)

# Save the training score to 3 decimal places in an object named mm_score
mm_score = knn.score(X_train_scaled, y_train).round(3)
mm_score
