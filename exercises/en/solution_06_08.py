import altair as alt
import pandas as pd
from vega_datasets import data


# The data sources
gapminder_df = pd.read_csv('data/gapminder_codes.csv', parse_dates=['year'])
world_df = alt.topo_feature(data.world_110m.url, 'countries')

# The map
world_plot = (
    alt.Chart(world_df).mark_geoshape().encode(
        alt.Color('life_expectancy:Q', scale=alt.Scale(scheme='redblue', domainMid=72)),
        tooltip=[alt.Tooltip('country:N', title='Country'),
                 alt.Tooltip('life_expectancy:Q', title='Life Expectancy (years)')]
    ).transform_lookup(
        lookup='id',
        from_=alt.LookupData(gapminder_df, 'id', ['life_expectancy', 'country']))
).properties(width=580, height=400,
            title='African countries tend to have below average life expectancies'
            ).project(type='equalEarth').configure_legend(orient='bottom')

world_plot