import altair as alt
import pandas as pd


penguins_df = pd.read_csv('data/penguins.csv').dropna(subset=['sex'])

culmen_stacked_plot = ___.___.___.encode(
    alt.X(___),
    alt.Y(___),
    color=___
    ).properties(___, width=230, height=200
    )

culmen_stacked_plot
