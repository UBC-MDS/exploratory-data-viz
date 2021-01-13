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

<exercise id="2" title="True or False: Data Visualization">

**True or False**       
*It is easier for humans to interpret plots than raw numbers.*
<choice id="1" >

<opt text="True"  correct="true">
You got it! We saw in the slides that sometimes humans can pick up more information about the data in plots. 
</opt>


<opt text="False">
Take a look at the slides. Is it easier to notice trends and patterns with the data displayed in tables or in plots?

</opt>


</choice>

**True or False**       
*Statistical summaries are often useful, but it is a good idea to also visualize your data before drawing any conclusions.*

<choice id="2" >
<opt text="True"  correct="true">
You've been paying attention. 
</opt>

<opt text="False">
Summaries are helpful but don't get us a full picture like a visualization can. 
</opt>
</choice>
</exercise>


<exercise id="3" title="How Can We Visualize Data?" type="slides,video">
<slides source="module1/module1_03" shot="1" start="0:003" end="07:12"> </slides>
</exercise>

<exercise id="4" title="Test Your Knowledge: Visualization Libraries">

**Question 1**      
What is another way of describing high-level visualization libraries? 

<choice id="1" >
<opt text="Imperative">

This is low level plotting.

</opt>

<opt text="Declarative" correct="true">

Great!

</opt>

<opt text="immediate">

This isn't quite right. We made this part up!

</opt>


<opt text="Definitive">

This isn't quite right. We made this part up!

</opt>

</choice>


**Question 2**      
What kind of components are combined in declarative plotting to create visualizations?

<choice id="2" >
<opt text="Dictionary Keys">

This is a data structure and not quite a plotting structure.

</opt>

<opt text="Block Components">

Think more language oriented.

</opt>

<opt text="Grammatical Components"  correct="true">

You got it!

</opt>


<opt text="Grouping Components">

I'm note entirely sure what a grouping component is since we made this up!

</opt>

</choice>


</exercise>

<exercise id="5" title="True or False: Visualization Libaries">


**True or False**    
*A low level visualization library focuses on plot construction details.*

<choice id="1" >
<opt text="True"  correct="true">

Great job! 

</opt>

<opt text="False">

Hmmm. It's possible you got mixed up with high level visualization. 

</opt>

</choice>

**True or False**    
*A high level visualization library focuses on data and relationships.*

<choice id="2" >

<opt text="True"  correct="true">

Nice work!

</opt>

<opt text="False">

High level visualization libraries concentrate on the data and the relationships between them. 

</opt>

</choice>
</exercise>


<exercise id="6" title="Your First Plot">

**Instructions:**    
Be patient when running a coding exercise for the first time, it can take a few minutes.. 

**When you see `____` in a coding exercise, replace it with what you assume to be the correct code. Run the code to see if you obtain the desired output
and submit it to validate if you were correct.**


Let's use the same vehicle dataset we saw in the lecture, but visualize the relationship between two different columns.

The data has already been imported for you in this exercise.

Here is what it looks like:

<codeblock id="cars_data">

</codeblock>

Tasks: 

- Fill out the missing fields in the Altair plotin order to create a scatter plot.
- The cars' `Horsepower` should be on the x-axis and their `Weight_in_lbs` on the y-axis.
- Color the points by the `Origin` of the cars.

<codeblock id="01_06">

- Are the column names expressed in quotes, e.g. `y='Horsepower'`?

</codeblock>
</exercise>


<exercise id="7" title="Aggregations, Lines, and Layers" type="slides,video">
<slides source="module1/module1_07" shot="1" start="0:003" end="07:12"></slides>
</exercise>


<exercise id="8" title="Questions on How Plots are Created">

**Question 1**     
When combining plots in Altair, we say that each plot has its own ___.

<choice id="1">

<opt text="Overlay">

Not quite right here. 

</opt>

<opt text="Layer"  correct="true">

That's it!

</opt>

<opt text= "Panel">

This is something else by good try. 

</opt>

</choice>

**Question 2**     
Line plots are often preferable to point plots when visualizing trends over time because...

<choice id="2">
<opt text="The lines make the plot more visually appealing.">
There is more to plots then just being visually appealing. 
</opt>
<opt text= "Line plots are faster to create.">
They both take approximately the same time to create.
</opt>
<opt text="The line makes it easy to see which values are connected in the same group and its slope facilitates our interpretation of the overall trend."  correct="true">
Nailed it!
</opt>
</choice>

</exercise>

<exercise id="9" title="Creating a Line Plot for Change Over Time">


**Instructions:**    
Be patient when running a coding exercise for the first time, it can take a few minutes.. 

**When you see `____` in a coding exercise, replace it with what you assume to be the correct code. Run the code to see if you obtain the desired output
and submit it to validate if you were correct.**

_**Make sure you remove the hash (`#`) symbol in the coding portions of this question.  We have commented them so that the line won't execute and you can test your code after each step.**_

Let's use a line plot to visualize how the price of a few common stocks has changed over time.

Tasks:

- Fill out the missing fields in the code below.
- Import the correct library from `vega_datasets`.
- Before going further take a look at the stock data.
- Create a line plot with the stocks' date on the x-axis and their price on the y-axis.
- You should color the lines by the stock symbol,
so that you can compare the stock development for the different companies.

<codeblock id="01_09a">

- Are you putting the column names in quotes, e.g. `y='price'`?
- Look at the dataframe by typing `stocks.columns` if you are unsure about the exact column names.

</codeblock>


**Question**   
In the chart above, which stock was priced the highest in 2003?

<choice id="1">

<opt text="GOOG">

GOOG wasn't present in 2003.

</opt>

<opt text= "AAPL">

This stock was quite low in 2003.

</opt>

<opt text= "AMZN">

This stock was quite low in 2003.

</opt>

<opt text="IBM"  correct="true">

You got it!

</opt>

</choice>


**Combining a point and line plot**

Let's add points to the line above to indicate each observation along the line.

Tasks:  

- Fill out the missing fields in the code below.
- Assign the line plot to a variable name (of your choice),
and then use this name to combine a line plot and a point plot.

<codeblock id="01_09b">

- Remember that the column names should be in quotes, e.g. `y='price'`.
- Look at the dataframe by typing `stocks.columns` if you are unsure about the exact column names.
- Revisit the slides on how to build upon existing plots when layering.

</codeblock>
</exercise>

<exercise id="10" title="Plotting an Aggregated Value">

**Instructions:**    
Be patient when running a coding exercise for the first time, it can take a few minutes.. 

**When you see `____` in a coding exercise, replace it with what you assume to be the correct code. Run the code to see if you obtain the desired output
and submit it to validate if you were correct.**


Instead of showing the value for each individual stock value,
we could explore the average trend over time
for all five companies.

Tasks:

- Use the code from exercise 9 above as a base.
- Modify the code to plot one line with the average value of all stocks over time,
instead of giving each company its own line.

<codeblock id="01_10">

- Remember that the column names should be in quotes, e.g. `y='price'`.
- Look at the dataframe by typing `stocks.columns` if you are unsure about the exact column names.
- Remember that the string syntax for creating and average is `'mean(column_name)'`

</codeblock>
</exercise>



<exercise id="11" title="What Did We Just Learn?" type="slides, video">
<slides source="module1/module1_end" shot="0" start="04:5307" end="05:5911">
</slides>
</exercise>
