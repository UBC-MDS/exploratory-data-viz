---
title: 'Module 1: Why Visualize Data?'
description:
  'In this module we will be learning about the importance of data visualization and how a grammar of graphics can help us effectively visualize data.'
prev: ../../module0
next: ../../module2
type: chapter
id: 1
---

<exercise id="0" title="Module Learning Outcomes"  type="slides, video">
<slides source="module1/module1_00" shot="0" start="3:5707" end="4:5306"> </slides>
</exercise>


<exercise id="1" title="What is Data Visualization?" type="slides,video">
<slides source="module1/module1_01" shot="1" start="0:003" end="07:12"> </slides>
</exercise>

<exercise id="2" title="Why Visualize Data?">
<p><strong>True or False: It is easier for humans to interpret plots than raw numbers.</strong></p>
<choice id="1" >
<opt text="True"  correct="true"></opt>
<opt text="False"></opt>
</choice>

<p><strong>True or False: Statistical summaries are often useful,
but it is a good idea to also visualize your data before drawing any conclusions.</strong></p>
<choice id="2" >
<opt text="True"  correct="true"></opt>
<opt text="False"></opt>
</choice>
</exercise>


<exercise id="3" title="How Can We Visualize Data?" type="slides,video">
<slides source="module1/module1_02" shot="1" start="0:003" end="07:12"> </slides>
</exercise>

<exercise id="4" title="Exercises">
<p><strong>True or False: An low level visualization library focuse on plot construction details.</strong></p>
<choice id="3" >
<opt text="True"  correct="true"></opt>
<opt text="False"></opt>
</choice>

<p><strong>True or False: A high level visualization library focuses on data and relationships.</strong></p>
<choice id="4" >
<opt text="True"  correct="true"></opt>
<opt text="False"></opt>
</choice>

**Your first plot!**

*When you see `____` in a coding exercise,
replace it with what you assume to be the correct code.
Run the code to see if you obtain the desired output
and submit it to validate if you were correct.
Be patient when running a coding exercise for the first time,
it can take a few minutes.*

Let's use the same vehicle dataset we saw in the lecture,
but visualize the relationship between two different columns.
The data has already been imported for you in this exercise,
Your task is to fill out the missing fields in the Altair plot
in order to create a scatter plot
with the cars' horsepower on the x-axis and their weight on the y-axis.
You should color the dots by the origin of the cars.

<codeblock id="01_03">

- Remember that the column names should be in quotes, e.g. `y='Horsepower'`.

</codeblock>
</exercise>


<exercise id="5" title="Lines and layers" type="slides,video">
<slides source="module1/module1_03" shot="1" start="0:003" end="07:12"></slides>
</exercise>


<exercise id="5" title="Exercises">
<p><strong>When combining plots in Altair, we say that each plot has its own `___`.</strong></p>
<choice id="5">
<opt text="Overlay"></opt>
<opt text="Layer"  correct="true"></opt>
<opt text= "Panel"></opt>
</choice>

<p><strong>Line plots are often preferable to point plots when visualizing trends over time because...</p></strong>
<choice id="6">
<opt text="The lines make the plot more visually appealing."></opt>
<opt text= "Line plots are faster to create."></opt>
<opt text="The line makes it easy to see which values are connected in the same group and its slope facilitates our interpretation of the overall trend."  correct="true"></opt>
</choice>

**Creating a line plot for change over time**

*When you see `____` in a coding exercise,
replace it with what you assume to be the correct code.
Run the code to see if you obtain the desired output
and submit it to validate if you were correct.
Be patient when running a coding exercise for the first time,
it can take a few minutes.*

Let's use a line plot to visualize how the price of a few common stocks has changed over time.
Your task is to fill out the missing fields in the code below
in order to create a line plot
with the stocks' date on the x-axis and their price on the y-axis.
You should color the lines by the stock symbol,
so that you can compare the stock development for the different companies.

<codeblock id="01_06">

- Remember that the column names should be in quotes, e.g. `y='price'`.
- Look at the dataframe by typing `stocks.columns` if you are unsure about the exact column names.

</codeblock>

