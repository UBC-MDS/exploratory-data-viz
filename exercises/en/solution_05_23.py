import altair as alt
import pandas as pd
from calendar import month_name

temps_df = pd.read_csv('data/temperature.csv', parse_dates=['date'])
temps_df = temps_df.assign(month=temps_df['date'].dt.month_name())

top_month = temps_df.groupby('month')['total_rain_mm'].sum().idxmax()

rain_plot = alt.Chart(temps_df).mark_bar().encode(
    alt.X('sum(total_rain_mm)',
    title="Total rainfall per month (mm)"),
    alt.Y('month', sort=list(month_name), title=None),
    color=alt.condition(alt.datum.month == top_month,
                        alt.value('darkslateblue'),
                        alt.value('powderblue'))
).properties(
    title='Between 2009-2012, May had the greatest total rainfall collectively')

text_plot = rain_plot.mark_text(align='left', dx=4).encode(
    text=alt.Text('sum(total_rain_mm)', format='d'),
    color = alt.value('black'))

(rain_plot + text_plot).configure_view(strokeWidth=0)