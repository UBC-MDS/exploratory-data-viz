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

## <span class="absolute-center" style="font-size: 3.0em; text-align: center;">How Can We Visualize Data?</span> {.slide}

<blockquote>
<strong>Transcript:</strong> There are many different data visualization strategies so which
one should we choose when visualizing our data?
</blockquote>

---

## There are two types of visualization approaches {.slide}

When learning about data visualization, it is helpful to distinguish
between the following two approaches to visualization:

1)  Imperative
1)  Declarative

<blockquote>
<strong>Transcript:</strong> There are a plethora of visualization packages in Python.<br>
This rich selection can be beneficial but it is also confusing,
especially when starting out and trying to decide which package to
choose.<br>
When learning about data visualization, it is helpful to distinguish
between plotting packages that follow either an *imperative* or a
*declarative* visualization philosophy.
</blockquote>

---

## Imperative (low level) plotting focuses on plot mechanics {.slide}

-   Focus on plot construction details.
    -   Often includes loops, low-level drawing commands, etc.
-   Specify *how* something should be done
    -   “Draw a red point for every observation that has value X in
        column A, a blue point for every observation that has value Y in
        column A, etc.”
-   Minute control over plotting details, but laborious for complex
    visualization.

<blockquote>
<strong>Transcript:</strong> **Imperative** (or **low level**) plotting packages focus on plot
construction details such as *how* to implement the visualization in
terms of for-loops, low-level drawing commands, etc.<br>
This approach gives us minute control over what is plotted, but it
becomes quite laborious when we need to plot larger dataframes, or
create more complex visualizations.
</blockquote>

---

## The data we will be plotting

<center>
<table style="width:50%;">
<thead>
<tr class="header">
<th style="text-align: left;">
Country
</th>
<th style="text-align: right;">
Area
</th>
<th style="text-align: right;">
Population
</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>
Russia
</td>
<td style="text-align: right;">
17098246
</td>
<td style="text-align: right;">
144386830
</td>
</tr>
<tr class="even">
<td>
Canada
</td>
<td style="text-align: right;">
9984670
</td>
<td style="text-align: right;">
38008005
</td>
</tr>
<tr class="odd">
<td>
China
</td>
<td style="text-align: right;">
9596961
</td>
<td style="text-align: right;">
1400050000
</td>
</tr>
</tbody>
</table>
</center>

<blockquote>
<strong>Transcript:</strong>
In the example in the next slide, we will plot the area and the
population for the three largest countries in the world to see how they
compare. This is the table we are plotting.
</blockquote>

---

## Example of imperative plotting

``` python {class="small-code"}
# Pseudocode
colors = ['blue', 'red', 'yellow']
plot = create_plot()
for row_number, row_data in enumerate(dataframe):
    plot.add_point(x=row_data['Area'], y=row_data['Population'], color=colors[row_number])
```
<div class="content-container">
  <img src="../../../static/module1/pseudocode-plot.svg" alt=""></img>

  <div class="right-aligned-transcript">
  <span data-notes>
    <strong>Transcript:</strong> Humans are not good at detecting patterns in raw numbers, and we
    don’t have good intuition about how different distributions of data can
    contribute to identical statistical summaries.<br>
    But guess what we excel at?
    <strong>Detecting visual patterns!</strong><br>
    It is immediately clear to us how these sets of numbers differ once they
    are shown as graphical elements instead of textual objects.<br>
    This is one of the main reasons why <strong>data visualization</strong> is such a
    powerful tool for data exploration and communication.<br>
    In our example here, we would come to widely different conclusions about
    the behaviour of the data for the four different data sets.<br>
    Sets <strong>A</strong> and <strong>C</strong> are roughly linearly increasing at similar rates, whereas
    set <strong>B</strong> reaches a plateau and starts to drop, and set <strong>D</strong> has a constant
    X-value for all numbers except one big outlier.
  </span>
