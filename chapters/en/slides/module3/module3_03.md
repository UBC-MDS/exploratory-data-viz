---
type: slides
---

# Comparing many distributions

Notes: We have seen have we can use facetting for histograms and both
faceting and coloring for density plots to compare multiple
distributions against each other. So far we only studied these plots
with up to three different distributions to compare, but what if we had
many more that, such as 10, 20 or even 50?

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

Notes: For this exercise we will use another movies dataset containing
additional genres. Here we are loading in that dataset from the vega
sample repository and dropping all the rows that have an NaN value in
the column `"Major Genre"`.

The question we will try to answer is “Which genres have the highest
worldwide gross?”.

---

## Many distributions can’t be effectively compared with histograms

``` python
alt.Chart(movies_extended).mark_bar().encode(
    alt.X('Worldwide Gross', bin=alt.Bin(maxbins=30)),
    alt.Y('count()'),
    alt.Color('Major Genre'))
```

<iframe src="/module3/charts/03/unnamed-chunk-2.html" width="100%" height="400px" style="border-width:0;">
</iframe>

Notes: As we have seen, histograms often effective for comparing
multiple distributions, and not at all with this many different groups.

Most genres have a really low worldwide gross, and because our histogram
is stacked this bar dominates with around 2000 movies, and extends the
y-axis so that it is hard to see how many observations there are for
highest x-values (but we know there are some since the axis extends that
far).

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

<iframe src="/module3/charts/03/unnamed-chunk-3.html" width="100%" height="400px" style="border-width:0;">
</iframe>

Notes: Although we saw previously that a layered density chart is better
than a stacked histogram, it is not effective in comparing this many
distributions either.

Here, the density chart shares many of the issues with the histogram
from the previous slide, and this visualization is a poor choice for our
data.

We could try faceting vertically with one distribution per plot, but
there would be a lot of subplots with this many genres and they might
not be that easy to compare when they are in subplots far apart.

So what can we do to create an effective comparison between all the
genres?

---

## Bar charts are effective for comparing a single value but hides any variation

``` python
alt.Chart(movies_extended).mark_bar().encode(
    alt.X('mean(Worldwide Gross)'),
    alt.Y('Major Genre'))
```

<iframe src="/module3/charts/03/unnamed-chunk-4.html" width="100%" height="400px" style="border-width:0;">
</iframe>

Notes: We could use a barplot if we were only interested in comparing a
single value from each distribution, such as the mean or median.

However, this is generally not a good idea because any plot that only
shows a single value will hide the variation in our data and could lead
to us drawing the wrong conclusion as you will see in the next slide.

---

## Showing a single value can lead to incorrect conclusions

<img src=/module3/barplot-hiding-points.png></img>

