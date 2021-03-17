---
type: slides
---

# Effective use of colour for categorical data

Notes: In this slide deck you will learn how to select colors that
accurately represents your data and effectively communicate it to the
reader.

---

## Colour choices can have profound impact on the interpretation of the results

![](/module5/color-importance-vessels.png)

Notes: In module 2 we discussed how changing the colorscheme drastically
improved a clinical outcome by almost doubling physician’s detection
rate of blodd vessles regions indicative of potential future heart
disease (from 40% to 70%).

In this slide deck we will discuss some of the consideration that goes
into evaluating if a colorscheme (also called a colormap) is suitable
for the data you are visualizing.

---

## Colour can be broken down into hue, lightness, and saturation

<center>
<img src="/module5/hsl-cylinder.png" width="90%"></img>
</center>

Notes: There are several different ways to represent colors. You might
arleady have heard of RGB (red, green, blue) or CMYK (cyan, magenta,
yellow, black) where different amount of a set of base colors are
combined to create all possible colors.

When discussing colors in the context of data visualization, We will be
describing them with the parameters “hue”, “saturation” and “lightness”.

The left schematic in this slide is a 2D circular representation
including only hue and saturation. When we add lightness this circle
grows into cylinder with lightness as the height.

On the next slide we will break down exactly what each of these three
parameters represent.

---

## Hue, lightness, and saturation describes different properties of colours

<center>
<img src="/module5/hsl-questions.png" width="60%"></img>
</center>

Notes: We could verbalize the changes we saw in the previous slide in
the following manner:

Hue is what we traditionally think of as the “color”, is it red, blue,
etc?

Each hue can have a varying saturation, which ranges from a dull,
greyish appearance to a vibrant fully saturated hue.

Lightness is how bright the color is. For every hue, it starts at black
(no lightness) and ends at white (full lightness).

Hue and lightness are the most important from a data visualization
perspective, and we use them for categorical and quantitative data,
respectively.

Saturation is often used more as a stylistic choice to decide whether
the colors we use should be muted/desaturated or vivid/saturated.

---

## Hues are used to distinguish categorical values

<iframe src="/module5/charts/categorical-hues.html" width="100%" height="420px" style="border:none;">
</iframe>

Notes: Hue is useful to distinguish between categories, because it is
often relatively easy for us to to say that different hues are distinct.
We can see that blue, orange, red, etc are different and don’t easily
mix them up.

The leftmost plot uses different hues to separate the points belonging
to different categories. We can quickly identify that there is a total
of three distinct colors being used here even without looking at the
legend.

In the plot to the right we used lightness within a single hue (blue) to
label the different categories. Here it is much harder to say how many
different categories there are, and even when we have the legend, it is
difficult to tell which points are which shade of blue.

---

## It is often better to use established colour schemes instead of making your own

<center>
<img src=/module5/color-schemes.png></img>
</center>

Notes: There are many different hues we could use to represent our
colors and some might not go as well together as others, so how do we
decide which ones to use?

Fortunately, we don’t have to design our own combination of colors to
use, but can pick from combinations designed by experts to be easy to
tell apart and in most cases also suitable for people with color vision
deficiencies.

These color combinations are referred to as color schemes in Altair, but
you might also hear them being called colormaps or color palettes.

In this slide, you can see some of the color schemes for categorical
values that are built into Altair.

