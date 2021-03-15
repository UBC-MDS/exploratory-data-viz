import altair as alt
import pandas as pd


penguins_df = pd.read_csv('data/penguins.csv')


# The base plot 
base = alt.Chart(penguins_df).mark_bar().encode(
    alt.Y('species', title=None),
    alt.X('count()', title='Number of penguins'))
base

# Create added text 
text = alt.Chart(____).____(____, ____).encode(
alt.____('species'),
alt.____('count()'),
alt.____(____))

# Set up the title and subtitle formatting
penguin_title = alt.____(
    ____,
    ____,
    ____,
    subtitleColor=____)

formatted_plot = (base + text).configure_view(____=0
).properties(height=200, width=300, title=penguin_title)

formatted_plot