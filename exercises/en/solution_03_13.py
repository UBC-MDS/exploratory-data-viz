import altair as alt
import pandas as pd


penguins = pd.read_csv('data/penguins.csv')

mass_boxplot = alt.Chart(penguins).mark_boxplot().encode(
    alt.X('body_mass_g'),
    alt.Y('species')).properties(
         title='Body mass among penguin species', height=200)

mass_boxplot