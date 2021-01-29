import altair as alt
import pandas as pd


penguins = pd.read_csv('data/penguins.csv').dropna(subset=['sex'])

culmen_plot = alt.Chart(penguins).mark_bar(opacity=0.4).encode(
    alt.X('culmen_depth_mm', bin=alt.Bin(maxbins=30)),
    alt.Y('count()', stack=None),
    color='species'
    ).facet('sex'
    ).resolve_scale(y='independent'
    ).properties(title="Penguin culmen depth distributions among species")

culmen_plot