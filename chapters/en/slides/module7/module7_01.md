---
type: slides
---

# Tooltips, Zoom, and Selections

Notes: One of the unique features of Altair is that it does not only
define a grammar of graphics, but also a grammar of interactivity.

In this module we will see how to use this grammar to add tooltips,
selections, panning, and zooming to our charts.

One conceptual difference from previous modules is that while
interactive chart elements can be added as part of answering a specific
question they are often used to help the person interacting with your
graphs to answer additional questions that might come up as they are
studying your visualizations.

---

## Tooltips can provide additional information about data points

``` python
import altair as alt
from vega_datasets import data

cars = data.cars()
alt.Chart(cars).mark_circle().encode(
    alt.X('Horsepower', title='Enging power (hp)'),
    alt.Y('Miles_per_Gallon', title='Fuel efficiency (miles / gal)'),
    tooltip='Name')
```

<iframe src="/module7/charts/01/unnamed-chunk-1.html" width="100%" height="420px" style="border:none;">
</iframe>

Notes: We have already seen in previous modules how we adding a tooltip
can provide us with information that is not captured on the axes.

In this plot, we have added the name of each vehicle as the tooltip,
which can be seen when hovering over the respective point with the
mouse.

Tooltips are particularly useful for dataframe columns that contain many
unique values so that it would not be possible to visualize them using
e.g. different colors and a legend as we saw an example of in an earlier
module.

---

## Tooltips can also add more precise values for dataframe columns on the chart axes

``` python
alt.Chart(cars).mark_circle().encode(
    alt.X('Horsepower', title='Enging power (hp)'),
    alt.Y('Miles_per_Gallon', title='Fuel efficiency (miles / gal)'),
    tooltip=['Name', 'Horsepower'])
```

<iframe src="/module7/charts/01/unnamed-chunk-2.html" width="100%" height="420px" style="border:none;">
</iframe>

Notes: We can also use tooltips for other information than string
labels, for example when it is important to know an exact value of a
quantitative dataframe column.

In this slide we have added both the `Name` label and the `Horsepower`
value to the tooltip by specifying them as a list.

As you can see when hovering over the points, Altair automatically adds
the name of the dataframe column as grey text so that we know what the
two values in the tooltip represent.

---

## Points can be linked to an URL to provide more information about the data

``` python
cars['URL'] = 'https://duckduckgo.com/?q=' + cars['Name']
alt.Chart(cars).mark_circle().encode(
    alt.X('Horsepower', title='Enging power (hp)'),
    alt.Y('Miles_per_Gallon', title='Fuel efficiency (miles / gal)'),
    href='URL',
    tooltip='Name')
```

<iframe src="/module7/charts/01/unnamed-chunk-3.html" width="100%" height="420px" style="border:none;">
</iframe>

Notes: While a tooltip that shows each cars name when hovering over it
adds some information, it might not be that meaningful to those of us
that are not familiar with car model names.

To facilitate finding more information about each cars, we could add an
interaction so that clicking the point would search for the name of the
car online.

In this slide we create a new column in the dataframe to be used with
the `href` encoding. Now that we click a point in the chart, we will be
taken to the search page for this car name at DuckDuckGo (a
privacy-focused search engine).

---

## Zooming in can help resolve detail in crowded areas of the chart

``` python
alt.Chart(cars).mark_circle().encode(
    alt.X('Horsepower', title='Enging power (hp)'),
    alt.Y('Miles_per_Gallon', title='Fuel efficiency (miles / gal)'),
    href='URL',
    tooltip='Name').interactive()
```

<iframe src="/module7/charts/01/unnamed-chunk-4.html" width="100%" height="420px" style="border:none;">
</iframe>

Notes: In all our previous charts, it has been difficult to resolve
exactly which point a tooltip refers to in the more dense regions of the
charts where points overlap.

One approach to deal with this would be to making the points smaller or
the visualization larger. However, this might make individual points
harder to see or take up more space than we have available for our
visualizations.

Instead, we could enable zooming and panning on the chart with the
`interactive()` method. This works on all visualizations except maps and
allows us to zoom in by using the scroll wheel of the mouse and click &
drag to pan around the chart. Double clicking resets the zoom to the
default view.

In addition to resolving tooltip ambiguity, this allows your audience to
decide which regions of the chart they want to look closer at, which
would not be possible with a static visualization.

---

