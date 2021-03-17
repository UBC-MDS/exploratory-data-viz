---
type: slides
---

# Descriptive titles and labels

Notes: In this slide deck we will see how we can change different
aesthetic elements of the plot to cater to communication in various
settings.

---

## Charts without titles are hard to interpret

<iframe src="/module5/charts/chart-without-titles.html" width="100%" height="420px" style="border:none;">
</iframe>

Notes: Why do we need to add chart titles and labels to our plots?

Let’s find out by looking at an example. To the left you can see a
poorly labeled chart. There y-axis label is not very descriptive, there
is no overall chart title and we have even forgotten to include the
legend.

It is impossible to tell what this figure is showing!

---

## Descriptive titles make charts more effective

<iframe src="/module5/charts/chart-with-titles.html" width="100%" height="420px" style="border:none;">
</iframe>

Notes: In this slide we have a chart with a descriptive title that
convey the main take home message of our visualization. The y-axis is
also clearly titled while its unit (`$`) is embedded in the axis label.

This figure makes it immediately clear why we have made this
visualization and what question we are trying to answer.

This is a major goal when making visualizations: there should be no
supplementary text needed to explain why we made the figure and what its
main takeaways are.

Properly used chart and axis titles are a big help for to reach this
goal.

In this slide deck we will gradually build up to creating a figure like
the one you can see in this slide.

---

## Chart titles should convey the main take home message

``` python
import altair as alt
from vega_datasets import data

stocks = data.stocks()
stock_title = "Google's stock experiencing heavier fluctuations than competitors"
alt.Chart(stocks, title=stock_title).mark_line().encode(
    alt.X('date'),
    alt.Y('price'),
    color='symbol').properties(height=275)
```

<iframe src="/module5/charts/04/unnamed-chunk-4.html" width="100%" height="420px" style="border:none;">
</iframe>

Notes: The title of the chart should clearly convey the take home
message of the figure to the reader. It should answer the question you
posed before making the visualization.

It you made a more general visualization or answered multiple questions,
it is ok with a more general title. Note however such general
visualizations are rarer in communication compared to exploration.

We could have had a title targeted to a specific time period, such as
“Google’s stock outperforms competitors in 2009”, but then we might want
to narrow down the date region at least a bit.

A less effective title here would be something like “Stock prices over
time”, which is too general and not very informative.

---

## Subtitles can provide additional detail

``` python
stock_title = alt.TitleParams(
    "Google's stock experiencing heavier fluctuations than competitors",
     subtitle = "Prices have been surging since 2009, but have still not reached an all-time high")
alt.Chart(stocks, title=stock_title).mark_line().encode(
    alt.X('date'),
    alt.Y('price'),
    color='symbol')
```

<iframe src="/module5/charts/04/unnamed-chunk-5.html" width="100%" height="420px" style="border:none;">
</iframe>

Notes: If you want to add additional details you can create a subtitle.
Here we use `TitleParams` to create the main title text and the subtitle
which we then pass to the `title` parameter in `Chart`.

---

## Titles can be aligned according the the presentation context

``` python
stock_title_left = alt.TitleParams(
    "Google's stock experiencing heavier fluctuations than competitors",
     subtitle = "Prices have been surging since 2009, but have still not reached an all-time high",
     anchor='start')
alt.Chart(stocks, title=stock_title_left).mark_line().encode(
    alt.X('date'),
    alt.Y('price'),
    color='symbol')
```

<iframe src="/module5/charts/04/unnamed-chunk-6.html" width="100%" height="420px" style="border:none;">
</iframe>

Notes: Depending on the context in which we are presenting the figure,
it can look more appealing to left align the title.

This is done via the `anchor` parameter in Altair.

---

## Breaking titles into multiple line can improve readability

``` python
stock_title_linebreak = alt.TitleParams(
    "Google's stock experiencing heavier fluctuations than competitors",
     subtitle = ["Prices have been surging since 2009 but have still", "not reached the same levels as in late 2007."])
alt.Chart(stocks, title=stock_title_linebreak).mark_line().encode(
    alt.X('date'),
    alt.Y('price'),
    color='symbol')
```

<iframe src="/module5/charts/04/unnamed-chunk-7.html" width="100%" height="420px" style="border:none;">
</iframe>

Notes: If we have a really long title, we can improve readability by
breaking it into multiple lines. Altair converts lists of strings into
multiline titles.

When creating a multiline title, is is advisable to try to keep all
lines about the same length. Generally it also looks better if the lines
are ordered by length, for example from the longest to the shortest as
in this slide.

For this chart, the single line subtitle still looks more appealing due
to all the whitespace on the sides of the subtitle in this slide, so we
will go back to a single line subtitle in the next slide.

---

## Axis titles should be capitalized regular words rather than dataframe column names

