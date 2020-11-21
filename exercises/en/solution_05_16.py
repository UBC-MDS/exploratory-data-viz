import pandas as pd
from sklearn.model_selection import train_test_split, cross_validate
from sklearn.neighbors import KNeighborsClassifier
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline


# Loading in the data
bball_df = pd.read_csv('data/bball.csv')
bball_df = bball_df[(bball_df['position'] =='G') | (bball_df['position'] =='F')]

# Define X and y
X = bball_df.loc[:, ['height', 'weight', 'salary']]
y = bball_df['position']

# Split the dataset
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=7)

# Build a pipeline named bb_pipe
bb_pipe = Pipeline(
            steps=[("imputer", SimpleImputer(strategy="median")),
                   ("scaler", StandardScaler()),
                   ("knn", KNeighborsClassifier())])

# Cross-validate on the pipeline steps using X_train and y_train
# Save the results in an object named cross_scores
cross_scores = cross_validate(bb_pipe, X_train, y_train, return_train_score=True)

# Transform cross_scores to a dataframe and take the mean of each column
# Save the result in an object named mean_scores
mean_scores = pd.DataFrame(cross_scores).mean()
mean_scores
