import altair as alt
import pandas as pd


penguins_df = pd.read_csv('data/penguins.csv')

mass_density_plot = alt.Chart(penguins_df).transform_density(
     'body_mass_g',
     groupby=['island'],
     as_=['body_mass_g', 'density'],
     steps=100
     ).mark_area(opacity=0.5).encode(
          alt.X('body_mass_g', title='Mass (grams)'),
          alt.Y('density:Q', title='Density'),
          alt.Color('island', title='Antarctic Island')).properties(
               title="Penguin mass among species")

mass_density_plot