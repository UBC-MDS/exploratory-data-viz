---
type: slides
---

# Exploratory Data Analysis

Notes: Exploratory data analysis (EDA), refers to an early phase in the
data analysis pipeline where you are actively exploring and getting to
know the data.

It can be contrasted with formal statistical hypothesis testing
(confirmatory data analysis) and analysis/visualization for
communication where you spend more time designing your figures.

Being able to perform EDA effectively is a key part of most data science
positions!

---

## Glancing at the values in the dataframe is a good first step to get familiar with a new dataset

``` python
import pandas as pd

movies_extended = pd.read_csv('data/movies-extended-eda.csv')
movies_extended
```

```out
     Major Genre MPAA Rating  Running Time min  IMDB Rating  IMDB Votes
0         Action           R             108.0          5.8     33584.0
1         Comedy       PG-13              95.0          5.8     51109.0
2         Action       PG-13             106.0          5.2     15817.0
3      Adventure         NaN             108.0          5.9     45773.0
4          Drama           R             111.0          6.1      9908.0
...          ...         ...               ...          ...         ...
996       Comedy       PG-13              89.0          6.4     69296.0
997       Comedy           R              87.0          7.8     81629.0
998       Comedy           R             101.0          7.0     55687.0
999    Adventure          PG             129.0          5.7     21161.0
1000   Adventure       PG-13             136.0          6.7      4789.0

[1001 rows x 5 columns]
```

Notes: In this slide deck, you will see how EDA allows us to identify
interesting relationships that we want to study closer, suggest
hypothesis to test, assess assumptions of the data, and inform further
data collection.

The very first thing we do in EDA, is often to glance at the dataframe
by printing out a few values like in this slide.

This gives us an idea about which columns are numerical and categorical
as well as the size of the dataframe.

You can also see that we don’t have the exact same dataframe columns as
in the previous slide decks. We have left out a few since we will be
including all dataframe columns in the same chart and want to make sure
it fits on the slide.

---

## Viewing the column data types and missing values protects us from errors later on

``` python
movies_extended.info()
```

```out
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 1001 entries, 0 to 1000
Data columns (total 5 columns):
 #   Column            Non-Null Count  Dtype  
---  ------            --------------  -----  
 0   Major Genre       996 non-null    object 
 1   MPAA Rating       994 non-null    object 
 2   Running Time min  1001 non-null   float64
 3   IMDB Rating       945 non-null    float64
 4   IMDB Votes        945 non-null    float64
dtypes: float64(3), object(2)
memory usage: 39.2+ KB
```

Notes: Next, it is a good idea to check the type of data in each column
and how many missing values there are.

From looking looking at the values in the table, we already have an idea
of what the column data types are, and this matches the output from the
`info` method. The columns with categorical data are referred to as
“objects” and the numerical columns are read in as decimal numbers or
“floats”.

Although it seem unnecessary in this case, it is good practice to
perform this check since there are rare cases where pandas might
interpret a column differently from what we think.

A common example of this is when people use a text string to encode
missing values, for example “missing”, “null”, or “nan” instead of
leaving the value blank which is best practice. This can make pandas
treat a column as an object, which we might not detect when printing
only the first few rows of the dataframe.

This can also happen with dates, which might be parsed as numbers unless
you specify `parse_dates=['column_name']` to `read_csv`.

Speaking of missing values, this is the next thing to check for. Columns
that are missing some values might need to be imputed or dropped for
machine learning tasks, and when we performing statistical test, we need
to know how many observations we have with data.

Importantly, patterns in missing values can also give hints to which
columns have strong relationships between their values and indicate if
that something went wrong in the data collection process, which we
should investigate before performing our analysis.

Here, it looks like there are some NaNs in many of the columns, and the
IMDB ratings and votes seems to have the most: about 60 rows are missing
a value.

The IMDB rating and number of votes have the exact same amount of
missing values, and it makes sense that movies without votes can’t have
a rating. But if we didn’t know how these columns were related, how
could we check?

