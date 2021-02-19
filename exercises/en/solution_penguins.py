import altair as alt
import pandas as pd


penguins_df = pd.read_csv('data/penguins.csv')
print(penguins_df.iloc[:5, :4])
print(penguins_df.iloc[:5, 4:])