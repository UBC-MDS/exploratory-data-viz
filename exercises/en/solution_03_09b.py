import altair as alt
import pandas as pd


penguins = pd.read_csv('data/penguins.csv')

mass_faceted_plot = alt.Chart(penguins).transform_density(
     'body_mass_g',
     groupby=['island','species'],
     as_=['body_mass_g', 'density'],
     steps=100
     ).mark_area(opacity=0.5).encode(
         x='body_mass_g',
         y='density:Q',
         color='island').properties(
              title='body mass distribution by species and island',
              width=150).facet('species')

mass_faceted_plot