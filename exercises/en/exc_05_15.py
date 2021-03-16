import altair as alt
import pandas as pd


penguins_df = pd.read_csv('data/penguins.csv')

colour_plot = alt.Chart(penguins_df).mark_point(____).encode(
    alt.X('flipper_length_mm', 
          scale=____, 
          title=____),
    alt.Y('body_mass_g', 
          scale=____, 
          title=____),
    alt.____('species', ____, ____),
    alt.____('species')
).properties(____)

colour_plot


