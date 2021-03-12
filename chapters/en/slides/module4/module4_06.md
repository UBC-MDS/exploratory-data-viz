---
type: slides
---

# Visualizing Categorical Distributions

Notes: In this slide deck, we will learn how to visualize categorical
distributions.

---

## Reading in the data

``` python
import altair as alt
import pandas as pd

movies_extended = pd.read_csv('data/movies-extended.csv')
movies_extended
```

```out
                           Title    US Gross  Worldwide Gross  US DVD Sales  Production Budget Release Date MPAA Rating  Running Time min           Distributor                     Source        Major Genre         Creative Type         Director  Rotten Tomatoes Rating  IMDB Rating  IMDB Votes
0             Boynton Beach Club   3127472.0        3127472.0           NaN          2900000.0  Mar 24 2006           R             104.0  Wingate Distribution        Original Screenplay    Romantic Comedy  Contemporary Fiction              NaN                     NaN          NaN         NaN
1                   Broken Arrow  70645997.0      148345997.0           NaN         65000000.0  Feb 09 1996           R             108.0      20th Century Fox        Original Screenplay             Action  Contemporary Fiction         John Woo                    55.0          5.8     33584.0
2                         Brazil   9929135.0        9929135.0           NaN         15000000.0  Dec 18 1985           R             136.0             Universal        Original Screenplay       Black Comedy               Fantasy    Terry Gilliam                    98.0          8.0     76635.0
3                  The Cable Guy  60240295.0      102825796.0           NaN         47000000.0  Jun 14 1996       PG-13              95.0         Sony Pictures        Original Screenplay             Comedy  Contemporary Fiction      Ben Stiller                    52.0          5.8     51109.0
4                 Chain Reaction  21226204.0       60209334.0           NaN         55000000.0  Aug 02 1996       PG-13             106.0      20th Century Fox        Original Screenplay             Action  Contemporary Fiction     Andrew Davis                    13.0          5.2     15817.0
...                          ...         ...              ...           ...                ...          ...         ...               ...                   ...                        ...                ...                   ...              ...                     ...          ...         ...
1185                  Zombieland  75590286.0       98690286.0    28281155.0         23600000.0  Oct 02 2009           R              87.0         Sony Pictures        Original Screenplay             Comedy               Fantasy  Ruben Fleischer                    89.0          7.8     81629.0
1186  Zack and Miri Make a Porno  31452765.0       36851125.0    21240321.0         24000000.0  Oct 31 2008           R             101.0         Weinstein Co.        Original Screenplay             Comedy  Contemporary Fiction      Kevin Smith                    65.0          7.0     55687.0
1187                      Zodiac  33080084.0       83080084.0    20983030.0         85000000.0  Mar 02 2007           R             157.0    Paramount Pictures  Based on Book/Short Story  Thriller/Suspense         Dramatization    David Fincher                    89.0          NaN         NaN
1188         The Legend of Zorro  45575336.0      141475336.0           NaN         80000000.0  Oct 28 2005          PG             129.0         Sony Pictures                     Remake          Adventure    Historical Fiction  Martin Campbell                    26.0          5.7     21161.0
1189           The Mask of Zorro  93828745.0      233700000.0           NaN         65000000.0  Jul 17 1998       PG-13             136.0         Sony Pictures                     Remake          Adventure    Historical Fiction  Martin Campbell                    82.0          6.7      4789.0

[1190 rows x 16 columns]
```

Notes: We’re continuing to work with the movies data set from the last
slide deck, but here we will focus on the categorical dataframe columns.

---

## Bar charts are effective for visualizing categorical “distributions” of a single column

``` python
alt.Chart(movies_extended).mark_bar().encode(
    alt.X('count()'),
    alt.Y('Major Genre', sort='x'))
```

<iframe src="/module4/charts/06/unnamed-chunk-2.html" width="100%" height="420px" style="border:none;">
</iframe>

Notes:

