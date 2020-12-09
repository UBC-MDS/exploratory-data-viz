import altair as alt
from vega_datasets import data


stocks = data.stocks()

___ = alt.Chart(stocks).mark_line().encode(
    x='date',
    y='price',
    color='symbol')

___ + ___