The default one is “tableau10” and it was named this way because it was
originally designed by the company Tableau, but is now one of the most
common categorical color schemes used in data visualization. [All Altair
color schemes can be viewed
here](https://vega.github.io/vega/docs/schemes/).

---

## Specifying colour schemes in Altair

``` python
alt.Chart(cars).mark_point(size=70, filled=True).encode(
    alt.X('Horsepower', title='Engine power (hp)'),
    alt.Y('Miles_per_Gallon', title='Fuel efficiency (miles/gallon)'),
    color=alt.Color('Origin', title=None, scale=alt.Scale(scheme='set1')))
```

<iframe src="/module5/charts/12/unnamed-chunk-2.html" width="100%" height="420px" style="border:none;">
</iframe>

Notes: You can change the color scheme of a plot by specifying its name
as a string to the `scheme` parameter inside `alt.Scale`.

To more easily see the changes we are making to the colors, we also
increase the size of all points via the `size` parameter of the mark.

---

## Redundant coding can make charts easier to interpret

``` python
alt.Chart(cars).mark_point(size=70, filled=True).encode(
    alt.X('Horsepower', title='Engine power (hp)'),
    alt.Y('Miles_per_Gallon', title='Fuel efficiency (miles/gallon)'),
    color=alt.Color('Origin', title=None, scale=alt.Scale(scheme='set1')),
    shape='Origin')
```

<iframe src="/module5/charts/12/unnamed-chunk-3.html" width="100%" height="420px" style="border:none;">
</iframe>

Notes: Although many of the color schemes in Altair are designed
according to the guidelines for effective color uses, they can sometimes
be difficult to interpret for people with color vision deficiencies.

Especially color schemes that mix red and green as the one in the
previous slide.

In addition to using a more suitable color scheme (such as the default),
we could also change the shape of the points for each category.

Although this is technically redundant since the color is already used
for the categorical groups, it can make your visualization more
effective since it makes the points more distinct from each other.

Note that `shape=` is only available to use with `mark_point`, not
`mark_circle`, `mark_square`, etc.

For line plots we could achieve a similar effect by using the
`strokeDash` encoding instead of `shape`, which together with direct
labeling from the previous slide deck can facilitate interpretation of
these plots.

---

## Specifying custom colours

``` python
colors = ['coral', '#4682b4', 'rebeccapurple']
alt.Chart(cars).mark_point(size=70, filled=True).encode(
    alt.X('Horsepower', title='Engine power (hp)'),
    alt.Y('Miles_per_Gallon', title='Fuel efficiency (miles/gallon)'),
    color=alt.Color('Origin', title=None, scale=alt.Scale(range=colors)),
    shape='Origin')
```

<iframe src="/module5/charts/12/unnamed-chunk-4.html" width="100%" height="420px" style="border:none;">
</iframe>
<!-- #region -->

Notes: Most of the time it is a good idea to stick to the predefined
color scheme because of the advantages mentioned in the previous slide.

However, sometimes the categories we are representing might have a color
already associated with them, such as political parties or sports team.

In these cases, it is often better to design a custom color scheme using
the colors naturally associated with each category.

In Altair we can create a custom color scheme by passing a list of
colors to the `range` parameter of `alt.Scale`.

You can specify colors either by their HTML/CSS name (such as ‘coral’)
or their hex code (such as ‘\#4682b4’). [All HTML/CSS color names can be
found in the image in this
post](https://stackoverflow.com/a/37232760/2166823).

Hex codes are defines over the range `#000000` for black (“zero color”)
to `#ffffff` for white (“full color”) and [are easiest chosen via color
pickers such as this one](https://colorpicker.me/).

---

## Don’t use more than 5-8 distinct hues for categories

<center>
<img src=/module5/hue-guidelines.png></img>
</center>

Notes: Although many of the categorical color schemes contain ten or
more hues, if is often not a good idea to use all that many because it
becomes near impossibe to distinguish the different hues from each
other.

The guidelines on what is too many hues differ between different sources
and also depends on your use case. A good rule of thumb is that when you
get to around five different hues, you should really consider if this is
the best way to represent your data or if you could split it up into
multiple visualizations instead.

If the data is neatly organized in well-separated clusters, it is
possible that you could visualize more than five colors (maybe even ten)
effectively, but in data where the datapoints are more mixed, you will
rarely, if ever, be able to go this high.

---

## Too many hues are impossible to distinguish

<!-- #endregion -->

``` python
alt.Chart(cars).mark_point(size=70, filled=True).encode(
    alt.X('Horsepower', title='Engine power (hp)'),
    alt.Y('Miles_per_Gallon', title='Fuel efficiency (miles/gallon)'),
    color=alt.Color('Name', title=None))
```

<iframe src="/module5/charts/12/unnamed-chunk-5.html" width="100%" height="420px" style="border:none;">
</iframe>

Notes: This is an example of what happens when too many categorical hues
are used. In this plot, we can not separate the colors even if we spent
a considerable amount of effort studying the chart.

As we saw on the last slide, categorical color schemes have a limited
amount of hues so in addition of it being hard to differentiate this
many hues in general, it become practically impossible in cases where
there are more categories than coor hues, since the color scheme starts
repeating as in the chart.

A better approach here would have been to label specific points of
interest directly and keeping the rest as either a single color or using
a categorical variable with fewer values, e.g. by grouping the cars into
brands rather than their full model name.

Since Altair allows for interactive elements, we could also have used
the tooltip here as we saw in a previous module.

---

## Redundant coding of bar charts can be disorienting

``` python
cars['Brand'] = cars['Name'].str.split().str[0]  # Extract brand from the name column
chart = alt.Chart(cars).mark_bar().encode(
    alt.Y('Brand', title=None, sort='x'),
    alt.X('mean(Horsepower)')).properties(width=200, height=350)
chart | chart.encode(alt.Color('Brand', legend=None, scale=alt.Scale(scheme='tableau20')))
```

<iframe src="/module5/charts/12/unnamed-chunk-6.html" width="100%" height="420px" style="border:none;">
</iframe>

Notes: A few slides ago we saw how encoding the same variable as both
shape and color could make our figures more effective although it is
technically redundant.

Similarly, you might come across bar charts where the author of the
visualization has added a distinct color for each bar.

This can work when there are relatively few bars, but it usually does
not add anything and can become directly disorienting when there are
many bars as in this slide.

It is usually preferable to color all the bars in the same color (or
after another categorical variable, such as “Origin” in this data), and
let the axis labels alone identify which category the bar belongs too.

One exception to this is if each axis label is broken down into
subcategories where each location has multiple bars based on another
categorical variable, then color can help.

You can also see that the car brands are not systematically named and we
would need to clean this data to unify e.g. ‘vw’, ‘vokswagen’, and
‘volkswagen’. The reason we’re setting the height is just to fit the
plot on the slide.

---

## Use consistent colouring between subplots even when it is redundant

``` python
chart = alt.Chart(cars).mark_bar().encode(
    alt.X('Origin', title=None),
    alt.Y('mean(Horsepower)'),
    alt.Color('Origin', title=None))
(chart | chart.mark_line().encode(alt.X('Year', title=None), alt.StrokeDash('Origin', title=None)))
```

<iframe src="/module5/charts/12/unnamed-chunk-7.html" width="100%" height="420px" style="border:none;">
</iframe>

Notes:

When creating a figure that contains several subplots, it is important
to be consistent in the coloring between these even if the coloring is
redundant in one of the subplots.

Here we have colored the bars to match the lines although we could tell
the categories only from reading the axis labels.

It is important to not use different colors for the same categories
between subplots. For example, if we made an additional subplot which
only contained Japan and USA, then we should make sure that these are
still colored in orange and red. Since the default Altair color scheme
will always start with blue, we would need to manually specify the
colors in this case.

---

# Let’s apply what we learned!

Notes: <br>
