import altair as alt
import pandas as pd


temps_df = pd.read_csv('data/temperature.csv', parse_dates=['date'])

temp_plot = alt.Chart(temps_df).mark_circle(size=50).encode(
    alt.X('date', 
        title="Date"),
    alt.Y('total_rain_mm',
        title='rainfall total for the month (mm)'),
    alt.Color('mean_temp',
        title=' Mean Temperature',
        scale=alt.Scale(scheme='blueorange'))
    ).properties(title='Hotter months tend to have higher levels of rainfall')

line_plot = alt.Chart(temps_df).mark_line(size=1, color='grey').encode(
    alt.X('date'),
    alt.Y('total_rain_mm'))

temp_plot + line_plot