We have already seen examples of visualizing categorical distributions
when we used bar charts to plot the count of categories in previous
modules.

Although these plots represent categorical distributions, it’s good to
know that they are commonly referred to as just showing the counts of
the categories, rather than their “distribution”.

Here we have made a bar chart to answer the question “Which is the most
common genre among movies in this dataset?”.

We can see that the dataset consists of mostly comedies and dramas with
very few concert/performance films.

---

## Stacked bar charts can visualize counts for combinations of two categorical columns

``` python
alt.Chart(movies_extended).mark_bar().encode(
    alt.X('count()'),
    alt.Y('Major Genre', sort='x'),
    alt.Color('MPAA Rating'))
```

<iframe src="/module4/charts/06/unnamed-chunk-3.html" width="100%" height="420px" style="border:none;">
</iframe>

Notes:

What if we wanted to ask a more complex question that involves
visualizing the combinatorial counts of two categorical columns?

Our data contains the MPAA rating for each movie, which is
classification given by the Motion Picture Association indicating what
age groups a movie is suitable for:

-   G – General Audiences
-   PG – Parental Guidance Suggested
-   PG-13 – Parents Strongly Cautioned
-   R – Restricted

Do you think there are any differences in the proportions of ratings
between movie genres?

For example, we might already have a hypothesis that there won’t be any
horror movies that are appropriate for children.

To find out, we could color the bars according to the MPAA rating as in
this slide. However, one aspect of our chart is not very intuitive: the
color legend and the stacked bar segments are not sorted in the same
order.

---

## Reordering the bar segments aligns it with the order in the legend

``` python
alt.Chart(movies_extended).mark_bar().encode(
    alt.X('count()'),
    alt.Y('Major Genre', sort='x'),
    alt.Color('MPAA Rating'),
    alt.Order('MPAA Rating'))
```

<iframe src="/module4/charts/06/unnamed-chunk-4.html" width="100%" height="420px" style="border:none;">
</iframe>

Notes: Here we have reordered the bar segments using `alt.Order`, so
that they are in the same order as the legend. We could have opted to
reorder the legend instead, but it is more natural to start with the
rating for children (G) and proceed towards increasingly more mature
ratings.

In this chart we can see that most comedies are rated PG-13, most dramas
are rated R, that action movies almost only have movies rated either R
or PG-13

But this doesn’t really answer our question, which was if there are any
differences in the **proportions** of MPAA ratings **between** movie
genres?

While we can roughly see the relative proportions within a single bar,
it is quite hard to compare the colored segments between bars as
proportions since the bars are of different length.

It is also impossible to see the proportions in the genres with fewer
movies.

---

## Rescaling the bar lengths facilitates comparing proportions between bars

``` python
alt.Chart(movies_extended).mark_bar().encode(
    alt.X('count()', stack='normalize', title='Proportion of movies'),
    alt.Y('Major Genre', sort='x'),
    alt.Color('MPAA Rating'),
    alt.Order('MPAA Rating'))
```

<iframe src="/module4/charts/06/unnamed-chunk-5.html" width="100%" height="420px" style="border:none;">
</iframe>

Notes: Here we have changed the strategy for how the segments are
stacked together by setting `stack='normalize'`, which means to
normalize/rescale each bar to span the entire length of the x-axis and
label it as a proportion.

The plot looks quite unordered, because ‘x’ is not a meaningful way to
sort the bars when they are all the same length. Instead we would like
to sort them by the length of one of the colored segments.

---

## Sorting by the length of one of the colored segments make the chart easier to rea

``` python
sort_order = ['Adventure', 'Musical', 'Comedy', 'Romantic Comedy', 'Action',
              'Drama', 'Concert/Performance', 'Documentary', 'Western',
              'Thriller/Suspense', 'Horror', 'Black Comedy'] 
alt.Chart(movies_extended).mark_bar().encode(
    alt.X('count()', stack='normalize', title='Proportion of movies'),
    alt.Y('Major Genre', sort=sort_order),
    alt.Color('MPAA Rating'),
    alt.Order('MPAA Rating'))
```

