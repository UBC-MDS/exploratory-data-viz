import altair as alt
import pandas as pd


penguins_df = pd.read_csv('data/penguins.csv')

colour_plot = alt.Chart(penguins_df).mark_point(size=10).encode(
    alt.X('flipper_length_mm', 
          scale=alt.Scale(domain=[140, 240]), 
          title="Flipper length (mm)"),
    alt.Y('culmen_length_mm', 
          scale=alt.Scale(domain=[25, 65]), 
          title='Culmen length (mm)'),
    alt.Color('species', title='Penguin species', scale=alt.Scale(scheme='set2')),
    alt.Shape('species')
).properties(
    title='Gentoo penguins tend to have the longest flipper length among Antarctic penguins')

colour_plot
