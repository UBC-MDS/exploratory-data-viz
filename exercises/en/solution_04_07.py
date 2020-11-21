import pandas as pd
from math import sqrt

# Loading in the data
pokemon_df = pd.read_csv('data/pokemon.csv')

# Define X and y
X = pokemon_df.drop(columns = ['deck_no', 'name','total_bs', 'type', 'legendary'])
y = pokemon_df['legendary']


# Subtract the two first pokemon feature vectors 
# Save it in an object name sub_pk
sub_pk = X.iloc[1] - X.iloc[0]

# Square the difference 
# Save it in an object named sq_sub_pk
sq_sub_pk = sub_pk ** 2

# Sum the squared difference from each dimension 
# Save the result in an object named sss_pk
sss_pk = sq_sub_pk.sum()

# Finally, take the square root of the entire calculation 
# Save it in an object named pk_distance
pk_distance = sqrt(sss_pk)

pk_distance