<p><strong>In the chart above, which stock was priced the highest in 2003?</strong></p>
<choice id="7">
<opt text="GOOG"></opt>
<opt text= "AAPL"></opt>
<opt text="IBM"  correct="true"></opt>
</choice>

**Combining a point and line plot**

Let's add points to the line above to indicate each observation along the line.
Your task is to fill out the missing fields in the code below
in order to assign the line plot to a variable name (of your choice),
and then use this name to combine a line plot and a point plot.

<codeblock id="01_07">

- Remember that the column names should be in quotes, e.g. `y='price'`.
- Look at the dataframe by typing `stocks.columns` if you are unsure about the exact column names.
- Revisit the slides on how to build upon existing plots when layering.

</codeblock>

**Plotting an aggregated value**

Instead of showing the value for each individual stock value,
we could explore the average trend over time
for all five companies.
Use the first coding exercise above as a base
and modify the code to plot one line with the average value over time,
instead of giving each company its own line.

<codeblock id="01_08">

- Remember that the column names should be in quotes, e.g. `y='price'`.
- Look at the dataframe by typing `stocks.columns` if you are unsure about the exact column names.
- Remember that the string syntax for creating and average is `'mean(column_name)'`

</codeblock>
</exercise>

<!--
**Question 1**

How many example did the model of this matrix correctly label as "Guard"?

<choice id="1">

<opt text="19">

This is the number of example the model correctly predicted as **Forward**.

</opt>

<opt text= "3">
 
This is the number of examples the model predicted **Guard** when the true label was **Forward**.

</opt>

<opt text="4">

This is the number of examples the model predicted **Forward** when the true label was **Guard**.

</opt>

<opt text="26"  correct="true">

Nice!

</opt>

</choice>


**Question 2**

If **Forward** is the positve label, how many ***false positive*** values?

<choice id="2" >

<opt text="19">

This is the number of example true positives. 

</opt>

<opt text= "3">
 
This is the number of false negatives! 

</opt>

<opt text="4"  correct="true">

Great! This is the number of examples the model predicted **Forward** (positive) when the true label was **Guard** (negative) .

</opt>

<opt text="26" >

This the the number of true negatives. 

</opt>

</choice>


</exercise>


<exercise id="3" title="Question Title Here">

Running a coding exercise for the first time could take a bit of time for everything to load.  Be patient, it could take a few minutes. 

**When you see `____` in a coding exercise, replace it with what you assume to be the correct code.  Run it and see if you obtain the desired output.  Submit your code to validate if you were correct.**

_**Make sure you remove the hash (`#`) symbol in the coding portions of this question.  We have commented them so that the line won't execute and you can test your code after each step.**_

We've seen our basketball dataset before and predicted using `SVC` with it before but this time we are going to have a look at how well our model does by building a confusion matrix. 

Tasks:   
- Import the plotting confusion matrix library. 
- Build a pipeline naed `pipe_bb` that preprocesses with `preprocessor` and builds an `SVC()` model with default hyperparameters. 
- Fit the pipeline on `X_train` and `y_train`. 
- Next, build a confusion matrix using `plot_confusion_matrix` and calling `pipe_bb` and the **test** set. Pick any colour you like with `cmap`. You can find the colour options <a href=" https://matplotlib.org/3.1.0/tutorials/colors/colormaps.html" target="_blank">here</a>.

<codeblock id="01_03">

- Are you using `.shape` to find the dimensions? 

</codeblock>



**Question 1**       
How many features does the data have?

<choice  id="1">
<opt text="8">

This is not the number of features.

</opt>

<opt text="9" correct="true">

Yes! Good job!

</opt>

<opt text="25">

This is not the number of features.

</opt>

<opt text="10">

We don't include the index or the target as a feature.

</opt>
</choice>



**Question 2**      
 How many examples does the data have?

<choice  id="2">

<opt text="9">

This is the total number of columns, not the number of examples.

</opt>

<opt text="8" >

This is the not the number of examples.

</opt>

<opt text="25" correct="true">

Well done!

</opt>

<opt text="26">
This is not the number of examples.

</opt>
</choice>
</exercise>

-->


<exercise id="6" title="What Did We Just Learn?" type="slides, video">
<slides source="module1/module1_end" shot="0" start="04:5307" end="05:5911">
</slides>
</exercise>
