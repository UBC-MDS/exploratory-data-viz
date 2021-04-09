---
type: slides
---

# Using Widgets to Control Selections

Notes: In this slide deck we will learn how to use widgets such as
dropdowns, radio buttons, and sliders to control filtering events in
Altair.

---

## Reading in the movies dataset

``` python
import altair as alt
import pandas as pd

movies = pd.read_csv('data/movies.csv', parse_dates=['Release_Year'])
movies
```

```out
     Worldwide_Gross Release_Year  IMDB_Rating  Rotten_Tomatoes_Rating   Major_Genre MPAA_Rating
0        148345997.0   1996-01-01          5.8                    55.0        Action           R
1          9929135.0   1985-01-01          8.0                    98.0  Black Comedy           R
2        102825796.0   1996-01-01          5.8                    52.0        Comedy       PG-13
3         60209334.0   1996-01-01          5.2                    13.0        Action       PG-13
4         20278055.0   1996-01-01          6.1                    55.0         Drama           R
..               ...          ...          ...                     ...           ...         ...
973       60780981.0   2001-01-01          6.4                    62.0        Comedy       PG-13
974       98690286.0   2009-01-01          7.8                    89.0        Comedy           R
975       36851125.0   2008-01-01          7.0                    65.0        Comedy           R
976      141475336.0   2005-01-01          5.7                    26.0     Adventure          PG
977      233700000.0   1998-01-01          6.7                    82.0     Adventure       PG-13

[978 rows x 6 columns]
```

Notes: To demonstrate how we can use widgets in Altair we will be using
an abbreviated version of the movies dataset which you can see in this
slide.

---

## Interactive selections can make charts with many categories more effective

``` python
select_genre = alt.selection_single(fields=['Major_Genre'], bind='legend')

points = alt.Chart(movies).mark_circle().encode(
    alt.X('Rotten_Tomatoes_Rating', title='Rotten Tomatoes rating'),
    alt.Y('IMDB_Rating', title='IMDB rating'),
    alt.Color('Major_Genre', title='Major genre'),
    opacity=alt.condition(select_genre, alt.value(0.7), alt.value(0.1))).properties(height=200)
points.add_selection(select_genre)
```

<iframe src="/module7/charts/03/unnamed-chunk-2.html" width="100%" height="420px" style="border:none;">
</iframe>

Notes: We saw in the previous slide deck how we could use the `bind`
parameter of a selection to link it to the legend of the plot and
highlight points by clicking the legend.

Here we create that same type of plot using the movie data set that we
saw previously.

If this chart would have been static, it would not have been very
effective since the many colors makes it hard to distinguish the
different genres.

But since we can click the legend to show the points from only a
specific genre, this problem is alleviated.

---

## Binding selections to dropdowns instead of legends

``` python
genres = sorted(movies['Major_Genre'].unique())
dropdown = alt.binding_select(name='Genre ', options=genres)
select_genre = alt.selection_single(fields=['Major_Genre'], bind=dropdown)

points.add_selection(select_genre).encode(
    opacity=alt.condition(select_genre, alt.value(0.7), alt.value(0.1)))
```

<iframe src="/module7/charts/03/unnamed-chunk-3.html" width="100%" height="420px" style="border:none;">
</iframe>

Notes: Driving our interactions via a dropdown instead of a legend could
be useful if we have too many categories to show in the legend, or if we
wanted to have a different dataframe column in the dropdown and in the
legend.

Here we use the same column as for coloring the points, so that you can
clearly see how the interaction works.

We can create a dropdown selection widget via `alt.binding_select`.
Then, instead of binding `alt.selection_single` to the legend we can
pass the dropdown to the `bind` parameter.

The dropdown requires an array to be passed to the options parameter;
here we sort the genres alphabetically before passing them to the
dropdown.

Since we recreated the `select_genre` variable, we need to also redefine
the opacity encoding and add this new variable to overwrite the old one.

Now you can use the dropdown to select movies of different genres!

Note that the location of the dropdown is fixed and there is no way
change its location.

---

## Setting the default value in a widget

``` python
select_genre = alt.selection_single(
    fields=['Major_Genre'], bind=dropdown, init={'Major_Genre': 'Comedy'})

points.add_selection(select_genre).encode(
    opacity=alt.condition(select_genre, alt.value(0.7), alt.value(0.1)))
```

