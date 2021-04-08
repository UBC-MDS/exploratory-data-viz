import altair as alt
import pandas as pd
from vega_datasets import data


# The data sources
gapminder_df = pd.read_csv('data/gapminder_codes.csv', parse_dates=['year'])
world_df = alt.topo_feature(data.world_110m.url, 'countries')

# The map
pop_dense_plot = (
    alt.Chart(world_df).mark_geoshape().encode(
        alt.Color('pop_density:Q',
                  scale=alt.Scale(scheme='blueorange', domainMid=81),
                  title='Population Density (people/Km^2)')
    ).transform_lookup(
        lookup='id',
        from_=alt.LookupData(gapminder_df, 'id', ['pop_density']))
).properties(width=580, height=340,
            title='Country population densities are higher in Europe and parts of Asia and Africa'
            ).project(scale=80, translate=[290, 240]).configure_legend(orient='bottom')

pop_dense_plot