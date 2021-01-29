import altair as alt
import pandas as pd


penguins = pd.read_csv('data/penguins.csv')
print(penguins.iloc[:5, :4])
print(penguins.iloc[:5, 4:])
