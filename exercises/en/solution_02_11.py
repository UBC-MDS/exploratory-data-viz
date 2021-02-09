import altair as alt
import pandas as pd


penguins = pd.read_csv('data/penguins.csv')

penguin_bar = alt.Chart(penguins).mark_bar().encode(
    x='count()',
    y=alt.Y('species', sort='x')
    ).properties(title='Frequency of penguin species', width=300, height=150)

penguin_bar