## Adding selections allows us to highlight data points

``` python
brush = alt.selection_interval()
 
(alt.Chart(cars).mark_circle().encode(
    alt.X('Horsepower', title='Enging power (hp)'),
    alt.Y('Miles_per_Gallon', title='Fuel efficiency (miles / gal)'))
.add_selection(brush))
```

<iframe src="/module7/charts/01/unnamed-chunk-5.html" width="100%" height="420px" style="border:none;">
</iframe>

Notes: Selections are useful to highlight certain points in a chart.
This is particularly helpful when highlighting the same points in
multiple linked charts, to interrogate these observations across
additional dataframe columns.

In a few slides, we will see a concrete example of how this can be used
to answer a specific question, but let us first walk through the syntax
for adding an interaction to a single chart.

To add a selection to a chart, we first need to create the selection
object.

Here we create and “interval selection”, and assign it to the variable
name `brush`. The reason for this name is that selecting points with an
interval is often referred to as “brushing”, and you will see this
terminology when reading online resources on interactive selections.

After creating the selection object, we add it to our chart using
`add_selection()`, which means that we can drag and drop in the chart to
create a grey selection rectangle.

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

<iframe src="/module7/charts/01/unnamed-chunk-6.html" width="100%" height="420px" style="border:none;">
</iframe>

Notes: To highlighted the selected in a different color than the rest of
the data, we can use a conditional statement.

Altair has a built in `if/else` function called `condition` that checks
if an event is present (such as selection) and then lets us define what
to do if it is `True` and if it is `False`. You can think of it like
this:

    alt.condition(check-this, if-true-do-this, if-false-do-this)

In this plot we check if our selection `brush` is on the points, and if
that is true we use the `Origin` dataframe column to color the points,
otherwise we use the value `'lightgray'`.

`alt.value` is a help function for when we want to use a single value
for all the data points, rather than values from a column in the
dataframe.

You can click to drag the selection around and to clear it you can
either double click the selection or click once outside the selected
region.

---

## Linking selections between charts helps exploring observations across more columns

``` python
brush = alt.selection_interval()
 
points = (alt.Chart(cars).mark_circle().encode(
    alt.X('Horsepower', title='Enging power (hp)'),
    alt.Y('Miles_per_Gallon', title='Fuel efficiency (miles / gal)'),
    color=alt.condition(brush, 'Origin', alt.value('lightgray')))
.add_selection(brush))

points | points.encode(y='Weight_in_lbs', x='Acceleration')
```

<iframe src="/module7/charts/01/unnamed-chunk-7.html" width="100%" height="420px" style="border:none;">
</iframe>

Notes: In this slide we have plotted `Horsepower` against
`Miles_per_Gallon` and `Acceleration` against `Weight_in_lbs`. We can
see how the data is spread out in both charts, but we don’t know how the
points are related between the two charts.

For example, we might wonder if the cars with really powerful engines
and low mileage are the ones with low or high acceleration and weight.
There is not way to tell this from just looking at these two chart but
by highlighting points in one of the charts, the same observations will
be highlighted in the other chart.

Now we can answer our question! Our highlight shows that the cars with
high engine power and low mileage are largely heavy cars with slow
acceleration. Importantly, the relationships of other observations can
also be explored in the plot without us having to change anything.

As you can see in this slide selections are automatically linked between
plots that are created from the same base chart, so we don’t need to add
any code to link the selection between the charts in this case.

---

## Multiple selections can be used to highlight points

``` python
brush = alt.selection_interval(resolve='intersect')
 
points = (alt.Chart(cars).mark_circle().encode(
    alt.X('Horsepower', title='Enging power (hp)'),
    alt.Y('Miles_per_Gallon', title='Fuel efficiency (miles / gal)'),
    color=alt.condition(brush, 'Origin', alt.value('lightgray')))
.add_selection(brush))

points | points.encode(y='Weight_in_lbs', x='Acceleration')
```

<iframe src="/module7/charts/01/unnamed-chunk-8.html" width="100%" height="420px" style="border:none;">
</iframe>

Notes: In the previous slide we only had one selection, if we started to
select in the right hand plot, the chart to the left would clear its
selection.

We could modify this behavior so that there are separate selections in
the the two charts and only points that fall within the intersection or
union of both the selections are highlighted as in this slide.

---

# Let’s apply what we learned!

Notes: <br>