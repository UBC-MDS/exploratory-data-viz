import altair as alt
import pandas as pd


temps_df = pd.read_csv('data/temperature.csv', parse_dates=['date'])
print(temps_df.iloc[:5, :5])
print(temps_df.iloc[:5, 5:])