``` python
alt.Chart(stocks, title=stock_title).mark_line().encode(
    alt.X('date', title='Date'),
    alt.Y('price', title='Price (USD)'),
    color='symbol')
```

<iframe src="/module5/charts/04/unnamed-chunk-8.html" width="100%" height="420px" style="border:none;">
</iframe>

Notes: During EDA, axis titles etc don’t matter that much, since you are
the primary person interpreting them and it is often clear to you what
titles mean as long as you have given your dataframe reasonable column
names.

In communication however, your plots need to be interpreted by other
people, often on their own without your explanation. Setting descriptive
titles adds significantly to this interpretability.

Axis titles should be regular words that are descriptive, capitalized,
and contain spaces instead of underscores. Cryptic lower case column
names with underscores are not at all effective for communication
figures and look unprofessional.

Any relevant units of measurement can be included in parenthesis to
clarify further for the reader or as part of the axis label as we will
see later.

To set the title for the axes, we use the `title` parameter in the axis,
similar to how we used it in the Chart for the figure title.

---

## Legend and axis titles are often redundant for categorical and temporal variable

``` python
# Assigning to a variable for use in the next slide
lines = alt.Chart(stocks, title=stock_title).mark_line().encode(
    alt.X('date', title=None),
    alt.Y('price', title='Price (USD)'),
    alt.Color('symbol', title=None))
lines
```

<iframe src="/module5/charts/04/unnamed-chunk-9.html" width="100%" height="420px" style="border:none;">
</iframe>

Notes: For axis titles that encode a temporal variable we rarely need a
title as it is clear that the x-axis represents time. Here we remove the
title text by setting the parameter to `None`.

Similarly, axis and legend titles that denote a categorical variable are
often redundant and it is clear what the categories are.

Thanks to Altair’s consistent grammar, we change the title of the legend
in the same way that we change the axis titles.

---

## Direct labeling is often preferred over legend when applicable

``` python
stock_max_date = stocks[stocks['date'] == stocks['date'].max()]
texts = alt.Chart(stock_max_date).mark_text(align='left', dx=2).encode(
    x='date',
    y='price',
    text='symbol',
    color=alt.Color('symbol', legend=None))

lines + texts
```

<iframe src="/module5/charts/04/unnamed-chunk-10.html" width="100%" height="420px" style="border:none;">
</iframe>

Notes: In this graph, we could label the lines directly instead of
relying on the legend text and additional colored lines marks.

This has the advantage that we don’t have to go back and forth between
the legend and the plot, and avoids issues from matching up the colors
incorrectly.

We use `align` to attach the left part of the label to the data point at
the end of the line, and then `dx` (delta x) to add a little whitespace
between the label and the end of the line.

To show both the lines and text labels, we layer the chart `lines` that
we created in the last slide with the chart `texts` that we create here.

---

## To solve overlapping text labels we have to manually specify their position

``` python
stock_max_date.loc[stock_max_date['symbol'] == "IBM", 'price'] = 140
stock_max_date.loc[stock_max_date['symbol'] == "AMZN", 'price'] = 110
texts = alt.Chart(stock_max_date).mark_text(align='left', dx=2).encode(
    x='date',
    y='price',
    text='symbol',
    color=alt.Color('symbol', legend=None))
lines + texts
```

<iframe src="/module5/charts/04/unnamed-chunk-11.html" width="100%" height="420px" style="border:none;">
</iframe>

Notes: There is no way to automatically separate the labels in Altair,
so we have to manually specify new y-axis values for the text of the
overlapping labels.

Here we modify the dataframme we created in the last slide by setting
the value for the IBM text label to 140 and the value for the AMZN text
label to 110 so that they are no longer overlapping.

---

## Units can be incorporated directly in the axis labels instead of the axis title

``` python
lines = alt.Chart(stocks, title=stock_title).mark_line().encode(
    alt.X('date', title=None),
    alt.Y('price', title='Price', axis=alt.Axis(format='$')),
    color=alt.Color('symbol', legend=None))

lines + texts
```

<iframe src="/module5/charts/04/unnamed-chunk-12.html" width="100%" height="420px" style="border:none;">
</iframe>

Notes: Instead of writing measurement units in parenthesis in the axis
title, they can be incorporated directly in each axis label by setting
the axis format.

You can see that the dollar sign was prefixed each numerical label on
the y-axis, but because we overwrote the default formatting of the axis,
it changed the labels to scientific notation instead of standard
international units.

---

## Axis formatting labels can be combined

``` python
lines = alt.Chart(stocks, title=stock_title).mark_line().encode(
    alt.X('date', title=None),
    alt.Y('price', title='Closing price', axis=alt.Axis(format='$s')),
    color=alt.Color('symbol', legend=None))

lines + texts
```