<iframe src="/module4/charts/06/unnamed-chunk-6.html" width="100%" height="420px" style="border:none;">
</iframe>

Notes:

That’s much better! Sorting the chart in an intuitive order has once
again shown to be crucial for making our plot easier to interpret.

In a normalized stacked bar chart it makes sense to sort by either the
first or the last colored segment. Since not all genres have movies
rated `'G'`, we chose to set the order based on `'R'` instead.

If you are more interested in one genre than others, you could also
choose to sort by that genre.

Now we can directly compare the the length of individual bar segments
between the genres. We see that there certainly are differences in the
proportions of MPAA ratings between movies in different genres.

For the R rating, it is immediately obvious exactly how big these
differences are, and we can see that all black comedies are rated R,
while almost no adventure movies receive this rating.

It is a little bit harder to compare the other rating because the
colored segments do not share the same baseline. We can still see that
concerts and performance movies has the highest proportions of movies
that are kids-friendly at 50%, while musicals, documentaries, and action
movies have around 20% kids-friendly movies.

(We specified the sort order manually in this slide, because it is
rather advanced to extract this order using pandas, but we include an
example in the transcript if you are interested in how this could be
done:)

``` python
sort_order = (
    movies_extended
    .groupby('Major Genre')['MPAA Rating']
    .value_counts(normalize=True)
    .xs('R', level='MPAA Rating')
    .sort_values()
    .index
    .to_list())
```

---

## Normalize stacked bar charts are effective at visualizing just a few categories

``` python
sort_order = ['Concert/Performance', 'Musical', 'Documentary', 'Adventure', 
              'Comedy', 'Romantic Comedy', 'Drama',  'Action']
alt.Chart(movies_extended[movies_extended['MPAA Rating'].isin(['G', 'PG'])]).mark_bar().encode(
    alt.X('count()', stack='normalize', title='Proportion of movies'),
    alt.Y('Major Genre', sort=sort_order),
    alt.Color('MPAA Rating'),
    alt.Order('MPAA Rating'))
```

<iframe src="/module4/charts/06/unnamed-chunk-7.html" width="100%" height="420px" style="border:none;">
</iframe>

Notes: As with all charts, there are shortcoming to normalized stacked
bar charts as well. We saw in the last slide that it was a bit harder to
compare the colored segments that did not share a baseline versus the
segments at the ends where the baseline is the same.

This means that normalized stacked bar charts are ideal when there are
only two categories, since both segments will be easy to compare between
categories.

We can see an example in this slide where we filtered the dataset to
contain only movies rated either `'G'` or `'PG'`. It is easy to make
comparison for both the blue and the orange segments.

Stacked bar charts also work fine for 3-4 categories, but beyond that
they are usually ineffective. Even for 3-4 categories it is often
preferred to show the bars side by side instead of stacked.

---

## Showing bars side by side makes it easier to compare their exact heights within a category

``` python
(alt.Chart(movies_extended).mark_bar().encode(
    alt.X('count()', title=''),
    alt.Y('MPAA Rating', title=''),
    alt.Color('MPAA Rating', legend=None))
 .properties(width=100, height=45)
 .facet('Major Genre', columns=4)
 .resolve_scale(x='independent'))
```

<iframe src="/module4/charts/06/unnamed-chunk-8.html" width="100%" height="420px" style="border:none;">
</iframe>

Notes: It is not (yet) possible to pass a different value to `stack`,
which would put the bars next to each other. Instead, we could use
faceting as in this slide.

Here, we have also removed some of the axis title to make the figure
more compact and less crowded with text. You will learn more about
customizing elements such as titles in the next module.

By resolving the x-scale to be independent between the plots, the bar
height is not relative the max in each facet. This makes them easier to
compare **as proportions** both within and between facets while still
retaining an indication of the count on the x-axis.