<iframe src="/module7/charts/03/unnamed-chunk-4.html" width="100%" height="420px" style="border:none;">
</iframe>

Notes: If we don’t specify a default value in a widget, the first value
in the options array show up in the widget, but it is not used for
selection until we interact with the dropdown.

If we wanted to set a specific default value and immediately use it to
highlight the data, we could specify which column and value to use via
the `init` parameter as we have done in this slide.

---

## Adding multiple widgets to the same charts

``` python
mpaa_rating = sorted(movies['MPAA_Rating'].unique())
dropdown_mpaa = alt.binding_radio(name='MPAA Rating ', options=mpaa_rating)
dropdown_genre = alt.binding_select(name='Genre ', options=genres)
select_genre_and_mpaa = alt.selection_single(
    fields=['Major_Genre', 'MPAA_Rating'],
    bind={'Major_Genre': dropdown_genre, 'MPAA_Rating': dropdown_mpaa})

points.add_selection(select_genre_and_mpaa).encode(
    opacity=alt.condition(select_genre_and_mpaa, alt.value(0.7), alt.value(0.1)))
```

<iframe src="/module7/charts/03/unnamed-chunk-5.html" width="100%" height="420px" style="border:none;">
</iframe>

Notes: Sometimes we want to highlight our data based on more than a
single widget. For example, we might want to show only comedies that are
rated as suitable for children to watch.

We have already seen how to perform such breakdowns via faceting, but we
could also do it by combining multiple interactive widgets.

Here we’re adding a set of radio buttons for the maturity rating of the
movies and a dropdown button for the genre selection.

We create the radio buttons and dropdown separately, and then add then
bind them both to the `selection_single` object to their respective
fields.

To trigger a selection, we now need to both click a radio button **and**
make a selection in the dropdown.

---

## Adding sliders allows us to highlight points based on quantitative value comparisons

``` python
slider = alt.binding_range(name='Tomatometer ')
select_rating = alt.selection_single(
    fields=['Rotten_Tomatoes_Rating'],
    bind=slider)

points.encode(
    opacity=alt.condition(select_rating, alt.value(0.7), alt.value(0.1))
).add_selection(select_rating)
```

<iframe src="/module7/charts/03/unnamed-chunk-6.html" width="100%" height="420px" style="border:none;">
</iframe>

Notes: So far we have seen how to select categorical values from
dropdown menus and radio buttons. To instead highlight based on
quantitative values, we can use a slider.

Adding a slider is similar to adding a dropdown or set of radio buttons,
and we do it via `binding_range()`. Here we link the slider to the same
column as on the x-axis, so that you can see how it works.

If you drag the slider around, you can see that the default behavior is
to only highlight points that are of the exact values as the slider.

This is useful for selection widgets like the dropdown, but for the
slider we want to make comparisons such as bigger and smaller than.

Let’s see how to do that in the next slide.

---

## Highlighting points smaller or bigger than a slider value

``` python
points.encode(
    opacity=alt.condition(
        alt.datum.Rotten_Tomatoes_Rating < select_rating.Rotten_Tomatoes_Rating,
        alt.value(0.7), alt.value(0.1))
).add_selection(select_rating)
```

<iframe src="/module7/charts/03/unnamed-chunk-7.html" width="100%" height="420px" style="border:none;">
</iframe>

Notes: To highlight values that are smaller than the slider, we need to
compare the current value of the slider with the value of the data
points.

The current value of the slider can be accessed via
`select_rating.Rotten_Tomatoes_Rating`, and Altair has a special `datum`
object to access values from different columns in the dataframe. To
compare against the column with the Rotten Tomatoes Ratings, we use
`alt.datum.Rotten_Tomatoes_Rating`.

This might seem cumbersome at first, but it is necessary to avoid
ambiguity with only writing `"Rotten_Tomatoes_Rating"`, which in
comparison expressions means just the string and is not a reference to a
column in the dataframe.

Now that we drag the slider you can see that all the points are
highlighted that have a value less than the slider value.

---

## Customizing a slider widget

``` python
slider = alt.binding_range(name='Tomatometer ', min=10, max=60, step=10)
select_rating = alt.selection_single(
    fields=['Rotten_Tomatoes_Rating'],
    bind=slider,
    init={'Rotten_Tomatoes_Rating': 20})

points.encode(
    opacity=alt.condition(
        alt.datum.Rotten_Tomatoes_Rating < select_rating.Rotten_Tomatoes_Rating,
        alt.value(0.7), alt.value(0.1))
).add_selection(select_rating)
```