</div>
</div>

---

## Declarative (high level) plotting focuses on the data

-   Focus on data and relationships.
    -   Often includes linking columns to visual channels.
-   Specify *what* should be done
    -   “Assign colors based on the values in column A”
-   Smart defaults give us what we want without complete control over
    minor plotting details.

<blockquote>
<strong>Transcript:</strong>
**Declarative** (or **high level**) plotting packages declare links
between dataframe columns and visual channels, such as the x-axis,
y-axis, colour, *etc*.<br>
This means that you can provide a high-level specification of *what* you
want the visualization to include, and the plot details are handled
automatically.<br>
In summary, declarative visualization tools let you think about
**data and relationships**, while imperative visualization tools focus
on **plot construction details**.
</blockquote>

---

## Example of declarative plotting

``` python {class="small-code"}
# Pseudocode
point_plot(data=dataframe, x='Area', y='Population', color='Country')
```
<div class="content-container">
  <img src="../../../static/module1/pseudocode-plot-with-legend.svg" alt="" width="65%" height="70%"></img>

  <div class="right-aligned-transcript">
  <span data-notes>
    <strong>Transcript:</strong> The visualization on this page is an example of what a plot could
look like when run with real code similar to our pseudocode.<br>
You will notice that this time the plot also includes a legend without
us having to create it explicitly, which is a common convenience in
declarative plotting packages.
  </span>
</div>
</div>

---

## A high-level grammar of graphics helps us compose plots effectively

-   Simple grammatical components combine to create visualizations.
-   Visualization grammars often consist of three main components:
    1)  Create a chart linked to a dataframe.
    1)  Add graphical elements (such as points, lines, etc).
    1)  Encode dataframe columns as visual channels (such as x, etc).

``` python {class="small-code"}
# Pseudocode
chart(dataframe).add_points().encode_columns(x='Area', y='Population', color='Country')`.
```
<blockquote>
<strong>Transcript:</strong>
The declarative plotting concept can be implemented in different
ways.<br>
In the previous slide, we had a dedicated function for creating the
pointplot, and there would be a separate function for creating a
lineplot, barplot, etc.<br>
With this approach, it is often not easy to combine plots together,
unless there is a specific function for that purpose and the three
bullets points on this slide are all executed by this single function.<br>
Another way to use declarative plotting is via a visualization grammar.
Generally, a grammar governs how individual parts come together to
compose more complex constructs.
For example, a linguistic grammar decides how words and phrases can be
combined into coherent sentences. A data visualization grammar
determines how to combine individual parts of the plotting syntax to
create complete visualization.
In the example on this slide, you can see that the three bullet points
are now broken down into one main function to create the chart linked to
the data, and then we build upon this by adding the graphical elements
(`add_points()`) and the encoding of the columns to properties of this
chart (`encode_columns()`).
By combining these three grammatical components in different ways, we
can build a wide range of visualizations, without memorizing a unique
function for each plot type. <br>
Thanks to this grammatical visualization approach, we also only require
minimal changes to our code to change the type of plot.
</blockquote>

---

## The Python plotting landscape

<br> 

<img src="../../../static/module1/py-plotting-landscape.png" alt="The Python plotting landscape" width="100%"></img>

<blockquote>
<strong>Transcript:</strong>
Now that we know the basic concepts of how data can be
visualized, let’s select a Python package and get coding!<br>
In this image, you can see the most commonly used Python plotting
packages. There are many more, but these are the ones you are the most likely to
hear about, so it is good to know that they exist.<br>
The text to the left in the image is a legend to explain the colours
used for the different Python packages (blue for high level, declarative
packages and orange for low-level, imperative packages).<br>
As you can see there are several high and low-level language, so how do
we chose?<br>
In this course we will use
<a href="https://altair-viz.github.io/" target="_blank">Altair</a>,
because it is a powerful declarative visualization tool with a clear and
consistent grammar that also allows us to add interactive components to
our plots, such as tooltips and selections.<br>
We have also included some of the most common visualization packages for
the web which are built-in Javascript and coloured in white.<br>
The reason we mention these is that the Altair library is a little bit
of Python code connected to an already existing powerful JavaScript
package called VegaLite, which in turns builds on D3, the most dominant
visualization package on the web today.<br>
By leveraging these well-established JavaScript visualization packages
Altair can create plots that work natively on the web and includes
interactive features without reinventing the wheel.<br>
Since Altair and VegaLite are relatively new visualization libraries,
they don’t yet support every single plot type out there, but they more
than make up for it with their ease of use and support for powerful
interactive visualizations, as we will see later.
</blockquote>

---

## Sample data can be found in Altair’s companion package vega\_datasets

``` python {class="small-code"}
from vega_datasets import data

