import numpy as np
import pandas as pd
import altair as alt
alt.data_transformers.disable_max_rows()
from sklearn.tree import DecisionTreeClassifier

def plot_tree(X, y, model):
    # Join data for plotting
    sample = (X.join(y))
    # Create a mesh for plotting
    step = (X.max() - X.min()) / 50
    x1, x2 = np.meshgrid(np.arange(sample.min()[0]-step[0], sample.max()[0]+step[0], step[0]),
                         np.arange(sample.min()[1]-step[1], sample.max()[1]+step[1], step[1]))

    # Store mesh in dataframe
    mesh_df = pd.DataFrame(np.c_[x1.ravel(), x2.ravel()], columns=['x1', 'x2'])

    # Mesh predictions
    mesh_df['predictions'] = model.predict(mesh_df[['x1', 'x2']])

    # Plot
    scat_plot = alt.Chart(sample).mark_circle(
        stroke='black',
        opacity=1,
        strokeWidth=1.5,
        size=100
    ).encode(
        x=alt.X(X.columns[0], axis=alt.Axis(labels=True, ticks=True, title=X.columns[0])),
        y=alt.Y(X.columns[1], axis=alt.Axis(labels=True, ticks=True, title=X.columns[1])),
        color=alt.Color(y.columns[0])
    )
    base_plot = alt.Chart(mesh_df).mark_rect(opacity=0.5).encode(
        x=alt.X('x1', bin=alt.Bin(step=step[0])),
        y=alt.Y('x2', bin=alt.Bin(step=step[1])),
        color=alt.Color('predictions', title='Legend')
    ).properties(
        width=400,
        height=400
    )
    return alt.layer(base_plot, scat_plot).configure_axis(
        labelFontSize=20,
        titleFontSize=20
    ).configure_legend(
        titleFontSize=20,
        labelFontSize=20
    )