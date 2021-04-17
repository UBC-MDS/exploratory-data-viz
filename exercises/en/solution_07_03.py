import altair as alt
import pandas as pd


penguins_df = pd.read_csv('data/penguins.csv')

brush = alt.selection_interval()

linked_scatter = (alt.Chart(penguins_df).mark_circle().encode(
    alt.X('body_mass_g', title='Body mass (g)', scale=alt.Scale(zero=False)),
    alt.Y('flipper_length_mm', title='Flipper length (mm)', scale=alt.Scale(zero=False)),
    color=alt.condition(brush, 'species', alt.value('lightgray')))
    .add_selection(brush))
    
together_plots = (linked_scatter &
                  linked_scatter.encode(alt.X('culmen_length_mm',
                                              title='Culmen length (mm)',
                                              scale=alt.Scale(zero=False)),
                                       alt.Y('culmen_depth_mm',
                                             title='Culmen depth (mm)',
                                             scale=alt.Scale(zero=False))))
together_plots