import altair as alt
import pandas as pd


penguins_df = pd.read_csv('data/penguins.csv')


penguin_title = alt.TitleParams(
    "Google's stock experiencing heavier fluctuations than competitors",
     subtitle = "Prices have been surging since 2009 but have still not reached the same levels as in late 2007.",
     fontSize=18, subtitleColor='steelblue', subtitleFontWeight='bold')


base = alt.Chart(penguins_df, penguin_title).mark_line().encode(
    alt.X('species'),
    alt.Y('count()'))


texts = alt.Chart(penguins_df).mark_text(align='top', dx=2).encode(
    alt.X('species'),
    alt.Y('count()'),
    alt.Text('count()'))

(base + text).configure_view(strokeWidth=0)