import altair as alt
import pandas as pd


penguins_df = pd.read_csv('data/penguins.csv')

penguin_heatmap = alt.Chart(____).____().encode(
    alt.X(____,  bin=____, title=____),
    alt.Y(____,  bin=____, title=____),
    alt.Color(____, title=____)
    ).____(title=____, ____=250, =____=200)
   
penguin_heatmap 