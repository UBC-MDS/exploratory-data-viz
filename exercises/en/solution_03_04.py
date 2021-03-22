import altair as alt
import pandas as pd


penguins_df = pd.read_csv('data/penguins.csv').dropna(subset=['sex'])

culmen_stacked_plot = alt.Chart(penguins_df).mark_bar().encode(
    alt.X('culmen_depth_mm', bin=alt.Bin(maxbins=30), title='Culmen depth (mm)'),
    alt.Y('count()'),
    color='species'
    ).properties(title="Penguin culmen depth distributions among species", width=230, height=200
    )

culmen_stacked_plot
