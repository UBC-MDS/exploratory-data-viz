import altair as alt
import pandas as pd


temps_df = pd.read_csv('data/temperature.csv', parse_dates=['date'])

temp_plot = alt.Chart(temps_df).____(____).encode(
    alt.X('date', ____),
    alt.Y('total_rain_mm', ____),
    alt.____(____, ____, ____)
    ).properties(title=____)

temp_plot 