cars = data.cars()
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
Before we start visualizing data, we need to select a dataset and
often also a question we want to answer. 
Altair works with dataframes in the
<a href="http://vita.had.co.nz/papers/tidy-data.html" target="_blank">“tidy”</a>
format (which we talked about in the
<a href="https://prog-learn.mds.ubc.ca/" target="_blank">Programming in
Python for Data Science course</a>), which means that they should
consist of rows with one **observation** each and a set of named data
**columns** with one feature each (you might also have heard these
called **fields** or **variables**, but we will stick to **columns** for
clarity).
In this course, we will often use data from the
<a href="https://github.com/vega/vega-datasets" target="_blank">vega-datasets</a>
package, which has many plot-friendly practice datasets available as
Pandas dataframes and can be loaded as demonstrated in this slide. We
can use these datasets by importing the `data` module from the
`vega_datasets` packages as in this slide. Here, our data contains the
name of different cars and some attributes relating to each car. There
are many interesting questions we could ask from this data set! For our
first plot, let’s explore the relationship between how heavy a car is
(the `Weight_in_lbs` column) and how good gas mileage it has
(the `Miles_per_gallon` column).
Before starting to code the visualization, take a few seconds and think
about what you would expect the relationship between these two columns
to look like when you plot it.
</blockquote>

---

## Adding graphical elements via marks

``` python {class="small-code"}
import altair as alt

alt.Chart(cars).mark_point()
```

```{=html}
<iframe src="../../../static/module1/charts/03/unnamed-chunk-4.html" 
        width="100%" 
        height="420px" 
        style="border:none;">
</iframe>
```

<blockquote>
<strong>Transcript:</strong>
Here we assigned a shorter name (`alt`) to the Altair library
when importing it to save us some typing later. The Altair syntax is
similar to the grammar of graphics pseudocode we saw a few slides ago.
The fundamental object in Altair is the `Chart`, which takes a data
frame as a single argument, e.g. `alt.Chart(cars)`.<br>
After the chart object has been created, we can specify how the
graphical element should look that we use to visualize the data. This is
called a graphical *mark* in Altair, and in this slide, we have used
`mark_point()` to show the data as points.<br>
Since we have not specified which columns should be used for the x and y
axes, we appear to only see one point in this plot since all the data is
plotted on top of each other in the same location.<br>
To the right of the chart, there is a button with three dots on it.
Don’t worry about it for now, we will explain what this is for at the
end of the chapter.
</blockquote>

---

## Encoding columns as visual channels

***Mapping a dataframe column to the x-scale***

``` python {class="small-code"}
alt.Chart(cars).mark_point().encode(
    x='Weight_in_lbs')
```

```{=html}
<iframe src="../../../static/module1/charts/03/unnamed-chunk-5.html" 
        width="100%" 
        height="420px" 
        style="border:none;">
</iframe>
```

