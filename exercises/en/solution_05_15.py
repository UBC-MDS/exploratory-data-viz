import altair as alt
import pandas as pd


penguins_df = pd.read_csv('data/penguins.csv')

colour_plot = alt.Chart(penguins_df).mark_point(size=10).encode(
    alt.X('flipper_length_mm', 
          scale=alt.Scale(domain=[160, 240]), 
          title="Flipper length (mm)"),
    alt.Y('body_mass_g', 
          scale=alt.Scale(domain=[2500, 6500]), 
          title='Mass (grams)'),
    alt.Color('species', title='Penguin species', scale=alt.Scale(scheme='set2')),
    alt.Shape('species')
).properties(
    title='Gentoo penguins tend to have the longest flippers and weight the most among the penguin species.')

colour_plot