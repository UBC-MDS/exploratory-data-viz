---
type: slides
---

# Figure Composition

Notes: In this module we will see how we layout plots together in a
panel, instead of showing only one at a time.

---

## Recreating the chart from last slide deck

``` python
import altair as alt
import pandas as pd
from vega_datasets import data

state_map = alt.topo_feature(data.us_10m.url, 'states')
state_pop = pd.read_csv('data/us_population_coordinates_asthma-cases.csv')
state_pop['asthma_cases_per_capita'] = state_pop['number_of_asthma_cases'] / state_pop['population']
choropleth = (alt.Chart(state_map).mark_geoshape().transform_lookup(
    lookup='id',
    from_=alt.LookupData(state_pop, 'id', ['asthma_cases_per_capita']))
.encode(color=alt.Color('asthma_cases_per_capita:Q', title='Asthma cases per capita'))
.project(type='albersUsa')
.properties(width=500, height=150))
choropleth
```

<iframe src="/module6/charts/03/unnamed-chunk-1.html" width="100%" height="420px" style="border:none;">
</iframe>

Notes: On this slide we are recreating the choropleth pointplot map from
the end of the last slide deck. We are saving it as an object so that we
can use it to practice laying out plots together in a panel on the
following slides.

We set the width of this map because we will be combining it with other
figures later and we want them all to be of the same width for the
figure panel to look aesthetically pleasing.

---

# A barchart is able to represent relative differences more precisely

``` python
bars = (alt.Chart(state_pop).mark_bar().encode(
    alt.X('state', sort='-y', title=''),
    alt.Y('asthma_cases_per_capita', title='Asthma cases per capita'))
    .properties(width=500, height=80))
bars
```

<iframe src="/module6/charts/03/unnamed-chunk-2.html" width="100%" height="420px" style="border:none;">
</iframe>

Notes: At the end of the last slide deck we mentioned that it would good
to couple our map with a bar char since this would make it easier to
compare the relative differences between the states more precisely.

Here we create that bar chart and as you can see, we can now tell apart
small differences between the states and we are able to clearly see the
values also for states with small areas, such as Rhode Island which is
barely visible on the map.

While having the labels on the x-axis makes them harder to read it will
make our bar plot fit in better with the map in the figure layout, which
is why we have opted for this encoding here.

We’re setting a pretty low height so that this chart will work well in
the multi-panel figures we are creating in later on in this slide deck.

---

## Placing plots next to each other allows us to make direct comparisons

``` python
# alt.vconcat(choropleth, bars)
choropleth & bars
```

<iframe src="/module6/charts/03/unnamed-chunk-3.html" width="100%" height="420px" style="border:none;">
</iframe>

Notes: To place these two plots in a vertical layout we can use the
ampersand (`&`) operator. You may have already seen us using this
operator occasionally in previous modules.

We could also accomplish the same thing by using the
`alt.vconcat(choropleth, points_on_map)` syntax. Here, we chose however
to opt for the pipe operator as it is more efficient (keystroke-wise).

Now we can study both figures in the same view, instead of flipping back
and fourth between slides.

These figures also complement each other in the sense that the
choropleth highlights small differences due to the colorscale not
starting at zero and the bar chart shows the actual size of the
differences since each bar starts from zero.

---

## Plots can also be concatenated horizontally

``` python
# alt.hconcat(choropleth, bars)
choropleth.properties(width=250) | bars.properties(width=400)
```

<iframe src="/module6/charts/03/unnamed-chunk-4.html" width="100%" height="420px" style="border:none;">
</iframe>

Notes: To place plots in a panel stacked horizontally instead of
vertically, we can use the pipe (`|`) operator.

We could also have used the `alt.hconcat(choropleth, points_on_map)`,
but again, using the operator is a bit more efficient.

We have to shrink the plot widths a bit to fit them on this slide. This
makes it hard to read the bar chart x-labels so a horizontal layout is
not as good as a vertical layout for this particular figure.

In general, whether to choose a horizontal or vertical layout depends on
the available space you have for the figure. For example, in this
lecture material we’re limited by the size of the slides and have to
adjust our figure layouts to work well within this space.

Note where the color legend for the plots get placed when we do this; it
is placed to the right of both plots.

---

## Vertical and horizontal concatenation can be combined

