import pandas as pd
import altair as alt
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split, cross_validate

# Loading in the data
bball_df = pd.read_csv('data/bball.csv')
bball_df = bball_df[(bball_df['position'] =='G') | (bball_df['position'] =='F')]

# Define X and y
X = bball_df.loc[:, ['height', 'weight', 'salary']]
y = bball_df['position']

# Split the dataset
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=33)

results_dict = {"depth": [], "mean_train_score": [], "mean_cv_score": []}

# Create a for loop and fill in the blanks
for depth in range(1,20):
    model = DecisionTreeClassifier(max_depth=depth)
    scores = cross_validate(model, X_train, y_train, cv=10, return_train_score=True)
    results_dict["depth"].append(depth)
    results_dict["mean_cv_score"].append(scores["test_score"].mean())
    results_dict["mean_train_score"].append(scores["train_score"].mean())

# Wrangles the data into a form suitable for plotting 
results_df = pd.DataFrame(results_dict).melt(id_vars=['depth'],
                                             value_vars=['mean_train_score',
                                                         'mean_cv_score'], 
                                             var_name='split',
                                             value_name='score')

# Create a chart that plots depth vs score
chart1 = alt.Chart(results_df).mark_line().encode(
         alt.X('depth:Q', axis=alt.Axis(title="Tree Depth")),
         alt.Y('score:Q', scale=alt.Scale(domain=[.80, 1.00])), 
         alt.Color('split:N', scale=alt.Scale(domain=['mean_train_score',
                                                     'mean_cv_score'],
                                             range=['teal', 'gold'])))
chart1