---

## Visualizing missing values helps us identify potential issues with the data

``` python
import altair as alt

alt.data_transformers.disable_max_rows();

movies_nans = movies_extended.isna().reset_index().melt(id_vars='index', var_name='column', value_name='NaN')
movies_nans
```

```out
      index       column    NaN
0         0  Major Genre  False
1         1  Major Genre  False
2         2  Major Genre  False
3         3  Major Genre  False
4         4  Major Genre  False
...     ...          ...    ...
5000    996   IMDB Votes  False
5001    997   IMDB Votes  False
5002    998   IMDB Votes  False
5003    999   IMDB Votes  False
5004   1000   IMDB Votes  False

[5005 rows x 3 columns]
```

Notes: To create a visualization of missing values for all columns, we
must first reshape the data into a format where the column names become
a single categorical column in the dataframe, which we can use on the
y-axis in Altair. The index column will be used to give each column the
same numbers on the x-axis.

Since this reshape operations makes our dataframe longer than 5000 rows,
we need to disable the max rows warning in Altair, which otherwise would
prevent us from making this chart.

Whenever we do this, we should also check the final size of our
visualization if we save it to a file or in the notebook to ensure that
it is not too large for what we can currently handle.

---

## Visualizing missing values helps us identify potential issues with the data

``` python
alt.Chart(movies_nans).mark_rect(height=17).encode(
    x='index:O',
    y='column',
    color='NaN',
    stroke='NaN').properties(width=800)
```

<iframe src="/module4/charts/08/unnamed-chunk-5.html" width="100%" height="420px" style="border:none;">
</iframe>

Notes: By visualizing the missing values for each column next to each
other, we can quickly see if there are similar patterns between columns.

A common cause for such correlations, could for example be due to the
same day or hour missing for several columns when working with time
series data.

This information could help us decide whether we might want to remove an
entire row from our analysis (when most column values for that
observation are missing or look suspect) or if we should impute a
missing value (if most column values for that observation look OK).

Here we can confirm that the missing values from IMDB ratings and votes
are indeed missing for the same rows in the data frame, since the orange
lines show up on the same positions throughout the index, which suggests
that these columns are linked in the data collection process.

The reason we specified the stroke encoding in this plot is to color the
outline of each rectangle, which is white by default.

Before continuing with our analysis we could consider dropping the NaN
values, but it might also be a good idea to create all our
visualizations both with and without them, to see if this impacts our
conclusions.

Ultimately, domain expertise should also be involved in the decision to
drop the NaN-values and understanding why they are present is important
before deciding whether to get rid of them.

---

## A statistical summary is useful to complement visualizations

``` python
movies_extended.describe()
```

```out
       Running Time min  IMDB Rating     IMDB Votes
count       1001.000000   945.000000     945.000000
mean         110.312687     6.279577   43514.432804
std           20.701090     1.178046   52241.047929
min           72.000000     1.700000      48.000000
25%           95.000000     5.500000   12747.000000
50%          107.000000     6.300000   26303.000000
75%          122.000000     7.100000   55248.000000
max          222.000000     8.900000  465000.000000
```

Notes: Now that we are aware of what data types we are working with and
how the missing values are distributed, let’s start visualizing the data
that is not missing!

Visualization is a critical component throughout EDA as it is key in
communicating information about the data to us.

We will start by visualizing the distributions of numerical data, in
order to familiarize ourselves with how the values are spread out for
each numerical column.

Before doing so let’s print out the summary statistics for these
numerical columns.

While it is difficult to make statements about how the data is
distributed by only looking at these numbers, they are useful to have
available for cross-reference when visualizing the data and also give us
an idea of what to expect when creating our visualization.

After visualizing the data, we can also go back and look at these
numbers to ensure ourselves that they align and that we don’t have a
typo somewhere causing an error.

---

## Visualizing the distributions of all numerical columns helps us understand the data

