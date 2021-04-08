import altair as alt
import pandas as pd
from vega_datasets import data


# The data sources
gapminder_df = pd.read_csv('data/gapminder_codes.csv', parse_dates=['year'])
world_df = alt.____(data.world_110m.url, ____)

# The map
pop_dense_plot = (
    alt.Chart(____).____().encode(
        alt.____('____:Q',
                  ____=alt.Scale(scheme=____, domainMid=____),
                  title='Population Density (people/Km^2)')
    ).____(
        lookup='id',
        from_=alt.____(____, 'id', [____]))
).properties(width=580, height=340,
            title='Country population densities are higher in Europe and parts of Asia'
            ).____(____=80, translate=[290, 240]).configure_legend(orient='bottom')

pop_dense_plot