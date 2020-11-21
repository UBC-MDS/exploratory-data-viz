import pandas as pd
import altair as alt
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split, cross_validate

# Loading in the data
pokemon_df = pd.read_csv('data/pokemon.csv')

# Define X and y
X = pokemon_df.drop(columns = ['deck_no', 'name','total_bs', 'type', 'legendary'])
y = pokemon_df['legendary']

# Split the dataset
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=33)

results_dict = {"n_neighbors": [], "mean_train_score": [], "mean_cv_score": []}

# Create a for loop and fill in the blanks
for k in range(1,50,5):
    model = KNeighborsClassifier(n_neighbors=k)
    scores = cross_validate(model, X_train, y_train, cv=10, return_train_score=True)
    results_dict["n_neighbors"].append(k)
    results_dict["mean_cv_score"].append(scores["test_score"].mean())
    results_dict["mean_train_score"].append(scores["train_score"].mean())

# Wrangles the data into a form suitable for plotting 
results_df = pd.DataFrame(results_dict).melt(id_vars=['n_neighbors'],
                                             value_vars=['mean_train_score',
                                                         'mean_cv_score'], 
                                             var_name='split',
                                             value_name='score')

# Create a chart that plots depth vs score
chart1 = alt.Chart(results_df).mark_line().encode(
         alt.X('n_neighbors:Q', axis=alt.Axis(title="Number of Neighbours")),
         alt.Y('score:Q', scale=alt.Scale(domain=[.95, 1.00])), 
         alt.Color('split:N', scale=alt.Scale(domain=['mean_train_score',
                                                     'mean_cv_score'],
                                             range=['teal', 'gold'])))
chart1