``` python
numerical_columns = movies_extended.select_dtypes('number').columns.tolist()
(alt.Chart(movies_extended)
 .mark_bar().encode(
     alt.X(alt.repeat(), type='quantitative', bin=alt.Bin(maxbins=25)),
     y='count()')
 .properties(width=250, height=150)
 .repeat(numerical_columns))
```

<iframe src="/module4/charts/08/unnamed-chunk-7.html" width="100%" height="420px" style="border:none;">
</iframe>

Notes: Specific to EDA visualizations is that we often want to create
quick overview charts similar to the table we just printed. We worry
less about the details such as axis labels and titles, since we are
trying to understand the data ourselves through an interactive
explorative process, rather than making the figures look appealing in a
presentation (we will see how to do that later).

To create these overview visualizations, it is helpful make the same
type of plot for several dataframe columns and lay them out as subplots
within a figure.

Previously, we have made subplots via faceting, which uses a categorical
column to filter subsets of the data in each subplot, and all subplots
have the same columns mapped to the X and Y axes.

Here, we will see how we can create figures where the X and Y axes are
different between subplots, and all the data is present in each one of
them.

To achieve this in Altair, we say that we *repeat* the same `Chart`
setup for multiple columns.

Instead of typing each chart out manually out manually we specify which
columns we want to use via the `.repeat` method of a `Chart` object, and
indicate with `alt.repeat()` where these repeated columns should be
used.

Since we are not using the dataframe column directly, we also need to
specify which type the repeated columns are.

A great first step is to visualize the distribution of each of the
quantitative dataframe columns to get an overview of how our data looks
and examine it to see if there are any weird things going on
(e.g. values that are way too small or large, values all bunched up in
one place that could indicate measurement errors, etc).

To do this, we here create a histogram chart and repeat it for each of
the numerical columns.

This overview tells us that most movies have a runtime around 90-130
min, but there are some that are shorter and some that are longer.

Most movies have less than 80,000 votes, but there are some that have a
really high number.

The distribution for the IMDB ratings is centered around 6, with few
extreme values on either end and no notable shift in either direction.

Our EDA is already helping us finding interesting aspects of the data!

---

## Repeating columns of both X and Y lets us effectively explore pairwise relationships between columns

``` python
# Scroll down on the plot to see the last row
(alt.Chart(movies_extended)
 .mark_point(size=10).encode(
     alt.X(alt.repeat('column'), type='quantitative'),
     alt.Y(alt.repeat('row'), type='quantitative'))
 .properties(width=120, height=120)
 .repeat(column=numerical_columns, row=numerical_columns))
```

<iframe src="/module4/charts/08/unnamed-chunk-8.html" width="100%" height="420px" style="border:none;">
</iframe>

Notes: Equipped with the information about each column’s data
distribution, we move on to exploring the pairwise relationships between
columns. This type of visualization will help us understand which
columns are related to each other.

For example, we already saw earlier in this module that the ratings on
IMDB and Rotten Tomatoes have a strong relationship when we create a
scatter plot of these two dataframe columns. Here, we can ask that same
question of all columns in the dataset.

This is helpful both for our general knowledge about the data and if we
have a specific goal in mine, maybe we would want to predict the movie
ratings, but we are not sure which other dataframe columns would be
useful to have in the prediction model?

Instead of looking at just one relationship at a time, we visualize all
of them to be able to answer the same question for all pairs of columns.

To create this visualization, we need to use `alt.repeat` on both the
axes, instead of just one as for the histograms.

In the last slide we used `alt.repeat` without arguments, which means
that we are repeating over all the columns. Here we specifically set the
rows and columns attributes to ensure that our repeated chart will
include all the pairwise combinations of the dataframe columns.

In the resulting visualization, the diagonal compares the column against
itself, so this is not very interesting. The same pairwise comparisons
are also repeated above and below the diagonal, so we will focus our
attention only on the six plots below the diagonal.

This type of visualization is often referred to as a scatterplot matrix
or pairplot.

