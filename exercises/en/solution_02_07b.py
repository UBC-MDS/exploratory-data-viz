import altair as alt
from vega_datasets import data


cars = data.cars()


fuel_efficiency_org = alt.Chart(cars).mark_line().encode( # Or mark_area() would also be acceptable
    x='Year',
    y='mean(Miles_per_Gallon)',
    color = 'Origin').properties(title="Average origin fuel efficiency over time")

fuel_efficiency_org