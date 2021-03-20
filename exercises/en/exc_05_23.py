import altair as alt
import pandas as pd
from calendar import month_name

temps_df = pd.read_csv('data/temperature.csv', parse_dates=['date'])
temps_df = temps_df.assign(month=temps_df['date'].dt.month_name())

top_month = temps_df.groupby('month')['total_precipitate_mm'].sum().idxmax()

rain_plot = alt.Chart(temps_df).____().encode(
    alt.X('sum(total_rain_mm)',
    title=____),
    alt.Y('month', sort=list(month_name), title=None),
    ____=alt.condition(____ == ____, ____, ____)
).properties(____)

text_plot = rain_plot.____(____, ____).encode(
    text=alt.Text(____, format=____),
    color = ____(____))

(rain_plot + text_plot).configure_view(strokeWidth=0)