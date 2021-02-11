import altair as alt
import pandas as pd


penguins_df = pd.read_csv('data/penguins.csv')

# Obtain all the labels of the numeric columns in a list
# Name the list numeric_cols
numeric_cols = penguins_df.select_dtypes('number').columns.tolist()

# Next repeat a plot for every numeric column on the x and y axis.
numeric_heatmap = alt.Chart(penguins_df).mark_rect().encode(
     alt.X(alt.repeat('column'), type='quantitative'),
     alt.Y(alt.repeat('row'), type='quantitative')
     ).properties(width=150, height=150
     ).repeat(column=numerical_columns, row=numerical_columns)
    
numeric_heatmap