import altair as alt
from vega_datasets import data


stocks = data.stocks()

print(stocks.head())

price_lineplot = alt.Chart(stocks).mark_line().encode(
    x='date',
    y='price',
    color='symbol')

price_lineplot