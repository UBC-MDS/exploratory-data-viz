---
type: slides
---

# Creating Area Charts

<head>
<base target="_blank">
</head>
<head>
<base target="_blank">
</head>

Notes: In this module we will be learning how to create area charts and
when they are a suitable alternative to use instead of line charts.

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

This is the same data we are working with in the assignments for the
first two modules.

We will be looking at many different data sets in later labs, but we’re
sticking to a familiar one for now so that we can focus on laying down a
solid understanding of the visualization principles with data that we
already know.

---

## Read in and glimpse at the data with pandas

``` python
import pandas as pd

gm = pd.read_csv('data/world-data-gapminder.csv', parse_dates=['year'])
# TODO remove when we change to HTML or rewrite text as for why top ten
gm = gm[gm['country'].isin(gm[gm['year'] == '2018'].nlargest(10, ['population'])['country'])]
gm
```

```out
             country       year  population    region        sub_region  income_group  life_expectancy  income  children_per_woman  child_mortality  pop_density  co2_per_capita  years_in_school_men  years_in_school_women
2628      Bangladesh 1800-01-01    19200000      Asia     Southern Asia  Lower middle             25.5     876                6.70           508.00          NaN             NaN                  NaN                    NaN
2629      Bangladesh 1801-01-01    19300000      Asia     Southern Asia  Lower middle             25.5     876                6.70           508.00          NaN             NaN                  NaN                    NaN
2630      Bangladesh 1802-01-01    19300000      Asia     Southern Asia  Lower middle             25.5     876                6.70           508.00          NaN             NaN                  NaN                    NaN
2631      Bangladesh 1803-01-01    19300000      Asia     Southern Asia  Lower middle             25.5     876                6.70           508.00          NaN             NaN                  NaN                    NaN
2632      Bangladesh 1804-01-01    19400000      Asia     Southern Asia  Lower middle             25.5     876                6.70           508.00          NaN             NaN                  NaN                    NaN
...              ...        ...         ...       ...               ...           ...              ...     ...                 ...              ...          ...             ...                  ...                    ...
37225  United States 2014-01-01   318000000  Americas  Northern America          High             78.9   51800                1.95             6.80         34.7            16.5                 14.5                   14.9
37226  United States 2015-01-01   320000000  Americas  Northern America          High             78.8   52800                1.93             6.60         35.0             NaN                 14.6                   15.1
37227  United States 2016-01-01   322000000  Americas  Northern America          High             78.8   53300                1.92             6.50         35.2             NaN                  NaN                    NaN
37228  United States 2017-01-01   324000000  Americas  Northern America          High             79.0   54200                1.91             6.23         35.5             NaN                  NaN                    NaN
37229  United States 2018-01-01   327000000  Americas  Northern America          High             79.1   54900                1.90             6.06         35.7             NaN                  NaN                    NaN

[2190 rows x 14 columns]
```

Notes: This dataset is made available via an URL and we can download and
read it into pandas with `read_csv`.

Here we also tell pandas to read in the `year` column as a date, rather
than an integer, which is the default behaviour.

Remember that Altair uses the `pandas` data types to infer the data it
is working with. Integers would show up on the Altair chart axes as
`1,990, 2,000, etc` whereas dates are shown as `1990, 2000, etc`

---

## *.info()* shows column data types and missing values

``` python
gm.info()
```

```out
<class 'pandas.core.frame.DataFrame'>
Int64Index: 2190 entries, 2628 to 37229
Data columns (total 14 columns):
 #   Column                 Non-Null Count  Dtype         
---  ------                 --------------  -----         
 0   country                2190 non-null   object        
 1   year                   2190 non-null   datetime64[ns]
 2   population             2190 non-null   int64         
 3   region                 2190 non-null   object        
 4   sub_region             2190 non-null   object        
 5   income_group           2190 non-null   object        
 6   life_expectancy        2190 non-null   float64       
 7   income                 2190 non-null   int64         
 8   children_per_woman     2190 non-null   float64       
 9   child_mortality        2190 non-null   float64       
 10  pop_density            690 non-null    float64       
 11  co2_per_capita         1240 non-null   float64       
 12  years_in_school_men    460 non-null    float64       
 13  years_in_school_women  460 non-null    float64       
dtypes: datetime64[ns](1), float64(7), int64(2), object(4)
memory usage: 256.6+ KB
```

