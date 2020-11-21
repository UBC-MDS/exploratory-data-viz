import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import ____

# Loading in the data
pokemon_df = pd.read_csv('data/pokemon.csv')

# Split the data
train_df, test_df = train_test_split(pokemon_df, test_size=0.2, random_state=123)

# Define X and y for the training
X_train = train_df.drop(columns = ['deck_no', 'name','total_bs', 'type', 'legendary'])

# The Snoodles query point
query_point = [[53, 77, 43, 69, 80, 57, 5]]

# Create a model and name it nn (make sure you are finding the single closest pokemon)
____ = ____

# Train your model
____

# Predict your pokemon using kneighbors and save it in an object named snoodles_neighbour
____ = ____
#print(snoodles_neighbour)

# Which pokemon (the name) is Snoodle most similar to? Save it in an object named snoodle_name
____
____