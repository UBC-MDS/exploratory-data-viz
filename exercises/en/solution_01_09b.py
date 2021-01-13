import altair as alt
from vega_datasets import data


stocks = data.stocks()

stocks_line = alt.Chart(stocks).mark_line().encode(
    x='date',
    y='price',
    color='symbol')

stocks_line + stocks_line.mark_point()
