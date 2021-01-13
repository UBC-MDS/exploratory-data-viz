---
type: slides
---

# What is Data Visualization?

Notes: At its core, data visualization is about representing numbers
with graphical elements such as the position of a line, the length of a
bar, or the color of a point.

We often visualize data in order to help us answer a specific question
we have about our dataset, but it can also help us generate new
questions.

In addition to using visualizations to explore data ourselves, we can
use them to effectively communicate our insights to others, as we will
learn in later modules of this course.

---

## Why bother visualizing data instead of showing raw numbers?

### Can you see any differences in the general trends of these four sets of numbers?

<table border="1" style="width:70px; float:left; margin-right:40px">

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

Notes: Why do we need visualizations to help answer our questions?

Is it not enough to look at numbers in tables?

To understand why visualizations are so powerful, it is helpful to
remember that to answer a question, we often have to put the data in a
format that is easy for us humans to interpret.

Because our number systems have only been around for about 5,000 years,
we need to assert effort and train ourselves to recognize structure in
numerical data.

Visual systems, on the other hand, have undergone refinement during
500,000,000 years of evolution, so we can instinctively recognize visual
patterns and accurately estimate visual properties such as colors and
distances.

Practically, this means that we can arrive at correct conclusions faster
from studying visual rather than numerical representations of the same
data.

For example, have a look at the four sets of numbers in the table on the
slide.

This is a slightly modified version of the original,
<a href="https://en.wikipedia.org/wiki/Anscombe%27s_quartet" target="_blank">which
was put together by statistician Francis Anscombe in the 70s.</a>

Can you see the differences in the general trends between these four
sets of numbers?

---

## Although summary statistics are often useful, they don’t tell the whole story

### C is the only set with a different mean and standard deviation

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

Notes: Summaries, such as the mean and standard deviation, are helpful
statistical tools that are often useful for detecting difference between
datasets.

However, since they collapse the data into just a few numbers,
statistical summaries can’t tell the whole story about the data and
there can be important differences between datasets that summaries fail
to reveal.

Here, the mean and standard deviation indicate that set C is slightly
different from the other sets of data in terms of the centre of the
sample distribution and the spread of that distribution, while the
remaining three sets of data have a similar centre and spread.

---

## Plotting the data immediately reveals the differences to the human eye

### There are clear patterns in these datasets that we could not detect from only looking at the raw numbers or some summary statistics

<img src="/module1/modified-anscombes.svg" alt="" width="60%"></img>

Notes: Humans are not good at detecting patterns in raw numbers, and we
don’t have good intuition about how different distributions of data can
contribute to identical statistical summaries.

But guess what we excel at?

Detecting visual patterns\!

It is immediately clear to us how these sets of numbers differ once they
are shown as graphical elements instead of textual objects.

This is one of the main reasons why data visualization is such a
powerful tool for data exploration and communication.

In our example here, we would come to widely different conclusions about
the behavior of the data for the four different data sets.

Sets A and C are roughly linearly increasing at similar rates, whereas
set B reaches a plateau and starts to drop, and set D has a constant
X-value for all numbers except one big outlier.

---

## More examples of plotting versus statistical summaries

![](https://blog.revolutionanalytics.com/downloads/DataSaurus%20Dozen.gif)

<a href="https://www.autodesk.com/research/publications/same-stats-different-graphs" target="_blank">Source:
Matejka and Fitzmaurice, 2017</a>

Notes: A more recent and dynamic illustration of how graphical
representations are much easier for us to interpret compared to
statistical summaries, is the Datasaurus GIF
<a href="https://www.autodesk.com/research/publications/same-stats-different-graphs" target="_blank">from
Autodesk’s research team</a> in this slide.

It displays several different datasets, all with the same mean, standard
deviation and correlation between X and Y, but looking at the data
graphically shows us how different these datasets actually are.

---

# Let’s apply what we learned\!

Notes: <br>
