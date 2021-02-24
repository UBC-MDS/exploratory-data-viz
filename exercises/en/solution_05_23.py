import altair as alt
import pandas as pd
from calendar import month_name

temps_df = pd.read_csv('data/temperature.csv', parse_dates=['date'])
temps_df = temps_df.assign(month=temps_df['date'].dt.month_name())

rain_plot = alt.Chart(temps_df).mark_bar().encode(
    alt.X('sum(total_rain_mm)',
    title="Total rainfall per month (mm)"),
    alt.Y('month', sort=list(month_name), title=None),
    color=alt.condition(alt.datum.month == 'July',
                        alt.value('darkslateblue'),
                        alt.value('powderblue'))
).properties(
    title='Between 2008-2010, September had the greatest total precipitation collectively')

text_plot = rain_plot.mark_text(align='left', dx=5).encode(
    text=alt.Text('sum(total_rain_mm)', format='d'),
    color = alt.value('black'))

(rain_plot + text_plot).configure_view(strokeWidth=0)