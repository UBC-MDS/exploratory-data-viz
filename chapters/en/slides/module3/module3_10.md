---
type: slides
---

# Comparing many distributions

Notes: To compare multiple distributions we have seen have we can use
faceting for histograms and either faceting or colouring for density
plots.

So far we only studied these plots with up to three different
distributions to compare, but what if we had many more that, such as 10,
20 or even 50?

---

## The extended movies dataset

``` python
import altair as alt
from vega_datasets import data

movies_extended = data.movies().dropna(subset=['Major Genre'])
movies_extended
```

```out
                           Title    US Gross  Worldwide Gross  US DVD Sales  Production Budget Release Date MPAA Rating  Running Time min         Distributor                        Source        Major Genre         Creative Type         Director  Rotten Tomatoes Rating  IMDB Rating  IMDB Votes
1         First Love, Last Rites     10876.0          10876.0           NaN           300000.0  Aug 07 1998           R               NaN              Strand                          None              Drama                  None             None                     NaN          6.9       207.0
2     I Married a Strange Person    203134.0         203134.0           NaN           250000.0  Aug 28 1998        None               NaN           Lionsgate                          None             Comedy                  None             None                     NaN          6.8       865.0
3           Let's Talk About Sex    373615.0         373615.0           NaN           300000.0  Sep 11 1998        None               NaN           Fine Line                          None             Comedy                  None             None                    13.0          NaN         NaN
4                           Slam   1009819.0        1087521.0           NaN          1000000.0  Oct 09 1998           R               NaN             Trimark           Original Screenplay              Drama  Contemporary Fiction             None                    62.0          3.4       165.0
7                        Foolish   6026908.0        6026908.0           NaN          1600000.0  Apr 09 1999           R               NaN             Artisan           Original Screenplay             Comedy  Contemporary Fiction             None                     NaN          3.8       353.0
...                          ...         ...              ...           ...                ...          ...         ...               ...                 ...                           ...                ...                   ...              ...                     ...          ...         ...
3196  Zack and Miri Make a Porno  31452765.0       36851125.0    21240321.0         24000000.0  Oct 31 2008           R             101.0       Weinstein Co.           Original Screenplay             Comedy  Contemporary Fiction      Kevin Smith                    65.0          7.0     55687.0
3197                      Zodiac  33080084.0       83080084.0    20983030.0         85000000.0  Mar 02 2007           R             157.0  Paramount Pictures     Based on Book/Short Story  Thriller/Suspense         Dramatization    David Fincher                    89.0          NaN         NaN
3198                        Zoom  11989328.0       12506188.0     6679409.0         35000000.0  Aug 11 2006          PG               NaN       Sony Pictures  Based on Comic/Graphic Novel          Adventure            Super Hero     Peter Hewitt                     3.0          3.4      7424.0
3199         The Legend of Zorro  45575336.0      141475336.0           NaN         80000000.0  Oct 28 2005          PG             129.0       Sony Pictures                        Remake          Adventure    Historical Fiction  Martin Campbell                    26.0          5.7     21161.0
3200           The Mask of Zorro  93828745.0      233700000.0           NaN         65000000.0  Jul 17 1998       PG-13             136.0       Sony Pictures                        Remake          Adventure    Historical Fiction  Martin Campbell                    82.0          6.7      4789.0

[2926 rows x 16 columns]
```

Notes: For this exercise, we will use an extended movies dataset
containing additional genres.

We load in that dataset from the vega sample repository and drop all the
rows that have a NaN value in the column `"Major Genre"`, since we are
only interested in comparing the movies that we know belong to a genre.

The question we will try to answer in this slide deck is “Which genres
have the highest worldwide gross?”.

---

## Many distributions can’t be effectively compared with histograms

``` python
alt.Chart(movies_extended).mark_bar().encode(
    alt.X('Worldwide Gross', bin=alt.Bin(maxbins=30)),
    alt.Y('count()'),
    alt.Color('Major Genre'))
```

<iframe src="/module3/charts/10/unnamed-chunk-2.html" width="100%" height="420px" style="border:none;">
</iframe>

Notes: As we have seen, histograms are not very effective for comparing
multiple distributions, and not at all with this many different groups.

