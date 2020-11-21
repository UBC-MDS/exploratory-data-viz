import pandas as pd
from sklearn.model_selection import train_test_split, cross_validate
from sklearn.neighbors import KNeighborsClassifier
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.model_selection import GridSearchCV


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

# Build a grid of the parameters you wish to search. 
param_grid = {
    "knn__n_neighbors" : [1, 5, 10, 20, 30, 40, 50],
    "knn__weights" : ['uniform', 'distance']
}

# Conduct grid search with 10 fold cross-validation
grid_search = GridSearchCV(bb_pipe, param_grid, cv=10, verbose=1, n_jobs=-1)

# Fit your pipeline with grid search 
grid_search.fit(X_train, y_train)

# Save the best hyperparameter values in an object named best_hyperparams
best_hyperparams = grid_search.best_params_

# Print best_hyperparams
print(best_hyperparams)

# Score your model on the test set 
# Save your results in an object named `bb_test_score`
bb_test_score = grid_search.score(X_test, y_test)

# Display your score 
bb_test_score