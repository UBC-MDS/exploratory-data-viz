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

When we center bins on the data, we often use bell-shaped bins instead
of square ones as in the histogram. This removes noise or spikes in the
plotted area, which could arise when using a square bin.

These spikes are often not informative for us when trying to get an
overall idea of what the distribution looks like, and a smoother area is
more conducive to conveying the shape of the data distribution.

When we center bins on the data, we also usually have a round shape
instead of a square one, which gives the impression of a smoother
distribution that is more conducive to communicating the shape of the
data distribution.

The round bins (also called kernels) are then added together as in the
gif in this slide, and sum up to an overall distribution line. Formally,
this is called a Kernel Density Estimate (KDE), or just a density plot.

---

## Reading in the movies dataset

``` python
import pandas as pd

movies = pd.read_csv('data/movies.csv')
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

Notes: We will continue with the movies dataset in this slide deck, to
try to answer the question we posed at the end of the previous chapter:
“Are there differences in movie runtime between genres?”.

As we have seen previously, histograms are not effective for this type
of comparison between distributions, no matter if they are stacked or
layered.

We could use faceting to answer this question, but ideally we would
dedicate the separate facets for the countries so that we could also
explore the effect of genres within each country’s movies.

While row and column-based faceting would be possible, those plots
require a lot of space. Here we will instead explore a new type of
visualization, the “density plot”, which allows us to effectively
visualize both single and multiple distributions.

---

## Creating a density plot in Altair required two steps

``` python
import altair as alt

(alt.Chart(movies).transform_density(
    'runtime',
    as_=['runtime', 'density'])
 .mark_area().encode(
    x='runtime',
    y='density:Q'))
```

<iframe src="/module3/charts/02/unnamed-chunk-2.html" width="100%" height="400px" style="border-width:0;">
</iframe>

Notes: To visualize a density plot, we need to do two things:

1.  Calculate the bell-shaped bins and add them together as in the
    animation as few slides ago.
2.  Plot a line or area mark for the newly calculated sum of bins.

In Altair, these operations are done in two explicit steps, using
`transform_density` for the calculation.

First we specify which dataframe variable we want to use for the
calculation. Then we use the `as_` parameter to name the newly
calculated values, which we here call `'density'`.

Since the `'density'` variable is not part of the pandas dataframe,
Altair cannot ask pandas which data type it is. Therefore, we need to
add `':Q'` to indicate that the density has quantitative values.

We could also have calculated the sum of bins outside Altair and added
it as a new column in our pandas dataframe, but it is convenient to do
both the steps in Altair.

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

<iframe src="/module3/charts/02/unnamed-chunk-3.html" width="100%" height="400px" style="border-width:0;">
</iframe>

Notes: If we want to split and color the densities by a categorical
variable, we need to add an explicit `groupby` column when calculating
the density. This computes one density per color variable (`genre` in
this case), that will then be colored accordingly since we used the same
variable for the color argument.

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
     steps=2)
 .mark_area().encode(
     x='runtime',
     y='density:Q',
     color='genre'))
```

<iframe src="/module3/charts/02/unnamed-chunk-4.html" width="100%" height="400px" style="border-width:0;">
</iframe>

Notes: In the previous slide, we can see that the density curves are a
bit jagged rather than perfectly smooth.

This is because in the calculation of the density, we can indicate how
many steps along the curve the density should be calculated for. This
can be more intuitive to understand if we think of the extreme cases:

If we calculated a density for only a single step, there would be a
straight line between the start and end point, and for two steps there
the curve would have a single sharp peak like a triangle as you can see
in this slide.

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

<iframe src="/module3/charts/02/unnamed-chunk-5.html" width="100%" height="400px" style="border-width:0;">
</iframe>

Notes: If we instead increased the number of steps, we could make the
density curves appear smoother. Since a density is an approximation of
the true distribution underlying our data, it makes sense to set the
number of steps so that the areas appear smooth.

However, more steps takes more computing power since there are more
calculations to make. If we are working with a large data set or
creating many plots, we might therefore want to decrease the value
slightly

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

<iframe src="/module3/charts/02/unnamed-chunk-6.html" width="100%" height="400px" style="border-width:0;">
</iframe>

Notes: The density areas don’t suffer the same issues as the histograms
when made transparent. The continuous solid shape is easier to follow
even when it is semi transparent overlaps with the other areas.

The transparency gives us the advantage of knowing that there is not
small density area hiding behind a bigger one.

However, if we had more distributions to compare, a semi-transparent
density plot would become hard to decipher. In such cases we could
either filter the data to plot fewer distributions or facet them
vertically as we saw with the histograms previously.

---

## The y-axis does not indicate a meaningful value for density plots

``` python
(alt.Chart(movies).transform_density(
     'runtime',
     groupby=['genre', 'country'],
     as_=['runtime', 'density'],
     steps=200)
 .mark_area().encode(
     x='runtime',
     y='density:Q',
     color='genre')
 .properties(height=265).facet('country'))
```

<iframe src="/module3/charts/02/unnamed-chunk-7.html" width="100%" height="400px" style="border-width:0;">
</iframe>

Notes: If we facet these, you will notice that they look quite different
from the faceted histograms in the previous slide deck. This is because
the density rather than the count is shown by default on the y-axis.
Showing the density means that it is easier for us to compare the shape
of the distributions but is not really a useful numbers for us to know.

---

## Density plots of small datasets can be misleading

``` python
density = (alt.Chart(movies[:10]).transform_density(
    'runtime',
    as_=['runtime', 'density'])
 .mark_area().encode(
    x='runtime',
    y='density:Q'))
density
```

<iframe src="/module3/charts/02/unnamed-chunk-8.html" width="100%" height="400px" style="border-width:0;">
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

## Densities can be combined with plotting individual data points

``` python
(density.mark_area(opacity=0.7) + alt.Chart(movies[:10]).mark_tick(color='black', yOffset=140).encode(x='runtime'))
```

<iframe src="/module3/charts/02/unnamed-chunk-9.html" width="100%" height="400px" style="border-width:0;">
</iframe>

Notes:

Since it is so hard to tell how many observations are in a density plot,
you should always check this separately. Ways to do this include looking
at the number of rows in the dataframe, creating a separate histogram,
or layering the density plot together with a plot of the individual data
points.

Here we are using `mark_tick` to plot every single observation along the
x-axis and making the density area transparaent so that we can see the
tick marks. By default the ticks would be in the middle of the plot, so
we are using `yOffset` to align them with the x-axis.

With as few as 10 observations, we actually don’t need the density at
all and could instead just have showing the individual observations or
created a histogram.

---

# Scaling densities by the numbers of observations is possible but not very effective

Notes: <br>

``` python
(alt.Chart(movies[:10]).transform_density(
    'runtime',
    as_=['runtime', 'density'],
    counts=True)
 .mark_area().encode(
    x='runtime',
    y='density:Q'))
```

<iframe src="/module3/charts/02/unnamed-chunk-10.html" width="100%" height="400px" style="border-width:0;">
</iframe>

Notes: In Altair, we could actually scale the density plots by the count
of observations by specifying `counts=True` inside the
`transform_density`.

However, since a density is a continuous area counts are not as easy to
interpret as in a histogram where there is an exact count for each
discrete bin.

As we can see in this example, the y-axis has been scaled by 10, but we
don’t really know what it means, are there 0.08 observations at 110?

Although densities can be scaled by count, it is often confusing, which
means we must be careful when interpreting them and always check how
many observations are in the data by plotting the individual data
points!

---

# Let’s apply what we learned!

Notes: <br>
