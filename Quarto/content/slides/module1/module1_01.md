---
format: revealjs
revealjs:
  slide-level: 2
  preview-links: true
  margin: 0.05
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
        font-size: 0.6em;  
        color: #333;     
      }
      .reveal .slides section blockquote {
        font-size: 0.4em;  
        position: absolute;
        bottom: 0;
        width: 100%;
        padding: 10px 0;
        text-align: left;
      }
      table {
        font-size: 0.6em; 
        width: auto; 
        margin-right: 5px; 
        float: left; 
      }
      .reveal .slides section .content-container {
        display: flex;
        align-items: flex-start; 
        justify-content: space-between; 
      }
      .reveal .slides section .content-container img {
        width: 80%; 
        height: auto; 
      }
      .reveal .slides section .right-aligned-transcript {
        float: right;
        width: 30%;
        font-size: 0.7em;
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

## <span class="absolute-center" style="font-size: 3.0em; text-align: center;">What is Data Visualization ?</span> {.slide}

<blockquote>
<strong>Transcript:</strong> At its core, data visualization is about representing numbers
with graphical elements such as the position of a line, the length of a
bar, or the colour of a point.
We often use visualizations to explore data ourselves, and to
effectively communicate our insights to others, as we will learn in
later modules of this course.
</blockquote>

---

## What is the purpose of visualizing data? {.slide}

Visualizing data can be used to

- Answer a specific question
- Explore data more generally to generate new questions

To create an effective visualization, start by

- Looking at the data
- Thinking about what you want to achieve by making the visualization
- Drawing it out with pen and paper

<blockquote>
<strong>Transcript:</strong> We often visualize data in order to help us answer a specific
question we have about our dataset, but it can also help us generate new
questions.<br>
Before creating a visualization, it is important that you think about
why you are making it, and what you want to achieve from creating this
plot.<br>
Is there a specific question you are trying to answer, like comparing
the relationship between two dataframe columns? Or are you creating a
plot to help you understand the structure of your data more in general,
such as plotting the distribution of each dataframe column?<br>
In either case, it can be extremely helpful to draw out your plot with
pen and paper first. This helps you think about if the plot you are
creating makes sense or if there is another plot better suited for the
task at hand.<br>
Drawing with pen and paper also makes it easier to write the code
afterwards, since you clearly know what you are expecting the
visualization to look like.
</blockquote>

---

## Why bother visualizing data instead of showing raw numbers? {.slide}

**Can you see any differences in the general trends of these four sets of numbers?**

<table border="1" style="width:40px; float:left; margin-right:10px">
<thead style="text-align: center">
<tr>
<th colspan="2" halign="left">
A
</th>
</tr>
<tr>
<th>
X
</th>
<th>
Y
</th>
</tr>
</thead>
<tbody>
<tr>
<td>
10
</td>
<td>
8.04
</td>
</tr>
<tr>
<td>
8
</td>
<td>
6.95
</td>
</tr>
<tr>
<td>
13
</td>
<td>
7.58
</td>
</tr>
<tr>
<td>
9
</td>
<td>
8.81
</td>
</tr>
<tr>
<td>
11
</td>
<td>
8.33
</td>
</tr>
<tr>
<td>
14
</td>
<td>
9.96
</td>
</tr>
<tr>
<td>
6
</td>
<td>
7.24
</td>
</tr>
<tr>
<td>
4
</td>
<td>
4.26
</td>
</tr>
<tr>
<td>
12
</td>
<td>
10.84
</td>
</tr>
<tr>
<td>
7
</td>
<td>
4.81
</td>
</tr>
<tr>
<td>
5
</td>
<td>
5.68
</td>
</tr>
</tbody>
</table>
<table border="1" style="width:70px; float:left; margin-right:40px">
<thead style="text-align: center">
<tr>
<th colspan="2" halign="left">
B
</th>
</tr>
<tr>
<th>
X
</th>
<th>
Y
</th>
</tr>
</thead>
<tbody>
<tr>
<td>
10
</td>
<td>
9.14
</td>
</tr>
<tr>
<td>
8
</td>
<td>
8.14
</td>
</tr>
<tr>
<td>
13
</td>
<td>
8.74
</td>
</tr>
<tr>
<td>
9
</td>
<td>
8.77
</td>
</tr>
<tr>
<td>
11
</td>
<td>
9.26
</td>
</tr>
<tr>
<td>
14
</td>
<td>
8.10
</td>
</tr>
<tr>
<td>
6
</td>
<td>
6.13
</td>
</tr>
<tr>
<td>
4
</td>
<td>
3.10
</td>
</tr>
<tr>
<td>
12
</td>
<td>
9.13
</td>
</tr>
<tr>
<td>
7
</td>
<td>
7.26
</td>
</tr>
<tr>
<td>
5
</td>
<td>
4.74
</td>
</tr>
</tbody>
</table>
<table border="1" style="width:70px; float:left; margin-right:40px">
<thead style="text-align: center">
<tr>
<th colspan="2" halign="left">
C
</th>
</tr>
<tr>
<th>
X
</th>
<th>
Y
</th>
</tr>
</thead>
<tbody>
<tr>
<td>
10
</td>
<td>
7.46
</td>
</tr>
<tr>
<td>
8
</td>
<td>
6.77
</td>
</tr>
<tr>
<td>
13
</td>
<td>
8.50
</td>
</tr>
<tr>
<td>
9
</td>
<td>
7.11
</td>
</tr>
<tr>
<td>
11
</td>
<td>
7.81
</td>
</tr>
<tr>
<td>
14
</td>
<td>
8.84
</td>
</tr>
<tr>
<td>
6
</td>
<td>
6.08
</td>
</tr>
<tr>
<td>
4
</td>
<td>
5.39
</td>
</tr>
<tr>
<td>
12
</td>
<td>
8.15
</td>
</tr>
<tr>
<td>
7
</td>
<td>
6.42
</td>
</tr>
<tr>
<td>
5
</td>
<td>
5.73
</td>
</tr>
</tbody>
</table>
<table border="1" style="width:70px; float:left; margin-right:40px">
<thead style="text-align: center">
<tr>
<th colspan="2" halign="left">
D
</th>
</tr>
<tr>
<th>
X
</th>
<th>
Y
</th>
</tr>
</thead>
<tbody>
<tr>
<td>
8
</td>
<td>
6.58
</td>
</tr>
<tr>
<td>
8
</td>
<td>
5.76
</td>
</tr>
<tr>
<td>
8
</td>
<td>
7.71
</td>
</tr>
<tr>
<td>
8
</td>
<td>
8.84
</td>
</tr>
<tr>
<td>
8
</td>
<td>
8.47
</td>
</tr>
<tr>
<td>
8
</td>
<td>
7.04
</td>
</tr>
<tr>
<td>
8
</td>
<td>
5.25
</td>
</tr>
<tr>
<td>
19
</td>
<td>
12.50
</td>
</tr>
<tr>
<td>
8
</td>
<td>
5.56
</td>
</tr>
<tr>
<td>
8
</td>
<td>
7.91
</td>
</tr>
<tr>
<td>
8
</td>
<td>
6.89
</td>
</tr>
</tbody>
</table>

<div class="right-aligned-transcript">
<strong>Transcript:</strong> Why do we need visualizations to help answer our questions?<br>
Is it not enough to look at numbers in tables?<br>
To understand why visualizations are so powerful, it is helpful to remember that to answer a question, we often have to put the data in a format that is easy for us humans to interpret.<br>
Because our number systems have only been around for about 5,000 years, we need to assert effort and train ourselves to recognize numerical data.<br> 
Visual systems, on the other hand, have undergone refining during 500,000,000 years of evolution, so we can instinctively recognize visual properties such as colours and distances.<br>
Practically, this means that we can arrive at correct conclusions faster
from studying visual rather than numerical representations of the same
data.<br>
For example, have a look at the four sets of numbers in the table on the
slide. Can you see the differences in the general trends between these
four sets of numbers? This is a slightly modified version of the
original, <a href="https://en.wikipedia.org/wiki/Anscombe%27s_quartet" target="_blank" style="text-decoration: underline; color: blue;">which was put together by statistician Francis Anscombe in the 70s</a>.
</div>

---

## Although summary statistics are often useful, they don’t tell the whole story {.slide}

**C is the only set with a different mean and standard deviation**

<table border="1" style="width:70px; float:left; margin-right:40px">
<thead style="text-align: center">
<tr>
<th>
</th>
<th colspan="2" halign="left">
A
</th>
</tr>
<tr>
<th>
</th>
<th>
X
</th>
<th>
Y
</th>
</tr>
</thead>
<tbody>
<tr>
<td>
mean
</td>
<td>
9.00
</td>
<td>
7.50
</td>
</tr>
<tr>
<td>
std
</td>
<td>
3.32
</td>
<td>
2.03
</td>
</tr>
</tbody>
</table>
<table border="1" style="width:70px; float:left; margin-right:40px">
<thead style="text-align: center">
<tr>
<th>
</th>
<th colspan="2" halign="left">
B
</th>
</tr>
<tr>
<th>
</th>
<th>
X
</th>
<th>
Y
</th>
</tr>
</thead>
<tbody>
<tr>
<td>
mean
</td>
<td>
9.00
</td>
<td>
7.50
</td>
</tr>
<tr>
<td>
std
</td>
<td>
3.32
</td>
<td>
2.03
</td>
</tr>
</tbody>
</table>
<table border="1" style="width:70px; float:left; margin-right:40px">
<thead style="text-align: center">
<tr>
<th>
</th>
<th colspan="2" halign="left">
C
</th>
</tr>
<tr>
<th>
</th>
<th>
X
</th>
<th>
Y
</th>
</tr>
</thead>
<tbody>
<tr>
<td>
mean
</td>
<td>
9.00
</td>
<td style="background-color:#4853a4; color:#ffffff">
<b>7.11</b>
</td>
</tr>
<tr>
<td>
std
</td>
<td>
3.32
</td>
<td style="background-color:#4853a4; color:#ffffff">
<b>1.15</b>
</td>
</tr>
</tbody>
</table>
<table border="1" style="width:70px; float:left; margin-right:40px">
<thead style="text-align: center">
<tr>
<th>
</th>
<th colspan="2" halign="left">
D
</th>
</tr>
<tr>
<th>
</th>
<th>
X
</th>
<th>
Y
</th>
</tr>
</thead>
<tbody>
<tr>
<td>
mean
</td>
<td>
9.00
</td>
<td>
7.50
</td>
</tr>
<tr>
<td>
std
</td>
<td>
3.32
</td>
<td>
2.03
</td>
</tr>
</tbody>
</table>

<blockquote>
<strong>Transcript:</strong> Summaries, such as the mean and standard deviation, are helpful
statistical tools that are often useful for detecting the differences
between datasets.<br>
However, since they collapse the data into just a few numbers,
statistical summaries can’t tell the whole story about the data and
there can be important differences between datasets that summaries fail
to reveal.<br>
Here, the mean and standard deviation indicate that set C is slightly
different from the other sets of data in terms of the centre of the
sample distribution and the spread of that distribution, while the
remaining three sets of data have a similar centre and spread.<br>
</blockquote>

---

## Plotting the data immediately reveals patterns in the data {.slide}

**We could not detect these patterns from only looking at the raw numbers or summary statistics**

<div class="content-container">
  <img src="/static/module1/modified-anscombes.svg" alt="">

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

## More examples of plotting versus statistical summaries {.slide}

![](https://blog.revolutionanalytics.com/downloads/DataSaurus%20Dozen.gif)

<a href="<https://www.autodesk.com/research/publications/same-stats-different-graphs>" style="font-size: 0.6em" target="_blank">Source:
Matejka and Fitzmaurice, 2017</a>

<blockquote>
<strong>Transcript:</strong> A more recent and dynamic illustration of how graphical
representations are much easier for us to interpret compared to
statistical summaries, is the Datasaurus GIF <a href="https://www.autodesk.com/research/publications/same-stats-different-graphs" target="_blank">from
Autodesk’s research team</a> in this slide.<br>
It displays several different datasets, all with the same mean, standard
deviation and correlation between X and Y, but looking at the data
graphically shows us how different these datasets actually are.
</blockquote>

---

## <span class="absolute-center" style="font-size: 3.0em; text-align: center;">Let's apply what we learned!</span> {.slide}

