import altair as alt
import pandas as pd


penguins_df = pd.read_csv('data/penguins.csv')

penguin_hist = alt.Chart(____).____().encode(
    x=alt.X(____, ____),
    y='____',
    ).properties(____='Flipper length among Penguins', ____=300, height=____)

penguin_hist

