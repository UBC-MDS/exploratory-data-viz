import altair as alt
import pandas as pd


penguins_df = pd.read_csv('data/penguins.csv')

# Obtain all the labels of the numeric columns in a list
# Name the list numeric_cols
numeric_cols = penguins_df.select_dtypes('number').columns.tolist()

# Next repeat a histogram plot for every numeric column on the x axis
numeric_histograms = alt.Chart(penguins_df).mark_bar().encode(
     alt.X(alt.repeat(), type='quantitative', bin=alt.Bin(maxbins=30)),
     alt.Y('count()'),
     ).properties(width=150, height=150
     ).repeat(numeric_cols, columns=2)
    
numeric_histograms
