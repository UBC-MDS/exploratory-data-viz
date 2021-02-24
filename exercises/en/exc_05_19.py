import altair as alt
import pandas as pd


temps_df = pd.read_csv('data/temperature.csv', parse_dates=['date'])

temp_plot = alt.Chart(____).____(____).encode(
    alt.X(____, ____),
    alt.Y(____, ____),
    alt.____(____, ____, ____)
    ).____(title=____)

line_plot = alt.Chart(____).____(____).encode(
    alt.X(____),
    alt.Y(____))

temp_plot + line_plot
