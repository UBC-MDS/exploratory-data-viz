import altair as alt
import pandas as pd


penguins_df = pd.read_csv('data/penguins.csv')

penguin_heatmap = alt.Chart(____).____().encode(
    alt.X(____),
    alt.Y(____),
    alt.Color(____)
    ).____(____)
   
penguin_heatmap 