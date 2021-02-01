import altair as alt
import pandas as pd


penguins_df = pd.read_csv('data/penguins.csv')

mass_density_plot = alt.Chart(___).transform_density(
    ___,
    groupby=___,
    ___=['body_mass_g', 'density'],
    ___=100
    ).mark_area(___).encode(
        x=___,
        ___,
        colour=___).properties(___)

mass_density_plot
