---
type: slides
---

# Figure composition

Notes: In this module we will see how we layout plots together instead
of showing only one at a time.

---

## Loading in the data

Notes: On this slide we are recreating the choropleth and pointplot map
from the end of the last slide deck. We are saving these as variables so
that we can use them to practice laying out plots on the following
slides.

TODO fix so that this code shows up correctly on the slide

---

## Placing plots next to each other allows us to make more direct comparisons

``` python
choropleth | points_on_map
```

Notes: To place plot side by side, vi can use the pipe (`|`) operator.
You have already seen us using this occasionally in previous modules.

We could also have used the `alt.hconcat(choropleth, points_on_map)`,
but it takes less typing to use the operator.

We can see that the legends are stacked to the right of both plots.

---

## Plots can also be concatenated vertically

``` python
choropleth & points_on_map
```

Notes: To place plots next to each other vertically, we can use the
ampersand (`&`) operator.

We could also have used the `alt.vconcat(choropleth, points_on_map)`,
but it takes less typing to use the operator.

---

## Vertical and horizontal concatenation can be combined

``` python
bars = alt.Chart(state_pop).mark_bar().encode(
    y='population',
    x=alt.Y('state', sort='y', title=None),
    color='population').properties(height=100, width=625)

points_on_map | choropleth & bars
```

<iframe src="/module6/charts/03/unnamed-chunk-4.html" width="100%" height="420px" style="border:none;">
</iframe>

Notes: Often we want to create more complex figure layouts where plots
are concatenated both horizontally and vertically. This allow to present
relevant information next to each other and can be useful if there is a
key comparison we want to make between multiple slots on a single slide
instead of flipping between slides which can be harder to follow.

In Altair, we can create the figure layout by combining the vertical and
the horizontal concatenation operators.

In this slide, we create a barplot of the population in each state that
we want to place under the two maps. But as we can see in this slide,
this places the barplot under only the rightmost map. Why is that?

---

## Parentheses can be used to indicate groupings in complex layouts

``` python
bars = alt.Chart(state_pop).mark_bar().encode(
    y='population',
    x=alt.Y('state', sort='y', title=None),
    color='population').properties(height=100, width=625)

(points_on_map | choropleth) & bars
```

<iframe src="/module6/charts/03/unnamed-chunk-5.html" width="100%" height="420px" style="border:none;">
</iframe>

Notes: The reason the plot in the previous slide did not looks as we
desired is that the `&` operator has higher priority than `|`, so the
choropleth and barplot are first vertically concatenated before being
horizontally concatenated to the point map.

We want the horizontal concatenation between the maps to occur first and
just like with mathematical expression, we can use parenthesis to
indicate which operations should have priority.

You can see an example of that in this slide, where we get the barplot
to show up below both the maps as desired.

---

## Titles can be added to each level of the layout

``` python
centered_map_title = alt.TitleParams(text='Map comparison', anchor='middle')
((points_on_map | choropleth) .properties(title=centered_map_title) & bars).properties(title='US population by state')
```

Notes: To make our visualization easier to interpret, we can add
descriptive titles. These are often particularly important when we
create more complex figures since there are now several panels within
each figure to keep track of.

This doesn’t mean that each panel absolutely needs a title, but when in
doubt it is better to add one title too many than one too few.

---

# Let’s apply what we learned!

Notes: <br>
