---
format: revealjs
revealjs:
  slide-level: 2
  preview-links: true
  margin: 0.05
  html: true
include-in-header:
  - text: |
      <style>
      .absolute-center {
        position: absolute;
        left: 0;
        right: 0;
        top: 0;
        bottom: 0;
        height: 90%;
        margin: auto;
        display: flex;
        align-items: center;
        justify-content: center;
      }
      .reveal .slides section h1 {
        font-size: 2.0em;  
        color: #333;     
      }
      .reveal .slides section h2,
      .reveal .slides section h3 {
        font-size: 0.9em;  
        color: #333;     
      }
      .reveal .slides section p, .reveal .slides section li {
        font-size: 0.8em;  
        color: #333;     
      }
      .reveal .slides section blockquote {
        font-size: 0.4em;  
        position: absolute;
        bottom: 0;
        width: 100%;
        padding: 10px 0 10px 15px;
        text-align: left;
      }
      .small-code {
        font-size: 0.4em !important;
      }
      table {
        font-size: 0.7em; 
        width: auto; 
        margin-right: 5px; 
        float: center; 
      }
      .reveal .slides section .content-container {
        display: flex;
        align-items: center; 
        justify-content: space-between;
        margin-top: 40px; 
      }
      .reveal .slides section .content-container img {
        width: 100%;  
        height: auto; 
        max-height: 90vh; 
        display: block;
        margin: auto;
      }
      .reveal .slides section .right-aligned-transcript {
        float: right;
        width: 35%;
        font-size: 0.5em;
        text-align: left;
        padding: 0 10px;
        border-left: 4px solid #888; 
        margin-left: 5px;
        color: #888 !important;
        align-self: flex-start;
      }
      .reveal .slides section .right-aligned-transcript * {
        border-left: none !important; 
        padding: 0; 
        margin: 0; 
        color: inherit; 
      }
      .reveal .slides section .img-transcript {
        width: 45%; 
        font-size: 0.7em;
        text-align: left;
        padding: 0 10px;
        border-left: 4px solid #888;
        color: #888 !important;
        max-height: 100%; 
        overflow: auto; 
      }
      </style>
---

## <span class="absolute-center" style="font-size: 3.0em; text-align: center;">Aggregations, lines, and layers</span> {.slide}

<blockquote>
<strong>Transcript:</strong> In this slide deck, we will see how to aggregate data in Altair (to plot
the mean, median, etc), how to create lineplots via `mark_line()`, and
how to combine line and point plots together via layers.
</blockquote>

---

## Including all the data can hinder visualization of general trends {.slide}

``` python {class="small-code"}
import altair as alt
from vega_datasets import data

cars = data.cars()
alt.Chart(cars).mark_point().encode(
    x='Weight_in_lbs',
    y='Miles_per_Gallon',
    color='Origin')
```

<div class="content-container">
  ```{=html}
<iframe src="../../../static/module1/charts/07/unnamed-chunk-1.html"
        width="55%"
        height="420px"
        style="border:none;">
</iframe>
```

  <div class="right-aligned-transcript">
  <span data-notes>
    <strong>Transcript:</strong> Throughout this course we will explore many different datasets,
but for now, we will stick to the `cars` dataset to keep it simple and
focus on introducing additional Altair functionality.<br>
Let’s refresh our memory with this plot from the previous module.<br>
We noted that it appears that cars differ in their weight and mileage
based on their country of origin. At least the American cars appear to
stand out, but it is difficult to see any differences between Europe and
Japan.<br>
Visualizing all data points as in this slide is helpful to detect
patterns in the data.<br>
But when showing all observations, it can be hard to pick up on general
trends in the data, e.g. if there are any differences in the mean weight
of cars made in either Japan or Europe.<br>
To more effectively visualize such general trends in the data, we can
create plots of statistical summaries, such as means and medians.<br>
In Altair (and pandas) these are referred to as data aggregations.
  </span>
</div>
</div>

---

## Data aggregations are built into Altair {.slide}

``` python {class="small-code"}
alt.Chart(cars).mark_point().encode(
    x='mean(Weight_in_lbs)',
    y='mean(Miles_per_Gallon)',
    color='Origin')
```

<div class="content-container">
  ```{=html}
<iframe src="../../../static/module1/charts/07/unnamed-chunk-2.html"
        width="55%"
        height="420px"
        style="border:none;">
</iframe>
```

  <div class="right-aligned-transcript">
  <span data-notes>
    <strong>Transcript:</strong> To plot the means of weight and mileage, we could use pandas to
