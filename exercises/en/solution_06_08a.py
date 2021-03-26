import altair as alt
import pandas as pd
from vega_datasets import data


# The data sources
world_df = alt.topo_feature(data.world_110m.url, 'countries')

# The map
world_plot = alt.Chart(world_df).mark_geoshape(
).project(type='equalEarth'
).properties(width=580, height=400,
            title='World Map'
            )
world_plot