``` python
us_map = (alt.Chart(state_map).mark_geoshape(color='lightgray', stroke='white')
          .project(type='albersUsa'))
points = (alt.Chart(state_pop).mark_circle().encode(
    longitude='longitude',
    latitude='latitude',
    size=alt.Size('number_of_asthma_cases', title='Total asthma case', scale=alt.Scale(range=(2,100))))
    .properties(width=240, height=100))

choropleth_small = choropleth.properties(width=240, height=100)
choropleth_small | us_map + points & bars
```

<iframe src="/module6/charts/03/unnamed-chunk-5.html" width="100%" height="420px" style="border:none;">
</iframe>

Notes: Often we want to create more complex figure layouts where
visualizations are stacked both horizontally and vertically. Such
layouts allow us to present connected, or related information near to
one another, and can be useful if there is a key comparison we want to
make between multiple visualizations.

Yes, we could always place each visualization on its own slide or page
(when sharing figures on paper), however, our working memories are only
so good. We often forget key details about visualizations we just saw
when it is removed and we are presented with a new one.

In Altair, we can create the figure layout by combining the vertical and
the horizontal concatenation operators.

In this slide, we create a pointmap to indicate the total amount of
asthma cases in each state, and adjust the size range of the circles to
avoid them overlapping on the map.

Now we would like to place the barplot under the two maps by using the
`&` operator, but as we can see in this slide, this places the barplot
under only the rightmost map. Why is that?

---

## Parentheses can be used to indicate groupings in complex layouts

``` python
(choropleth_small | (us_map + points)) & bars
```

<iframe src="/module6/charts/03/unnamed-chunk-6.html" width="100%" height="420px" style="border:none;">
</iframe>

Notes: The reason that the plot in the previous slide did not look like
we wanted it to, was that the `&` operator has higher priority than `|`
operator.

The resulted in the choropleth and barplot being vertically concatenated
before the point map was horizontally concatenated.

What we really want is the horizontal concatenation between the maps to
occur first, followed by the vertical concatenation of the barplot.

Just as we use parentheses in mathematics to change the default order of
mathematical operations, we can use parentheses to change the default
order of concatenation operations.

You can see an example of that in this slide, where we place the
parentheses around different parts of the expression to force the
horizontal concatenation between the maps to occur first, and that leads
us to get the barplot to show up below both the maps as desired.

We also add a parenthesis around the two charts that we are layering
together, to make it clear which objects the `+` operator is operating
on.

---

## Redundant colouring can make it clearer which charts represent the same values

``` python
(choropleth_small | (us_map + points)) & bars.encode(color='asthma_cases_per_capita')
```

<iframe src="/module6/charts/03/unnamed-chunk-7.html" width="100%" height="420px" style="border:none;">
</iframe>

Notes: To make it clearer that the bars and the choropleth map both
represent the asthma cases, we could add redundant colouring to the
bars.

Now it is clear that the bars are the same as the choropleth and
separate from the pointmap, whereas they has the same blue colour as the
pointmap in the previous slide which could be confusing.

We still had the y-axis label correctly indicating what the bars
represented in the previous slide so this redundant colouring is not
strictly necessary, but it can help to remove ambiguity from your
figures, particularly as they get more complex.

---

## Titles can be added to each chart in the layout to clarify what they represent

``` python
choropleth_with_title = choropleth_small.properties(title='Asthma cases per capita')
pointmap_with_title = (us_map + points).properties(title='Total ashtma cases')
bars_with_title = (bars.encode(color='asthma_cases_per_capita').properties(title='Asthma cases per capita'))
figure_panel = (choropleth_with_title | pointmap_with_title) & bars_with_title
figure_panel_title = alt.TitleParams(text='Asthma cases among US states', dx=200)
figure_panel.properties(title=figure_panel_title)
```

<iframe src="/module6/charts/03/unnamed-chunk-8.html" width="100%" height="420px" style="border:none;">
</iframe>

Notes: To make our visualization easier to interpret, we can add
descriptive titles. These are often particularly important when we
create more complex figures since there are now several panels within
each figure to keep track of.

If we have already taken steps to reduce the ambiguity of the charts in
our figure (as we did in the previous slides), we might not need a title
for each chart in the figure, but when in doubt it is better to add one
title too many than one too few.

We should at least add an overall title to the figure as we learned in
previous modules. Here we use `dx` to center this figure over the charts
in the figure, rather than having it to the left or centered over the
entire charts + legends.

We here make the overall title more general, but could also have
highlighted a specific take home message, such as that there is no clear
geographical distribution of asthma cases or that the relative
differences between most states is rather small. Which title we chose
would depend on the narrative we are building with the figure.

---

# Let’s apply what we learned!

Notes: <br>