<blockquote>
<strong>Transcript:</strong>
To visually separate the points, we can encode columns in the
dataframe as visual channels, such as the axes or colours of the plot.<br>
Here, we *encode* the column `Miles_per_Gallon` as the x-axis. For
Pandas data frames, Altair automatically determines an appropriate data
type for the mapped column, which in this case is quantitative (or
numerical) and shows the numbers under the axis.<br>
You can see that there are several short black lines spread out evenly
on the x-axis. These are called axis ticks and help us see where the
values of this dataframe column lie along the axis.<br>
The faint gray lines are called grid lines and extend the locations of
the axis ticks so that it is easy to compare their position to the
points.<br>
This is particularly useful when the points might be further away from
the axis ticks, such as in the next slide.
</blockquote>

---

## Mapping a dataframe column to the y-scale

``` python {class="small-code"}
alt.Chart(cars).mark_point().encode(
    x='Weight_in_lbs',
    y='Miles_per_Gallon')
```

<div class="content-container">
  ```{=html}
<iframe src="../../../static/module1/charts/03/unnamed-chunk-6.html"
        width="55%"
        height="420px"
        style="border:none;">
</iframe>
```

  <div class="right-aligned-transcript">
  <span data-notes>
    <strong>Transcript:</strong> By spreading out the data along both the x and y-axis, we can
answer our initial question about the relationship between car weight
and gas mileage. as it appears that the heavier cars are the ones that
have the poorest mileage.<br>
Although we might have expected this to be the case, visualizing all the
data points also provides information on the nature of the relationship
between weight and mileage.<br>
It appears that the x-y points don’t simply follow a straight line, but
rather a curved line that where the mileage drop quickly when moving
away from the lightest cars, but then decreases more slowly throughout
the remainder of the data. <br>
This rich, easily interpretable display of information is one of the
main advantages of visualizing data and later in the course, we will
talk more about the different type of relationships, such as linear,
exponential, etc.<br>
  </span>
</div>
</div>

---

## Mapping a numerical dataframe column to the colour scale

``` python {class="small-code"}
alt.Chart(cars).mark_point().encode(
    x='Weight_in_lbs',
    y='Miles_per_Gallon',
    color='Horsepower')
```

<div class="content-container">
  ```{=html}
<iframe src="../../../static/module1/charts/03/unnamed-chunk-7.html"
        width="55%"
        height="420px"
        style="border:none;">
</iframe>
```

  <div class="right-aligned-transcript">
  <span data-notes>
    <strong>Transcript:</strong> Is there a relationship between horsepower and car weight, or
fuel-efficiency?<br>
To enrich this display of information further, we can colour the points
according to a column in the dataframe. When we encode a column as the
colour channel Altair will automatically figure out an appropriate
colour scale to use, depending on whether the data is numerical,
categorical, etc. Here we have indicated that we want to colour the
points according to the car’s horsepower, which indicated how powerful
its engine is.<br>
We can see that the heavier cars have more powerful engines, than the
lighter ones, but when using colour for a numerical comparison like
this, makes it is harder to tell whether the relationship follows a
straight line or is of another nature, so this encoding is mostly useful
as an approximate indication of the horsepower. <br>
We can also observe a relationship between the horsepower of a vehicle
and the fuel efficiency. It appears that cars with greater horsepower
(the points with a darker shade of blue) are less efficient with their
fuel since miles per Gallon is much lower. <br>
In the next module, we will learn more in detail about which encodings
are most suitable for different comparisons.
  </span>
</div>
</div>


---

## Mapping a categorical dataframe column to the colour scale

``` python {class="small-code"}
alt.Chart(cars).mark_point().encode(
    x='Weight_in_lbs',
    y='Miles_per_Gallon',
    color='Origin')
```
<div class="content-container">
  ```{=html}
<iframe src="../../../static/module1/charts/03/unnamed-chunk-8.html"
        width="55%"
        height="420px"
        style="border:none;">
</iframe>
```

  <div class="right-aligned-transcript">
  <span data-notes>
    <strong>Transcript:</strong> In the previous slide, a continuous, gradually increasing colour
