import pandas as pd
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split

# Loading in the data
pokemon_df = pd.read_csv('data/pokemon.csv')

# Define X and y
X = pokemon_df.drop(columns = ['deck_no', 'name','total_bs', 'type', 'legendary'])
y = pokemon_df['legendary']

# Split the dataset
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=33)

# Create a model
model = SVC(gamma=0.1, C=10)

# Fit your data 
model.fit(X_train,y_train)

# Score the model on the test set 
test_score = round(model.score(X_test, y_test), 4)

print("The test score: " + str(test_score))

