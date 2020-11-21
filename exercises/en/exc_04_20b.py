import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
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
____ = ____

# Fit your data 
____

# Score the model on the test set 
____ = ____

print("The test score: " + str(test_score))