[Beyond Bar and Line Graphs: Time for a New Data Presentation
Paradigm](https://journals.plos.org/plosbiology/article?id=10.1371/journal.pbio.1002128)

Notes: This image illustrates how the same barplot (A) could have been
generated from several different distributions (B, C, or D).

If we just looked at the barplot, we could not tell which of the
distributions it came from, but looking at the points directly we would
arrive at widely different conclusion to what was going on with our
data.

In sample B, the points seem to be slightly different between the two
groups, although there is significant overlap between the two
distributions.

In sample C there seems to be one outlier data point that increases the
mean a lot for the one group, but most of of the other points are pretty
similar between the two groups.

In D, both groups have their data distributed bimodally (in two peaks).
Maybe this means that there is a third group in this data which all the
high values belong too?

All the information that we just mentioned, is lost when displaying this
data as a bar chart. Bar plots are best suited for displaying individual
values, such as counts, proportions, and sums.

This is why we most of the times need to present a richer representation
of the data such as a histogram or a density plot, which are great as
long as we don’t have too many distributions to compare.

What other plots could we use instead of barplots for comparing many
distributions?

---

## Showing individual observations is often more helpful than a barplot

``` python
alt.Chart(movies_extended).mark_tick().encode(
    alt.X('Worldwide Gross'),
    alt.Y('Major Genre'))
```

<iframe src="/module3/charts/03/unnamed-chunk-5.html" width="100%" height="400px" style="border-width:0;">
</iframe>

Notes: One approach would be to show the individual observations, such
as in this chart. This is a compact plot, which makes it easy to compare
the different genres, since they are close to each other in the chart.

We can also clearly see the reason for why the x-axis goes up to such a
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

<iframe src="/module3/charts/03/unnamed-chunk-6.html" width="100%" height="400px" style="border-width:0;">
</iframe>

Notes: Altair really shines in answering questions like this! In
addition to having a robust visualization grammar, Altair also provides
a grammar for interactive features.

We will dive deep into more complex chart interactivity in the last
module in this course, and by simply adding a tooltip to our chart as in
this slide, we can answer the question we posed by hovering with the
mouse over the two highly grossing movies, try it!

(We need the `:N` because there are some title values that makes Altair
not recognize this dataframe variable as nominal otherwise)

Although this visualization is useful in getting information about the
individual movies, it is hard to tell exactly how many data points there
are in the area that are completely blue. Is it just enough so that we
don’t see any of the white background or are there thousands of
observations stacked on top of each other?

This is called plot “saturation” or “overplotting” and we will talk more
about it in the next module. In brief, we could use transparency to
alleviate this issue to some extend, but it is more effective to use
color for representing the counts, such as in a heatmap.

---

## Heatmaps can comparing multiple distributions without risk of overplotting

``` python
(alt.Chart(movies_extended).mark_rect().encode(
    alt.X('Worldwide Gross', bin=alt.Bin(maxbins=100)),
    alt.Y('Major Genre'),
    alt.Color('count()')))
```

<iframe src="/module3/charts/03/unnamed-chunk-7.html" width="100%" height="400px" style="border-width:0;">
</iframe>

Notes: A heatmap of the number of observations is very simiar to a
histogram, but the count is mapped to the color instead of to the height
on the y-axis.

This heatmap shows the “color histogram” for each of the genres right
next to each other so that they are easy to compare and contrast.

Here we can see that some genres seem to have most of their observations
close to zero, such as Comedy and Drama whereas others are more spread
out, such as Adventure movies.

This is a pretty effective visualization, but since the color scale is
the same for each genre and some genres have many more observations than
others, it can be difficult to accurately interpret the distribution of
those genres that have few observations.

We wouldn’t be able to distinguish between regions with 10-20 and 40-50
observations since the colors are so similar.

Remember that position can allow us to make more accurate
interpretations than color, so how can we use position to show multiple
distributions without using histograms?

---

## Boxplots show several key statistic from a distribution

<img src=/module3/boxplot-schematic.webp></img>

[What does a box plot tell you? Simply
psychology](https://www.simplypsychology.org/boxplots.html)

Notes: A boxplot is a mix between showing individual values and some key
summary statistics.

Instead of showing just the mean or median as with a bar plot, a box
plot shows 5 summary statistics:

The box represents three values, the median in the middle and the upper
and lower quartile at the edges This means that means that 50% of the
data points lie within the box.

The lines extending from the box as called whiskers and the can
represent a few different things. They can be showing the min and the
max (the range) of our data.

However, it is more common that they show the furthest points that are
still within 1.5 x the “interquartile” range from the edges of the box.
The interquartile range is the distance between the edges of the box

The edges of the box are called the first and third quartile, and the
median is the second quartile. These quartiles divide the box into four
“quarters”, with as many observations in each.

Conventionally, any observations that fall outside the whiskers, are
drawn out as individual points and are sometimes referred to as
“outliers”, and are occasionally discarded.

However, what really is an outlier in your data and what you should do
with them depends on the question you are asking. Maybe these data
points are the most important in your dataset or they could be
measurement errors. You should always look further and think carefully
before discarding data as outliers.

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

<iframe src="/module3/charts/03/unnamed-chunk-8.html" width="100%" height="400px" style="border-width:0;">
</iframe>

Notes: Here we show a boxplot next to the barplot we created initially.
The `|` operator works similarly to the `+` operator, but instead of
layering charts on top of each other, it puts them next to each other.

We can see that the box plots provides us with the same clear positional
comparison as in the barplot, but we now also has access to additional
information about each genres’ distribution. We can ensure ourselves
that the distributions are roughly the same shape and check to see that
where potential outliers are.

We can directly answer the question we posed at the beginning: the
Adventure genre generates the highest revenue when comparing both the
medians and the position of the boxes.

Then it seems like Action is the second most highly grossing genres, but
after that it becomes hard to compare. We could make this visualization
even more effective by sorting the boxes according to their median
value.

---

## Boxplots need to be sorted with a custom list

``` python
genre_order = movies_extended.groupby('Major Genre')['Worldwide Gross'].median().sort_values().index.tolist()
alt.Chart(movies_extended).mark_boxplot().encode(
    alt.X('Worldwide Gross'),
    alt.Y('Major Genre', sort=genre_order))
```

<iframe src="/module3/charts/03/unnamed-chunk-9.html" width="100%" height="400px" style="border-width:0;">
</iframe>

Notes: Altair does not support sorting boxplots via the “x” or “-x”
shortcut.

Instead we need to create a list of the genres, ordered by value.

We can do this with pandas by grouping the dataframe, computing the
median for the grossing columns, sorting the values, and then extracting
the index as a list.

Now the visualization is very effective! It is easy to compare genres
with similar grossing since they are right next to each other in the
plot.

---

## Boxplots can be scaled by the number of observations

``` python
alt.Chart(movies_extended).mark_boxplot().encode(
    alt.X('Worldwide Gross'),
    alt.Y('Major Genre', sort=genre_order),
    alt.Size('count()'))
```

<iframe src="/module3/charts/03/unnamed-chunk-10.html" width="100%" height="400px" style="border-width:0;">
</iframe>

Notes: The size of the boxes can be made proportional to the count of
observations in that group.

This helps us see if there are many more observations underlying some of
the boxes versus others. In our plot, we can see that the “comedy” genre
has the most movies whereas there are few documentaries and black
comedies.

If we wanted a more precise indication of the counts, we could have have
used separate barplot instead.

---

## TODO mention violinplots and striplots are often better but not available yet

Also shwo facetted histograms?

Notes: While it is possible to make [violin
plots](https://altair-viz.github.io/gallery/violin_plot.html) and
[stripplots](https://altair-viz.github.io/gallery/stripplot.html)
(categorical scatter plots) in Altair, these do currently not work with
a categorical x/y axies, and you need to use faceting instead to display
different categories, which gives us less flexibility. Therefore, we
will primarily use boxplots when comparing multiple distributions with
Altair.

---

# Let’s apply what we learned!

Notes: <br>
