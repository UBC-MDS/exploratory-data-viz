import altair as alt
import pandas as pd


penguins_df = pd.read_csv('data/penguins.csv')

penguin_facet = alt.Chart(____).____().encode(
    x=____('body_mass_g', ____),
    y=____,
    ).properties(____='Penguin mass', ____, ____
    ).____(____=____, ____='island')

penguin_facet
