import altair as alt
import pandas as pd


penguins_df = pd.read_csv('data/penguins.csv')

penguin_hist = alt.Chart(penguins_df).mark_bar().encode(
    x=alt.X('flipper_length_mm', bin=True),
    y='count()',
    ).properties(title='Flipper length among Penguins', width=300, height=150)

penguin_hist