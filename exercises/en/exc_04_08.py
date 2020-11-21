import pandas as pd
from sklearn.metrics.pairwise import ____

# Loading in the data
pokemon_df = pd.read_csv('data/pokemon.csv')

# Define X and y
X = pokemon_df.drop(columns = ['deck_no', 'name','total_bs', 'type', 'legendary'])
y = pokemon_df['legendary']


# Calculate the Euclidean distance of the first 2 pokemon 
# Save it in an object named pk_distance
____ =____
____