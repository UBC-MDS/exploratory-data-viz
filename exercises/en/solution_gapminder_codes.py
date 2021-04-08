import altair as alt
import pandas as pd
from vega_datasets import data

# The data sources
gapminder_df = pd.read_csv('data/gapminder_codes.csv', parse_dates=['year'])
gapminder_df.info()