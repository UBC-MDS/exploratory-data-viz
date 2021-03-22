import altair as alt
import pandas as pd


penguins_df = pd.read_csv('data/penguins.csv')

# Obtain all the labels of the columns with dtype object in a list
# Name the list cat_cols
cat_cols = penguins_df.select_dtypes('object').columns.tolist()

# Next create histogram pairplots for every categorical column
categorical_plots = alt.Chart(penguins_df).mark_circle().encode(
     alt.X(alt.repeat('column'), type='nominal'),
     alt.Y(alt.repeat('row'), type='nominal'),
     alt.Color('count()', title=None),
     alt.Size('count()', title=None)
     ).repeat(row=cat_cols, column=cat_cols
     ).resolve_scale(color='independent', size='independent')
    
categorical_plots