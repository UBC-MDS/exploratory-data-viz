---
type: slides
---

# Creating Area Charts

Notes: In this slide deck, we will be learning how to create area charts
and when they are a suitable alternative to use instead of line charts.

---

## Global Development Data

<font size="2">

| Column                   | Description                                                                                                                                                               |
|--------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| country                  | Country name                                                                                                                                                              |
| year                     | Year of observation                                                                                                                                                       |
| population               | Population in the country at each year                                                                                                                                    |
| region                   | Continent the country belongs to                                                                                                                                          |
| sub\_region              | Sub-region the country belongs to                                                                                                                                         |
| income\_group            | Income group [as specified by the world bank in 2018]( "https://datahelpdesk.worldbank.org/knowledgebase/articles/378833-how-are-the-income-group-thresholds-determined") |
| life\_expectancy         | The mean number of years a newborn would live if mortality patterns remained constant                                                                                     |
| income                   | GDP per capita (in USD) adjusted for differences in purchasing power                                                                                                      |
| children\_per\_woman     | Average number of children born per woman                                                                                                                                 |
| child\_mortality         | Deaths of children under 5 years of age per 1000 live births                                                                                                              |
| pop\_density             | Average number of people per km2                                                                                                                                          |
| co2\_per\_capita         | CO2 emissions from fossil fuels (tonnes per capita)                                                                                                                       |
| years\_in\_school\_men   | Mean number of years in primary, secondary, and tertiary school for 25-36 years old men                                                                                   |
| years\_in\_school\_women | Mean number of years in primary, secondary, and tertiary school for 25-36 years old women                                                                                 |

</font>

Notes: We will be visualizing global health data to answer the question:
How has the population for different regions around the world changed
over time?

This dataset is more similar to those you will encounter in the wild
than the sample dataset, we saw in the first module. We will be
exploring this data in the assignments for the first two modules.

In later labs we will look at many other datasets, but we’re sticking to
a familiar one for now so that we can focus on laying down a solid
understanding of the visualization principles with data that we already
know.

---

## Read in and glimpse at the data with pandas

``` python
import pandas as pd

gm = pd.read_csv('data/world-data-gapminder.csv', parse_dates=['year'])
gm
```

```out
           country       year  population  region          sub_region income_group  life_expectancy  income  children_per_woman  child_mortality  pop_density  co2_per_capita  years_in_school_men  years_in_school_women
0      Afghanistan 1800-01-01     3280000    Asia       Southern Asia          Low             28.2     603                7.00            469.0          NaN             NaN                  NaN                    NaN
1      Afghanistan 1801-01-01     3280000    Asia       Southern Asia          Low             28.2     603                7.00            469.0          NaN             NaN                  NaN                    NaN
2      Afghanistan 1802-01-01     3280000    Asia       Southern Asia          Low             28.2     603                7.00            469.0          NaN             NaN                  NaN                    NaN
3      Afghanistan 1803-01-01     3280000    Asia       Southern Asia          Low             28.2     603                7.00            469.0          NaN             NaN                  NaN                    NaN
4      Afghanistan 1804-01-01     3280000    Asia       Southern Asia          Low             28.2     603                7.00            469.0          NaN             NaN                  NaN                    NaN
...            ...        ...         ...     ...                 ...          ...              ...     ...                 ...              ...          ...             ...                  ...                    ...
38977     Zimbabwe 2014-01-01    15400000  Africa  Sub-Saharan Africa          Low             57.0    1910                3.90             64.3         39.8            0.78                 10.9                   10.0
38978     Zimbabwe 2015-01-01    15800000  Africa  Sub-Saharan Africa          Low             58.3    1890                3.84             59.9         40.8             NaN                 11.1                   10.2
38979     Zimbabwe 2016-01-01    16200000  Africa  Sub-Saharan Africa          Low             59.3    1860                3.76             56.4         41.7             NaN                  NaN                    NaN
38980     Zimbabwe 2017-01-01    16500000  Africa  Sub-Saharan Africa          Low             59.8    1910                3.68             56.8         42.7             NaN                  NaN                    NaN
38981     Zimbabwe 2018-01-01    16900000  Africa  Sub-Saharan Africa          Low             60.2    1950                3.61             55.5         43.7             NaN                  NaN                    NaN

[38982 rows x 14 columns]
```

Notes: As we read in the data with `pandas`, we specify to read in the
`year` column as a date, rather than an integer, which is the default
behaviour.

