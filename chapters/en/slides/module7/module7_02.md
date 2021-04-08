---
type: slides
---

# Advanced Selections

Notes: In this chapter we will learn how to create new types of
selections such as clicks and hovers. We will also see how to link
selections between charts that do not stem from the same base chart, and
how to add selections to geographical visualizations.

---

## Selections can be triggered on clicks instead of dragging with the mouse

``` python
import altair as alt
from vega_datasets import data

cars = data.cars()
click = alt.selection_multi()
bars = (alt.Chart(cars).mark_bar().encode(
    x='count()',
    y='Origin',
    color='Origin',
    opacity=alt.condition(click, alt.value(0.9), alt.value(0.2)))
.add_selection(click)).properties(width=300)

bars
```

<iframe src="/module7/charts/02/unnamed-chunk-1.html" width="100%" height="420px" style="border:none;">
</iframe>

Notes: When creating charts such as barcharts and maps, it is often more
intuitive to be able to click the objects to select rather than dragging
with the mouse.

In this slide we use `selection_multi` to create a selection based on
what we click with the mouse. If we hold the shift key, we can select
multiple bars (to disable this use `selection_single` instead).

You can also see that instead of changing the color of the bar on
selection, we here use `alt.condition` to change the opacity instead.
Whether we change the color or opacity on selection is mostly an
aesthetic choice.

We assign the chart to a variable name because we will reuse it in the
next slide and set the dimensions of the plot to fit on later slides
with more complex layouts.

---

## Combining charts with different selections

``` python
brush = alt.selection_interval()
points = (alt.Chart(cars).mark_circle().encode(
    x='Horsepower',
    y='Miles_per_Gallon',
    color=alt.condition(brush, 'Origin', alt.value('lightgray')))
.add_selection(brush)).properties(width=300, height=200)

points & bars
```

<iframe src="/module7/charts/02/unnamed-chunk-2.html" width="100%" height="420px" style="border:none;">
</iframe>

Notes: To add two charts together, we can use what we learned previously
about Altair’s layout operators. To concatenate the charts vertically,
we’re here using the `&` operator.

In contrast to the two scatterplots in an earlier slide, these charts
are not created from the same base chart, so there selections are not
linked.

What if we want to link the selections so that when we select a region
of origin in the bar chart the points in the scatter plot that are from
the same origin would be highlighted?

This would be useful to study observations from each Origin separately,
so how can we perform this linkage in Altair?

---

## Linking selections from separate charts requires explicit columns to select on

``` python
click = alt.selection_multi(fields=['Origin'])
bars = bars.add_selection(click)
points = points.encode(opacity=alt.condition(click, alt.value(0.9), alt.value(0.2)))

points & bars
```

<iframe src="/module7/charts/02/unnamed-chunk-3.html" width="100%" height="420px" style="border:none;">
</iframe>

Notes: To link separate charts together, we need to be explicit about
what happens when a selection is made.

For example, to link a click of a bar to a selection in the scatterplot,
we need to say which column in the dataframe should be used to select
on.

In this case, we only have a single column that we use in the chart
`"Origin"`, so this is both our only option and what we want since both
the barchart and scatterplot contain this column as an encoding in the
chart.

To successfully link this selection we need to do three things:

1.  Create a new selection that specifies which columns should be used
    for selections (the `fields` parameter).
2.  Add this new selection to the bar plot
3.  Add an encoding to the scatterplot that depends on the new `click`
    selections. Here we use `opacity`.

Now that we click the bars the opacity of the corresponding points
changes as we would expect!

Note that we can still click and drag in the scatterplot since our
`brush` selection is unchanged from previously.

---

## A selection can be bound to the legend instead of a particular chart

``` python
click_legend = alt.selection_multi(fields=['Origin'], bind='legend')
points = points.encode(opacity=alt.condition(click_legend, alt.value(0.9), alt.value(0.2)))

points.add_selection(click_legend)
```

<iframe src="/module7/charts/02/unnamed-chunk-4.html" width="100%" height="420px" style="border:none;">
</iframe>

Notes: We don’t always have a barchart to drive the selections from.
What if we only created a scatterplot, but still wanted to be able to
select data from different Origins?

Instead of using a separate chart, we could use the legend to make the
selections. We can specify to Altair that we want to make the legend
interactive, by binding `selection_multi` to it.

We then need to link this new selection (called `click_legend` to
distinguish it from the previous slide) to the points opacity encoding
and add it to the plot.

Now if you click the legend, it will select the corresponding
observations in the scatterplot!

---

## Legend selections can be added to multiple charts

``` python
bars = bars.encode(opacity=alt.condition(click_legend, alt.value(0.9), alt.value(0.2)))
(points & bars).add_selection(click_legend) 
```

<iframe src="/module7/charts/02/unnamed-chunk-5.html" width="100%" height="420px" style="border:none;">
</iframe>

Notes: When creating a combined charts the syntax for adding the legend
interactivity is similar, but we need to add the selection to both
charts since the legend belongs to both of them.

We could do this one by one, or both at once as we do in this slide.

---

## Instead of highlighting, a selection can be used for filtering data