Most genres have a low worldwide gross and because our histograms are
stacked on top of each other the left-most bar dominates with around
2000 movies. It extends the y-axis so that it is hard to see how many
observations there are for the highest x-values (but we know there are
some since the axis extends that far).

---

## Many distributions can’t be effectively compared with densities either

``` python
(alt.Chart(movies_extended).mark_area().transform_density(
    'Worldwide Gross',
    groupby=['Major Genre'],
    as_=['Worldwide Gross', 'density'])
 .encode(
    alt.X('Worldwide Gross'),
    alt.Y('density:Q'),
    alt.Color('Major Genre')))
```

<iframe src="/module3/charts/10/unnamed-chunk-3.html" width="100%" height="420px" style="border:none;">
</iframe>

Notes: Although we saw previously that a layered density chart is better
than a stacked histogram, it is not effective in comparing this many
distributions either. Particularly not when the bulk of the distribution
is concentrated in a small area, such as the low x-values in this plot.

This density chart shares many of the issues with the histogram from the
previous slide, and this visualization is a poor choice for our data.

We could try faceting vertically with one density or histogram per
facets, but there would be a lot of subplots with this many genres and
they might not be that easy to compare when they are in facets far
apart.

So how can we create an effective comparison between all the genres?

---

## Bar charts are effective for comparing a single value per group but hides variation

``` python
alt.Chart(movies_extended).mark_bar().encode(
    alt.X('mean(Worldwide Gross)'),
    alt.Y('Major Genre'))
```

<iframe src="/module3/charts/10/unnamed-chunk-4.html" width="100%" height="420px" style="border:none;">
</iframe>

Notes: We could use a barplot if we were only interested in comparing a
single value from each distribution, such as the mean or median.

However, this is generally not a good idea because any plot that only
shows a single value from a distribution will hide the variation in the
data, which could lead us to arrive at incorrect conclusions as you will
see in the next slide.

---

## Showing a single value can lead to incorrect conclusions