Unfortunately, these plots are saturated, so although we can see that
there might be some correlative relationships, we should remake this
plot as a 2D histogram heatmap, using the techniques we learned in the
previous slide deck.

---

## Heatmaps can be used for repeated charts to avoid saturation

``` python
# Scroll down on the plot to see the last row
(alt.Chart(movies_extended)
 .mark_rect().encode(
     alt.X(alt.repeat('column'), type='quantitative', bin=alt.Bin(maxbins=30)),
     alt.Y(alt.repeat('row'), type='quantitative', bin=alt.Bin(maxbins=30)),
     alt.Color('count()', title=None))
 .properties(width=110, height=110)
 .repeat(column=numerical_columns, row=numerical_columns)).resolve_scale(color='independent')
```

<iframe src="/module4/charts/08/unnamed-chunk-9.html" width="100%" height="420px" style="border:none;">
</iframe>

Notes: As we learned earlier, we can create a heatmap to avoid the
issues with saturation in the scatter plot.

Thanks to our repeated charts, we can quickly assess if there are strong
relationships between any of the column pairs.

In addition to the relationship between the two ratings, there IMDB
Rating and the Running Time appears to be related and the number of
votes number of votes also seem to be related to the IMDB rating.

Pairs of columns that appear correlated in this visualization are good
candidates to explore further e.g. with formal statistical testing to
assess the strength of these correlations or to test in our machine
learning models as predictors for another column

We should also use our domain expertise to understand why these columns
might correlate and the nature of their relationship (for example, if
one directly causes the other one to change values the relationship
would be directly causative).

However, as interesting to explore later could be columns that we had
expected to be correlated, but appears not to be in this plot.

Note that we set the color title to `None` to save some space between
the subplots, and since it is the same for each color bar (“Count of
records”).

To get more resolution of the counts for each column pair, we resolve
the colorscale to be set individually for each subplot. Otherwise the
high counts in the few bins of diagonals would drown out the counts in
the other plots which would have the same color almost everywhere.

---

## Repeat also allows us to explore the relationship between categorical and numerical columns

``` python
categorical_columns = movies_extended.select_dtypes('object').columns.tolist()
(alt.Chart(movies_extended)
 .mark_boxplot().encode(
     alt.X(alt.repeat('column'), type='quantitative'),
     alt.Y(alt.repeat('row'), type='nominal', title=''))
 .properties(width=150)
 .repeat(column=numerical_columns, row=categorical_columns))
```

<iframe src="/module4/charts/08/unnamed-chunk-10.html" width="100%" height="420px" style="border:none;">
</iframe>

Notes: In addition to repeating charts with numerical data only, we can
use the same principles to explore the relationships between the
categorical and the numerical columns in our dataset.

Here, we spread out the three categorical dataframe columns along the
columns of the plot to be able to answer questions regarding how the
different categories compare, e.g. how does different genres impact
movie runtime?

The categories labeled “null” are the ones which are missing a value in
that categorical column in the dataframe, but still has values in the
numerical column that is plotted on the x-axis.

We have also removed the “Title” item from the list of categorical
columns, as well as dropped it from the dataframe, since we would have
created a giant plot if all thousands titles were included.

So what is the answer to our question, how does genres impact movie
runtime? It seems like Westerns, Musicals, and Dramas have the longest
run times. For the other categories it seems like it is Dramatization
and Historical Fiction as well as PG-13 an R rated movies that run the
longest.

As we have discussed before, it is often easier to compare plots where
the values are sorted.

For a single boxplot, we learned previously that we can pass a list of
the categories in the order we want to plot them.

In this case, we have different columns on the y-axis, so we would need
to pass a list of all categories in all these three columns. We could
use a loop with pandas to create this like so:

``` python
running_time_order = []
for groupby_col in ['Major Genre', 'MPAA Rating']:
    running_time_order.extend(
        movies_extended
        .groupby(groupby_col)
        .median()
        ['Running Time min']
        .sort_values()
        .index
        .to_list())
```

---

# Let’s apply what we learned!

Notes: <br>