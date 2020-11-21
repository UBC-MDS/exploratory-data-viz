import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import ____

# Loading in the data
pokemon_df = pd.read_csv('data/pokemon.csv')

# Split the data
train_df, test_df = train_test_split(pokemon_df, test_size=0.2, random_state=123)

# Define X and y for the training set
X_train = train_df.drop(columns = ['deck_no', 'name','total_bs', 'type', 'legendary'])
y_train = train_df['legendary']

# Define X and y for the test set 
X_test = test_df.drop(columns = ['deck_no', 'name','total_bs', 'type', 'legendary'])
y_test = test_df['legendary']

# Create a KNeighborsClassifier model with n_neighbors equal to 5 and name it model
____ =  ____

# Train your model
____

# Score your model on the training set using score and save it in an object named train_score
____ = ____

# Score your model on the test set using score and save it in an object named test_score
____ = ____

print("The training score is", train_score.round(4))
print("The test score is", test_score.round(4))