import altair as alt
import pandas as pd


penguins_df = pd.read_csv('data/penguins.csv')

colour_plot = alt.Chart(____).____(____).encode(
    alt.X(____, 
          scale=____, 
          title=____),
    alt.Y(____, 
          ____, 
          ____),
    alt.____(____, ____),
    alt.____(____)
).properties(____)

colour_plot


