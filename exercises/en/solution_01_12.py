import pandas as pd


# Loading in the data
candybar_df = pd.read_csv('data/candybars.csv')

X = candybar_df.loc[:, 'chocolate':'multi']
y = candybar_df['availability']

print(X.head())
print(y.head())