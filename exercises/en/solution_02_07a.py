import altair as alt
from vega_datasets import data


cars = data.cars()

fuel_efficiency = alt.Chart(cars).mark_area().encode(
    x='Year',
    y='mean(Miles_per_Gallon)').properties(title="Fuel efficiency over time")

fuel_efficiency