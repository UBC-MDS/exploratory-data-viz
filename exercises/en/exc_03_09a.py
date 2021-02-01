import altair as alt
import pandas as pd


penguins = pd.read_csv('data/penguins.csv')

mass_density_plot = alt.Chart(___).transform_density(
    ___,
    ___,
    ___,
    ___
    ).mark_area(___).encode(
        ___,
        ___,
        ___).___

mass_density_plot