first calculate the mean values, and then plot the resulting dataframe
in Altair.<br>
This is powerful since we can access all aggregations built into pandas,
but it is a bit verbose for simple common operations, such as the mean.<br>
Fortunately, Altair has shortcuts for plotting simple aggregations where
you provide the name of the aggregation together with the name of the
column inside a string as in the example in this slide.<br>
<a href="https://altair-viz.github.io/user_guide/encoding.html#binning-and-aggregation" target="_blank">The
Altair documentation includes a table with all available
aggregations</a> (scroll down a little on the linked page).<br>
In this visualization, we can detect small differences between the means
of the Japanese and Europeans cars, which was not discernible when we
plotted all the points.<br>
Whether this difference is big enough to reach a different conclusion
than when inspecting the previous plots depends on our application and
the purpose of the data exploration.
  </span>
</div>
</div>


---

## Plotting aggregations to visualize trends over time

``` python {class="small-code"}
cars
```

```out {class="small-code"}
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

<blockquote>
<strong>Transcript:</strong>
Aggregations are often helpful when comparing trends over time,
especially when there are multiple groups in the data. In the cars
dataset, there is a `Year` column, indicating when the car was made. <br>
Often when there is a notion of time in the data, it is interesting to
see how values in the dataframe change over time. <br>
In this case, we might be interested in knowing whether newer cars are
more fuel-efficient than older ones.<br>
Presumably, they should be, but does it differ depending on where the
car was made?<br>
Let’s find out!
</blockquote>

---

## Plotting aggregations to visualize trends over time works well {.slide}

``` python {class="small-code"}
alt.Chart(cars).mark_point().encode(
    x='Year',
    y='mean(Miles_per_Gallon)')
```

<div class="content-container">
  ```{=html}
<iframe src="../../../static/module1/charts/07/unnamed-chunk-4.html"
        width="55%"
        height="420px"
        style="border:none;">
</iframe>
```

  <div class="right-aligned-transcript">
  <span data-notes>
    <strong>Transcript:</strong> To visualize the mean mileage for each year of all cars, we want
to perform the aggregation on the `Miles_per_Gallon` column while
leaving the `Year` column intact.<br>
As you can see this plot one value (the mean) for each year in the
dataframe.<br>
Here we can see that the observations in this dataframe span the years
1970-1982 and it does indeed look like the mileage is getting better
over time as we expected!<br>
  </span>
</div>
</div>

---

## Plotting all data to visualize trends over time is not effective {.slide}

``` python {class="small-code"}
alt.Chart(cars).mark_point().encode(
    x='Year',
    y='Miles_per_Gallon')
```

<div class="content-container">
  ```{=html}
<iframe src="../../../static/module1/charts/07/unnamed-chunk-5.html"
        width="55%"
        height="420px"
        style="border:none;">
</iframe>
```

  <div class="right-aligned-transcript">
  <span data-notes>
    <strong>Transcript:</strong> As a comparison with the previous slide, if we instead of the
mean would plot all the data points for each year, it would be much more
difficult to see the pattern over time as you can see here.
  </span>
</div>
</div>

---

## Plotting points to visualize trends over time is not ideal {.slide}

``` python {class="small-code"}
alt.Chart(cars).mark_point().encode(
    x='Year',
    y='mean(Miles_per_Gallon)',
    color='Origin')
```

<div class="content-container">
  ```{=html}
<iframe src="../../../static/module1/charts/07/unnamed-chunk-6.html"
        width="55%"
        height="420px"
        style="border:none;">
</iframe>
```

  <div class="right-aligned-transcript">
  <span data-notes>
    <strong>Transcript:</strong> If we try to explore the mileage over time while grouping the
cars according to their origin, it is a bit difficult to immediately
recognize which points belong to which group.<br>
In fact, using points for visualizing trends is not ideal, and lines are
often preferred as we will see in the next slide.
  </span>
</div>
</div>

---

## Plotting lines to visualize trends over time is ideal {.slide}

``` python {class="small-code"}
alt.Chart(cars).mark_line().encode(
    x='Year',
    y='mean(Miles_per_Gallon)',
    color='Origin')
```

<div class="content-container">
  ```{=html}
<iframe src="../../../static/module1/charts/07/unnamed-chunk-7.html"
        width="55%"
        height="420px"
        style="border:none;">
</iframe>
```

  <div class="right-aligned-transcript">
  <span data-notes>
    <strong>Transcript:</strong> One key advantage of line plots is that they connect all the
observations that belong to the same group presenting them as one
unified graphical object (one line), which is easy for us to distinguish
when looking at the plot instead of trying to connect the dots mentally.<br>
Another advantage is that the slope of the line makes it easier to see
if the value from one year to another is increasing or decreasing.<br>
Altair grammar lets us switch from a point plot to a line plot, by only
changing `mark_point()` to `mark_line()`, and keeping the rest of the
code as-is.<br>
In this plot, we can clearly compare the mileage trends over time to
conclude that cars from all origins improved their mileage, and that the
trajectory and mileage values are the most similar between Europe and
Japan.
  </span>
</div>
</div>

---

## Combining a line with a set of points via layers {.slide}

``` python {class="small-code"}
line = alt.Chart(cars).mark_line().encode(
    x='Year',
    y='mean(Miles_per_Gallon)')

