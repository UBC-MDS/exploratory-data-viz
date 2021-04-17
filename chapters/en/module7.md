---
title: 'Module 7: Chart Interactivity'
description:
  'In this module we will be learning about how to add interactive elements to our visualizations.'
prev: ../../module6
next: ../../module8
type: chapter
id: 7
---

<exercise id="0" title="Module Learning Outcomes"  type="slides, video">
<slides source="module7/module7_00" shot="0" start="12:2802" end="13:12"> </slides>
</exercise>

<exercise id="1" title="Tooltips, Zoom, and Selections" type="slides,video">
<slides source="module7/module7_01" shot="4" start="0:003" end="10:59"> </slides>
</exercise>


<exercise id="2" title="True or False: Getting Truthful With Interactivity">

**True or False**       
*Panning, zooming and brush selections can be simply added to Altair charts by using the `.interactive()` method.*


<choice id="1" >

<opt text="True" >

Try again! Brush selections are added via `.add_selection()` and `.selection_interval()`, not the `.interactive()` method.


</opt>


<opt text="False"  correct="true">

Great work! 

</opt>


</choice>

**True or False**       
*In Altair, brush selections are automatically linked between scatter plots that are created from the same dataframe.*

<choice id="2" >

<opt text="True"  correct="true">

Great work! This is a great feature of Altair!

</opt>

<opt text="False" >

Try again! It's easier than you think to link selections between scatter plots in Altair!

</opt>

</choice>

</exercise>


<exercise id="3" title="Your First Interactive Plot!">

**Instructions:**
Be patient when running a coding exercise for the first time, it can take a few minutes.

**When you see `____` in a coding exercise, replace it with what you assume to be the correct code. Run the code to see if you obtain the desired output and submit it to validate if you were correct.**