If we wanted to compare the absolute counts between facets, we would
leave the axis axis at its default value: “shared”.

This type of visualization is effective when we want to accurately
compare the heights of bars **within** a genre. For example to answer
the question: “Which are the most common MPAA ratings for each genre?”.

---

## Switching the faceting and y column targets the plot towards a slightly different question

``` python
(alt.Chart(movies_extended).mark_bar().encode(
    alt.X('count()', title=''),
    alt.Y('Major Genre', title='', sort='x'),
    alt.Color('MPAA Rating', legend=None))
 .properties(width=100, height=150)
 .facet('MPAA Rating')
 .resolve_scale(x='independent'))
```

<iframe src="/module4/charts/06/unnamed-chunk-9.html" width="100%" height="420px" style="border:none;">
</iframe>

Notes: If we instead wanted to answer the question: “Which are the most
common genres for each MPAA Rating?”, we would switch the faceting and y
columns.

Here, we kept the color column as the MPAA Rating so that it is
consistent with the previous figures, and because with this many
categories, it would look quite messy if we colored by the Major Genre
instead.

We can see that the most common G-rated movies are adventure films, and
that most PG-13 rated movies are Comedies, Dramas and action movies. It
is important to remember that genres have more movies in total, so we
would expect them to show up highly in all the facets. Whether this is
desired or not depends on the question we are asking, but it does make
sense here.

---

## Heatmaps are effective for visualizing counts of two dimensional categorical data

``` python
alt.Chart(movies_extended).mark_rect().encode(
    alt.Color('count()'),
    alt.X('MPAA Rating'),
    alt.Y('Major Genre', sort='color'))
```

<iframe src="/module4/charts/06/unnamed-chunk-10.html" width="100%" height="420px" style="border:none;">
</iframe>

Notes:

If we want to get an overview of the information from both the faceted
plots in the previous two slides, we could create a heatmap. In this
heatmap the color represents the combinatorial counts of two categorical
columns, such as how many movies are both rated G and in the comedy
genre.

Comparing squares vertically in this heatmap is similar to the first
faceted plot we made and comparing them horizontally is similar to the
faceted visualization in the last slide.

In other words, if we want to compare which genre is most common for a
certain rating, we compare the colors *column-wise* in the heatmap. If
we instead are interested in the most common rating assigned to a movie
we compare the columns *row-wise*. We can quickly see that most dramas
are rated PG-13 or R and most horror movies are rated R.

Sorting on color/count puts the genres with many observations close
together, similar to how we sorted on `'x'` and `'y'` in previous
modules. We could sort the x-axis also, but since it has a natural order
to it, we have decided to keep it as is here.

This visualization is effective for quickly communicating the main
takeaways from the two questions and giving us an overview of the data,
but it is harder to tell that exact count for each color so if that is
of great importance a bar chart is more suitable.

---

## Using both the color and marker size to indicate the count creates a more effective visualization

``` python
alt.Chart(movies_extended).mark_circle().encode(
    alt.X('MPAA Rating'),
    alt.Y('Major Genre', sort='color'),
    alt.Color('count()'),
    alt.Size('count()'))
```

<iframe src="/module4/charts/06/unnamed-chunk-11.html" width="100%" height="420px" style="border:none;">
</iframe>

Notes: One potential concern with heatmaps is that they rely solely on
color to communicate the value of interest.

We cannot perceive small variations in color as accurately as we can for
other visual channels, such as position of size.

Color can also be problematic for people with color vision deficiencies,
which is almost 10% of the population, which we will talk more about in
a later module.

To ameliorate these issues, we can use the same marks as when creating
scatter plots, such as `mark_circle` or `mark_square`, which allows us
to change the size of each mark in addition to its color.

This visualization is highly effective in answering both of the
questions we posed initially, and if we wanted to, we could now facet by
a third categorical column such as the movie distributor, to interrogate
three categorical columns simultaneously.

---

# Let’s apply what we learned!

Notes: <br>
