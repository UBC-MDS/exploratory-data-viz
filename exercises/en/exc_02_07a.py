import altair as alt
from vega_datasets import data


cars = data.cars()

fuel_efficiency = alt.Chart(____).____().encode(
    x=____,
    y='____').properties(____=____)

____