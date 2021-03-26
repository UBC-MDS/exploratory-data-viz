import altair as alt
import pandas as pd
from vega_datasets import data


# The data sources
world_df = alt.____(data.world_110m.url, ____)

# The map
world_plot = alt.Chart(____).____(
).____(type=____
).properties(width=580, height=400,
            title='World Map'
            )

world_plot