import altair as alt
import pandas as pd


income_df = pd.read_csv('data/income_expenditure.csv')

income_plot = alt.Chart(income_df).mark_circle(____).encode(
    alt.Y('tot_income',
          axis=____,
          title=____),
    alt.X('education_expenditure',
          axis=____,
          title=____)
).properties(title=____)

income_plot