Remember that Altair uses the `pandas` data types to infer the data it
is working with. Integers would show up on the Altair chart axes as
`1,990, 2,000, etc` whereas dates are shown as `1990, 2000, etc`, so
make sure to parse these columns as dates when using pandas.

---

## *.info()* shows column data types and missing values

``` python
gm.info()
```

```out
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 38982 entries, 0 to 38981
Data columns (total 14 columns):
 #   Column                 Non-Null Count  Dtype         
---  ------                 --------------  -----         
 0   country                38982 non-null  object        
 1   year                   38982 non-null  datetime64[ns]
 2   population             38982 non-null  int64         
 3   region                 38982 non-null  object        
 4   sub_region             38982 non-null  object        
 5   income_group           38982 non-null  object        
 6   life_expectancy        38982 non-null  float64       
 7   income                 38982 non-null  int64         
 8   children_per_woman     38982 non-null  float64       
 9   child_mortality        38980 non-null  float64       
 10  pop_density            12282 non-null  float64       
 11  co2_per_capita         16285 non-null  float64       
 12  years_in_school_men    8188 non-null   float64       
 13  years_in_school_women  8188 non-null   float64       
dtypes: datetime64[ns](1), float64(7), int64(2), object(4)
memory usage: 4.2+ MB
```

Notes: When reading in a new dataset, it is always a good idea to
glimpse at a few rows like we did in the previous slide to get an idea
of what the data looks like.

Another helpful practice is to use the `.info()` method to get an
overview of the column data types and see if there are any `NaNs`
(missing values).

If there are many missing values in a column, we would want to look into
why that is. Later in the course, we will learn about how to visualize
missing values to understand if there are patterns in which values are
missing, which could affect our data analysis.

In this and the previous slide, we can also see that our dataset is
pretty big, there are almost 40,000 rows!

The first time working with such large datasets in Altair can be a bit
confusing because Altair saves the entire dataframe as part of the
visualization, when working with `pandas` dataframes,

This is great because each visualization is reproducible in itself, we
don’t need to go looking for the data if we come across a plot on the
web, or worry that the authors didn’t upload it.

However, for large datasets this causes the visualizations files to
become really big, and Altair shows a warning for any dataset larger
than 5000 rows.

We will talk about this in detail in a later module, and see different
strategies for working with large datasets.

---

## Working with large data in Altair via URLs

``` python
alt.Chart('https://website.com/data.csv').mark_line().encode(
    x='column1:T',
    y='column2:Q')
```

Notes: In this slide deck, we’re going to leverage the fact that Altair
does not have to work with dataframes, but can also use a URL link that
points to data that has been uploaded somewhere on the web. The slides
show an example of what this syntax looks like in general.

Since we have uploaded our dataset to the course online repository, we
will read the data directly from there using this URL
<https://raw.githubusercontent.com/UBC-MDS/exploratory-data-viz/main/chapters/en/slides/module2/data/world-data-gapminder.csv>.

This is powerful since we can use any data online without downloading it
first and it allows us to create Altair charts without worrying that the
entire dataframe will be included! Since Altair knows the location of
the data online, the chart is still reproducible as long as the data is
not removed from its online location.

The drawback of not using a dataframe, is that Altair cannot rely on
pandas to infer what type of data there is in each column, so we need to
help it by indicating the datatype.

This is what the `:T` and `:Q` after the column names do and an
explanation of all the data types in Altair can be found in the next
slide.

---

## Data types need to be manually specified when not working with pandas

| Data Type    | Shorthand Code | Description                    | Examples                               |
|--------------|----------------|--------------------------------|----------------------------------------|
| Ordinal      | `O`            | a discrete ordered quantity    | “dislike”, “neutral”, “like”           |
| Nominal      | `N`            | a discrete un-ordered quantity | eye color, postal code, university     |
| Quantitative | `Q`            | a continuous quantity          | 5, 5.0, 5.011                          |
| Temporal     | `T`            | a time or date value           | date (August 13 2020), time (12:00 pm) |

