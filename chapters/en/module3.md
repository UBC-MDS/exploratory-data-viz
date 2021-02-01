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
- Plot the counts of the `culmen_depth_mm`  and distinguise the penguin `species` using the color channel.
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

This species actually has a lot of over lap with the Adelie species. 

</opt>

<opt text="Gentoo" correct="true">

These penguins tend to have a shorter culmen depth. 

</opt>

<opt text="Adelie" >

This species actually has a lot of over lap with the Chinstrap species. 

</opt>

</choice>
</exercise>



<exercise id="5" title="Layered plotting with Penguins">


**Instructions:**    
Be patient when running a coding exercise for the first time, it can take a few minutes. 

**When you see `____` in a coding exercise, replace it with what you assume to be the correct code. Run the code to see if you obtain the desired output
and submit it to validate if you were correct.**


Using the [penguins](https://www.kaggle.com/parulpandey/palmer-archipelago-antarctica-penguin-data) dataset again, we are going to try create a layered historgram. 


<codeblock id="penguins">

</codeblock>

We want to understand how penguins culmen depth differs over different penguin species. This means we will need to layer the histogram shapes of the `culmen_depth_mm` column. We also want to facet on the `sex` columm to see if this has a effect on the distribution. 

Tasks: 

Fill in the blanks in the code below so that the following gets accomplished.

- Use the data source `penguins` to make a **layered** histogram plot and make sure to give it an appropriate opacity.
- Plot the counts of the `culmen_depth_mm`  and distinguise the penguin `species` using the color channel.
- Make sure to set the `maxbins` argument to something appropriate and any other arguments needed to make a layered plot. 
- Give it an appropriate title and facet by the `sex` column. 
- Make sure to give each faceted plot an independent axis.

<codeblock id="03_05">

- Are you setting `opacity=0.4` in `mark_bar()`?
- Are you setting `alt.X('culmen_depth_mm', bin=alt.Bin(maxbins=30))`?
- Are you specifying `stack=None` in the `alt.Y()` helper function?
- Are you setting a title in `properties()`?
- Are you faceting by `sex` using `.facet('sex')`?
- Are you giving the plots independent axis with `.resolve_scale(y='independent')`?

</codeblock>

**Question**      

For each species of penguin, do the female penguins tend to have less deep culmen?

<choice id="1" >
<opt text=“Yes” correct=“true”>

It appears that the culmen values for the female penguins on a per species level are lower.

</opt>

<opt text=“No”>

Why don’t you compare the bars on a per colour basis?

</opt>

</choice>

</exercise>




<exercise id="6" title="Visulize Distributions with Density Plots" type="slides,video">
<slides source="module3/module3_02" shot="1" start="0:003" end="07:12"> </slides>
</exercise>


<exercise id="7" title="True or False: Distributions">

**True or False**       
*Using the same data, a histogram's shape can change depending on the bin size.*


<choice id="1" >

<opt text="True"  correct="true">

You got it!  

</opt>


<opt text="False">

If we have more bins for a histogram, the shape may differ from a histogram using less bins. 

</opt>


</choice>

**True or False**       
*Using density plots can be misleading for small data sets.*

<choice id="2" >

<opt text="True"  correct="true">

You got it! Since we don't show the number of obervations in the plot, the plots can appear smooth like plots that have many observation which is not the case. 

</opt>

<opt text="False" >

What about plots with small amounts of data?

</opt>

</choice>

</exercise>


<exercise id="8" title="Multiple Choice Questions on Single Column Plots">

**Question 1**      
Another name for a density plot is a ___?

<choice id="1" >
<opt text="Count Estimation Plot (CEP)">

Take a quick look at slide 3 for more information on this. 

</opt>

<opt text="Kernel Density Estimate (KDE)" correct="true">

That's right!

</opt>

<opt text="Kernel Smoothing Plot (KSP)" >

Take a quick look at slide 3 for more information on this.

</opt>


<opt text="Count Smoothing Estimate (CSE)" >

Take a quick look at slide 3 for more information on this.

</opt>

</choice>


**Question 2**      
Unlike other plots using Altair, making a density plot requires 2 steps. The first step involves generating a new column of samples of the estimated densities. Which of the following code is needed to calculated the estimated densities?



<choice id="2" >
<opt text="<code>.transform_density()</code>" correct="true">

Cool!

</opt>

<opt text="<code>.estimate_density()</code>" >

You are right that we use a method for the first step but this is not the right named method. 

</opt>

<opt text="<code>transform_density=True</code>">

Using an argument is not the right type of coding needed. 

</opt>


<opt text="<code>estimate_density=True</code>">

Using an argument is not the right type of coding needed. 

</opt>

</choice>


</exercise>

<exercise id="9" title="Application: Make Your Own Density Plot">


**Instructions:**    
Be patient when running a coding exercise for the first time, it can take a few minutes. 

**When you see `____` in a coding exercise, replace it with what you assume to be the correct code. Run the code to see if you obtain the desired output
and submit it to validate if you were correct.**


Bringing back our trusty [penguins](https://www.kaggle.com/parulpandey/palmer-archipelago-antarctica-penguin-data) data, we are going to try to make a density plot that will provide insights into the distribution of penguins mass among the different islands. 


<codeblock id="penguins">

</codeblock>

Create a density plot for the `body_mass_g` column for penguins located on different islands.

Tasks: 

Fill in the blanks in the code below so that the following gets accomplished.

- Use the data source `penguins` to make the plot.
- Calculate the KDE of the `body_mass_g` column and make sure to split it up by the categorical column `island`. When you create your new variable for the calculation make sure to name it `density`. 
- Set the step size to 100. 
- Give the area plot an appropriate opacity.
- Map the `body_mass_g` and the `density` column that was made to the x and y axis and making sure to specify that `density` is a quantitative variable. 
- Map the island to the colour (color) channel. 
- Make sure to give your plot a title.

<codeblock id="03_09a">

- Are you setting `groupby=['island']` and `as_=['body_mass_g', 'density']` in `transform_density()`?
- Are you setting `steps=100`?
- Are you setting `opacity=0.5` in `mark_bar()`?
- Are you specifying `x='body_mass_g'` or `alt.X('body_mass_g')`?
- Are you specifying `y='density:Q'` or `alt.Y('density:Q')`?
- Are you specifying `color='island'` or `alt.Color('island')`?
- Are you setting a title in `properties()`?

</codeblock>

**Question**      

Which island tend to have penguins with a higher body mass?

<choice id="1" >
<opt text="Biscoe" correct="true">

This island appears to have penguins with a heavier mass. 

</opt>

<opt text="Dream">

This island doesn't have any penguins with a body mass greater than 5000 g. 

</opt>

<opt text="Torgersen" >

This island doesn't have any penguins with a body mass greater than 5000 g.

</opt>

</choice>


Now let's facet based on species and see if that gives us some more insight. 


Create a density plot for the `body_mass_g` column for penguins located on different islands but this time facet for species 

Tasks: 

- Use the data source `penguins` to make the plot and assign it to an object named `mass_faceted_plot`.
- Calculate the KDE of the `body_mass_g` column and make sure to split it up by the categorical column `island` and penguin `species`. When you create your new variable for the calculation make sure to name it `density`. 
- Set the step size to 100. 
- Give the area plot an appropriate opacity.
- Map the `body_mass_g` and the `density` column that was made to the x and y axis and making sure to specify that `density` is a quantitative variable. 
- Map the island to the colour (color) channel. 
- Make sure to give your plot a title and set the width of the plot to 150.
- Facet the plot by the penguin `species`. 

<codeblock id="03_09b">

- Are you setting `groupby=['island','species']` and `as_=['body_mass_g', 'density']` in `transform_density()`?
- Are you setting `steps=100`?
- Are you setting `opacity=0.5` in `mark_bar()`?
- Are you specifying `x='body_mass_g'` or `alt.X('body_mass_g')`?
- Are you specifying `y='density:Q'` or `alt.Y('density:Q')`?
- Are you specifying `color='island'` or `alt.Color('island')`?
- Are you setting a title in `properties()`?
- Are you faceting with `.facet('species')`?

</codeblock>



**Question**      

Based on the plot we just made, what did we learn?

<choice id="1" >
<opt text="The Chinstrap species of penguin is available on Dream and Torgersen island.">

Chinstrap species of penguin is only on Dream island.

</opt>


<opt text="The Gentoo penguin species appears to have higher body mass compared to other species."  correct="true">

This species only inhabits on Gentoo island and appears to have a heavier body mass distribution.

</opt>


<opt text="Dream island tend to have penguins with a higher body mass compared to the other islands." >

Dream island inhabits penguins of only the Chinstrap species and this body mass distribution appears similar to the Adelie species.

</opt>

</choice>

</exercise>



<exercise id="12" title="What Did We Just Learn?" type="slides, video">
<slides source="module3/module3_end" shot="0" start="04:5307" end="05:5911">
</slides>
</exercise>
