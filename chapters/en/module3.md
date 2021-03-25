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
<slides source="module3/module3_00" shot="0" start="6:48" end="7:30"> </slides>
</exercise>

<exercise id="1" title="How To Visualize Data From a Single Column" type="slides,video">
<slides source="module3/module3_01" shot="1" start="100:5401" end="109:1017"> </slides>
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
This is a rugplot: 

<center>
<img src="/module3/rugplot.svg" width="60%"></img>
</center>

Why can they be problematic?

<choice id="1" >
<opt text="They can take a lot time to produce.">

The time it takes to make a plot is more dependent on the amount of data you have!

</opt>

<opt text="They visualize too many features at a time." >

Rugplots are mostly used to display a single feature.  

</opt>

<opt text="They do not provide enough details for insights." >

The problem might be that they have too much detail. 

</opt>


<opt text="With large quantities of data, they can be very difficult to interpret." correct="true">

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

The culmen, also sometimes referred to as the bill, is the [upper ridge of a bird's beak](https://allisonhorst.github.io/palmerpenguins/articles/articles/art.html). 
Below, we've included a diagram made by [Allison Horst](https://twitter.com/allison_horst) which should help give you a bit of an idea of what these values are measuring. 

<center>
<img src="/module3/penguin_culmen.jpg" width="60%"></img>
</center>

The culmen measurements can useful for predicting the sex between penguin species, however, it may be interesting to see if it's indicative of species as well!


For this question let's create a stacked histogram of the values in the `culmen_depth_mm` column for different penguin species and determine if there is any type of relationship between the culmen depth and the species of penguin. 


Tasks: 

Fill in the blanks in the code below so that the following gets accomplished.

- Use the data source `penguins` to make a **stacked** histogram plot.
- Plot the counts of the `culmen_depth_mm`  and distinguish the penguin `species` using the colour channel.
- Make sure to set the `maxbins` argument to something appropriate. 
- Give it an appropriate title. 


<codeblock id="03_04">

- Are you setting `alt.X('culmen_depth_mm', bin=alt.Bin(maxbins=30))`?
- Are you setting a title in `properties()`?

</codeblock>


**Question**      

Which species of penguin tend to have more shallow culmen?

<choice id="1" >
<opt text="Chinstrap">

This species actually has a lot of overlap with the Adelie species. 

</opt>

<opt text="Gentoo" correct="true">

These penguins tend to have a shorter culmen depth. 

</opt>

<opt text="Adelie" >

This species actually has a lot of overlap with the Chinstrap species. 

</opt>

</choice>
</exercise>



<exercise id="5" title="Layered plotting with Penguins">


**Instructions:**    
Be patient when running a coding exercise for the first time, it can take a few minutes. 

**When you see `____` in a coding exercise, replace it with what you assume to be the correct code. Run the code to see if you obtain the desired output
and submit it to validate if you were correct.**


Using the [penguins](https://www.kaggle.com/parulpandey/palmer-archipelago-antarctica-penguin-data) dataset again, we are going to try to create a layered histogram. 


<codeblock id="penguins">

</codeblock>

We want to understand how penguins' culmen depth differs over different penguin species. This means we will need to layer the histogram shapes of the `culmen_depth_mm` column. We also want to facet on the `sex` column to see if this affects the distribution. 

Tasks: 

Fill in the blanks in the code below so that the following gets accomplished.

- Use the data source `penguins_df` to make a **layered** histogram plot named `culmen_layered_plot` and make sure to give it an appropriate opacity.
- Plot the counts of the `culmen_depth_mm`  and distinguish the penguin `species` using the colour channel.
- Make sure to set the `maxbins` argument to something appropriate and any other arguments needed to make a layered plot. 
- Give it an appropriate title and facet by the `sex` column making sure that there is only 1 column so the graphs are stacked vertically. 
- Make sure to give each faceted plot an independent axis.

<codeblock id="03_05">

- Are you setting `opacity=0.5` in `mark_bar()`?
- Are you setting `alt.X('culmen_depth_mm', bin=alt.Bin(maxbins=30))`?
- Are you specifying `stack=None` in the `alt.Y()` helper function?
- Are you setting a title in `properties()`?
- Are you faceting by `sex` using `.facet('sex', columns=1)`?
- Are you giving the plots independent axis with `.resolve_scale(y='independent')`?

</codeblock>

**Question**      

For each species of penguin, do the female penguins tend to have less deep culmen?

<choice id="1" >
<opt text='Yes' correct=“true”>

It appears that the culmen values for the female penguins on a per species level are lower.

</opt>

<opt text='No'>

Why don’t you compare the bars on a per colour basis?

</opt>

</choice>

</exercise>




<exercise id="6" title="Visulize Distributions with Density Plots" type="slides,video">
<slides source="module3/module3_06" shot="1" start="109:1900" end="120:5922"> </slides>
</exercise>


<exercise id="7" title="True or False: Distributions">

**True or False**       
*Using the same data, a histogram's shape can change depending on the bin size.*


<choice id="1" >

<opt text="True"  correct="true">

You got it!  

</opt>


<opt text="False">

If we have more bins for a histogram, the shape may differ from a histogram using fewer bins. 

</opt>


</choice>

**True or False**       
*Using density plots can be misleading for small data sets.*

<choice id="2" >

<opt text="True"  correct="true">

You got it! Since we don't show the number of observations in the plot, the plots can appear smooth like plots that have many observations which is not the case. 

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
Unlike other plots using Altair, making a density plot requires 2 steps. The first step involves generating a new column of samples of the estimated densities. Which of the following code is needed to calculate the estimated densities?



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

- Use the data source `penguins_df` to make a plot assigned to an object named `mass_density_plot`.
- Calculate the KDE of the `body_mass_g` column and make sure to split it up by the categorical column `island`. When you create your new values for the calculation make sure to name them `density`.
- Set the step size to 100.
- Give the area plot an appropriate opacity.
- Map `body_mass_g` and `density` to the x and y-axis and make sure to specify that `density` consists of quantitative values. 
- Map the island to the colour (colour) channel. 
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

Which island tends to have penguins with higher body masses?

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

- Use the data source `penguins_df` to make the plot and assign it to an object named `mass_faceted_plot`.
- Calculate the KDE of the `body_mass_g` column and make sure to split it up by the categorical column `island` and penguin `species`. When you create your new values for the calculation make sure to name them `density`. 
- Set the step size to 100. 
- Give the area plot an appropriate opacity.
- Map `body_mass_g` and `density` to the x and y-axis and make sure to specify that `density` consists of quantitative values.
- Map the island to the colour (colour) channel. 
- Make sure to give your plot a title and set the width of the plot to 200 and height to 100.
- Facet the plot by the penguin `species` and display them all in a single column. 

<codeblock id="03_09b">

- Are you setting `groupby=['island','species']` and `as_=['body_mass_g', 'density']` in `transform_density()`?
- Are you setting `steps=100`?
- Are you setting `opacity=0.5` in `mark_bar()`?
- Are you specifying `x='body_mass_g'` or `alt.X('body_mass_g')`?
- Are you specifying `y='density:Q'` or `alt.Y('density:Q')`?
- Are you specifying `color='island'` or `alt.Color('island')`?
- Are you setting a title, height and width in `properties()`?
- Are you faceting with `.facet('species', columns=1)`?

</codeblock>



**Question**      

Based on the plot we just made, what did we learn?

<choice id="2" >
<opt text="The Chinstrap species of penguin is available on Dream and Torgersen island.">

The Chinstrap penguin species is only on Dream island.

</opt>


<opt text="The Gentoo penguin species appears to have higher body mass compared to other species."  correct="true">

This species only inhabits Gentoo island and appears to have a heavier body mass distribution.

</opt>


<opt text="Dream island tend to have penguins with a higher body mass compared to the other islands." >

Dream island inhabits penguins of only the Chinstrap species and this body mass distribution appears similar to the Adelie species.

</opt>

</choice>

</exercise>

<exercise id="10" title="Comparing Multiple Distributions" type="slides,video">
<slides source="module3/module3_10" shot="1" start="121:0900" end="135:1904"> </slides>
</exercise>


<exercise id="11" title="True or False: Many Distributions">

**True or False**       
*Using a bar plot to display a statistic like the mean, is an effective way to compare quantitative dataframe columns.*

<choice id="1" >

<opt text="True"  >

This hinders us from seeing any variation in the data and can be problematic and cause us to draw incorrect conclusions. 

</opt>


<opt text="False" correct="true">

Nice! 

</opt>


</choice>

**True or False**       
*We can sort boxplots by their median value within an Altair plot by specifying sort='median'.*

<choice id="2" >

<opt text="True"  >

We have to first use `pandas` to sort the categorical dataframe column's mean values outside of the `alt.Chart()`.

</opt>

<opt text="False" correct="true">

Great! You remembered that we must do this first before making the plot! 

</opt>

</choice>

</exercise>


<exercise id="12" title="Why and How to Compare Multiple Distributions">

**Question 1**      
When comparing the value counts of certain dataframe columns, why can it be extremely difficult to obtain meaningful insights from density plots such as the one below?


<?xml version="1.0" encoding="utf-8"?>


<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" version="1.1" class="marks" width="698" height="342" viewBox="0 0 698 342"><rect width="698" height="342" fill="white"/><g fill="none" stroke-miterlimit="10" transform="translate(107,5)"><g class="mark-group role-frame root" role="graphics-object" aria-roledescription="group mark container"><g transform="translate(0,0)"><path class="background" aria-hidden="true" d="M0.5,0.5h400v300h-400Z" stroke="#ddd"/><g><g class="mark-group role-axis" aria-hidden="true"><g transform="translate(0.5,300.5)"><path class="background" aria-hidden="true" d="M0,0h0v0h0Z" pointer-events="none"/><g><g class="mark-rule role-axis-grid" pointer-events="none"><line transform="translate(0,-300)" x2="0" y2="300" stroke="#ddd" stroke-width="1" opacity="1"/><line transform="translate(29,-300)" x2="0" y2="300" stroke="#ddd" stroke-width="1" opacity="1"/><line transform="translate(57,-300)" x2="0" y2="300" stroke="#ddd" stroke-width="1" opacity="1"/><line transform="translate(86,-300)" x2="0" y2="300" stroke="#ddd" stroke-width="1" opacity="1"/><line transform="translate(114,-300)" x2="0" y2="300" stroke="#ddd" stroke-width="1" opacity="1"/><line transform="translate(143,-300)" x2="0" y2="300" stroke="#ddd" stroke-width="1" opacity="1"/><line transform="translate(171,-300)" x2="0" y2="300" stroke="#ddd" stroke-width="1" opacity="1"/><line transform="translate(200,-300)" x2="0" y2="300" stroke="#ddd" stroke-width="1" opacity="1"/><line transform="translate(229,-300)" x2="0" y2="300" stroke="#ddd" stroke-width="1" opacity="1"/><line transform="translate(257,-300)" x2="0" y2="300" stroke="#ddd" stroke-width="1" opacity="1"/><line transform="translate(286,-300)" x2="0" y2="300" stroke="#ddd" stroke-width="1" opacity="1"/><line transform="translate(314,-300)" x2="0" y2="300" stroke="#ddd" stroke-width="1" opacity="1"/><line transform="translate(343,-300)" x2="0" y2="300" stroke="#ddd" stroke-width="1" opacity="1"/><line transform="translate(371,-300)" x2="0" y2="300" stroke="#ddd" stroke-width="1" opacity="1"/><line transform="translate(400,-300)" x2="0" y2="300" stroke="#ddd" stroke-width="1" opacity="1"/></g></g><path class="foreground" aria-hidden="true" d="" pointer-events="none" display="none"/></g></g><g class="mark-group role-axis" aria-hidden="true"><g transform="translate(0.5,0.5)"><path class="background" aria-hidden="true" d="M0,0h0v0h0Z" pointer-events="none"/><g><g class="mark-rule role-axis-grid" pointer-events="none"><line transform="translate(0,300)" x2="400" y2="0" stroke="#ddd" stroke-width="1" opacity="1"/><line transform="translate(0,250)" x2="400" y2="0" stroke="#ddd" stroke-width="1" opacity="1"/><line transform="translate(0,200)" x2="400" y2="0" stroke="#ddd" stroke-width="1" opacity="1"/><line transform="translate(0,150)" x2="400" y2="0" stroke="#ddd" stroke-width="1" opacity="1"/><line transform="translate(0,100)" x2="400" y2="0" stroke="#ddd" stroke-width="1" opacity="1"/><line transform="translate(0,50)" x2="400" y2="0" stroke="#ddd" stroke-width="1" opacity="1"/></g></g><path class="foreground" aria-hidden="true" d="" pointer-events="none" display="none"/></g></g><g class="mark-group role-axis" role="graphics-symbol" aria-roledescription="axis" aria-label="X-axis titled 'Worldwide Gross' for a linear scale with values from 0 to 2,800,000,000"><g transform="translate(0.5,300.5)"><path class="background" aria-hidden="true" d="M0,0h0v0h0Z" pointer-events="none"/><g><g class="mark-rule role-axis-tick" pointer-events="none"><line transform="translate(0,0)" x2="0" y2="5" stroke="#888" stroke-width="1" opacity="1"/><line transform="translate(29,0)" x2="0" y2="5" stroke="#888" stroke-width="1" opacity="1"/><line transform="translate(57,0)" x2="0" y2="5" stroke="#888" stroke-width="1" opacity="1"/><line transform="translate(86,0)" x2="0" y2="5" stroke="#888" stroke-width="1" opacity="1"/><line transform="translate(114,0)" x2="0" y2="5" stroke="#888" stroke-width="1" opacity="1"/><line transform="translate(143,0)" x2="0" y2="5" stroke="#888" stroke-width="1" opacity="1"/><line transform="translate(171,0)" x2="0" y2="5" stroke="#888" stroke-width="1" opacity="1"/><line transform="translate(200,0)" x2="0" y2="5" stroke="#888" stroke-width="1" opacity="1"/><line transform="translate(229,0)" x2="0" y2="5" stroke="#888" stroke-width="1" opacity="1"/><line transform="translate(257,0)" x2="0" y2="5" stroke="#888" stroke-width="1" opacity="1"/><line transform="translate(286,0)" x2="0" y2="5" stroke="#888" stroke-width="1" opacity="1"/><line transform="translate(314,0)" x2="0" y2="5" stroke="#888" stroke-width="1" opacity="1"/><line transform="translate(343,0)" x2="0" y2="5" stroke="#888" stroke-width="1" opacity="1"/><line transform="translate(371,0)" x2="0" y2="5" stroke="#888" stroke-width="1" opacity="1"/><line transform="translate(400,0)" x2="0" y2="5" stroke="#888" stroke-width="1" opacity="1"/></g><g class="mark-text role-axis-label" pointer-events="none"><text text-anchor="start" transform="translate(0,15)" font-family="sans-serif" font-size="10px" fill="#000" opacity="1">0</text><text text-anchor="middle" transform="translate(28.57142857142857,15)" font-family="sans-serif" font-size="10px" fill="#000" opacity="0">200,000,000</text><text text-anchor="middle" transform="translate(57.14285714285714,15)" font-family="sans-serif" font-size="10px" fill="#000" opacity="0">400,000,000</text><text text-anchor="middle" transform="translate(85.71428571428571,15)" font-family="sans-serif" font-size="10px" fill="#000" opacity="0">600,000,000</text><text text-anchor="middle" transform="translate(114.28571428571428,15)" font-family="sans-serif" font-size="10px" fill="#000" opacity="1">800,000,000</text><text text-anchor="middle" transform="translate(142.85714285714286,15)" font-family="sans-serif" font-size="10px" fill="#000" opacity="0">1,000,000,000</text><text text-anchor="middle" transform="translate(171.42857142857142,15)" font-family="sans-serif" font-size="10px" fill="#000" opacity="0">1,200,000,000</text><text text-anchor="middle" transform="translate(200,15)" font-family="sans-serif" font-size="10px" fill="#000" opacity="0">1,400,000,000</text><text text-anchor="middle" transform="translate(228.57142857142856,15)" font-family="sans-serif" font-size="10px" fill="#000" opacity="1">1,600,000,000</text><text text-anchor="middle" transform="translate(257.14285714285717,15)" font-family="sans-serif" font-size="10px" fill="#000" opacity="0">1,800,000,000</text><text text-anchor="middle" transform="translate(285.7142857142857,15)" font-family="sans-serif" font-size="10px" fill="#000" opacity="0">2,000,000,000</text><text text-anchor="middle" transform="translate(314.2857142857143,15)" font-family="sans-serif" font-size="10px" fill="#000" opacity="0">2,200,000,000</text><text text-anchor="middle" transform="translate(342.85714285714283,15)" font-family="sans-serif" font-size="10px" fill="#000" opacity="1">2,400,000,000</text><text text-anchor="middle" transform="translate(371.42857142857144,15)" font-family="sans-serif" font-size="10px" fill="#000" opacity="0">2,600,000,000</text><text text-anchor="end" transform="translate(400,15)" font-family="sans-serif" font-size="10px" fill="#000" opacity="0">2,800,000,000</text></g><g class="mark-rule role-axis-domain" pointer-events="none"><line transform="translate(0,0)" x2="400" y2="0" stroke="#888" stroke-width="1" opacity="1"/></g><g class="mark-text role-axis-title" pointer-events="none"><text text-anchor="middle" transform="translate(200,30)" font-family="sans-serif" font-size="11px" font-weight="bold" fill="#000" opacity="1">Worldwide
Gross</text></g></g><path class="foreground" aria-hidden="true" d="" pointer-events="none" display="none"/></g></g><g class="mark-group role-axis" role="graphics-symbol" aria-roledescription="axis" aria-label="Y-axis titled 'density' for a linear scale with values from 0.00000000 to 0.00000006"><g transform="translate(0.5,0.5)"><path class="background" aria-hidden="true" d="M0,0h0v0h0Z" pointer-events="none"/><g><g class="mark-rule role-axis-tick" pointer-events="none"><line transform="translate(0,300)" x2="-5" y2="0" stroke="#888" stroke-width="1" opacity="1"/><line transform="translate(0,250)" x2="-5" y2="0" stroke="#888" stroke-width="1" opacity="1"/><line transform="translate(0,200)" x2="-5" y2="0" stroke="#888" stroke-width="1" opacity="1"/><line transform="translate(0,150)" x2="-5" y2="0" stroke="#888" stroke-width="1" opacity="1"/><line transform="translate(0,100)" x2="-5" y2="0" stroke="#888" stroke-width="1" opacity="1"/><line transform="translate(0,50)" x2="-5" y2="0" stroke="#888" stroke-width="1" opacity="1"/></g><g class="mark-text role-axis-label" pointer-events="none"><text text-anchor="end" transform="translate(-7,303)" font-family="sans-serif" font-size="10px" fill="#000" opacity="1">0.00000000</text><text text-anchor="end" transform="translate(-7,252.99999999999997)" font-family="sans-serif" font-size="10px" fill="#000" opacity="1">0.00000001</text><text text-anchor="end" transform="translate(-7,203)" font-family="sans-serif" font-size="10px" fill="#000" opacity="1">0.00000002</text><text text-anchor="end" transform="translate(-7,153)" font-family="sans-serif" font-size="10px" fill="#000" opacity="1">0.00000003</text><text text-anchor="end" transform="translate(-7,102.99999999999997)" font-family="sans-serif" font-size="10px" fill="#000" opacity="1">0.00000004</text><text text-anchor="end" transform="translate(-7,52.999999999999986)" font-family="sans-serif" font-size="10px" fill="#000" opacity="1">0.00000005</text></g><g class="mark-rule role-axis-domain" pointer-events="none"><line transform="translate(0,300)" x2="0" y2="-300" stroke="#888" stroke-width="1" opacity="1"/></g><g class="mark-text role-axis-title" pointer-events="none"><text text-anchor="middle" transform="translate(-91,150) rotate(-90) translate(0,-2)" font-family="sans-serif" font-size="11px" font-weight="bold" fill="#000" opacity="1">density</text></g></g><path class="foreground" aria-hidden="true" d="" pointer-events="none" display="none"/></g></g><g class="mark-group role-scope pathgroup" role="graphics-object" aria-roledescription="group mark container"><g transform="translate(0,0)"><path class="background" aria-hidden="true" d="M0,0h400v300h-400Z"/><g><g class="mark-area role-mark marks" role="graphics-object" aria-roledescription="area mark container"><path aria-label="Major Genre: Drama; Worldwide Gross: 0; density: 1.44424720047e-8" role="graphics-symbol" aria-roledescription="area mark" d="M0,227.78763997655835L4.5309174514285715,260.5435171237179L9.061834902857143,281.62660249010924L13.592752354285711,290.92105336081L18.123669805714286,293.6775016427389L22.654587257142857,296.23806738826926L27.185504708571422,297.9418533945787L31.716422160000008,297.5390291148264L36.24733961142857,298.6201853864766L40.77825706285714,299.3653273939833L45.309174514285715,298.8111042263535L49.84009196571429,299.2853816706925L54.371009417142844,299.63689836851955L58.90192686857143,299.7793933873255L63.432844320000015,299.92144350803585L67.96376177142857,299.8094912328355L72.49467922285714,299.8325724583856L77.02559667428572,299.9603750296905L81.55651412571429,299.9995176376596L86.08743157714285,299.8424280446291L90.61834902857143,299.9652788421899L95.14926648000001,299.84922502557475L99.68018393142857,299.58470017735266L104.21110138285717,299.9839037082034L108.74201883428569,299.99444989899456L113.27293628571428,299.7843360491982L113.27293628571428,300L108.74201883428569,300L104.21110138285717,300L99.68018393142857,300L95.14926648000001,300L90.61834902857143,300L86.08743157714285,300L81.55651412571429,300L77.02559667428572,300L72.49467922285714,300L67.96376177142857,300L63.432844320000015,300L58.90192686857143,300L54.371009417142844,300L49.84009196571429,300L45.309174514285715,300L40.77825706285714,300L36.24733961142857,300L31.716422160000008,300L27.185504708571422,300L22.654587257142857,300L18.123669805714286,300L13.592752354285711,300L9.061834902857143,300L4.5309174514285715,300L0,300Z" fill="#b279a2"/></g></g><path class="foreground" aria-hidden="true" d="" display="none"/></g><g transform="translate(0,0)"><path class="background" aria-hidden="true" d="M0,0h400v300h-400Z"/><g><g class="mark-area role-mark marks" role="graphics-object" aria-roledescription="area mark container"><path aria-label="Major Genre: Comedy; Worldwide Gross: 0; density: 8.52802226222e-9" role="graphics-symbol" aria-roledescription="area mark" d="M0,257.35988868891604L3.545688182857143,251.0040046902376L7.091376365714286,271.18843062613087L10.637064548571429,283.46497304578224L14.182752731428572,289.39359588007784L17.728440914285713,292.9477420146153L21.274129097142858,293.25704947149427L24.819817280000002,292.6969793063541L28.365505462857143,295.1691500129199L31.91119364571428,297.33572233348417L35.456881828571426,297.9538253116325L39.00257001142857,297.7182807662953L42.548258194285715,297.59978101374304L46.09394637714285,298.50721815405865L49.639634560000005,298.7464796703493L53.185322742857146,299.3716550403724L56.73101092571429,299.6078073024964L60.27669910857144,299.3869963313005L63.82238729142856,299.2600562224332L67.36807547428572,299.00023774819795L70.91376365714285,299.17141402520036L74.45945184,299.3649031871381L78.00514002285713,299.67707249657303L81.5508282057143,299.7618696234897L85.09651638857143,299.6929981582983L88.64220457142858,299.7454513023682L88.64220457142858,300L85.09651638857143,300L81.5508282057143,300L78.00514002285713,300L74.45945184,300L70.91376365714285,300L67.36807547428572,300L63.82238729142856,300L60.27669910857144,300L56.73101092571429,300L53.185322742857146,300L49.639634560000005,300L46.09394637714285,300L42.548258194285715,300L39.00257001142857,300L35.456881828571426,300L31.91119364571428,300L28.365505462857143,300L24.819817280000002,300L21.274129097142858,300L17.728440914285713,300L14.182752731428572,300L10.637064548571429,300L7.091376365714286,300L3.545688182857143,300L0,300Z" fill="#72b7b2"/></g></g><path class="foreground" aria-hidden="true" d="" display="none"/></g><g transform="translate(0,0)"><path class="background" aria-hidden="true" d="M0,0h400v300h-400Z"/><g><g class="mark-area role-mark marks" role="graphics-object" aria-roledescription="area mark container"><path aria-label="Major Genre: Musical; Worldwide Gross: 0; density: 6.06143341112e-9" role="graphics-symbol" aria-roledescription="area mark" d="M0,269.6928329443893L2.305582462857143,265.89786802245163L4.611164925714286,266.9840974395593L6.916747388571428,271.74742391367965L9.222329851428572,277.90216401408463L11.527912314285715,283.5638178835023L13.833494777142857,287.76613020706554L16.139077240000002,290.2453656909139L18.444659702857145,291.2413891205432L20.750242165714287,291.40497762008965L23.05582462857143,291.51001349651386L25.36140709142857,292.05541324741404L27.666989554285713,293.10240552828805L29.972572017142856,294.3998887046243L32.278154480000005,295.59943592855103L34.58373694285714,296.4416085539748L36.88931940571429,296.8764163932298L39.194901868571435,297.0657202588026L41.500484331428574,297.26238439021495L43.80606679428571,297.6408145712951L46.11164925714286,298.18378528871744L48.41723171999999,298.7072932813438L50.72281418285714,299.01212966042976L53.028396645714295,299.04311110642084L55.33397910857143,298.9296410012533L57.63956157142858,298.87888874589345L57.63956157142858,300L55.33397910857143,300L53.028396645714295,300L50.72281418285714,300L48.41723171999999,300L46.11164925714286,300L43.80606679428571,300L41.500484331428574,300L39.194901868571435,300L36.88931940571429,300L34.58373694285714,300L32.278154480000005,300L29.972572017142856,300L27.666989554285713,300L25.36140709142857,300L23.05582462857143,300L20.750242165714287,300L18.444659702857145,300L16.139077240000002,300L13.833494777142857,300L11.527912314285715,300L9.222329851428572,300L6.916747388571428,300L4.611164925714286,300L2.305582462857143,300L0,300Z" fill="#9d755d"/></g></g><path class="foreground" aria-hidden="true" d="" display="none"/></g><g transform="translate(0,0)"><path class="background" aria-hidden="true" d="M0,0h400v300h-400Z"/><g><g class="mark-area role-mark marks" role="graphics-object" aria-roledescription="area mark container"><path aria-label="Major Genre: Thriller/Suspense; Worldwide Gross: 0; density: 7.32819297617e-9" role="graphics-symbol" aria-roledescription="area mark" d="M0,263.35903511915495L10.530742600000002,278.70949084360245L21.061485200000003,294.60026288038654L31.5922278,296.5956132480385L42.12297040000001,298.3140776726223L52.653713,299.4438843096835L63.1844556,299.8417208691465L73.7151982,299.854958580544L84.24594080000001,299.99980247312976L94.7766834,299.644243968835L105.307426,299.45632825966305L115.8381686,299.9726650675178L126.3689112,299.999999990627L136.8996538,300L147.4303964,300L157.961139,300L168.49188160000003,300L179.02262420000002,300L189.5533668,300L200.08410940000002,300L210.614852,300L221.1455946,300L231.6763372,300L242.2070798,299.9999999999845L252.7378224,299.9990169452095L263.268565,299.60818930857033L263.268565,300L252.7378224,300L242.2070798,300L231.6763372,300L221.1455946,300L210.614852,300L200.08410940000002,300L189.5533668,300L179.02262420000002,300L168.49188160000003,300L157.961139,300L147.4303964,300L136.8996538,300L126.3689112,300L115.8381686,300L105.307426,300L94.7766834,300L84.24594080000001,300L73.7151982,300L63.1844556,300L52.653713,300L42.12297040000001,300L31.5922278,300L21.061485200000003,300L10.530742600000002,300L0,300Z" fill="#4c78a8"/></g></g><path class="foreground" aria-hidden="true" d="" display="none"/></g><g transform="translate(0,0)"><path class="background" aria-hidden="true" d="M0,0h400v300h-400Z"/><g><g class="mark-area role-mark marks" role="graphics-object" aria-roledescription="area mark container"><path aria-label="Major Genre: Adventure; Worldwide Gross: 0; density: 2.02187847231e-9" role="graphics-symbol" aria-roledescription="area mark" d="M0,289.8906076384335L6.474441857142857,287.4975933196307L12.948883714285714,287.48138252419983L19.42332557142857,289.27331543831014L25.897767428571427,291.5360719253615L32.372209285714284,293.33967742431884L38.84665114285714,294.49386651335465L45.321093000000005,295.25675399087146L51.795534857142854,295.9684475924111L58.26997671428571,296.77538269764517L64.74441857142857,297.5497716893814L71.21886042857143,298.1065600767519L77.69330228571428,298.43902350754087L84.16774414285715,298.65986274151453L90.64218600000001,298.8188008782915L97.11662785714286,298.8710425827516L103.59106971428571,298.77553908911057L110.06551157142856,298.5794482497719L116.53995342857142,298.39930095457885L123.0143952857143,298.33807310746624L129.48883714285714,298.4433701561111L135.963279,298.69839575409L142.43772085714286,299.02041702035956L148.9121627142857,299.31537664927583L155.38660457142856,299.54452279294173L161.86104642857143,299.71664603669086L161.86104642857143,300L155.38660457142856,300L148.9121627142857,300L142.43772085714286,300L135.963279,300L129.48883714285714,300L123.0143952857143,300L116.53995342857142,300L110.06551157142856,300L103.59106971428571,300L97.11662785714286,300L90.64218600000001,300L84.16774414285715,300L77.69330228571428,300L71.21886042857143,300L64.74441857142857,300L58.26997671428571,300L51.795534857142854,300L45.321093000000005,300L38.84665114285714,300L32.372209285714284,300L25.897767428571427,300L19.42332557142857,300L12.948883714285714,300L6.474441857142857,300L0,300Z" fill="#f58518"/></g></g><path class="foreground" aria-hidden="true" d="" display="none"/></g><g transform="translate(0,0)"><path class="background" aria-hidden="true" d="M0,0h400v300h-400Z"/><g><g class="mark-area role-mark marks" role="graphics-object" aria-roledescription="area mark container"><path aria-label="Major Genre: Action; Worldwide Gross: 0; density: 3.7716362804e-9" role="graphics-symbol" aria-roledescription="area mark" d="M0,281.14181859797947L15.816522851428571,286.3630539505048L31.633045702857142,294.21031536935493L47.44956855428571,296.32277091386294L63.266091405714285,297.9024805806831L79.08261425714286,299.2989583663021L94.89913710857142,299.77451130200507L110.71565996000001,299.61868789203953L126.53218281142857,299.8639526341454L142.34870566285713,299.88153783356876L158.16522851428573,299.9897039491015L173.98175136571427,299.99999978549624L189.79827421714285,300L205.61479706857142,300L221.43131992000002,300L237.24784277142854,300L253.06436562285714,300L268.88088847428577,300L284.69741132571426,300L300.51393417714286,300L316.33045702857146,300L332.14697988,300L347.96350273142855,300L363.7800255828571,299.99999999496043L379.5965484342857,299.99822698096756L395.4130712857143,299.87483400409104L395.4130712857143,300L379.5965484342857,300L363.7800255828571,300L347.96350273142855,300L332.14697988,300L316.33045702857146,300L300.51393417714286,300L284.69741132571426,300L268.88088847428577,300L253.06436562285714,300L237.24784277142854,300L221.43131992000002,300L205.61479706857142,300L189.79827421714285,300L173.98175136571427,300L158.16522851428573,300L142.34870566285713,300L126.53218281142857,300L110.71565996000001,300L94.89913710857142,300L79.08261425714286,300L63.266091405714285,300L47.44956855428571,300L31.633045702857142,300L15.816522851428571,300L0,300Z" fill="#4c78a8"/></g></g><path class="foreground" aria-hidden="true" d="" display="none"/></g><g transform="translate(0,0)"><path class="background" aria-hidden="true" d="M0,0h400v300h-400Z"/><g><g class="mark-area role-mark marks" role="graphics-object" aria-roledescription="area mark container"><path aria-label="Major Genre: Romantic Comedy; Worldwide Gross: 0; density: 5.9563842043e-9" role="graphics-symbol" aria-roledescription="area mark" d="M0,270.21807897849L2.648,265.43656567568956L5.296,267.8727819923353L7.944,274.7407102032084L10.592,281.8359430862L13.239999999999998,286.99995358460416L15.888,290.2271849505979L18.536,292.18491702776845L21.184,293.3512331320155L23.832,293.9728562850058L26.479999999999997,294.2656291523244L29.128,294.5015361687678L31.776,294.86022365088195L34.424,295.284352807232L37.072,295.6540779785503L39.72,295.98932391950945L42.368,296.32653240122994L45.016,296.5756600758668L47.664,296.66755920503726L50.312,296.77057398260166L52.959999999999994,297.193666465395L55.608000000000004,297.99027652505305L58.256,298.82090321858004L60.904,299.32846282216383L63.552,299.4891190065545L66.2,299.52542986475737L66.2,300L63.552,300L60.904,300L58.256,300L55.608000000000004,300L52.959999999999994,300L50.312,300L47.664,300L45.016,300L42.368,300L39.72,300L37.072,300L34.424,300L31.776,300L29.128,300L26.479999999999997,300L23.832,300L21.184,300L18.536,300L15.888,300L13.239999999999998,300L10.592,300L7.944,300L5.296,300L2.648,300L0,300Z" fill="#bab0ac"/></g></g><path class="foreground" aria-hidden="true" d="" display="none"/></g><g transform="translate(0,0)"><path class="background" aria-hidden="true" d="M0,0h400v300h-400Z"/><g><g class="mark-area role-mark marks" role="graphics-object" aria-roledescription="area mark container"><path aria-label="Major Genre: Horror; Worldwide Gross: 0; density: 8.01575942079e-9" role="graphics-symbol" aria-roledescription="area mark" d="M0,259.9212028960269L3.343175434285714,243.25982342498887L6.686350868571428,263.469537691571L10.029526302857143,279.99570318102013L13.372701737142856,286.57743806243184L16.715877171428573,289.43539778152854L20.059052605714285,293.68290884620296L23.40222804,294.7650062414786L26.745403474285713,294.7016919943395L30.088578908571428,295.66405233157803L33.43175434285715,297.8172096295773L36.77492977714286,298.92639553782396L40.11810521142857,299.82849782680927L43.46128064571428,299.98364071612343L46.80445608,299.7801234383062L50.147631514285706,299.44856153833973L53.490806948571425,299.68043459851L56.83398238285714,299.4644364894259L60.177157817142856,299.70311426993874L63.520333251428575,299.81747063472164L66.8635086857143,299.4589624215067L70.20668411999999,299.748487306465L73.54985955428572,299.9837861435889L76.89303498857144,299.989428211052L80.23621042285714,299.79653303105505L83.57938585714285,299.45225434870093L83.57938585714285,300L80.23621042285714,300L76.89303498857144,300L73.54985955428572,300L70.20668411999999,300L66.8635086857143,300L63.520333251428575,300L60.177157817142856,300L56.83398238285714,300L53.490806948571425,300L50.147631514285706,300L46.80445608,300L43.46128064571428,300L40.11810521142857,300L36.77492977714286,300L33.43175434285715,300L30.088578908571428,300L26.745403474285713,300L23.40222804,300L20.059052605714285,300L16.715877171428573,300L13.372701737142856,300L10.029526302857143,300L6.686350868571428,300L3.343175434285714,300L0,300Z" fill="#ff9da6"/></g></g><path class="foreground" aria-hidden="true" d="" display="none"/></g><g transform="translate(0,0)"><path class="background" aria-hidden="true" d="M0,0h400v300h-400Z"/><g><g class="mark-area role-mark marks" role="graphics-object" aria-roledescription="area mark container"><path aria-label="Major Genre: Western; Worldwide Gross: 14873; density: 1.50362976487e-8" role="graphics-symbol" aria-roledescription="area mark" d="M0.0021247142857142858,224.81851175639844L2.426039725714286,218.97486130691007L4.849954737142858,256.4355252758361L7.273869748571428,277.11540972670383L9.697784760000001,282.4852648517087L12.121699771428572,290.2082340004865L14.545614782857141,291.28002605253937L16.969529794285716,295.17848502885937L19.39344480571429,299.4134691503748L21.817359817142858,299.9855363564461L24.24127482857143,299.99992864617354L26.665189839999996,299.99999993032117L29.089104851428573,299.99999999998664L31.513019862857146,300L33.93693487428572,300L36.36084988571429,300L38.78476489714286,300L41.20867990857143,300L43.63259492,300L46.05650993142857,299.99999999999943L48.48042494285715,299.99999999523374L50.90433995428572,299.99999209154777L53.32825496571429,299.9974737848801L55.75216997714286,299.8446496072872L58.17608498857142,298.16084822499323L60.6,295.8083407005724L60.6,300L58.17608498857142,300L55.75216997714286,300L53.32825496571429,300L50.90433995428572,300L48.48042494285715,300L46.05650993142857,300L43.63259492,300L41.20867990857143,300L38.78476489714286,300L36.36084988571429,300L33.93693487428572,300L31.513019862857146,300L29.089104851428573,300L26.665189839999996,300L24.24127482857143,300L21.817359817142858,300L19.39344480571429,300L16.969529794285716,300L14.545614782857141,300L12.121699771428572,300L9.697784760000001,300L7.273869748571428,300L4.849954737142858,300L2.426039725714286,300L0.0021247142857142858,300Z" fill="#f58518"/></g></g><path class="foreground" aria-hidden="true" d="" display="none"/></g><g transform="translate(0,0)"><path class="background" aria-hidden="true" d="M0,0h400v300h-400Z"/><g><g class="mark-area role-mark marks" role="graphics-object" aria-roledescription="area mark container"><path aria-label="Major Genre: Documentary; Worldwide Gross: 0; density: 5.50885628936e-8" role="graphics-symbol" aria-roledescription="area mark" d="M0,24.557185532192214L1.270940097142857,169.51917784392845L2.541880194285714,247.24676230457746L3.812820291428571,284.8847729355303L5.083760388571428,286.4172617402167L6.354700485714286,299.45112355179805L7.625640582857142,294.7656007531655L8.896580680000001,292.0499112596568L10.167520777142856,290.07254334029506L11.438460874285711,297.16916057259635L12.709400971428572,299.9870327935237L13.980341068571429,299.9999990616756L15.251281165714284,299.99998509717886L16.522221262857144,299.92678035094696L17.793161360000003,294.3176097799086L19.064101457142854,293.03407665208556L20.335041554285713,299.8651128576508L21.60598165142857,299.9999587421452L22.876921748571423,299.99999999980065L24.14786184571429,300L25.418801942857144,300L26.689742040000002,299.99999999999994L27.960682137142857,299.9999999169084L29.231622234285716,299.9973503006987L30.502562331428567,298.6653104733317L31.773502428571426,289.3804004682371L31.773502428571426,300L30.502562331428567,300L29.231622234285716,300L27.960682137142857,300L26.689742040000002,300L25.418801942857144,300L24.14786184571429,300L22.876921748571423,300L21.60598165142857,300L20.335041554285713,300L19.064101457142854,300L17.793161360000003,300L16.522221262857144,300L15.251281165714284,300L13.980341068571429,300L12.709400971428572,300L11.438460874285711,300L10.167520777142856,300L8.896580680000001,300L7.625640582857142,300L6.354700485714286,300L5.083760388571428,300L3.812820291428571,300L2.541880194285714,300L1.270940097142857,300L0,300Z" fill="#eeca3b"/></g></g><path class="foreground" aria-hidden="true" d="" display="none"/></g><g transform="translate(0,0)"><path class="background" aria-hidden="true" d="M0,0h400v300h-400Z"/><g><g class="mark-area role-mark marks" role="graphics-object" aria-roledescription="area mark container"><path aria-label="Major Genre: Black Comedy; Worldwide Gross: 0; density: 1.88096173928e-8" role="graphics-symbol" aria-roledescription="area mark" d="M0,205.95191303584903L0.9338042000000001,184.0810696071579L1.8676084000000002,189.0801482765057L2.8014126,206.09565095532326L3.7352168000000003,223.54909431688498L4.669021,244.11101400250965L5.6028252,267.5562672255279L6.536629400000001,285.5154166462481L7.470433600000001,293.2194662622639L8.4042378,292.51625398343856L9.338042,288.40739797709534L10.2718462,286.1539773042876L11.2056504,287.5342524014603L12.1394546,291.0680304084181L13.073258800000001,295.0435152217151L14.007063,298.0500864492792L14.940867200000001,299.4943178495217L15.8746714,299.9167584950028L16.8084756,299.9913980562823L17.7422798,299.9984392089221L18.676084,299.98564870404476L19.6098882,299.87497357558766L20.5436924,299.32593236905876L21.477496600000006,297.7543151277634L22.4113008,295.3768709023329L23.345105,294.1188116243428L23.345105,300L22.4113008,300L21.477496600000006,300L20.5436924,300L19.6098882,300L18.676084,300L17.7422798,300L16.8084756,300L15.8746714,300L14.940867200000001,300L14.007063,300L13.073258800000001,300L12.1394546,300L11.2056504,300L10.2718462,300L9.338042,300L8.4042378,300L7.470433600000001,300L6.536629400000001,300L5.6028252,300L4.669021,300L3.7352168000000003,300L2.8014126,300L1.8676084000000002,300L0.9338042000000001,300L0,300Z" fill="#e45756"/></g></g><path class="foreground" aria-hidden="true" d="" display="none"/></g><g transform="translate(0,0)"><path class="background" aria-hidden="true" d="M0,0h400v300h-400Z"/><g><g class="mark-area role-mark marks" role="graphics-object" aria-roledescription="area mark container"><path aria-label="Major Genre: Concert/Performance; Worldwide Gross: 2255000; density: 1.08094342683e-8" role="graphics-symbol" aria-roledescription="area mark" d="M0.3221428571428571,245.95282865834523L0.7165816057142858,238.61798815798952L1.1110203542857144,231.51144505136992L1.5054591028571427,224.71511073781878L1.8998978514285714,218.51829951975117L2.2943366000000003,213.43434660035345L2.6887753485714283,210.0759016998447L3.0832140971428577,208.9436161540952L3.477652845714286,210.2398330575309L3.872091594285714,213.80680022060338L4.266530342857143,219.21395915028165L4.660969091428571,225.9308333882658L5.055407839999999,233.4789770663016L5.449846588571429,241.48332190622892L5.844285337142858,249.61651929835762L6.238724085714286,257.4980275017305L6.633162834285715,264.631542178887L7.027601582857143,270.4345412509959L7.422040331428572,274.3588958794115L7.816479080000001,276.055788355694L8.210917828571429,275.52034785843097L8.605356577142857,273.1600740813502L8.999795325714285,269.75537432611907L9.394234074285714,266.31167280684906L9.788672822857142,263.8358218858138L10.183111571428572,263.09825926822367L10.183111571428572,300L9.788672822857142,300L9.394234074285714,300L8.999795325714285,300L8.605356577142857,300L8.210917828571429,300L7.816479080000001,300L7.422040331428572,300L7.027601582857143,300L6.633162834285715,300L6.238724085714286,300L5.844285337142858,300L5.449846588571429,300L5.055407839999999,300L4.660969091428571,300L4.266530342857143,300L3.872091594285714,300L3.477652845714286,300L3.0832140971428577,300L2.6887753485714283,300L2.2943366000000003,300L1.8998978514285714,300L1.5054591028571427,300L1.1110203542857144,300L0.7165816057142858,300L0.3221428571428571,300Z" fill="#54a24b"/></g></g><path class="foreground" aria-hidden="true" d="" display="none"/></g></g><g class="mark-group role-legend" role="graphics-symbol" aria-roledescription="legend" aria-label="Symbol legend titled 'Major Genre' for fill color with 12 values: Action, Adventure, Black Comedy, Comedy, Concert/Performance, ending with Western"><g transform="translate(418,0)"><path class="background" aria-hidden="true" d="M0,0h168v170h-168Z" pointer-events="none"/><g><g class="mark-group role-legend-entry"><g transform="translate(0,16)"><path class="background" aria-hidden="true" d="M0,0h0v0h0Z" pointer-events="none"/><g><g class="mark-group role-scope" role="graphics-object" aria-roledescription="group mark container"><g transform="translate(0,0)"><path class="background" aria-hidden="true" d="M0,0h168v11h-168Z" pointer-events="none" opacity="1"/><g><g class="mark-symbol role-legend-symbol" pointer-events="none"><path transform="translate(6,6)" d="M5,0A5,5,0,1,1,-5,0A5,5,0,1,1,5,0" fill="#4c78a8" stroke-width="1.5" opacity="1"/></g><g class="mark-text role-legend-label" pointer-events="none"><text text-anchor="start" transform="translate(16,9)" font-family="sans-serif" font-size="10px" fill="#000" opacity="1">Action</text></g></g><path class="foreground" aria-hidden="true" d="" pointer-events="none" display="none"/></g><g transform="translate(0,13)"><path class="background" aria-hidden="true" d="M0,0h168v11h-168Z" pointer-events="none" opacity="1"/><g><g class="mark-symbol role-legend-symbol" pointer-events="none"><path transform="translate(6,6)" d="M5,0A5,5,0,1,1,-5,0A5,5,0,1,1,5,0" fill="#f58518" stroke-width="1.5" opacity="1"/></g><g class="mark-text role-legend-label" pointer-events="none"><text text-anchor="start" transform="translate(16,9)" font-family="sans-serif" font-size="10px" fill="#000" opacity="1">Adventure</text></g></g><path class="foreground" aria-hidden="true" d="" pointer-events="none" display="none"/></g><g transform="translate(0,26)"><path class="background" aria-hidden="true" d="M0,0h168v11h-168Z" pointer-events="none" opacity="1"/><g><g class="mark-symbol role-legend-symbol" pointer-events="none"><path transform="translate(6,6)" d="M5,0A5,5,0,1,1,-5,0A5,5,0,1,1,5,0" fill="#e45756" stroke-width="1.5" opacity="1"/></g><g class="mark-text role-legend-label" pointer-events="none"><text text-anchor="start" transform="translate(16,9)" font-family="sans-serif" font-size="10px" fill="#000" opacity="1">Black
Comedy</text></g></g><path class="foreground" aria-hidden="true" d="" pointer-events="none" display="none"/></g><g transform="translate(0,39)"><path class="background" aria-hidden="true" d="M0,0h168v11h-168Z" pointer-events="none" opacity="1"/><g><g class="mark-symbol role-legend-symbol" pointer-events="none"><path transform="translate(6,6)" d="M5,0A5,5,0,1,1,-5,0A5,5,0,1,1,5,0" fill="#72b7b2" stroke-width="1.5" opacity="1"/></g><g class="mark-text role-legend-label" pointer-events="none"><text text-anchor="start" transform="translate(16,9)" font-family="sans-serif" font-size="10px" fill="#000" opacity="1">Comedy</text></g></g><path class="foreground" aria-hidden="true" d="" pointer-events="none" display="none"/></g><g transform="translate(0,52)"><path class="background" aria-hidden="true" d="M0,0h168v11h-168Z" pointer-events="none" opacity="1"/><g><g class="mark-symbol role-legend-symbol" pointer-events="none"><path transform="translate(6,6)" d="M5,0A5,5,0,1,1,-5,0A5,5,0,1,1,5,0" fill="#54a24b" stroke-width="1.5" opacity="1"/></g><g class="mark-text role-legend-label" pointer-events="none"><text text-anchor="start" transform="translate(16,9)" font-family="sans-serif" font-size="10px" fill="#000" opacity="1">Concert/Performance</text></g></g><path class="foreground" aria-hidden="true" d="" pointer-events="none" display="none"/></g><g transform="translate(0,65)"><path class="background" aria-hidden="true" d="M0,0h168v11h-168Z" pointer-events="none" opacity="1"/><g><g class="mark-symbol role-legend-symbol" pointer-events="none"><path transform="translate(6,6)" d="M5,0A5,5,0,1,1,-5,0A5,5,0,1,1,5,0" fill="#eeca3b" stroke-width="1.5" opacity="1"/></g><g class="mark-text role-legend-label" pointer-events="none"><text text-anchor="start" transform="translate(16,9)" font-family="sans-serif" font-size="10px" fill="#000" opacity="1">Documentary</text></g></g><path class="foreground" aria-hidden="true" d="" pointer-events="none" display="none"/></g><g transform="translate(0,78)"><path class="background" aria-hidden="true" d="M0,0h168v11h-168Z" pointer-events="none" opacity="1"/><g><g class="mark-symbol role-legend-symbol" pointer-events="none"><path transform="translate(6,6)" d="M5,0A5,5,0,1,1,-5,0A5,5,0,1,1,5,0" fill="#b279a2" stroke-width="1.5" opacity="1"/></g><g class="mark-text role-legend-label" pointer-events="none"><text text-anchor="start" transform="translate(16,9)" font-family="sans-serif" font-size="10px" fill="#000" opacity="1">Drama</text></g></g><path class="foreground" aria-hidden="true" d="" pointer-events="none" display="none"/></g><g transform="translate(0,91)"><path class="background" aria-hidden="true" d="M0,0h168v11h-168Z" pointer-events="none" opacity="1"/><g><g class="mark-symbol role-legend-symbol" pointer-events="none"><path transform="translate(6,6)" d="M5,0A5,5,0,1,1,-5,0A5,5,0,1,1,5,0" fill="#ff9da6" stroke-width="1.5" opacity="1"/></g><g class="mark-text role-legend-label" pointer-events="none"><text text-anchor="start" transform="translate(16,9)" font-family="sans-serif" font-size="10px" fill="#000" opacity="1">Horror</text></g></g><path class="foreground" aria-hidden="true" d="" pointer-events="none" display="none"/></g><g transform="translate(0,104)"><path class="background" aria-hidden="true" d="M0,0h168v11h-168Z" pointer-events="none" opacity="1"/><g><g class="mark-symbol role-legend-symbol" pointer-events="none"><path transform="translate(6,6)" d="M5,0A5,5,0,1,1,-5,0A5,5,0,1,1,5,0" fill="#9d755d" stroke-width="1.5" opacity="1"/></g><g class="mark-text role-legend-label" pointer-events="none"><text text-anchor="start" transform="translate(16,9)" font-family="sans-serif" font-size="10px" fill="#000" opacity="1">Musical</text></g></g><path class="foreground" aria-hidden="true" d="" pointer-events="none" display="none"/></g><g transform="translate(0,117)"><path class="background" aria-hidden="true" d="M0,0h168v11h-168Z" pointer-events="none" opacity="1"/><g><g class="mark-symbol role-legend-symbol" pointer-events="none"><path transform="translate(6,6)" d="M5,0A5,5,0,1,1,-5,0A5,5,0,1,1,5,0" fill="#bab0ac" stroke-width="1.5" opacity="1"/></g><g class="mark-text role-legend-label" pointer-events="none"><text text-anchor="start" transform="translate(16,9)" font-family="sans-serif" font-size="10px" fill="#000" opacity="1">Romantic
Comedy</text></g></g><path class="foreground" aria-hidden="true" d="" pointer-events="none" display="none"/></g><g transform="translate(0,130)"><path class="background" aria-hidden="true" d="M0,0h168v11h-168Z" pointer-events="none" opacity="1"/><g><g class="mark-symbol role-legend-symbol" pointer-events="none"><path transform="translate(6,6)" d="M5,0A5,5,0,1,1,-5,0A5,5,0,1,1,5,0" fill="#4c78a8" stroke-width="1.5" opacity="1"/></g><g class="mark-text role-legend-label" pointer-events="none"><text text-anchor="start" transform="translate(16,9)" font-family="sans-serif" font-size="10px" fill="#000" opacity="1">Thriller/Suspense</text></g></g><path class="foreground" aria-hidden="true" d="" pointer-events="none" display="none"/></g><g transform="translate(0,143)"><path class="background" aria-hidden="true" d="M0,0h168v11h-168Z" pointer-events="none" opacity="1"/><g><g class="mark-symbol role-legend-symbol" pointer-events="none"><path transform="translate(6,6)" d="M5,0A5,5,0,1,1,-5,0A5,5,0,1,1,5,0" fill="#f58518" stroke-width="1.5" opacity="1"/></g><g class="mark-text role-legend-label" pointer-events="none"><text text-anchor="start" transform="translate(16,9)" font-family="sans-serif" font-size="10px" fill="#000" opacity="1">Western</text></g></g><path class="foreground" aria-hidden="true" d="" pointer-events="none" display="none"/></g></g></g><path class="foreground" aria-hidden="true" d="" pointer-events="none" display="none"/></g></g><g class="mark-text role-legend-title" pointer-events="none"><text text-anchor="start" transform="translate(0,9)" font-family="sans-serif" font-size="11px" font-weight="bold" fill="#000" opacity="1">Major
Genre</text></g></g><path class="foreground" aria-hidden="true" d="" pointer-events="none" display="none"/></g></g></g><path class="foreground" aria-hidden="true" d="" display="none"/></g></g></g></svg>

<choice id="1" >
<opt text="There are too many records.">

Having a lot of observations has no impact on a density plot. 

</opt>

<opt text="The majority of the observations lie on the left side of the plot making the values and genres difficult to observe." correct="true">

Got it! 

</opt>

<opt text="There are too many columns being plotted." >

We are only plotting one column from a dataframe so this should not matter.

</opt>


<opt text="The x-axis tend to display too many values without reason." >

If our plot includes the axis to the length shown, there are records for the values but they are so close to 0, that they cannot be identified. 
</opt>

</choice>


**Question 2**      
Which of the following statistics is **NOT** displayed in a boxplot?



<choice id="2" >
<opt text="Mean" correct="true">

🎉.

</opt>

<opt text="Maximum">

This is displayed at the end of the top (or right) whisker. 

</opt>

<opt text="Minimum">

This is displayed at the end of the bottom (or left) whisker. 

</opt>


<opt text="Median">

This is what the middle line in the box represents! 

</opt>

</choice>


</exercise>

<exercise id="13" title="Boxplots and Penguins">


**Instructions:**    
Be patient when running a coding exercise for the first time, it can take a few minutes. 

**When you see `____` in a coding exercise, replace it with what you assume to be the correct code. Run the code to see if you obtain the desired output
and submit it to validate if you were correct.**


In the last few slides, we were faceting and using colour channels to compare the body mass of different species of penguins. Let's explore this but this time using a boxplot!

<codeblock id="penguins">

</codeblock>


Tasks: 

Fill in the blanks in the code below so that the following gets accomplished.

- Use the data source `penguins_df` to make **boxplots** for the body mass values among the different penguin species.
- Make sure to give it an appropriate title and set the plot dimensions to a height of 200 and a width of 400.
- Remember to assign the `species` to the y-axis and the `body_mass_g` to the y-axis since we want to read the labels easily as we learned in the previous module.


<codeblock id="03_13">

- Are you using `mark_boxplot()`?
- Are you setting `alt.X('body_mass_g')`?
- Are you setting `alt.Y('species')`?
- Are you setting a title, height and width in `properties()`?

</codeblock>


**Question 1**      

Which species of penguin tend to have the most outliers?

<choice id="1" >
<opt text="Chinstrap" correct="true">

Great!

</opt>

<opt text="Gentoo">

The points on either side of the whiskers are indicative of outliers. Does the boxplot for the Gentoo species have these?

</opt>

<opt text="Adelie" >

The points on either side of the whiskers are indicative of outliers. Does the boxplot for the Adelie species have these?
 

</opt>

</choice>

**Question 2**      

Which species of penguin tend to have the highest median?

<choice id="2" >
<opt text="Chinstrap" >

Not quite here. 

</opt>

<opt text="Gentoo" correct="true">

The points on either side of the whiskers are indicative of outliers. Does the boxplot for the Gentoo species have these?

</opt>

<opt text="Adelie" >

Unfortunately not this one!
 

</opt>

</choice>


**Question 3**      

Which species of penguin tend to lowest maximum?

<choice id="3" >
<opt text="Chinstrap" correct="true">

Great!

</opt>

<opt text="Gentoo">

This one has the highest actually!

</opt>

<opt text="Adelie" >

Nope!
 

</opt>

</choice>


</exercise>


<exercise id="12" title="What Did We Just Learn?" type="slides, video">
<slides source="module3/module3_end" shot="0" start="07:32" end="08:20">
</slides>
</exercise>
