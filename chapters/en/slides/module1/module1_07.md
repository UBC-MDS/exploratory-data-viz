---
type: slides
---

# Aggregations, lines, and layers

Notes:

In this slide deck, we will see how to aggregate data in Altair (to plot
the mean, median, etc), how to create lineplots via `mark_line()`, and
how to combine line and point plots together via layers.

---

## Including all the data can hinder visualization of general trends

``` python
import altair as alt
from vega_datasets import data

cars = data.cars()
alt.Chart(cars).mark_point().encode(
    x='Weight_in_lbs',
    y='Miles_per_Gallon',
    color='Origin')
```

<iframe src="/module1/charts/07/unnamed-chunk-1.html" width="100%" height="420px" style="border:none;">
</iframe>

Notes: Throughout this course we will explore many different datasets,
but for now, we will stick to the `cars` dataset to keep it simple and
focus on introducing additional Altair functionality.

Let’s refresh our memory with this plot from the previous module.

We noted that it appears that cars differ in their weight and mileage
based on their country of origin. At least the American cars appear to
stand out, but it is difficult to see any differences between Europe and
Japan.

Visualizing all data points as in this slide is helpful to detect
patterns in the data.

But when showing all observations, it can be hard to pick up on general
trends in the data, e.g. if there are any differences in the mean weight
of cars made in either Japan or Europe.

To more effectively visualize such general trends in the data, we can
create plots of statistical summaries, such as means and medians.

In Altair (and pandas) these are referred to as data aggregations.

---

## Data aggregations are built into Altair

``` python
alt.Chart(cars).mark_point().encode(
    x='mean(Weight_in_lbs)',
    y='mean(Miles_per_Gallon)',
    color='Origin')
```

<iframe src="/module1/charts/07/unnamed-chunk-2.html" width="100%" height="420px" style="border:none;">
</iframe>

Notes: To plot the means of weight and mileage, we could use pandas to
first calculate the mean values, and then plot the resulting dataframe
in Altair.

This is powerful since we can access all aggregations built into pandas,
but it is a bit verbose for simple common operations, such as the mean.

Fortunately, Altair has shortcuts for plotting simple aggregations where
you provide the name of the aggregation together with the name of the
column inside a string as in the example in this slide.

<a href="https://altair-viz.github.io/user_guide/encoding.html#binning-and-aggregation" target="_blank">The
Altair documentation includes a table with all available
aggregations</a> (scroll down a little on the linked page).

In this visualization, we can detect small differences between the means
of the Japanese and Europeans cars, which was not discernible when we
plotted all the points.

Whether this difference is big enough to reach a different conclusion
than when inspecting the previous plots depends on our application and
the purpose of the data exploration.

---

## Plotting aggregations to visualize trends over time

``` python
cars
```

```out
                          Name  Miles_per_Gallon  Cylinders  Displacement  Horsepower  Weight_in_lbs  Acceleration       Year  Origin
0    chevrolet chevelle malibu              18.0          8         307.0       130.0           3504          12.0 1970-01-01     USA
1            buick skylark 320              15.0          8         350.0       165.0           3693          11.5 1970-01-01     USA
2           plymouth satellite              18.0          8         318.0       150.0           3436          11.0 1970-01-01     USA
3                amc rebel sst              16.0          8         304.0       150.0           3433          12.0 1970-01-01     USA
4                  ford torino              17.0          8         302.0       140.0           3449          10.5 1970-01-01     USA
..                         ...               ...        ...           ...         ...            ...           ...        ...     ...
401            ford mustang gl              27.0          4         140.0        86.0           2790          15.6 1982-01-01     USA
402                  vw pickup              44.0          4          97.0        52.0           2130          24.6 1982-01-01  Europe
403              dodge rampage              32.0          4         135.0        84.0           2295          11.6 1982-01-01     USA
404                ford ranger              28.0          4         120.0        79.0           2625          18.6 1982-01-01     USA
405                 chevy s-10              31.0          4         119.0        82.0           2720          19.4 1982-01-01     USA

[406 rows x 9 columns]
```

Notes: Aggregations are often helpful when comparing trends over time,
especially when there are multiple groups in the data. In the cars
dataset, there is a `Year` column, indicating when the car was made.

Often when there is a notion of time in the data, it is interesting to
see how values in the dataframe change over time.

In this case, we might be interested in knowing whether newer cars are
more fuel-efficient than older ones.

Presumably, they should be, but does it differ depending on where the
car was made?

Let’s find out!

---

## Plotting aggregations to visualize trends over time works well

``` python
alt.Chart(cars).mark_point().encode(
    x='Year',
    y='mean(Miles_per_Gallon)')
```

<iframe src="/module1/charts/07/unnamed-chunk-4.html" width="100%" height="420px" style="border:none;">
</iframe>

Notes: To visualize the mean mileage for each year of all cars, we want
to perform the aggregation on the `Miles_per_Gallon` column while
leaving the `Year` column intact.

As you can see this plot one value (the mean) for each year in the
dataframe.

Here we can see that the observations in this dataframe span the years
1970-1982 and it does indeed look like the mileage is getting better
over time as we expected!

---

## Plotting all data to visualize trends over time is not effective

``` python
alt.Chart(cars).mark_point().encode(
    x='Year',
    y='Miles_per_Gallon')
```

