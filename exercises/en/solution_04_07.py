import altair as alt
import pandas as pd


pokemon_df = pd.read_csv('data/pokemon.csv')

pokemon_cicleplot = alt.Chart(pokemon_df).mark_circle().encode(
    alt.X('gen:O', title='Generation'),
    alt.Y('type', title='Type'),
    alt.Color('count()', title='Number of Pokemon'),
    alt.Size('count()', title='Number of Pokemon')
    ).properties(title='Number of Pokemon types per generation')
    
pokemon_cicleplot