Notes: Altair recognizes the four main column types, which you can see
in this slide (that you also saw in the [Programming with Python
course](https://prog-learn.mds.ubc.ca/en/)).

Ordinal and nominal both describe categorical data.

Ordinal implies that there is a natural order to the categories. for
example, movie ratings with 1-5 stars would be an ordinal scale since a
five-star rating is better than a single-star rating.

In contrast, there is no such order for nominal categories, for example
colours, fruits, or countries.

Quantitative data describes data that is continuous, which means that it
is a number that can be described with infinite precision. For example,
someone’s height could be said to be either 170 cm, 170.12 cm, 170.1281
cm, and so on depending on how accurately we can measure them.

Dates are generally temporal, but there are instances when it makes
sense to defines them as ordinal or even nominal categories, for example
when having just a few dates to compare between.

Armed with this knowledge, let’s get started visualizing our data!

---

## Draw a line chart for how you think the world population has changed since the 1800s

<br> <br> <br> <br>

Take a few minutes to first sketch out how you would expect your plot to
appear before going to the next slide.

Notes:

Now that we have seen what the data table looks like, and which data
type the values in each column are, let’s think about what we would want
to visualize and why.

Since the data reaches all the way back to the 1800s, it would be really
interesting to plot how the world population has been growing up until
today. We could use a line plot for this as we learned in the first
module.

Draw this out on paper yourself so that it is clear what you expect the
plot before going to the next slide.

---

### Our sketched out plot

<center>
<img src="/module2/drawing.png"  width = "70%">
</center>

Notes:

If we drew this visualization out on paper, we would expect something a
little like this - a single line that increases from the 1800s up until
today as the population increased. It’s a good idea to include axis
labels too!

---

## A line chart is a good choice for trends over time

``` python
import altair as alt

gm_url = 'https://raw.githubusercontent.com/UBC-MDS/exploratory-data-viz/main/chapters/en/slides/module2/data/world-data-gapminder.csv'
alt.Chart(gm_url).mark_line().encode(
    x='year:T',
    y='population:Q')
```

<iframe src="/module2/charts/04/unnamed-chunk-3.html" width="100%" height="420px" style="border:none;">
</iframe>

Notes:

Next, we try to plot it in Altair using `mark_line()` and mapping `year`
to the x-axis and `population` to the y-axis.

But the plot on this slide doesn’t look like a line plot, why is that?

Because every country has multiple entries, one for each year. We have
plotted the population for every single country in every year and
connected them all with a line.

That’s not what we want!

---

## The *.sum()* aggregate method will show us the trend of the entire world

``` python
alt.Chart(gm_url).mark_line().encode(
    x='year:T',
    y='sum(population):Q')
```

<iframe src="/module2/charts/04/unnamed-chunk-4.html" width="100%" height="420px" style="border:none;">
</iframe>

Notes: We want to see how the **world** population has been changing.

We can calculate this by summing up all the countries’ populations for
each year via the `.sum()` aggregation method in Altair.

That looks much better!

Interestingly, it seems like the world population have been growing in
two distinct phases: slowly before 1950, and more rapidly afterwards.

We will talk more about that in a few slides.

We can see here that Altair automatically changes the axis label for us
to reflect the operation that we have performed on the data, here taking
the “sum” of the countries.

This is often great to keep track of how we have aggregated the data,
but is not always needed.

In this case, our plot could be made even clearer if the axis title read
“World population” instead.

---

## Changing axes titles clarifies makes our plot easier to interpret

``` python
alt.Chart(gm_url).mark_line().encode(
    x='year:T',
    y=alt.Y('sum(population):Q', title='World population'))
```

<iframe src="/module2/charts/04/unnamed-chunk-5.html" width="100%" height="420px" style="border:none;">
</iframe>

Notes:

To change an axis title, we can use the helper functions `alt.X` and
`alt.Y`, instead of `x=` and `y=`.

These have the role of customizing things like titles, orders, groups,
and scales for the axes. When using just `y='column'`, we’re still
calling `alt.Y()` under the hood, we just save ourselves some typing.

We can also get rid of the `y=` and `x=` parts altogether as well which
is even more efficient.

We will do a deep dive into titles for axis and other chart elements in
a later module.

From now on we will just use it to clarify when an automatic label might
be confusing.

---

## Area charts are also effective at visualizing trends over time

``` python
alt.Chart(gm_url).mark_area().encode(
    alt.X('year:T'),
    alt.Y('sum(population):Q', title='World population'))
```

<iframe src="/module2/charts/04/unnamed-chunk-6.html" width="100%" height="420px" style="border:none;">
</iframe>

Notes: Let’s see how we can visualize the world population changes with
an area chart instead of a line chart.

Thanks to Altair’s consistent visualization grammar, the modifications
we need to make to the code are minor. Replace `mark_line` with
`mark_area` and we’re done.

For showing a single trend over time, the choice between a line and area
chart comes down to aesthetics. They are both effective choices for this
purpose.

However, when visualizing the trends over time for multiple groups,
lines and areas have different advantages, as we will see next.

---

## Area charts are preferred when the total of the groups is the most important

``` python
alt.Chart(gm_url).mark_area().encode(
    alt.X('year:T'),
    alt.Y('sum(population):Q', title='World population'),
    color='region:N')
```

<iframe src="/module2/charts/04/unnamed-chunk-7.html" width="100%" height="420px" style="border:none;">
</iframe>

Notes: The y-axis range of this chart is the same as the one on the
previous slide, so it is easy to see how the total world population has
changed over time.

From the stacked coloured regions, we also get a rough idea of how each
region has grown, but it is hard to compare exactly, especially for
regions that are not stacked next to each other.

For example, we can’t really tell if Europe or Africa, has the largest
population in the most recent year.

---

## It is helpful to clarify that the areas are stacked on top of each other

``` python
alt.Chart(gm_url).mark_area().encode(
    alt.X('year:T'),
    alt.Y('sum(population):Q', title='Cumulative population of stacked regions'),
    color='region:N')
```

<iframe src="/module2/charts/04/unnamed-chunk-8.html" width="100%" height="420px" style="border:none;">
</iframe>

Notes: Altair stacks by areas by default, which is usually what we want
when creating an area chart with groups.

But if someone saw our chart without knowing this, they might think that
the areas are layered behind each other, so that we only see the top of
the blue region peak out behind the orange region.

To prevent this misunderstanding, we can change the y-axis label to
clearly state that areas are stacked.

Taken together, stacked area charts are ideal when you want to focus on
a total measurement and give a rough idea of the contributions from
different groups.

---

## Line charts are preferred when the individual groups are the most important

``` python
alt.Chart(gm_url).mark_line().encode(
    alt.X('year:T'),
    alt.Y('sum(population):Q', title='Population'),
    color='region:N')
```

<iframe src="/module2/charts/04/unnamed-chunk-9.html" width="100%" height="420px" style="border:none;">
</iframe>

Notes: Using a line chart is the preferred choice when we want to view
the exact values of each group and don’t care as much about the total of
the groups added together.

For example, here it is immediately clear that Africa has a bigger
population than Europe and we can see that the populations shifted
shortly after the year 2000.

On the other hand, it’s quite cognitively demanding to try to
reconstruct the total world population by adding all the lines up
together, especially over time!

In summary, split line charts are ideal when you want to compare the
different groups accurately.

---

## When will the world’s population stop growing?

``` python
alt.Chart(gm_url).mark_area().encode(
    alt.X('year:T'),
    alt.Y('sum(population):Q', title='World population'))
```

<iframe src="/module2/charts/04/unnamed-chunk-10.html" width="100%" height="420px" style="border:none;">
</iframe>

Notes: Going back to the area chart with one group, let’s look closer at
the growth curve of the world’s population.

First, there is a slow linear phase, but soon after the end of the
second world war, it the growth starts increasing much more rapidly (but
still in a straight line).

Will the world population keep growing like this for much longer?

---

## The world population is predicted to stabilize at around 11 billion

``` python
alt.Chart(gm_url).mark_area().encode(
    alt.X('year:T'),
    alt.Y('mean(children_per_woman):Q', title='Average children per woman worldwide'))
```

<iframe src="/module2/charts/04/unnamed-chunk-11.html" width="100%" height="420px" style="border:none;">
</iframe>

Notes: Fortunately, the world population is predicted to stabilize
around 11 billion people at the end of the century.

Why? Because as living conditions improve around the world, child
mortality is going down as can be seen in this visualization.

In countries where child mortality is high, women will often give birth
to more children than they want in order to protect against losing some
of their children.

Lower child mortality leads to more predictable family planning, which
in turn often leads to smaller families. In the majority of countries
where child mortality has been observed to decrease, the number of
children per woman has followed and stabilized around two.

If you’re interested in knowing more about the world population
predictions, you can use Gapminder’s online resources, for example [this
video on population
growh](https://www.gapminder.org/answers/how-did-the-world-population-change/)
and [this one on why it will slow
down](https://www.gapminder.org/answers/the-rapid-growth-of-the-world-population-when-will-it-slow-down/).

---

# Let’s apply what we learned!

Notes: <br>
