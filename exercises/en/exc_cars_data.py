import altair as alt
from vega_datasets import data


cars = data.cars()

print(cars.columns)
cars.head()