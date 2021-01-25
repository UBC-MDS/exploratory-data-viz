import altair as alt
from vega_datasets import data


cars = data.cars()

alt.Chart(cars).mark_point().encode(
    x='Weight_in_lbs',
    y='Horsepower',
    color='Origin')
