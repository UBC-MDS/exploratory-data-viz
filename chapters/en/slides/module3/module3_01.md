---
type: slides
---

# Visualizing data from one column

Notes: In the previous modules we have seen how graphical marks in
Altair can be used to create plots and we learned about which visual
channels are effective for displaying data.

Now that you are equipped with this knowledge and can create your own
plots, we will dive deeper into when it is appropriate to use certain
charts instead of others.

---

## The movies dataset

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

Notes: For this module, we will study a dataset of movies containing
each movie’s title, runtime, budget, revenue, genre, country of
production, and average user rating.

Upon see this table, there are several questions that might come to
mind, e.g.

-   Are high budget movies more profitable?
-   Do some countries make more movies of certain genres?
-   Are some genres rated higher than others?

Before diving into these comparisons, we want to understand the data for
each of the columns in our dataset.

Let’s start by looking at the ratings the movies received and explore
the best ways to visualize this data.

---

## Visualizing a single column with a point plot along one axis

``` python
import altair as alt

alt.Chart(movies[:5]).mark_point().encode(
    x='runtime')
```

<iframe src="/module3/charts/01/unnamed-chunk-2.html" width="100%" height="400px" style="border-width:0;">
</iframe>

Notes: Visualizing data distributions are useful in understanding the
measurements of a variable, as doing this allows us to quickly and
easily see the range and frequency of values that occur.

One of the simplest visualizations to understand a distribution of a
single dataframe variable is to plot each individual observations as a
point.

This is similar to a scatter plot, but only using one of the plot axes.

It works well when there are just a few plots to visualize, which is why
we subset the data in this slide.

---

## Single axis point plots can become saturated when there is a lot of data to plot

``` python
alt.Chart(movies[:50]).mark_point().encode(
    x='runtime')
```

<iframe src="/module3/charts/01/unnamed-chunk-3.html" width="100%" height="400px" style="border-width:0;">
</iframe>

Notes: When there are more observations, it becomes really hard to see
which ones are where since the circular marks are overlapping with each
other.

When it becomes hard to tell individual observations apart, we say that
a plot become saturated. We will talk more about this concept later in
the module.

---

## Thinner marks avoids saturation

``` python
alt.Chart(movies[:50]).mark_tick().encode(
    x='runtime')
```

<iframe src="/module3/charts/01/unnamed-chunk-4.html" width="100%" height="400px" style="border-width:0;">
</iframe>

Notes: It is often easier to separate individual observations when they
are represented as thin tick marks instead of the thick points as in the
previous slide.

The disadvantage of this plot type is that it can be a bit harder to see
individual observations. However, when we are visualization many marks,
we are often more interested in how the data is shaped (or distributed)
in general, rather than looking at individual points.

This type of plot with vertical tick marks along one axis is so common
that it is sometimes referred to by a special name: rugplot.

The visualization grammar of Altair let’s us think about it more
intuitively by composing it with a mark and a single encoding, instead
of remembering a specific name.

---

## Thinner marks also saturate for large data sets

``` python
alt.Chart(movies).mark_tick().encode(
    x='runtime')
```

<iframe src="/module3/charts/01/unnamed-chunk-5.html" width="100%" height="400px" style="border-width:0;">
</iframe>

Notes: However, when we increase the number of observations even further
(to about 500) it becomes difficult to tell exactly how the data
distribution looks, even with these thin marks.

---

## Using histograms to visualize distributions avoids saturation issues

``` python
alt.Chart(movies).mark_bar().encode(
    alt.X('runtime', bin=alt.Bin(maxbins=30)),
    y='count()')
```

<iframe src="/module3/charts/01/unnamed-chunk-6.html" width="100%" height="400px" style="border-width:0;">
</iframe>

Notes: Instead of visualizing each individual observation, we can use
the histograms we learnt about in last module, where we divide one axis
into groups (or “bins”) and represent the count of observations in each
group with bar.

In this plot, we can directly see that most movies are around 100 min in
length, because all the highest bars are around this value.

We would say that this distribution has a single peak around 100 min.
Some distributions has multiple peaks which are not necessarily in the
center of the distribution, and some have no distinct peaks at all, but
are instead more uniformly distributed.

From our experience, we know that factors such as genre and production
year, can influence movie length and we also see wide variation in the
length of movies in the plot.

The shortest movie is just 20-30 min long, while the longest is
somewhere between 2010 and 220 minutes.

How can we separate the data based on other columns in the dataset and
compare multiple distributions?

---

## Comparing multiple distributions via faceting

``` python
(alt.Chart(movies).mark_bar().encode(
    alt.X('runtime', bin=alt.Bin(maxbins=30)),
    y='count()')
 .facet('country'))
```

<iframe src="/module3/charts/01/unnamed-chunk-7.html" width="100%" height="400px" style="border-width:0;">
</iframe>

Notes: Let’s start by comparing the movie length broken down per
country. As we saw in the last module, faceting is a good way to compare
multiple distributions and here we use it to create one histogram per
country.

This is a little bit of repetition, but we will discuss the histograms
in more detail in these slides now that we have learned more about what
they represent.

You can see that this particular dataset only contains movies made in
the UK or the US. Because there are so many more movies made in the US
compared to the UK, it is quite hard to tell if there are any meaningful
differences between movies from the two countries.

The location of the distribution on the x-axis looks quite similar, but
we can’t say if the location and number of peaks, and the overall shape
of the distribution is the same from this visualization.

---

## Comparing multiple distributions via faceting with independent y-axes

``` python
(alt.Chart(movies).mark_bar().encode(
    alt.X('runtime', bin=alt.Bin(maxbins=30)),
    y='count()')
 .facet('country')
 .resolve_scale(y='independent'))
```

<iframe src="/module3/charts/01/unnamed-chunk-8.html" width="100%" height="400px" style="border-width:0;">
</iframe>

Notes: By default when faceting, the y-axis is the same for all the
subplots. This is often the most suitable choice, because it gives us an
idea of both the shape of the distribution and the total number of
observations.

If we want to drill down and compare the distribution shape more closely
regardless of the number of observations we could define the y-axes to
be independent for each subplot, instead of linked to the same axis
range, as we have done in this slide.

Now we can get a better view of the UK histogram. it looks like the UK
one could be slightly bimodal (it has two peaks), whereas the US one is
unimodal (it has one peak).

However, since we have such few observations, we can’t state this with
much confidence; it might just be an artifact of which intervals the
bins are set to cover or from the small sample number.

To be more certain about if there are any meaningful differences between
these two histograms, we would need to have a larger sample set from the
UK and create multiple visualizations each with a different number of
maxbins to see if that changes the histogram appearance.

Maybe there are other groups in the dataset that would better explain
the spread in movie length that we saw in the initial histogram?

In the next module we will explore if there are more distinct
differences in movie length based on which genre the movies belong to
rather than its production country.

---

# Let’s apply what we learned!

Notes: <br>
