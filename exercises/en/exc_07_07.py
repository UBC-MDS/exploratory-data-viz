import altair as alt
import pandas as pd


penguins_df = pd.read_csv('data/penguins.csv')

click = alt.selection_multi(fields=____, bind=____)

click_legend = (alt.Chart(penguins_df).mark_bar().encode(
    alt.X('count()', title='Number of Penguins'),
    alt.Y('island', title=None, sort=____),
    alt.Color(____, title="Island"),
    alt.Row('species', title=None),
    opacity=alt.condition(____, ____, ____))
.add_selection(____)).properties(width=300)

click_legend