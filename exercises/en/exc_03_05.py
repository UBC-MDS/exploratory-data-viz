import altair as alt
import pandas as pd


penguins_df = pd.read_csv('data/penguins.csv').dropna(subset=['sex'])

culmen_layered_plot = alt.Chart(___).mark_bar(___).encode(
    ___,
    ___,
    ___
    ).___(___, width=230, height=200
    ).___(___, ___
    ).___

culmen_layered_plot
