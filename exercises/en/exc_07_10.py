import altair as alt
import pandas as pd


penguins_df = pd.read_csv('data/penguins.csv')

slider = alt.____(name=.____, max=max(penguins_df.____))
select_rating = alt.____(
    fields=[____],
    bind=____)

slider_scatter = (alt.Chart(penguins_df).mark_circle().encode(
    alt.X('culmen_length_mm', title='Culmen length (mm)', scale=alt.Scale(zero=False)),
    alt.Y('culmen_depth_mm', title='Culmen depth (mm)', scale=alt.Scale(zero=False)),
    color='species',
    opacity=alt.condition(____ < ____, alt.value(0.7), alt.value(0.05)))
    .add_selection(____))

slider_scatter