Let’s now look at the [penguins](https://www.kaggle.com/parulpandey/palmer-archipelago-antarctica-penguin-data) data set again and see whether species differences in body shape also relates to species differences in culmen shape. 

Which penguins are more abundant? Are there penguins that have a greater flipper length (`flipper_length_mm`) but with a smaller body mass (`body_mass_g)`? Does the mass of a penguin have a relationship to its flipper length? 

Let’s take a look!

<codeblock id="penguins">

</codeblock>


The first scatter plot should show body mass (y-axis) vs flipper length (x-axis) and be named `linked_scatter`. Colour the points be species. The second plot should show culmen depth (y-axis) vs culmen length (x-axis) - this second scatter plot can be created by just overwriting the encoding of the first. Horizontally concatenate these two scatter plots.

Tasks: 

Fill in the blanks in the code below so that the following gets accomplished:
- Create a selection interval and save it in an object named `brush`. 
- Create a scatter plot thats maps body mass on the y axis and flipper length on the x-axis. Map species to the colour channel and save this plot in an object named `linked_scatter`. 
-  In a second plot using `linked_scatter` as a base, map the culmen length (x-axis) by culmen depth (y-axis) and display them on top of each other by saving them in an object called `together_plot`. 

<codeblock id="07_03">

- Are you creating a selection interval using `alt.selection_interval()`
- Are you using the data `penguins_df` to create `linked_scatter`? 
- Are you plotting `body_mass_g` on the x-axis in `linked_scatter`?
- Are you setting the selection interval as an argument in condition? 
- Are you setting `brush` in  `add_selection`?

</codeblock>


**Question 1**      

Do the smallest Gentoo penguins (as measured by body size and flipper size) also have the smallest culmens?


<choice id="1" >
<opt text="Yes"  correct="true">

Nice work! When we use our cursor to select the smallest Gentoo penguins in the scatter plot on the left, we see that this also highlights the Gentoo penguins with the smallest culmens in the scatter plot on the right.

</opt>

<opt text="No" >

Try again, making sure you select the Gentoo penguins with the smallest body mass and flipper lengths!

</opt>

<opt text="It is not possible to answer this with this visualization"  >

This is indeed possible with scatter plots that have linked brush selections. Make sure you are using your cursor on the scatter plot on the left to select the Gentoo penguins with the smallest body mass and flipper lengths!

</opt>

</choice>

**Question 2**      

If we wanted to be able to get more detail about the linked observations between the two penguins scatter plots we just created, which of the following would **NOT** be helpful?



<choice id="2" >
<opt text="Use <code>resolve='intersect'</code> with <code>.selection_interval()</code> so that we can make brush selections in both scatter plots to highlight only intersecting points.">

Try again! This would be helpful as we could highlight only the observations that intersect in a select space between the two charts!

</opt>

<opt text="Use <code>.interactive()</code> so that we can zoom in and pan to areas of interest" >

Try again! Adding `.interactive()` would let us get more detail through panning and zooming.

</opt>

<opt text= "Use <code>tooltip</code> so that the island the penguin came from and it's sex is shown when a cursor hovers over an observation."  correct="true">

Nice work! Adding a tooltip would only be useful if here if we had unique identifiers for each observation. We do not have this here in this data set. It's important to note, that even if we did, this would be less effective that the other two options in this question.

</opt>

</choice>

</exercise>

<exercise id="4" title="Advanced Selections" type="slides,video">
<slides source="module7/module7_02" shot="4" start="0:003" end="10:59"> </slides>
</exercise>


<exercise id="5" title="True or False: Selecting Correctly">

**True or False**       
*In Altair, click selections can be bound to another chart or the legend.*


<choice id="1" >

<opt text="True" correct="true">

 Great work! This is a great feature of Altair!


</opt>


<opt text="False" >

Try again! In the previous slides we showed you how to do both of these things!

</opt>


</choice>

**True or False**       
*Interactive features in Altair are only possible for scatter plots and bar charts.*

<choice id="2" >

<opt text="True" >

Are you sure? What about the interactive maps we saw in the last few slides?

</opt>

<opt text="False"  correct="true">

Great work! You can use Altair to create interactive features with any chart you can make in Altair!

</opt>

</choice>

</exercise>

<exercise id="6" title="Muti-Select for Mutiple Choice Questions">

**Question**      
Which method in Altair would allow us to use a brush selection in one chart to filter data to highlight in another chart in?

<choice id="1" >
<opt text="<code>.transform_filter()</code>" correct="true">

 Nice work! `transform_filter()` let's you use a brush selection for filtering data in another chart!

</opt>

<opt text="<code>.interactive()</code>"  >

Try again! `.interactive()` let's you add zooming and panning functionality!

</opt>

<opt text="<code>.add_selection()</code>" >

Try again! `.add_selection()` let's you add click highlighting functionality! 

</opt>

</choice>

</exercise>

<exercise id="7" title="Clicks not Cliques">

**Instructions:**
Be patient when running a coding exercise for the first time, it can take a few minutes.

**When you see `____` in a coding exercise, replace it with what you assume to be the correct code. Run the code to see if you obtain the desired output and submit it to validate if you were correct.**

Let’s now look at the [penguins](https://www.kaggle.com/parulpandey/palmer-archipelago-antarctica-penguin-data) data set again and see how the Penguins of each species were studied on each island.

Let’s take a look!

<codeblock id="penguins">

</codeblock>

Create a grouped, horizontal bar chart where the number of penguins on each island is plotted for each species. You are aiming to have a plot that looks like you have 3 subplots, where each subplot is for each species. Add interactivity, so that you can select which island to highlight on the bar chart by clicking the legend. 

Tasks: 

Fill in the blanks in the code below so that the following gets accomplished:

- Create a multiple selection tool that binds to the legend selecting the observations from the columns `island`. Name this object `click`. 
- In a horizontal bar plot named `click_legend`, map the counts of penguins on the x-axis and the island the penguins were onserved on the y axis. Make sure to sort the islands by increasing count values. 
- Color the points by island and facet the plot by species using `.Row()`. 
- Add a condition to the opacity channel that depends on the selection tool `click` giving an opacity of 0.9 if selected and 0.2 if not. 

<codeblock id="07_07">

- Are you setting `fields=['island']` and binding to legend in the `click` selection tool?
- Are you setting `sort='x'` in the  `alt.Y()` function? 
- Are you plotting `body_mass_g` on the x-axis in `linked_scatter`?
- Are you setting the `island` to the colour channel?? 
- Are you setting `alt.condition(click, alt.value(0.9), alt.value(0.2))`?
- Are you remembering to call `click` in `.add_selection()` at the end of the plot?

</codeblock>


**Question**      

Which penguins species do we have the greatest number of observations for on Biscoe island?


<choice id="1" >
<opt text="Adelie" >

Try again, there are some Adelie penguins that were studied on Biscoe island, but they are the not the species for which we have the greatest number of observations for that island. Try clicking on "Biscoe" in the legend to highlight the bars of interest for answering this question.

</opt>

<opt text="Chinstrap" >

Try again, there are no Chinstrap penguins that were studied on Biscoe island. Try clicking on "Biscoe" in the legend to highlight the bars of interest for answering this question.

</opt>

<opt text="Gentoo"  correct="true">

Nice work! Was it easier to answer this question correctly when you clicked on the island of interest in the legend to highlight it?

</opt>

</choice>

</exercise>


<exercise id="8" title="Using Widgets to Control Selections" type="slides,video">
<slides source="module7/module7_03" shot="4" start="0:003" end="10:59"> </slides>
</exercise>

<exercise id="9" title="Sharing Altair Visualizations" type="slides,video">
<slides source="module7/module7_04" shot="4" start="0:003" end="10:59"> </slides>
</exercise>

<exercise id="10" title="What Did We Just Learn?" type="slides, video">
<slides source="module7/module7_end" shot="0" start="13:13" end="13:42"></slides>
</exercise>
