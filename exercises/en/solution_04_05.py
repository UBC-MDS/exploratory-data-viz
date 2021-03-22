import altair as alt
import pandas as pd


penguins_df = pd.read_csv('data/penguins.csv')

penguin_heatmap = alt.Chart(penguins_df).mark_rect().encode(
    alt.X('flipper_length_mm', bin=alt.Bin(maxbins=30), title='Flipper length (mm)'),
    alt.Y('body_mass_g', bin=alt.Bin(maxbins=30), title='Penguin mass (g)'),
    alt.Color('count()', title='Penguin quantity')
    ).properties(title="Body mass and flipper length among Antartic penguins",
     width=250, height=200
    )
   
penguin_heatmap 