[Beyond Bar and Line Graphs: Time for a New Data Presentation
Paradigm](https://journals.plos.org/plosbiology/article?id=10.1371/journal.pbio.1002128)

<center>
<img src=/module3/barplot-hiding-points.png></img>
</center>

Notes: This image illustrates how the same bar chart (A) could have been
generated from three different distributions (B, C, or D).

If we just looked at the bar chart, we could not tell which of the
distributions it came from, but looking at the points directly we would
arrive at a widely different conclusion regarding our data.

In sample B, the points seem to on average be slightly different between
the two groups, although there is significant overlap between the
distributions.

In sample C there seems to be one outlier data point that increases the
mean significantly for its group, but most of the other points are
pretty similar between the two groups.

In D, both groups have their data distributed bimodally (in two peaks).
Maybe this means that there is a third group in this data to which all
the high values belong too?

All this valuable information about our data, is lost when visualizing
it as a bar chart. Remember, bar charts are best suited for displaying
individual values such as counts, proportions, and sums.

To arrive at more accurate conclusions we need to present a richer
representation of the data such as a histogram or a density plot, which
are great as long as we don’t have too many distributions to compare.

But which visualizations could we use to accurately represent the
distributions while still remaining effective for comparing many
distributions in the same plot?

---

## Showing individual observations gives a richer representation than bar charts

``` python
alt.Chart(movies_extended).mark_tick().encode(
    alt.X('Worldwide Gross'),
    alt.Y('Major Genre'))
```

<iframe src="/module3/charts/10/unnamed-chunk-5.html" width="100%" height="420px" style="border:none;">
</iframe>

Notes: One approach would be to show the individual observations, such
as in this chart. This is a compact plot, which makes it easy to compare
the different genres, since they are close to each other in the chart.

We can also clearly see the reason why the x-axis goes up to such a
large max value: There are two movies that grossed highly above the
rest!

Which are these movies?

---

## Tooltips are helpful for answering questions about specific observations

``` python
alt.Chart(movies_extended).mark_tick().encode(
    alt.X('Worldwide Gross'),
    alt.Y('Major Genre'),
    alt.Tooltip('Title:N'))
```

<iframe src="/module3/charts/10/unnamed-chunk-6.html" width="100%" height="420px" style="border:none;">
</iframe>

Notes: Altair really shines in answering questions like this! In
addition to having a robust visualization grammar, it also provides a
grammar for interactive features.

We will dive deep into more complex interactivity in the last module in
this course, but for now, we can simply add a tooltip and answer the
question we just posed by hovering with the mouse over the two highest
grossing movies. Try it!

(We need the `:N` because there are some title values that makes Altair
not recognize this dataframe column as nominal otherwise)

Although this visualization is useful in getting information about the
individual movies, it is hard to tell exactly how many data points there
are in the areas that are completely blue. Is there just enough so that
we don’t see any of the white background or are there thousands of
observations stacked on top of each other?

This plot is saturated, something we will discuss in detail in the next
module. We could use transparency to alleviate this issue to some
extend, but it is more effective to use colour for representing the
counts, such as in a heatmap.

---

## Heatmaps can compare multiple distributions without saturation

``` python
(alt.Chart(movies_extended).mark_rect().encode(
    alt.X('Worldwide Gross', bin=alt.Bin(maxbins=100)),
    alt.Y('Major Genre'),
    alt.Color('count()')))
```

<iframe src="/module3/charts/10/unnamed-chunk-7.html" width="100%" height="420px" style="border:none;">
</iframe>

Notes: A heatmap of the number of observations is very similar to a
histogram, but the count is mapped to the colour instead of to the
height on the y-axis.

This heatmap shows the histogram for each of the genres right next to
each other so that they are easy to compare and contrast, by looking at
the varying colours.

We can see that some genres appear to have most of their observations
close to zero, such as Comedy and Drama, whereas others are more spread
out, such as Adventure movies.

This is a pretty effective visualization, but since the colour scale is
the same for each genre and some genres have many more observations than
others, it can be difficult to accurately interpret the distribution of
those genres that have few observations.

For example, we wouldn’t be able to distinguish between regions with
10-20 and 40-50 observations since the colours are so similar.

Remember that comparing positions is more effective than comparing
colours, so how can we use position to compare multiple distributions?

---

## Boxplots show several key statistics from a distribution

[Jhguch at en.wikipedia via Wikimedia
Commons](https://commons.wikimedia.org/wiki/File:Boxplot_vs_PDF.svg)

<br> <br>

<center>
<img src=/module3/boxplot-schematic.svg></img>
</center>

Notes: A boxplot is a mix between showing individual values and a few
key summary statistics.

Instead of showing just the mean or median as with a bar plot, a box
plot shows 5 summary statistics.

The box represents three values, the median in the middle and the lower
and upper quartile at the edges This means that 50% of the data points
lie within the box.

The lines extending from the box are called whiskers and they can
represent a few different statistics. Sometimes, they are showing the
min and the max (the range) of our data.

However, it is more common that they show the furthest points that are
still within 1.5 x the “interquartile” range from the edges of the box.
The interquartile range is the distance between the edges of the box.

Conventionally, any observations that fall outside the whiskers, are
drawn out as individual points and are sometimes referred to as
“outliers”, which are occasionally discarded.

However, what really is an outlier in your data and what you should do
with them depends on the question you are asking. Maybe these data
points are the most important in your dataset or they could be
measurement errors. You should always look further and think carefully
before discarding data as outliers.

How does it look when we use boxplots to answer our question?

---

## Boxplots can effectively compare multiple distributions

``` python
bar = alt.Chart(movies_extended).mark_bar().encode(
    alt.X('mean(Worldwide Gross)'),
    alt.Y('Major Genre'))
    
box = alt.Chart(movies_extended).mark_boxplot().encode(
    alt.X('Worldwide Gross'),
    alt.Y('Major Genre'))

box | bar
```

<iframe src="/module3/charts/10/unnamed-chunk-8.html" width="100%" height="420px" style="border:none;">
</iframe>

Notes: Here we show a boxplot next to the barplot we created initially.
The `|` operator works similarly to the `+` operator, but instead of
layering charts on top of each other, it puts them next to each other.

We can see that the box plots provide us with the same clear positional
comparison as in the barplot, but we now also have access to additional
information about each genres’ distribution. We can ensure ourselves
that the distributions are roughly the same shape and view potential
outliers.

We can directly answer the question we posed at the beginning: the
Adventure genre generates the highest revenue both in terms of the
medians and the overall position of the boxes.

It seems like Action is the second most highly grossing genre, but after
that, it becomes hard to compare. We could make this visualization even
more effective by sorting the boxes according to their median value.

---

## Sorted boxplots more effective for comparing similar distributions

``` python
genre_order = movies_extended.groupby('Major Genre')['Worldwide Gross'].median().sort_values().index.tolist()
alt.Chart(movies_extended).mark_boxplot().encode(
    alt.X('Worldwide Gross'),
    alt.Y('Major Genre', sort=genre_order))
```

<iframe src="/module3/charts/10/unnamed-chunk-9.html" width="100%" height="420px" style="border:none;">
</iframe>

Notes: Altair does not support sorting boxplots via the “x” or “-x”
shortcut.

Instead, we need to create a list of the genres, ordered by value.

We can do this with pandas by grouping the dataframe, computing the
median for the grossing columns, sorting the values, and then extracting
the index as a list.

Now the visualization is very effective! It is easy to compare genres
with similar grossing since they are right next to each other in the
plot.

If we wanted to look closer at the differences between the bulk of the
distributions we could exclude the two most highly grossing movies.

---

## Zooming in facilitates comparison of small differences

``` python
filtered_movies = movies_extended[movies_extended['Worldwide Gross'] < 1_500_000_000]
alt.Chart(filtered_movies).mark_boxplot().encode(
    alt.X('Worldwide Gross'),
    alt.Y('Major Genre', sort=genre_order))
```

<iframe src="/module3/charts/10/unnamed-chunk-10.html" width="100%" height="420px" style="border:none;">
</iframe>

Notes: Here we can compare the distributions more clearly, and it really
looks like there are no large differences in the medians between the
five genres behind Adventure and Action.

We will need to keep in mind that there are two additional data points
that we have excluded from this visualization, but neither the median
line nor the box would be much affected by excluding just a few values
from a large population.

If we would have shown the mean instead of the median, this could have
been an issue since the mean can be affected significantly from just a
few extreme values.

---

## Boxplots can be scaled by the number of observations

``` python
alt.Chart(movies_extended).mark_boxplot().encode(
    alt.X('Worldwide Gross'),
    alt.Y('Major Genre', sort=genre_order),
    alt.Size('count()'))
```

<iframe src="/module3/charts/10/unnamed-chunk-11.html" width="100%" height="420px" style="border:none;">
</iframe>

Notes: The size of the boxes can be made proportional to the count of
observations in that group.

This helps us see if there are many more observations underlying some of
the boxes versus others. In our plot, we can see that the “comedy” genre
has the most movies whereas there are few documentaries and black
comedies.

However, it also makes it hard to tell where the lines of the median and
the boxes are for many of the distributions. A better alternative could
be to not scale the boxes and instead, include a bar chart with the
number of observations per genre together with the boxplot.

---

## Boxplots are not able to accurately represent data with multiple peaks

[From Autodesk
research](https://www.autodesk.com/research/publications/same-stats-different-graphs)

<center>
<img src=/module3/point-box-violin.gif></img>
</center>

Notes: While boxplots are effective for visualizing multiple
distributions, they also have their shortcomings.

One of their main downsides is that they are not effective in showing
distributions with multiple peaks. This can be seen in the animation in
this slide, where variation in the raw data does no result in any change
in the boxplots.

Two effective visualizations for many distributions that also handle
multiple peaks are [violin
plots](https://altair-viz.github.io/gallery/violin_plot.html) (as shown
in this slide) and
[stripplots](https://altair-viz.github.io/gallery/stripplot.html).

Violinplots are similar to density plots put next to each other, and
stripplots prevent overlap by distributing the points in a cloud instead
of a straight line.

There are also [sina
plots](https://cran.r-project.org/web/packages/sinaplot/vignettes/SinaPlot.html),
which combine the best of violin plots and strip plots together.

These are all highly effective, but not yet available to make easily in
Altair, so we will not be teaching them here.

Boxplots are still very effective in comparing multiple distributions,
and when there are even more distributions than what we have here,
e.g. 50+, then boxplots are often easier to interpret than the
alternatives mentions above, since they are simpler.

---

# Let’s apply what we learned!

Notes: <br>
