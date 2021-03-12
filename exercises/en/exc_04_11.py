import altair as alt
import pandas as pd


penguins_df = pd.read_csv('data/penguins.csv')

# Obtain all the labels of the numeric columns in a list
# Name the list numeric_cols
numeric_cols = ____

# Next repeat a histogram plot for every numeric column on the x axis
numeric_histograms = alt.Chart(____).____().____(
     alt.X(____),
     alt.Y(____),
     ).properties(____
     ).____(____)
         
____