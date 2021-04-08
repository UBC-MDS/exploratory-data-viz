import altair as alt
import pandas as pd


penguins_df = pd.read_csv('data/penguins.csv')

penguin_facet = alt.Chart(penguins_df).mark_bar().encode(
    x=alt.X('body_mass_g', bin=alt.Bin(maxbins=15)),
    y='count()',
    ).properties(title='Penguin mass', width=150, height=100
    ).facet(column='species', row='island')

penguin_facet