<iframe src="/module7/charts/03/unnamed-chunk-8.html" width="100%" height="420px" style="border:none;">
</iframe>

Notes: Just as with dropdowns we can set an explicit start value to have
an active selection when the chart first appears.

For slider widgets we can also define the range and step size for the
slider as we have done in this slide.

Now that we drag the slider handle it jumps ten steps at a time, instead
of the default single step.

---

## It is more useful to bind a slider to a dataframe column not displayed on the chart axes

``` python
slider = alt.binding_range(name='Year')
select_rating = alt.selection_single(fields=['Release_Year'], bind=slider)

points.encode(
    opacity=alt.condition( select_rating, alt.value(0.7), alt.value(0.1))
).add_selection(select_rating)
```

<iframe src="/module7/charts/03/unnamed-chunk-9.html" width="100%" height="420px" style="border:none;">
</iframe>

Notes: So far we have used the same column for the slider as we have on
the x-axis to clearly see the effect from changing the slider behavior.

However, when creating an interactive visualization it is often the most
useful to bind the slider to a dataframe column that is not already
included on one of the axes.

In this slide we try to use the slider widget to highlight movies based
on the year they were produced, so that we can effectively explore
movies from different time periods separately.

However, as you can see it doesn’t work as we expected and nothing
happens when we drag the slider handle back and fourth. The reason for
this is that sliders don’t work well with temporal data in Altair.

As an alternative to the slider, we can use another plot to to select
data, which has several other advantages as you will see in the next
slide.

---

## Driving slider-like selections from another plot is more effective

``` python
select_year = alt.selection_interval()
bar_slider = (alt.Chart(movies).mark_bar().encode(
    alt.X('Release_Year', title='Release Year'),
    alt.Y('count()'),
    opacity=alt.condition(select_year, alt.value(0.7), alt.value(0.1)))
.properties(height=50).add_selection(select_year))

points.encode(opacity=alt.condition(select_year, alt.value(0.7), alt.value(0.1))) & bar_slider
```

<iframe src="/module7/charts/03/unnamed-chunk-10.html" width="100%" height="420px" style="border:none;">
</iframe>

Notes: Instead of having a a slider, it is more effective to use a
histogram for the selection since this is also gives us information
about the distribution of the movies over the years.

We can use what we learned in the last slide deck to link the selection
between the two plots. The biggest difference here is that instead of a
single or multi selection, we will use the `selection_interval` function
to create a range selection.

In this histogram we can see that there are just a few movies from the
1980s in the data and only one in 2040, which must be an error in the
dataset.

In addition to showing the distribution of the data this also allows us
to select a range of values, which is not possible with sliders in
Altair. We can then drag the selection with the mouse, just as when we
were selecting in the scatter plots in the first slide deck of this
module.

If we wanted to we could also style the histogram chart to look more
like a widget, and remove the incorrect data point, but we won’t do that
here.

---

## Interval selection can also be used to create a “minimap” for chart navigation

``` python
movies_1995_2010 = movies.loc[movies['Release_Year'].between('1995', '2010')]
base = alt.Chart(movies_1995_2010).mark_area().encode(
    alt.X('Release_Year', title=None),
    alt.Y('mean(Worldwide_Gross)', title='Gross worldwide'))
select_year = alt.selection_interval()

lower = base.properties(height=60).add_selection(select_year)
upper = base.encode(alt.X('Release_Year', title=None, scale=alt.Scale(domain=select_year))).properties(height=200)
upper & lower
```

<iframe src="/module7/charts/03/unnamed-chunk-11.html" width="100%" height="420px" style="border:none;">
</iframe>

Notes: Particularly when visualizing data over long time periods, it can
be useful to both have and overview of the data and be able to zoom in
on specific event.

One way to achieve this is with the `interactive` method we used
earlier. However, we could also use the approach with an additional
chart as in the previous slide to create a so called “minimap” for
navigation of another chart.

The key to making this interaction work is to let the interval selection
control the axis extent (the domain) of the main chart, while only
adding it as a selection on the “minimap” chart.

The syntax for this is consistent with what we have learned earlier, but
instead of having a condition that checks if an observation falls within
the selection, we’re directly using the range of the selection to set
the domain in the main chart.

---

# Let’s apply what we learned

Notes: <br>
