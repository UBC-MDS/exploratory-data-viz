import altair as alt
import pandas as pd


penguins_df = pd.read_csv('data/penguins.csv')

mass_boxplot = alt.Chart(penguins_df).mark_boxplot().encode(
    alt.X('body_mass_g', title='Mass (grams)'),
    alt.Y('species', title='Species')).properties(
         title='Body mass among penguin species', height=200, width=400)

mass_boxplot