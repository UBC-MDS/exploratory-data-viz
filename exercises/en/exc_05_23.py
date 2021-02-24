import altair as alt
import pandas as pd
from calendar import month_name

temps_df = pd.read_csv('data/temperature.csv', parse_dates=['date'])
temps_df = temps_df.assign(month=temps_df['date'].dt.month_name())

rain_plot = alt.Chart(____).____().encode(
    alt.X(____,
    title=____),
    alt.Y(____, sort=list(month_name), title=None),
    ____=alt.condition(____ == ____, ____, ____)
).____(____)

text_plot = rain_plot.____(____, ____).encode(
    text=alt.Text(____, format=____),
    color = ____(____))

(rain_plot + text_plot).configure_view(strokeWidth=0)