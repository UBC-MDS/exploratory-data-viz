import altair as alt
import pandas as pd
from vega_datasets import data


# Scroll to the bottom of this cell to layout the next 4 plots

# Loading in the data
penguins_df = pd.read_csv('data/penguins.csv').dropna(subset=['sex', 'species'])

# Density plot
mass_density_plot = alt.Chart(penguins_df).transform_density(
     'body_mass_g',
     groupby=['species'],
     as_=['body_mass_g', 'density'],
     steps=100
     ).mark_area(opacity=0.5).encode(
          alt.X('body_mass_g', title='Mass (grams)'),
          alt.Y('density:Q', title='Density'),
          alt.Color('species', title='Species', legend=alt.Legend(orient="right"))
          ).properties(width=400, height=100)

# Boxplot
mass_boxplot = alt.Chart(penguins_df).mark_boxplot(opacity=0.5).encode(
    alt.X('culmen_length_mm', title='Culmen length (mm)', scale=alt.Scale(zero=False)),
    alt.Y('species'),
    alt.Color('species', legend=None)
    ).properties( height=100, width=180)

# Heatmap
penguin_heatmap = alt.Chart(penguins_df).mark_rect().encode(
    alt.X('flipper_length_mm', bin=alt.Bin(maxbins=30), title='Flipper length (mm)'),
    alt.Y('body_mass_g', bin=alt.Bin(maxbins=30), title='Penguin mass (g)'),
    alt.Color('count()', title='Quantity', scale=alt.Scale(scheme='blues'))
    ).properties(width=150, height=100)

# Histograms   
culmen_facet_plot = alt.Chart(penguins_df.dropna(subset=['sex', 'species'])).mark_bar(opacity=0.5).encode(
    alt.X('culmen_depth_mm', bin=alt.Bin(maxbins=40), title= 'Culmen depth (mm)'),
    alt.Y('count()', stack=None, title='Number of penguins'),
    alt.Color('species', title = 'Species')
    ).properties(width=180, height=100
    ).facet('sex', title='').resolve_scale(y='independent')

# Titles for full visualization
titles = alt.TitleParams(
    "We've discovered many insights from the Penguins dataset",
     subtitle = ["We've learned that the Adelie and Chinstrap penguin",
                 " species are have similar culmen depth and body mass, however quite different culmen length"],
     fontSize=18, align='center', anchor='middle')


# Organize the plots above so it looks like the example provided above.
combined_plot = (____).____(title=titles)

combined_plot