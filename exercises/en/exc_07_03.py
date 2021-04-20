import altair as alt
import pandas as pd


penguins_df = pd.read_csv('data/penguins.csv')

brush = ____

linked_scatter = (alt.Chart(____).mark_circle().encode(
    alt.X(____, title=____, scale=alt.Scale(zero=False)),
    alt.Y(____, title=____, scale=alt.Scale(zero=False)),
    color=alt.condition(____, 'species', alt.value('lightgray')))
    .add_selection(____))
    
together_plots = (____ &
                 ____.encode(alt.X(____,
                             title=____,
                             scale=alt.Scale(zero=False)),
                             alt.Y(____,
                             title=____, scale=alt.Scale(zero=False))))
together_plots