``` python
bars = bars.transform_filter(brush)
(points & bars).add_selection(click_legend) 
```

<iframe src="/module7/charts/02/unnamed-chunk-6.html" width="100%" height="420px" style="border:none;">
</iframe>

Notes: So far we have seen how to change graphical encodings such as
color and opacity to highlight points in the data. Another useful type
of interactivity is to actually filter the data based on a selection,
rather than just styling the chart appearance.

For example, we might wonder how many cars from different regions that
we have selected when we drag in the scatter plot. Let’s change the bar
chart to update dynamically as we select points in the scatterplot.

We can do this by adding a transform filter to our bar plot. Transform
filters can filter data similarly to what we might do in pandas, but are
not as powerful in general so they are best used for operations like
interactive filtering which are not possible in pandas. This type of
interaction is sometimes called a dynamic query.

We’re keeping the legend here since we have conditions in the charts’
encodings that depend on the `legend_click` selection variable, but we
could remove it if we change these.

Now that we have select points by dragging in the scatter plot we can
see that the barchart updates the count to reflect the number of points
we have selected of each color, neat!

---

## Fixing the extent of the x-axis makes the bars easier to compare

``` python
bar_chart_max = cars.groupby('Origin').size().max()
bars = bars.encode(alt.X('count()', scale=alt.Scale(domain=[0, bar_chart_max])))
(points & bars).add_selection(click_legend) 
```

<iframe src="/module7/charts/02/unnamed-chunk-7.html" width="100%" height="420px" style="border:none;">
</iframe>

Notes: It is a bit non-intuitive that the x-axis keep changing its
extent as we select different number of points, and it makes the bar
heights harder to compare as we move the selection around. Ideally only
the bars would change length, but the axis would stay the same.

In this slide we calculate the max number of cars from any region and
then use this number to fix the extent of the x-axis. Now that we select
in the scatterplot, only the lengths of the bars changes, but the range
of the axis remains the same.

---

## Interactive features work with all charts

``` python
import pandas as pd
state_map = alt.topo_feature(data.us_10m.url, 'states')
state_pop = pd.read_csv('data/us_population_coordinates_asthma-cases.csv')
state_pop['asthma_cases_per_capita'] = state_pop['number_of_asthma_cases'] / state_pop['population']

map_hover = alt.selection_single(fields=['state'], on='mouseover')
choropleth = (alt.Chart(state_map).mark_geoshape().transform_lookup(
    lookup='id',
    from_=alt.LookupData(state_pop, 'id', ['number_of_asthma_cases', 'state']))
.encode(
    color=alt.Color('number_of_asthma_cases:Q', title='Asthma cases'),
    opacity=alt.condition(map_hover, alt.value(1), alt.value(0.2)),
    tooltip=['state:N', alt.Tooltip('number_of_asthma_cases:Q', title='Asthma cases')])
.add_selection(map_hover)
.project(type='albersUsa')
.properties(height=150, width=300))
choropleth
```

<iframe src="/module7/charts/02/unnamed-chunk-8.html" width="100%" height="420px" style="border:none;">
</iframe>

Notes: Selections work with all types of charts in Altair. In this slide
we have recreated one of the maps we made in module 6, showing the
number of asthma cases per state as a choropleth.

We have added a helpful tooltip that shows which state we are hovering
over as well as the exact number of asthma cases in that state, which
would be hard to read out from the color alone.

We used `alt.Tooltip` to change the title in the tooltip, just as when
we change the title of an axis or legend.

We also added a `selction_single` interaction, but instead of binding it
to mouse clicks (the default), we bound it to `'mouseover'`, which is
when we are hovering over a state with the mouse pointer.

In this slide we can use this interaction to highlight a particular
state in the choropleth and in the next slide we will see how we can
also link it to another chart.

We set the dimensions of the plot to fit on the slide.

---

## Linking a map selection to another chart

``` python
points = (alt.Chart(state_pop).mark_circle(size=70).encode(
    alt.X('asthma_cases_per_capita', title='Asthma cases / capita', scale=alt.Scale(zero=False)),
    alt.Y('number_of_asthma_cases', title='Asthma cases'),
    stroke=alt.condition(map_hover, alt.value('black'), alt.value('#ffffff')),
    color='number_of_asthma_cases')).properties(height=150, width=300)
choropleth & points
```

<iframe src="/module7/charts/02/unnamed-chunk-9.html" width="100%" height="420px" style="border:none;">
</iframe>

Notes: To link an interaction on a map to another chart, we use the same
logic as we did in previous slides for linking the barchart and
scatterplot.

Here we create a separate scatterplot where the stroke color of each
points depends on whether we have selected that state on the map or not.

By default all states on the map are selected so all the points have a
black outline. As we hover over a state in the map, the outline changes
to white for the points whose states are not selected in the map.

In addition to adding one more visualization for the asthma cases, using
the map to identify states can be more helpful than just adding a
tooltip to the scatterplot since we might already have an intuition for
where different states are located on the map and don’t have to go
through each of the point’s tooltip looking for the state name of
interest.

TODO we could change this to be another variable in the map like
population, I don’t have a strong opinion, both have advantages.

---

# Let’s apply what we learned!

Notes: <br>