point = alt.Chart(cars).mark_point().encode(
    x='Year',
    y='mean(Miles_per_Gallon)')

line + point
```
<div class="content-container">
  ```{=html}
<iframe src="../../../static/module1/charts/07/unnamed-chunk-8.html"
        width="55%"
        height="420px"
        style="border:none;">
</iframe>
```

  <div class="right-aligned-transcript">
  <span data-notes>
    <strong>Transcript:</strong> To augment a line plot, it is sometimes helpful to add `point` marks for
each data point along the line, to emphasize where the observations
fall.<br>
This is helpful since the line drawn between points could be misleading
if we have very few points.<br>
For example, if you see a straight line, does that mean there are just
two points, one in each corner of the line?<br>
Or are there ten points spread out all along the line?<br>
To combine two different types of graphical marks (line and point in
this case), we will use Altair’s *layering* grammar.<br>
In this slide, we start by defining each chart separately:<br>
first a line plot, <br> then a point plot.<br>
We can then use the `+` (plus) operator to combine the two into a
layered chart.
  </span>
</div>
</div>

---

## Building upon previous plots can save time when combining charts {.slide}

``` python {class="small-code"}
line = alt.Chart(cars).mark_line().encode(
    x='Year',
    y='mean(Miles_per_Gallon)')

line + line.mark_point()
```
<div class="content-container">
  ```{=html}
<iframe src="../../../static/module1/charts/07/unnamed-chunk-9.html"
        width="55%"
        height="420px"
        style="border:none;">
</iframe>
```

  <div class="right-aligned-transcript">
  <span data-notes>
    <strong>Transcript:</strong> We can also create a layered plot by reusing a previous chart
definition.<br>
Rather than creating the point plot from scratch, we can start with the
line plot, and then invoke the `mark_point` method.<br>
We could also have typed `mark_line(point=True)`, which is a special
case for getting points on a line since it is such a common operation,
but the layering grammar extends to other plots, so it is more helpful
to focus on learning that.
  </span>
</div>
</div>

---

## Showing raw values together with the mean is often helpful {.slide}

``` python {class="small-code"}
line = alt.Chart(cars).mark_line().encode(
    x='Year',
    y='mean(Miles_per_Gallon)')

line + line.mark_point().encode(y='Miles_per_Gallon')
```

<div class="content-container">
  ```{=html}
<iframe src="../../../static/module1/charts/07/unnamed-chunk-10.html"
        width="55%"
        height="420px"
        style="border:none;">
</iframe>
```

  <div class="right-aligned-transcript">
  <span data-notes>
    <strong>Transcript:</strong> When we are combing plots in layers, we can not only change the
mark, but also the encodings.<br>
This way, we can create a layer with one point per observations, and
with a line for the average values.<br>
For this, we need to use `encode` again after creating the first plot,
to instruct Altair to use the raw values instead of the mean for the
points.<br>
(note that the axis now has two labels, we will see how to change that
in a future lecture).<br>
This type of visualization is helpful when we want to show both the
underlying data and a statistical summary, which is often helpful for
elucidating what the data tells us.<br>
It is also a good check to make sure nothing unexpected is going on with
the raw values as we saw in the introductory example with Anscombe’s
quartet.
  </span>
</div>
</div>

---

## All encodings of the base chart are propagated unless they are overwritten {.slide}

``` python {class="small-code"}
line = alt.Chart(cars).mark_line().encode(
    x='Year',
    y='mean(Miles_per_Gallon)',
    color='Origin')

line + line.mark_point().encode(y='Miles_per_Gallon')
```

<div class="content-container">
  ```{=html}
<iframe src="../../../static/module1/charts/07/unnamed-chunk-11.html"
        width="55%"
        height="420px"
        style="border:none;">
</iframe>
```

  <div class="right-aligned-transcript">
  <span data-notes>
    <strong>Transcript:</strong>  We have already seen that the x and y encoding remain the same in
any subsequently created plots.<br>
Here, we’re showing that this also applies to the colour encoding to
illustrate that any encoding will be propagated to all layers unless
they are specifically overwritten.<br>
If we would only have added colour to the point chart, there would still
have been a single line instead of three.
  </span>
</div>
</div>

---

## <span class="absolute-center" style="font-size: 3.0em; text-align: center;">Let’s apply what we learned!</span> {.slide}
