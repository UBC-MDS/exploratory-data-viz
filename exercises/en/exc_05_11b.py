import altair as alt
import pandas as pd


income_df = pd.read_csv('data/income_expenditure.csv')

income_log_plot = alt.Chart(____).____(____).encode(
    alt.Y(____,
          axis=____,
          title=____,
          scale=____),
    alt.X(____,
          axis=____,
          title=____,
          scale=____)
).properties(title=____)

income_log_plot