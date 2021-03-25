import altair as alt
import pandas as pd
from vega_datasets import data


# The data sources
gapminder_df = pd.read_csv('data/gapminder_codes.csv', parse_dates=['year'])
world_df = alt.____(data.world_110m.url, ____)

# The map
world_plot = (
    alt.Chart(____).____().encode(
        alt.____('____:Q', scale=alt.____(scheme=____, ____=____)),
        tooltip=[alt.Tooltip('____:N', title=____),
                 alt.Tooltip('____:Q', title='Life Expectancy (years)')]
    ).____(
        lookup=____,
        from_=alt.LookupData(____, 'id', [____, ____]))
).properties(width=580, height=400,
             title='African countries tend to have below average life expectancies'
).____(type=____).configure_legend(orient='bottom')

world_plot