<iframe src="/module5/charts/04/unnamed-chunk-13.html" width="100%" height="420px" style="border:none;">
</iframe>

[All Altair’s label format strings can be found
here](https://github.com/d3/d3-format#locale_format).

Notes: To revert back to displaying the full number instead of using
scentific formatting, we can combine the dollar sign with the format
string `s`, which stands for SI-units.

Now that we have the units in the label, the title “Price” appear a bit
redundant and we can either remove it or (preferably) improve it.

Here we add more detail to indicate that this is the closing price of
each stock.

In addition to being used in the x and y axis, axis formatting can be
applied to any aspect of Altair that uses `alt.Axis`, including legends
for colors and sizes.

Other useful format strings include `%` for including a percentage sign,
`e` to force scientific format, `d` to force integer format, `~` which
removes trailing zeros (e.g. 1.0 becomes 1), and `,` which adds a comma
as the thousands separator. [All label format strings can be found
here](https://github.com/d3/d3-format#locale_format).

---

## The number of axis ticks can be reduced to make the plot less noisy

``` python
lines = alt.Chart(stocks, title=stock_title).mark_line().encode(
    alt.X('date', title=None, axis=alt.Axis(tickCount=3)),
    alt.Y('price', title='Closing price', axis=alt.Axis(format='$s')),
    color=alt.Color('symbol', legend=None))

lines + texts
```

<iframe src="/module5/charts/04/unnamed-chunk-14.html" width="100%" height="420px" style="border:none;">
</iframe>

Notes: Altair usually picks a suitable number of axis ticks, but
sometimes we might want to tweak this in order to achieve a specific
effect, such as a more clean looking plot.

Here we reduce the number of ticks along the x-axis to only show three
of the years, by setting `tickCount=3` in `alt.Axis()`.

Note that Altair will round the number of ticks to a number that works
well with your data, so you might not always get the exact number you
ask for (e.g. it wouldn’t make much sense to have 4 ticks here since
that would mean year “2002.5” and “2007.5”).

---

## Gridlines can be removed when they are not helpful

``` python
lines = alt.Chart(stocks, title=stock_title).mark_line().encode(
    alt.X('date', title=None, axis=alt.Axis(tickCount=3, grid=False)),
    alt.Y('price', title='Closing price', axis=alt.Axis(format='$s')),
    color=alt.Color('symbol', legend=None))

(lines + texts).configure_view(strokeWidth=0)
```

<iframe src="/module5/charts/04/unnamed-chunk-15.html" width="100%" height="420px" style="border:none;">
</iframe>

Notes: Gridlines are usually helpful for guiding the eye and making
exact comparisons and as long as they are faint they don’t distract from
the visual overall.

There are still situations where we might want to remove them.

In our plot on the last slide, we might not like the appearance of the
single gridline in the middle and the one really close to the right
axis, so we can turn off the vertical gridlines by passing `grid=False`
to the `axis` parameter of `alt.X`.

To remove the gray box outlining the entire figure, we can set the
`strokeWidth` of the layered chart.

---

## Font sizes can be adjusted for different communication purposes

``` python
stock_title = alt.TitleParams(
    "Google's stock experiencing heavier fluctuations than competitors",
     subtitle = "Prices have been surging since 2009 but have still not reached the same levels as in late 2007.",
     fontSize=18, subtitleColor='steelblue', subtitleFontWeight='bold')
lines = alt.Chart(stocks, title=stock_title).mark_line().encode(
    alt.X('date', title=None, axis=alt.Axis(tickCount=3, grid=False)),
    alt.Y('price', title='Closing price', axis=alt.Axis(format='$s', labelFontSize=12, titleFontSize=16)),
    color=alt.Color('symbol', legend=None)).properties(height=275)
(lines + texts).configure_view(strokeWidth=0)
```

<iframe src="/module5/charts/04/unnamed-chunk-16.html" width="100%" height="420px" style="border:none;">
</iframe>

Notes: If you are making a figure for the web, the default font sizes in
Altair are generally a good choice. They are maybe a little bit on the
smaller side of the ideal range, but it is possible to zoom in if really
needed.

If you are making a figure for print, it is recommended to increase the
font sizes to make sure that your figure is readable for the context you
are presenting it in.

It is advisable to err on the side of larger rather than smaller, for
those members of the audience that have a hard time discerning small
text.

In this figure, you can see several examples of how to set fontsizes for
titles and labels, as well as how to change the font color and weight.

This figure does not necessarily look good as a whole, but serves to
demonstrate how to set multiple of these properties at once.

To learn more about good guidelines for titles and labels, you can read
[section 22 - 22.2 in the book Fundamentals of Data
Visualization](https://clauswilke.com/dataviz/figure-titles-captions.html).

---

# Let’s apply what we learned!

Notes: <br>
