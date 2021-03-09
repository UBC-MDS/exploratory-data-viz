import altair as alt
import pandas as pd


penguins_df = pd.read_csv('data/penguins.csv')

mass_faceted_plot = alt.Chart(___).___(
     'body_mass_g',
     groupby=___,
     ___=['body_mass_g', 'density'],
     steps=___
     ).___(___=0.5).encode(
         ___,
         ___='density:Q',
         color=___).___(
              ___='body mass distribution by species and island',
              ___).___(___, ___)

mass_faceted_plot
