import altair as alt
import pandas as pd


penguins_df = pd.read_csv('data/penguins.csv')

slider = alt.binding_range(name='Body mass (g)', max=max(penguins_df['body_mass_g']))
select_rating = alt.selection_single(
    fields=['body_mass_g'],
    bind=slider)

slider_scatter = (alt.Chart(penguins_df).mark_circle().encode(
    alt.X('culmen_length_mm', title='Culmen length (mm)', scale=alt.Scale(zero=False)),
    alt.Y('culmen_depth_mm', title='Culmen depth (mm)', scale=alt.Scale(zero=False)),
    color='species',
    opacity=alt.condition(alt.datum.body_mass_g < select_rating.body_mass_g,
                          alt.value(0.7), alt.value(0.05)))
    .add_selection(select_rating))

slider_scatter