Notes: When reading in a new dataset, it is always a good idea to
glimpse at a few rows like we did in the previous slide to get an idea
of what the data looks like.

Another helpful practice is to use the `.info()` method to get an
overview of the column data types and see if there are any `NaNs`
(missing values).

---

## Draw a line chart for how you think the world population has changed since the 1800s

<br> <br> <br> <br>

Take a few minutes to first sketch out how you would expect your plot to
appear before going to the next slide.

Notes:

Now that we are somewhat familiar with the data formats, let’s think
about what we would want to visualize and why.

Since the data reaches all the way back to the 1800s, it would be really
interesting to plot how the world population has been growing up until
today. We could use a line plot for this as we learned in the first
module.

Draw this out on paper yourself so that it is clear what you expect the
plot before going to the next slide.

---

### Our sketched out plot

<center>
<img src="/module2/drawing.png"  width = "80%">
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

alt.Chart(gm).mark_line().encode(
    x='year',
    y='population')
```

<iframe src="/module2/charts/04/unnamed-chunk-3.html" width="100%" height="400px" style="border-width:0;">
</iframe>

Notes:

Next, we try to plot it in Altair using `mark_line()` and maping `year`
to the x-axis and `population` to the y-axis.

Notes:

Next, we try to plot it in Altair using `mark_line()` and maping `year`
to the x-axis and `population` to the y-axis.

But the plot on this slide doesn’t look like a line plot, why is that?

Because every country has multiple entries, one for each year. We have
plotted the population for every single country in every year and
connected them all with a line.

That’s not what we want!

---

## The *.sum()* aggregate method will show us the trend of the entire world

``` python
alt.Chart(gm).mark_line().encode(
    x='year',
    y='sum(population)')
```

<iframe src="/module2/charts/04/unnamed-chunk-4.html" width="100%" height="400px" style="border-width:0;">
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
alt.Chart(gm).mark_line().encode(
    x='year',
    y=alt.Y('sum(population)', title='World population'))
```

<iframe src="/module2/charts/04/unnamed-chunk-5.html" width="100%" height="400px" style="border-width:0;">
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

For now on we will just use it to clarify when an automatic label might
be confusing.

---

## Area charts are also effective at visualizing trends over time

``` python
alt.Chart(gm).mark_area().encode(
      alt.X('year'),
      alt.Y('sum(population)', title='World population'))
```

<iframe src="/module2/charts/04/unnamed-chunk-6.html" width="100%" height="400px" style="border-width:0;">
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
alt.Chart(gm).mark_area().encode(
    alt.X('year'),
    alt.Y('sum(population)', title='World population'),
    color='region')
```

<iframe src="/module2/charts/04/unnamed-chunk-7.html" width="100%" height="400px" style="border-width:0;">
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
alt.Chart(gm).mark_area().encode(
    alt.X('year'),
    alt.Y('sum(population)', title='Cumulative population of stacked regions'),
    color='region')
```

<iframe src="/module2/charts/04/unnamed-chunk-8.html" width="100%" height="400px" style="border-width:0;">
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
alt.Chart(gm).mark_line().encode(
    alt.X('year'),
    alt.Y('sum(population)', title='Population'),
    color='region')
```

<iframe src="/module2/charts/04/unnamed-chunk-9.html" width="100%" height="400px" style="border-width:0;">
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
alt.Chart(gm).mark_area().encode(
    alt.X('year'),
    alt.Y('sum(population)', title='World population'))
```

<iframe src="/module2/charts/04/unnamed-chunk-10.html" width="100%" height="400px" style="border-width:0;">
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
alt.Chart(gm).mark_area().encode(
    alt.X('year'),
    alt.Y('mean(children_per_woman)', title='Average children per woman worldwide'))
```

<iframe src="/module2/charts/04/unnamed-chunk-11.html" width="100%" height="400px" style="border-width:0;">
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
