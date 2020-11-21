import pandas as pd


candybar_df = pd.read_csv('data/candybars.csv')

print(candybar_df.head())

candybar_dim = candybar_df.shape
print(candybar_dim)