---
type: slides
---

# Using density plots to visualize distributions

Notes: In this module we will see how to use density plots instead of
histograms to represent distributions of data.

---

## Histograms can give different results depending on the data

<img src=/module3/histogram-and-shifted.png></img>

[From
scikit-learn](https://scikit-learn.org/stable/auto_examples/neighbors/plot_kde_1d.html)

Notes: How many observations are counted per bar in a histogram depends
on exactly where on the axis the border between the bins are.

In the images on this slide, the actual observations are drawn with
black tick marks on the bottom and they are the same in both subplots.

The reason the histograms look different is that the border between the
groups is shifted in the rightmost picture.

As we see here, a histogram is not an as unbiased plot as we might think
at first, especially not if we have few data points, where the inclusion
or exclusion of just a few points makes a big difference for the bar
height.

---

## Centering the bins on the data can help create more accurate distribution plots

<img src=/module3/kde-buildup.gif></img>

Notes: Instead of setting fixed lines along the axis and then count
plots fully in one bin or another, we can create bins that are centered
on the data and then add them together.

When we center bins on the data, we also usually have a round shape
instead of a square one, which gives the impression of a smoother
distribution that is more conducive to communicating the shape of the
data distribution.

The round bins (also called kernels) are then added together as in the
gif in this slide, and sum up to an overall distribution line. Formally,
this is called a Kernel Density Estimate (KDE), or just a density plot.

---

## The movies dataset

``` python
import pandas as pd


movies = pd.read_csv('movies.csv')
movies
```

```out
                                                 title  runtime     budget     revenue      genre                   country  vote_average
0                                         Finding Nemo      100   94000000   940335536  Animation  United States of America          3.86
1    Pirates of the Caribbean: The Curse of the Bla...      143  140000000   655011224    Fantasy  United States of America          3.81
2                                   The Simpsons Movie       87   75000000   527068851  Animation  United States of America          3.44
3           Pirates of the Caribbean: Dead Man's Chest      151  200000000  1065659812    Fantasy  United States of America          3.47
4                                        Mars Attacks!      106   70000000   101371017    Fantasy  United States of America          2.96
..                                                 ...      ...        ...         ...        ...                       ...           ...
524                                     The Dark Tower       95   60000000    71000000    Fantasy  United States of America          3.20
525                                              Sully       96   60000000   238470033    History  United States of America          3.75
526                                    The Emoji Movie       86   50000000    66913939  Animation  United States of America          0.63
527                                    A Dog's Purpose      100   22000000   194647323    Fantasy  United States of America          3.61
528                           Batman: The Killing Joke       72    3500000     3775000  Animation  United States of America          2.94

[529 rows x 7 columns]
```

Notes: We will be using the movies dataset again, let’s see if we can
make a plot that is easier to interpret than the layered histograms from
the end of the last slide deck.

---

## Creating a density plot in Altair required two step

``` python
import altair as alt

(alt.Chart(movies).transform_density(
    'runtime',
    as_=['runtime', 'density'])  # Give a name to the KDE values, which we can use when plotting
 .mark_area().encode(
    x='runtime',
    y='density:Q'))
```

<iframe src="/module3/charts/02/unnamed-chunk-2.html" width="100%" height="420px" style="border:none;">
</iframe>

Notes: To visualize a density plot, we need to do two things:

1.  Calculate the KDE (adding the individual kernels and summing them
    together)
2.  Plot a line or area mark for the newly calculated KDE values.

In Altair, these operations are done in two explicit steps, using
`transform_density` for the calculation. We could also have calculated
this as a new column in our pandas data frame and then plotted that
column, but it is convenient to do both the steps in Altair.

The new variable we create is called `'density'`, and since this is not
part of the pandas data frame, Altair cannot ask pandas which data type
it is. Therefore, we need to add `':Q'` to indicate that the density has
quantitative (numeric) values.

---

## Creating a grouped density plot requires an explicit density grouping

``` python
(alt.Chart(movies).transform_density(
     'runtime',
     groupby=['genre'],
     as_=['runtime', 'density'])
 .mark_area().encode(
     x='runtime',
     y='density:Q',
     color='genre'))
```

<iframe src="/module3/charts/02/unnamed-chunk-3.html" width="100%" height="420px" style="border:none;">
</iframe>

Notes: If we want to split and colour the densities by a categorical
variable, we need to add an explicit `groupby` column when calculating
the density. This computes one density per colour variable (`genre` in
this case), that will then be coloured accordingly since we used the
same variable for the colour argument.

In this plot, it is quite easy to see the relationship between movie
lengths of different genres. The history genre has the longest running
movies as well as the most variation whereas most animation moves are
shorter and with less spread within the genre.

There are still a few things we could tweak to improve this plot!

---

## Creating smoother density plots with more calculation steps

``` python
(alt.Chart(movies).transform_density(
     'runtime',
     groupby=['genre'],
     as_=['runtime', 'density'],
     steps=200)
 .mark_area().encode(
     x='runtime',
     y='density:Q',
     color='genre'))
```

<iframe src="/module3/charts/02/unnamed-chunk-4.html" width="100%" height="420px" style="border:none;">
</iframe>

Notes: To make the curves smoother, we can increase the resolution over
which the KDE is calculated by setting the step size to a higher number.

Now there will be 200 points calculated, which gives the area a smoother
appearance.

---

## Making the overlapping areas slightly transparent make them easier to interpret

``` python
(alt.Chart(movies).transform_density(
     'runtime',
     groupby=['genre'],
     as_=['runtime', 'density'],
     steps=200)
 .mark_area(opacity=0.4).encode(
     x='runtime',
     y='density:Q',
     color='genre'))
```

<iframe src="/module3/charts/02/unnamed-chunk-5.html" width="100%" height="420px" style="border:none;">
</iframe>

Notes: The density areas don’t suffer the same issues as the histograms
when made transparent. The continuous solid shape is easier to follow
even when it is semi transparent overlaps with the other areas.

The transparency gives us the advantage of knowing that there is not
small density area hiding behind a bigger one.

---

## The y-axis does not indicate a meaningful value for density plots

``` python
(alt.Chart(movies).transform_density(
     'runtime',
     groupby=['genre', 'country'],
     as_=['runtime', 'density'])
 .mark_area().encode(
     x='runtime',
     y='density:Q',
     color='genre')
 .properties(height=265).facet('country'))
```

<iframe src="/module3/charts/02/unnamed-chunk-6.html" width="100%" height="420px" style="border:none;">
</iframe>

Notes: If we facet these, you will notice that they look quite different
from the faceted histograms in the previous slide deck. This is because
the density rather than the count is shown by default on the y-axis.
Showing the density means that it is easier for us to compare the shape
of the distributions but is not really a useful numbers for us to know.

---

## Density plots of small datasets can be misleading

``` python
(alt.Chart(movies[:10]).transform_density(
    'runtime',
    as_=['runtime', 'density'])  # Give a name to the KDE values, which we can use when plotting
 .mark_area().encode(
    x='runtime',
    y='density:Q'))
```

<iframe src="/module3/charts/02/unnamed-chunk-7.html" width="100%" height="420px" style="border:none;">
</iframe>

Notes: Since density plots don’t show the number of observations, they
can be very misleading for small data sets as they will still appear
smooth as if there were many data points to back up that smoothness.

When looking at this plot, are you be able to tell that the density is
made up of just ten observations?

It is a little bit easier in Altair to tel this, because the default is
to end the density where the data ends, which often creates sharp
borders as in this plot.

This is a great default in Altair, but many other plotting packages
instead extend the density beyond the observations in the dataset to
make it more smooth and it is therefore paramount to always ask how many
observations there are before interpreting a density plot.

---

## The density can be scaled by the count

``` python
(alt.Chart(movies).transform_density(
     'runtime',
     groupby=['genre', 'country'],
     as_=['runtime', 'density'],
     counts=True)
 .mark_area().encode(
     x='runtime',
     y='density:Q',
     color='genre')
 .properties(height=240).facet('country'))
```

<iframe src="/module3/charts/02/unnamed-chunk-8.html" width="100%" height="420px" style="border:none;">
</iframe>

Notes: In Altair, we could actually scale the density plots by the count
of observations, why does make the y-axis easier to interpret.

However, this only gives and indication of how many observations there
are for different parts of the density and it is not as easy to
interpret this y-value as in a histogram where there is and exact count
in each discrete bin.

Although densities can be scaled by count, they rarely are, which means
we must be careful when interpreting them and always check how many
observations are in the data!

---

# Let’s apply what we learned!

Notes: <br>
