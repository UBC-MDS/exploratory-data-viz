import altair as alt
import pandas as pd


income_df = pd.read_csv('data/income_expenditure.csv')

income_log_plot = alt.Chart(income_df).mark_circle(opacity=0.5, size=10).encode(
    alt.X('tot_income',
          axis=alt.Axis(format='s'),
          title='Income (PHP)',
          scale=alt.Scale(type='symlog')),
    alt.Y('education_expenditure',
          axis=alt.Axis(format='s'),
          title='Education expenditure (PHP)',
          scale=alt.Scale(type='symlog'))
).properties(
    title='The filipino population with higher income will generally spend more on education')

income_log_plot