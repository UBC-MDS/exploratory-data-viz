---
title: 'Module 4: Visualizing distributions and exploratory data analysis'
description:
  'In this module we will be learning about how to visualize two dimensional and categorical distributions of data as well as how to perform exploratory data analysis.'
prev: ../../module3
next: ../../module5
type: chapter
id: 4
---

<exercise id="0" title="Module Learning Outcomes"  type="slides, video">
<slides source="module4/module4_00" shot="0" start="3:5707" end="4:5306"> </slides>
</exercise>

<exercise id="1" title="How to visualize multidimensional and categorical distributions?" type="slides,video">
<slides source="module4/module4_01" shot="1" start="0:003" end="07:12"> </slides>
</exercise>

<exercise id="2" title="True or False: Plotting Multiple Numerical Columns">

**True or False**       
*Using a scatterplot to visualize the relationship between 2 numeric columns will always result in overplotting.*


<choice id="1" >

<opt text="True" >

Sometimes using a scatterplot helps avoid overplotting but in other cases, it can still cause saturated areas and no meaningful insights will be able to be observed.

</opt>


<opt text="False"  correct="true">

You've been paying attention!

</opt>


</choice>

**True or False**       
*Layered histograms are more interpretable than stacked histograms.*

<choice id="2" >

<opt text="True"  >

This isn't always true. In fact, depending on the question you are attempting to answer, layered histograms can do the opposite.

</opt>

<opt text="False" correct="true">

You are on a roll!

</opt>

</choice>

</exercise>


<exercise id="3" title="Which graph is appropriate?">

**Question 1**      
If we are interested in visualizing the relationship between two columns, which plot type is most appropriate?

<choice id="1" >
<opt text="Histogram">

This can be used to visualize a single column's distribution.

</opt>

<opt text="Violin plot" >

This can be used to visualize a single column's distribution.

</opt>

<opt text="density plot" >

This can be used to visualize a single column's distribution.

</opt>


<opt text="Scatterplot." correct="true">

You got it!

</opt>

</choice>


**Question 2**      
Which plot allows us to visualize the relationship between 2 distributions?


<choice id="2" >
<opt text="A heatmap" correct="true">

You've got the right argument but the wrong value being set. 

</opt>

<opt text="<code>stack=None</code>" correct="true">

Nice!

</opt>

<opt text="<code>layered=True</code>">

I think your argument should be called something else.

</opt>


<opt text="<code>stacked=None</code>">

You are extremely close, but no past tense is needed.

</opt>

</choice>


</exercise>


<exercise id="4" title="Graph Analysis">

**Question 1**      

<?xml version="1.0" encoding="utf-8"?>
<svg

<choice id="1" >


</choice>
</exercise>



<exercise id="4" title="Stacked plotting with Penguins">


**Instructions:**    
Be patient when running a coding exercise for the first time, it can take a few minutes. 

**When you see `____` in a coding exercise, replace it with what you assume to be the correct code. Run the code to see if you obtain the desired output
and submit it to validate if you were correct.**


Let's bring back our [penguins](https://www.kaggle.com/parulpandey/palmer-archipelago-antarctica-penguin-data) that we introduced in the previous module. 

<codeblock id="penguins">

</codeblock>


For this question let's create a stacked histogram of the values in the `culmen_depth_mm` column for different penguin species.

***([Culmen](https://allisonhorst.github.io/palmerpenguins/articles/articles/art.html): the upper ridge of a bird's beak)***

Tasks: 

Fill in the blanks in the code below so that the following gets accomplished.

- Use the data source `penguins` to make a **stacked** histogram plot.
- Plot the counts of the `culmen_depth_mm`  and distinguish the penguin `species` using the color channel.
- Make sure to set the `maxbins` argument to something appropriate. 
- Give it an appropriate title. 


<codeblock id="03_04">

- Are you setting `alt.X('culmen_depth_mm', bin=alt.Bin(maxbins=30))`?
- Are you setting a title in `properties()`?

</codeblock>


**Question**      

Which species of penguin tend to have lower culmen depths?

<choice id="1" >
<opt text="Chinstrap">

This species has a lot of overlap with the Adelie species. 

</opt>

<opt text="Gentoo" correct="true">

These penguins tend to have a shorter culmen depth. 

</opt>

<opt text="Adelie" >

This species has a lot of overlap with the Chinstrap species. 

</opt>

</choice>
</exercise>


<exercise id="2" title="How to create repeated plots and perform exploratory data analysis" type="slides,video">
<slides source="module4/module4_02" shot="1" start="0:003" end="07:12"> </slides>
</exercise>

<exercise id="3" title="What Did We Just Learn?" type="slides, video">
<slides source="module4/module4_end" shot="0" start="04:5307" end="05:5911">
</slides>
</exercise>
