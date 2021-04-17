import altair as alt
import pandas as pd


penguins_df = pd.read_csv('data/penguins.csv')

click = alt.selection_multi(fields=['island'], bind='legend')

click_legend = (alt.Chart(penguins_df).mark_bar().encode(
    alt.X('count()', title='Number of Penguins'),
    alt.Y('island', title=None, sort='x'),
    alt.Color('island', title="Island"),
    alt.Row('species', title=None),
    opacity=alt.condition(click, alt.value(0.9), alt.value(0.2)))
.add_selection(click)).properties(width=300)

click_legend