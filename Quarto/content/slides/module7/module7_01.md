---
type: slides
---

# Tooltips, Zoom, and Selections

Notes: One of the unique features of Altair is that it goes beyond
defining a grammar of graphics, and also defines a grammar of
interactivity.

In this module we will see how to use this grammar to add tooltips,
selections, panning, and zooming to our charts.

One conceptual difference from previous modules is that while
interactive chart elements can be added as part of answering a specific
question, they are also often used by your audience to answer additional
questions that might come up as they are studying your visualizations.

---

## The return of the cars dataset

``` python
import altair as alt
from vega_datasets import data

cars = data.cars()
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

Notes: For this slide deck we will be using the cars data set again,
since it lends itself well to demonstrate the interactive elements that
we will cover here.

You already saw this dataset in previous modules, but as a reminder it
contains data on individual car brands from three different regions over
time.

---

## Tooltips can provide additional information about data points

``` python
alt.Chart(cars).mark_circle().encode(
    alt.X('Horsepower', title='Enging power (hp)'),
    alt.Y('Miles_per_Gallon', title='Fuel efficiency (miles / gal)'),
    tooltip='Name')
```

<iframe src="/module7/charts/01/unnamed-chunk-2.html" width="100%" height="420px" style="border:none;">
</iframe>

Notes: We have seen in previous modules how adding a tooltip can provide
us with information that is not captured on the axes.

In this plot, we have used a tooltip to view the names of each vehicle
when hovering our cursor over the respective point.

Tooltips are particularly useful when we have dataframe columns that
contain many unique values; so many that it would not be possible to
visualize them effectively using different colours and a legend.

---

## Tooltips can also add more precise values for dataframe columns on the chart axes

``` python
alt.Chart(cars).mark_circle().encode(
    alt.X('Horsepower', title='Enging power (hp)'),
    alt.Y('Miles_per_Gallon', title='Fuel efficiency (miles / gal)'),
    tooltip=['Name', 'Horsepower'])
```

<iframe src="/module7/charts/01/unnamed-chunk-3.html" width="100%" height="420px" style="border:none;">
</iframe>

Notes: We can also use tooltips to add more than just one piece of
information when we hover over individual points.

For example, in addition to the car type for each observation, we have
also added the exact value for horsepower (which is mapped to the
x-axis) to make it easier to look them up on the chart.

We were able to do this by specifying the `Name` and the `Horsepower`
columns as a list that we passed to the tooltip argument.

When you hover the cursor over a point, you can also see that specifying
column names in a list to the tooltip parameter, leads Altair to
automatically add the name of the dataframe column as grey text so that
we know what the two values in the tooltip represent.

---

## Points can be linked to an URL to provide more information about the data

``` python
cars['URL'] = 'https://duckduckgo.com/?q=' + cars['Name']

alt.Chart(cars).mark_circle().encode(
    alt.X('Horsepower', title='Enging power (hp)'),
    alt.Y('Miles_per_Gallon', title='Fuel efficiency (miles / gal)'),
    href='URL',
    tooltip=['Name', 'URL'])
```

<iframe src="/module7/charts/01/unnamed-chunk-4.html" width="100%" height="420px" style="border:none;">
</iframe>

Notes: While a tooltip that shows each cars name when hovering over it
adds some information, it might not be that meaningful to those of us
that are not familiar with car model names.

To facilitate finding more information about each cars, we could add an
interaction so that clicking the point would search for the name of the
car online.

In this specific case, we have crafted the URL such that clicking the
point would search for the name of the car online using the DuckDuckGo
privacy-focused search engine.

We accomplished this by creating a new column in the dataframe called
`'URL'` which holds the full URL search address for each car.

The `href` encoding in Altair can be used to define a link action when a
chart element is clicked and here we set it to the URL field so that
when we click a point, we will open a browser at that web address.
`href` is what links are called in HTML code.

---

## Zooming and panning helps the audience explore the data

``` python
alt.Chart(cars).mark_circle().encode(
    alt.X('Horsepower', title='Enging power (hp)'),
    alt.Y('Miles_per_Gallon', title='Fuel efficiency (miles / gal)'),
    href='URL',
    tooltip=['Name', 'URL']).interactive()
```

<iframe src="/module7/charts/01/unnamed-chunk-5.html" width="100%" height="420px" style="border:none;">
</iframe>

Notes: In all our previous charts, it has been difficult to resolve
exactly which point a tooltip refers to in the more dense regions of the
charts where points overlap.

One approach to deal with this would be to make the points smaller or to
make the visualization larger. However, in some cases this might make
individual points harder to see or take up more space than we have
available for our visualizations.

Instead, we could enable zooming and panning on the chart with the
`interactive()` method. This works on all visualizations except maps and
allows us to zoom in by using the scrolling feature of our mouse or
touchpad, and pan by clicking and dragging the chart. Double clicking
resets the zoom and pan to the default view.

In addition to resolving tooltip ambiguity, adding the zooming and
panning feature allows your audience to decide which regions of the
chart they want to look closer at, which would not be possible with a
static visualization.

---

## Adding selections allows us to highlight data points

``` python
brush = alt.selection_interval()
 
