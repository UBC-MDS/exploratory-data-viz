import altair as alt
import pandas as pd


penguins = pd.read_csv('data/penguins.csv').dropna(subset=['sex'])

culmen_layered_plot = alt.Chart(penguins).mark_bar(opacity=0.5).encode(
    alt.X('culmen_depth_mm', bin=alt.Bin(maxbins=30)),
    alt.Y('count()', stack=None),
    color='species'
    ).properties(title="Penguin culmen depth distributions among species", width=230, height=200
    ).facet('sex'
    ).resolve_scale(y='independent')

culmen_layered_plot