<iframe src="/module1/charts/07/unnamed-chunk-5.html" width="100%" height="420px" style="border:none;">
</iframe>

Notes: As a comparison with the previous slide, if we instead of the
mean would plot all the data points for each year, it would be much more
difficult to see the pattern over time as you can see here.

---

## Plotting points to visualize trends over time is not ideal

``` python
alt.Chart(cars).mark_point().encode(
    x='Year',
    y='mean(Miles_per_Gallon)',
    color='Origin')
```

<iframe src="/module1/charts/07/unnamed-chunk-6.html" width="100%" height="420px" style="border:none;">
</iframe>

Notes: If we try to explore the mileage over time while grouping the
cars according to their origin, it is a bit difficult to immediately
recognize which points belong to which group.

In fact, using points for visualizing trends is not ideal, and lines are
often preferred as we will see in the next slide.

---

## Plotting lines to visualize trends over time is ideal

``` python
alt.Chart(cars).mark_line().encode(
    x='Year',
    y='mean(Miles_per_Gallon)',
    color='Origin')
```

<iframe src="/module1/charts/07/unnamed-chunk-7.html" width="100%" height="420px" style="border:none;">
</iframe>

Notes: One key advantage of line plots is that they connect all the
observations that belong to the same group presenting them as one
unified graphical object (one line), which is easy for us to distinguish
when looking at the plot instead of trying to connect the dots mentally.

Another advantage is that the slope of the line makes it easier to see
if the value from one year to another is increasing or decreasing.

Altair grammar lets us switch from a point plot to a line plot, by only
changing `mark_point()` to `mark_line()`, and keeping the rest of the
code as-is.

In this plot, we can clearly compare the mileage trends over time to
conclude that cars from all origins improved their mileage, and that the
trajectory and mileage values are the most similar between Europe and
Japan.

---

## Combining a line with a set of points via layers

``` python
line = alt.Chart(cars).mark_line().encode(
    x='Year',
    y='mean(Miles_per_Gallon)')

point = alt.Chart(cars).mark_point().encode(
    x='Year',
    y='mean(Miles_per_Gallon)')

line + point
```

<iframe src="/module1/charts/07/unnamed-chunk-8.html" width="100%" height="420px" style="border:none;">
</iframe>

Notes:

To augment a line plot, it is sometimes helpful to add `point` marks for
each data point along the line, to emphasize where the observations
fall.

This is helpful since the line drawn between points could be misleading
if we have very few points.

For example, if you see a straight line, does that mean there are just
two points, one in each corner of the line?

Or are there ten points spread out all along the line?

To combine two different types of graphical marks (line and point in
this case), we will use Altair’s *layering* grammar.

In this slide, we start by defining each chart separately:

first a line plot, <br> then a point plot.

We can then use `+` (plus) operator to combine the two into a layered
chart.

---

## Building upon previous plots can save time when combining charts

``` python
line = alt.Chart(cars).mark_line().encode(
    x='Year',
    y='mean(Miles_per_Gallon)')

line + line.mark_point()
```

<iframe src="/module1/charts/07/unnamed-chunk-9.html" width="100%" height="420px" style="border:none;">
</iframe>

Notes: We can also create a layered plot by reusing a previous chart
definition.

Rather than creating the point plot from scratch, we can start with the
line plot, and then invoke the `mark_point` method.

We could also have typed `mark_line(point=True)`, which is a special
case for getting points on a line since it is such a common operation,
but the layering grammar extends to other plots, so it is more helpful
to focus on learning that.

---

## Showing raw values together with the mean is often helpful

``` python
line = alt.Chart(cars).mark_line().encode(
    x='Year',
    y='mean(Miles_per_Gallon)')

line + line.mark_point().encode(y='Miles_per_Gallon')
```

<iframe src="/module1/charts/07/unnamed-chunk-10.html" width="100%" height="420px" style="border:none;">
</iframe>

Notes: When we are combing plots in layers, we can not only change the
mark, but also the encodings.

This way, we can create a layer with one point per observations, and
with a line for the average values.

For this, we need to use `encode` again after creating the first plot,
to instruct Altair to use the raw values instead of the mean for the
points.

(note that the axis now has two labels, we will see how to change that
in a future lecture).

This type of visualization is helpful when we want to show both the
underlying data and a statistical summary, which is often helpful for
elucidating what the data tells us.

It is also a good check to make sure nothing unexpected is going on with
the raw values as we saw in the introductory example with Anscombe’s
quartet.

---

## All encodings of the base chart are propagated unless they are overwritten

``` python
line = alt.Chart(cars).mark_line().encode(
    x='Year',
    y='mean(Miles_per_Gallon)',
    color='Origin')

line + line.mark_point().encode(y='Miles_per_Gallon')
```

<iframe src="/module1/charts/07/unnamed-chunk-11.html" width="100%" height="420px" style="border:none;">
</iframe>

Notes: We have already seen that the x and y encoding remain the same in
any subsequently created plots.

Here, we’re showing that this also applies to the colour encoding to
illustrate that any encoding will be propagated to all layers unless
they are specifically overwritten.

If we would only have added colour to the point chart, there would still
have been a single line instead of three.

---

# Let’s apply what we learned!

Notes: <br>
