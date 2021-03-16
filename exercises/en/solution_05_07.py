import altair as alt
import pandas as pd


penguins_df = pd.read_csv('data/penguins.csv')


# The base plot 
base = alt.Chart(penguins_df).mark_bar().encode(
    alt.Y('species', title=None),
    alt.X('count()', title='Number of penguins'))
base

# Create added text 
text = alt.Chart(penguins_df).mark_text(align='center', dx=10).encode(
    alt.Y('species'),
    alt.X('count()'),
    alt.Text('count()'))

# Set up the title and subtitle formatting
penguin_title = alt.TitleParams(
    "Adelie Penguins species most abundant in the Antarctic",
     subtitle = "The Chinstrap species appears to have the lowest penguin population.",
     fontSize=18,
     subtitleColor='firebrick')

formatted_plot = (base + text).configure_view(strokeWidth=0
).properties(height=200, width=300, title=penguin_title)

formatted_plot