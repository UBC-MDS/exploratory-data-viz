import altair as alt
import pandas as pd


penguins_df = pd.read_csv('data/penguins.csv').dropna(subset=['sex'])

culmen_layered_plot = alt.Chart(penguins_df).mark_bar(opacity=0.5).encode(
    alt.X('culmen_depth_mm', bin=alt.Bin(maxbins=30), title= 'Culmen depth (mm)'),
    alt.Y('count()', stack=None, title='Number of penguins'),
    alt.Color('species', title='Species')
    ).properties(title="Penguin culmen depth distributions among species", width=230, height=200
    ).facet('sex', columns=1
    ).resolve_scale(y='independent')

culmen_layered_plot