---
title: 'Module 3: Visualizing Distributions'
description:
  'In this module we will be learning about how we can display data distributions'
prev: ../../module2
next: ../../module4
type: chapter
id: 3
---

<exercise id="0" title="Module Learning Outcomes"  type="slides, video">
<slides source="module3/module3_00" shot="0" start="3:5707" end="4:5306"> </slides>
</exercise>

<exercise id="1" title="How To Visualize Data From a Single Column" type="slides,video">
<slides source="module3/module3_01" shot="1" start="0:003" end="07:12"> </slides>
</exercise>


<exercise id="2" title="True or False: Distributions">

**True or False**       
*When we are visualization data from a single column, we are (usually) more interested in the shape/distribution in general, than individual points.*


<choice id="1" >

<opt text="True"  correct="true">

You got it!  

</opt>


<opt text="False">

We are usually interested in the values as a collective.

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


<exercise id="3" title="Multple Choice Questions on Single Column Plots">

**Question 1**      
 Why can rugplots be problematic?

<choice id="1" >
<opt text="They can take a lot time to produce.">

The time it takes to make a plot is more dependent on the amount of data you have!

</opt>

<opt text="They cannot visualize multiple features." >

Rugplots are mostly used to display a single feature.  

</opt>

<opt text="They do not provide enough details for insights." >

The problem might be that they have too much detail. 

</opt>


<opt text="With large quantities of data, They can be very difficult to interpret." correct="true">

You got it!
</opt>

</choice>


**Question 2**      
To make a layered histogram instead of a stacked one, What should replace the `???` in the code below?


```python
hist_plot = alt.Chart(df_source).mark_bar(opacity=0.4).encode(
    alt.X('runtime', bin=alt.Bin(maxbins=30)),
    alt.Y('count()', ???),
    color='genre')
 .facet('country')
 .resolve_scale(y='independent'))
```



<choice id="2" >
<opt text="<code>stack=False</code>">

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

<exercise id="4" title="Plotting Single Columns with Penguins">


**Instructions:**    
Be patient when running a coding exercise for the first time, it can take a few minutes. 

**When you see `____` in a coding exercise, replace it with what you assume to be the correct code. Run the code to see if you obtain the desired output
and submit it to validate if you were correct.**


Let's bring back our [penguins](https://www.kaggle.com/parulpandey/palmer-archipelago-antarctica-penguin-data) that we introduced in the previous module. 


<codeblock id="penguins">

</codeblock>

This time we want to see the shape of the different penguin species 

Tasks: 

- Using a bar plot, visualize the count of penguins for each species in the data. 
- Choose the appropriate rotation, given the axis labels. 
- Sort your bars in an appropriate order. 
- Make sure to give it a title and set the dimensions to a height of 350 and a width of 500.
- Save your plot in an object named `penguin_bar`.

<codeblock id="03_4">

- Are you using `.mark_bar()`?
- Are you assigning the plot to an object named`penguin_bar`?
- Are you specifying `alt.Y('species', sort='x')` on the y-axis?
- Are you specifying `count()` on the x-axis?
- Are you giving the plot a title and proper dimensions using `.properties()`?

</codeblock>

**Question**      

Which species is most occurring in the dataset?

<choice id="1" >
<opt text="Chinstrap">

Are you looking at the right plot?

</opt>

<opt text="Gentoo" >

Maybe try again.

</opt>

<opt text="Adelie" correct="true">

Nice!

</opt>

</choice>

</exercise>




<exercise id="7" title="Visulize distributions with density plots" type="slides,video">
<slides source="module3/module3_02" shot="1" start="0:003" end="07:12"> </slides>
</exercise>







<exercise id="12" title="What Did We Just Learn?" type="slides, video">
<slides source="module3/module3_end" shot="0" start="04:5307" end="05:5911">
</slides>
</exercise>