(alt.Chart(cars).mark_circle().encode(
    alt.X('Horsepower', title='Enging power (hp)'),
    alt.Y('Miles_per_Gallon', title='Fuel efficiency (miles / gal)'))
.add_selection(brush))
```

<iframe src="/module7/charts/01/unnamed-chunk-6.html" width="100%" height="420px" style="border:none;">
</iframe>

Notes: Selections are useful to highlight certain points in a chart.
This is particularly helpful when highlighting the same points in
multiple linked charts.

In a few slides, we will see a concrete example of how this can be used
to answer a specific question, but first, let’s walk through the syntax
for adding selections to a single chart.

To add a selection to a chart, we first need to create the selection
object. In this slide we create and interval selection by specifying
`alt.selection_interval()` and then giving this the name `brush`.

The reason for this name is that selecting points with an interval is
often referred to as “brushing” in data visualization terminology. You
would commonly see this when reading online resources on interactive
selections in data visualization.

After creating the selection object, we add it to our chart using
`add_selection()`, which means that we can use our cursor in the chart
to create a grey selection rectangle by clicking and dragging with our
mouse or touchpad.

You can click to drag the selection around and to clear it you can
either double click the selection or click once outside the selected
region.

But it doesn’t look like any of the points are highlighted yet, why not?

---

## Highlighting points with selections requires a conditional statement

``` python
brush = alt.selection_interval()
 
(alt.Chart(cars).mark_circle().encode(
    alt.X('Horsepower', title='Enging power (hp)'),
    alt.Y('Miles_per_Gallon', title='Fuel efficiency (miles / gal)'),
    color=alt.condition(brush, 'Origin', alt.value('lightgray')))
.add_selection(brush))
```

<iframe src="/module7/charts/01/unnamed-chunk-7.html" width="100%" height="420px" style="border:none;">
</iframe>

Notes: To highlight the selected in a different colour than the rest of
the data, we can use a conditional statement.

Altair has a built in `if/else` function called `condition` that checks
if an event is present (such as selection) and then lets us define what
to do if it is `True`, and what to do if it is `False`. You can think of
it like this:

    alt.condition(check-this, if-true-do-this, if-false-do-this)

In the chart on this slide we check if our interval range selection
`brush` contains any data points. If that is true, we use the `Origin`
dataframe column to colour the points, otherwise we use the value
`'lightgray'`.

`alt.value` is a helper function for when we want to map a single value
to the data points, rather than mapping the values from a column in the
dataframe.

---

## Linking selections between charts helps exploring observations across more columns

``` python
brush = alt.selection_interval()
 
points = (alt.Chart(cars).mark_circle().encode(
    alt.X('Horsepower', title='Enging power (hp)'),
    alt.Y('Miles_per_Gallon', title='Fuel efficiency (miles / gal)'),
    color=alt.condition(brush, 'Origin', alt.value('lightgray')))
.add_selection(brush)).properties(height=225, width=300)

points | points.encode(x='Acceleration', y=alt.Y('Weight_in_lbs', title='Weight'))
```

<iframe src="/module7/charts/01/unnamed-chunk-8.html" width="100%" height="420px" style="border:none;">
</iframe>

Notes:

In this slide we have created two charts from the same dataframe. In the
first we have plotted `Horsepower` against `Miles_per_Gallon` and in the
second we have plotted `Acceleration` against `Weight_in_lbs`.

We can use this to see patterns or relationship between two variables
within each chart, but we don’t know how the points are related between
the two charts.

For example, we might wonder if the cars with really powerful engines
and low mileage are the ones with low or high acceleration and weight.
There is not way to tell this from just looking at these two charts.

However, if we could highlight points of interest in one chart, and then
see the same observations highlighted in the other chart - we would be
able to answer such a question!

As you can see in this slide selections are automatically linked between
the two charts. The reason this worked was because both these charts
have one point for each observation in the data, so that we selected a
point in one of the scatterplots the corresponding point for that same
observation could automatically be highlighted in the other scatterplot.

Now we can answer our question! Highlighting the observations where the
cars have high engine power and low mileage shows that they are mostly
heavy cars with slow acceleration. Importantly, the relationships of
other observations can also be explored in the plot without us having to
change anything.

---

## Multiple selections can be used to highlight points

``` python
brush = alt.selection_interval(resolve='intersect')
 
points = (alt.Chart(cars).mark_circle().encode(
    alt.X('Horsepower', title='Enging power (hp)'),
    alt.Y('Miles_per_Gallon', title='Fuel efficiency (miles / gal)'),
    color=alt.condition(brush, 'Origin', alt.value('lightgray')))
.add_selection(brush)).properties(height=225, width=300)

points | points.encode(x='Acceleration', y=alt.Y('Weight_in_lbs', title='Weight'))
```

<iframe src="/module7/charts/01/unnamed-chunk-9.html" width="100%" height="420px" style="border:none;">
</iframe>

Notes: In the previous slide we only had one selection possible at a
time. For example, if we started to first select observations in the
chart on the left, and then started to make another selection in the
chart on the right hand side, the chart to the left would clear its
selection.

We could modify this behavior so that there are separate selections in
the the two charts and only points that fall within the intersection or
union of both the selections are highlighted as in this slide.

This can be useful if you want to narrow down your data further select
observations that meet multiple conditions.

---

# Let’s apply what we learned!

Notes: <br>
