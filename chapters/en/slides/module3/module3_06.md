---
type: slides
---

# Using density plots to visualize distributions

Notes: In this slide deck, we will see how to use density plots instead
of histograms to represent distributions of data.

---

## Histograms can give different results depending on the data

[From
scikit-learn](https://scikit-learn.org/stable/auto_examples/neighbors/plot_kde_1d.html)

<img src=/module3/histogram-and-shifted.png></img>

Notes: How many observations are counted per bar in a histogram depends
on exactly where on the axis the border between the bins are.

In the images on this slide, the actual observations are drawn with
black tick marks on the bottom and they are the same in both subplots.

The only reason the histograms appear to be different is that the
borders between the bins are shifted in the rightmost picture.

As we can see here, a histogram is not as unbiased of a plot as we might
think at first. Especially if we have few data points, where the
inclusion or exclusion of just a few points makes a big difference for
the bar heights.

---

## Centering the bins on the data can help create more accurate distribution plots

[From Kimberly Fessel’s DataViz
videos](https://www.youtube.com/watch?v=DCgPRaIDYXA)

<img src=/module3/kde-buildup.gif></img>

Notes: Instead of setting fixed lines along the axis and then count
points fully in one bin or another, we can create bins that are centred
on the data and then add the bins together.

When we center bins on the data, we often use bell-shaped bins instead
of square ones as in the histogram. This removes noise or spikes in the
plotted area, which could arise when using a square bin.

These spikes are often not informative for us when trying to get an idea
of what the distribution looks like, and a smoother area is more
conducive to conveying the overall shape of the data distribution.

The bell-shaped bins (also called kernels) are then added together as in
the animation in this slide so that they sum up to an overall
distribution line. Formally, this is called a “Kernel Density Estimate”
(KDE), or just a “density plot”.

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
“Are there differences in movie runtimes between genres?”.

As we have seen previously, histograms are not effective for this type
of comparison between distributions, no matter if they are stacked or
layered.

We could use faceting to answer this question, but sometimes we want to
dedicate the separate facets for another categorical dataframe column,
as we will do later in this slide deck.

While row and column-based faceting would be possible, those plots
require a lot of space. Here we will instead explore how we can use
density plots, to effectively visualize both single and multiple
distributions.

---

## Creating a density plot in Altair requires two steps

``` python
import altair as alt

(alt.Chart(movies).transform_density(
    'runtime',
    as_=['runtime', 'density'])
 .mark_area().encode(
    x='runtime',
    y='density:Q'))
```

<iframe src="/module3/charts/06/unnamed-chunk-2.html" width="100%" height="420px" style="border:none;">
</iframe>

Notes: To create a density plot, we need to complete two tasks:

1.  Place the bell-shaped bins and add them together as in the animation
    a few slides ago.
2.  Plot a line or area mark for the newly calculated sum of bins.

In Altair, these operations are done in two explicit steps, using
`transform_density` for the calculation.

First, we specify which dataframe column we want to use for the
calculation. Then we use the `as_` parameter to name the newly
calculated values, which we here refer to as `'density'`.

Since the `'density'` values are not part of the pandas dataframe,
Altair cannot ask pandas which data type it is. Therefore, we need to
add `':Q'` to indicate that the density has quantitative values, just as
when we specified the data types in module 2.

We could also have calculated the sum of the bell-shaped bins as a
separate step outside Altair and added it as a new column in our pandas
dataframe, but it is more convenient to do both the steps in Altair.

We can see that this plot looks similar to the histogram we created in
the last slide deck, and we would reach similar conclusions when
studying it. Most movies peak around 100 min, but there is great
variation all the way from \~25 to \~215 min.

In contrast to a histogram, the y-axis of a density plot is not very
informative.

The definition of a density entails that the area under the curve should
sum up to 1, which represents all the observations.

Therefore the y-axis is simply adjusted based on the values on the
x-axis, so that the area equals 1.

Instead of looking at the y-axis, focus on the shape of the area and the
x-axis, those are the more informative in a density plot.

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

<iframe src="/module3/charts/06/unnamed-chunk-3.html" width="100%" height="420px" style="border:none;">
</iframe>

Notes: If we want to split and colour the densities by a categorical
dataframe column, we need to explicitly specify a dataframe column to
the `groupby` parameter when calculating the density.

Setting this parameter to the same column we use for the colour encoding
will compute one density for each of the differently coloured areas.

This plot effectively conveys the differences between runtimes of movies
from different genres.

Notably, we can see that the peaks are different locations on the x-axis
for the three genres. This indicates that the most common movie lengths
are different between genres.

This difference appears to be around 20 min, but it does not necessarily
tell us where the mean and median would fall, since that also depends on
where the rest of the values are distributed.

We can see that the Animation genre has the highest peak, which means
that the values are the most densely packed around the peak in this
distribution compared to the others. But we can only see the range of
the History distribution, since this is plotted on top of the others.

Let’s make the areas less opaque so that we can see the range of all the
distributions.

---

## Slightly transparent areas reveal more details

``` python
(alt.Chart(movies).transform_density(
     'runtime',
     groupby=['genre'],
     as_=['runtime', 'density'],
     steps=200)
 .mark_area(opacity=0.5).encode(
     x='runtime',
     y='density:Q',
     color='genre'))
```

<iframe src="/module3/charts/06/unnamed-chunk-4.html" width="100%" height="420px" style="border:none;">
</iframe>
<!-- #region -->

Notes: The density areas don’t suffer the same issues as the histograms
when made transparent. The continuous solid shape for each group is
easier to follow even when it is semi-transparent and overlaps with the
other areas.

The transparency gives us the advantage of knowing that there is not
small density area completely hiding behind a bigger one and we can also
see the range of all the distributions.

For example, we can tell that there are some Fantasy movies that are
almost as long as the longest History movies, whereas there is not a
single Animation movie that is longer than 120 minutes.

However, if we had more distributions to compare, a semi-transparent
density plot would become hard to decipher. In such cases, we could
either filter the data to plot fewer distributions or facet them
vertically as we saw with the histograms previously.

---

## Changing the number of density steps adjusts the smoothness of the curve

<!-- #endregion -->

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

<iframe src="/module3/charts/06/unnamed-chunk-5.html" width="100%" height="420px" style="border:none;">
</iframe>

Notes: In the previous slide, we can see that the density curves are a
bit jagged rather than perfectly smooth.

This is because, in the calculation of the density, we can indicate how
many steps along the curve the density should be calculated for. This
can be more intuitive to understand if we think of the extreme cases:

If we calculated a density for only a single step, there would be a
straight line between the start and endpoint, and for two steps there
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

<iframe src="/module3/charts/06/unnamed-chunk-6.html" width="100%" height="420px" style="border:none;">
</iframe>

Notes: If we instead increased the number of steps, we could make the
density curves appear smoother. Since a density is an approximation of
the true distribution underlying our data, it makes sense to set the
number of steps so that the areas appear smooth.

However, more steps take more computing power since there are more
calculations to make. If we are working with a large data set or
creating many plots, we might therefore want to decrease this value
slightly.

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

<iframe src="/module3/charts/06/unnamed-chunk-7.html" width="100%" height="420px" style="border:none;">
</iframe>

Notes: Since density plots don’t show the number of observations, they
can be misleading for small data sets where they will still appear
smooth as if there were many data points to back up that smoothness.

When looking at this plot, are you be able to tell that the density is
made up of just ten observations?

In Altair, a hint that a density is made up of few observations is the
sharp borders of the areas. This happens because the default behaviour
in Altair is to end the density where the data ends, which often creates
sharp borders for low numbers of observations.

Many other plotting packages instead, extend the density beyond the
observations in the dataset to make it appear smoother and it is
therefore paramount to always ask how many observations there are before
interpreting a density plot.

---

## Densities can be combined with plotting individual data points

``` python
(density.mark_area(opacity=0.7) + alt.Chart(movies[:10]).mark_tick(color='black', yOffset=140).encode(x='runtime'))
```

<iframe src="/module3/charts/06/unnamed-chunk-8.html" width="100%" height="420px" style="border:none;">
</iframe>

Notes:

Since it is so hard to tell how many observations are in a density plot,
you should always check this separately. Strategies to do this include
looking at the number of rows in the dataframe, creating a separate
histogram, or layering the density plot together with a plot of the
individual data points.

Here we are using `mark_tick` to plot every single observation along the
x-axis and making the density area transparent so that we can see the
tick marks. By default, the ticks would be in the middle of the plot, so
we are using `yOffset` to align them with the x-axis.

With as few as 10 observations, we actually don’t need the density at
all and could instead just have shown the individual observations or
created a histogram.

---

## Scaling densities by the numbers of observations is possible but not very effective

``` python
(alt.Chart(movies[:10]).transform_density(
    'runtime',
    as_=['runtime', 'density'],
    counts=True)
 .mark_area().encode(
    x='runtime',
    y='density:Q'))
```

<iframe src="/module3/charts/06/unnamed-chunk-9.html" width="100%" height="420px" style="border:none;">
</iframe>

Notes: In Altair, we could actually scale the density plots by the count
of observations by specifying `counts=True` inside the
`transform_density`.

However, since a density is a continuous area counts are not as easy to
interpret as in a histogram where there is an exact count for each
discrete bin.

As we can see in this example, the y-axis has been scaled by 10, but it
is still hard to interpret, are there 0.08 movies with a runtime of 110
min?

Although densities can be scaled by count, it is often confusing, which
means we must be careful when interpreting them and always check how
many observations are in the data by plotting the individual data
points!

---

# Let’s apply what we learned!

Notes: <br>
