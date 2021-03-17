import altair as alt
import pandas as pd


penguins_df = pd.read_csv('data/penguins.csv')

# Obtain all the labels of the columns with dtype object in a list
# Name the list cat_cols
____ = ____

# Next create histogram pairplots for every categorical column
categorical_plots = alt.Chart(____).____().encode(
     alt.X(____, type=____),
     alt.Y(____, type=____),
     alt.____(____, title=None),
     alt.____(____, title=None)
     ).____(____=____, ____=____
     ).resolve_scale(____='independent', ____='independent')
    
____