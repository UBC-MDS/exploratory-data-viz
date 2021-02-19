import altair as alt
import pandas as pd


income_df = pd.read_csv('data/income_expenditure.csv')

income_plot = alt.Chart(income_df).mark_circle(opacity=0.5, size=10).encode(
    alt.X('tot_income',
          axis=alt.Axis(format='s'),
          title='Income (PHP)'),
    alt.Y('education_expenditure',
          axis=alt.Axis(format='s'),
          title='Education expenditure (PHP)'),
).properties(
    title="There is substantial variation in the Filipino population's income")

income_plot