scale was used to visualize the gradual increase in the numerical column
`Horsepower`. In this slide, we instead chose to colour the points per
the categorical column `Origin` (where the car was made).<br>
As you can see, Altair detects that this column contains categorical
data (with the help of pandas) and picks a different colour scale to
facilitate distinction between the categories. As in the previous slide, <br>
Altair automatically adds a helpful legend, and we can see that the
heavier, more powerful cars are primarily manufactured in the US, while
the lighter more fuel-efficient ones are manufactured in Europe and
Japan (remember that this is true for this particular dataset, and not
necessarily all cars).<br>
  </span>
</div>
</div>

---

## Mapping a dataframe column to the shape scale

``` python {class="small-code"}
alt.Chart(cars).mark_point().encode(
    x='Weight_in_lbs',
    y='Miles_per_Gallon',
    color='Origin',
    shape='Origin')
```

<div class="content-container">
  ```{=html}
<iframe src="../../../static/module1/charts/03/unnamed-chunk-9.html"
        width="55%"
        height="420px"
        style="border:none;">
</iframe>
```

  <div class="right-aligned-transcript">
  <span data-notes>
    <strong>Transcript:</strong> Although Altair’s colour scales are designed to be effective and
easy to interpret, we can make the categories in our plot even more
distinct by encoding the same categorical column as both colour and
shape.<br>
This also makes visualizations much easier to interpret and understand
for anyone with visual colour deficiency (about 10% of the population).
We will talk more in-depth about colour theory in a later module.<br>
  </span>
</div>
</div>

---

## Mapping a dataframe column to the size scale

``` python {class="small-code"}
alt.Chart(cars).mark_point().encode(
    x='Weight_in_lbs',
    y='Miles_per_Gallon',
    color='Origin',
    shape='Origin',
    size='Horsepower')
```

<div class="content-container">
  ```{=html}
<iframe src="../../../static/module1/charts/03/unnamed-chunk-10.html"
        width="55%"
        height="420px"
        style="border:none;">
</iframe>
```
  <div class="right-aligned-transcript">
  <span data-notes>
    <strong>Transcript:</strong> Sometimes a visualization tries to do too much. In this example,
we have added the size channel to indicate the engine power.<br>
Although Altair elegantly handles the dual legends, it is difficult for
us to discern useful information from this plot. If you go back to the
plot where we encoded weight in the colour channel, you can see that the
plot is much clearer.<br>
Later we will learn more about how to efficiently load a visualization
with an appropriate amount of information, and what the research
indicates regarding which visual channels are the most efficient for
communicating information visually.<br>
  </span>
</div>
</div>

---

## The action button can be used to save the plot

``` python {class="small-code"}
alt.Chart(cars).mark_point().encode(
    x='Weight_in_lbs',
    y='Miles_per_Gallon',
    color='Origin',
    shape='Origin',
    size='Horsepower')
```
<div class="content-container">
  ```{=html}
<iframe src="../../../static/module1/charts/03/unnamed-chunk-11.html"
        width="55%"
        height="420px"
        style="border:none;">
</iframe>
```
  <div class="right-aligned-transcript">
  <span data-notes>
    <strong>Transcript:</strong> This is the same visualization as from the last slide, and we
will just use it as an example.<br>
The button to the right of the chart with three dots on it is called the
“action button”. and clicking it will bring up a menu.<br>
The first two items in ’s menu can be used to save the chart, either in
an image-based PNG-format or a text-based SVG-format.<br>
We will also be learning about programmatic ways to save our charts
later in the course.<br>
The last three menu items relate to the library VegaLite, which is what
we mentioned Altair is built upon, but we will not be using these in
this course.
  </span>
</div>
</div>

---

## <span class="absolute-center" style="font-size: 3.0em; text-align: center;">Let’s apply what we learned!</span> {.slide}
