---
title: 'Module 6: Stories, Maps and Layouts'
description:
  'In this module we will be learning about how to create narratives with our visualizations, visualize geographical data, and layout our plots effectively.'
prev: ../../module5
next: ../../module7
type: chapter
id: 6
---

<exercise id="0" title="Module Learning Outcomes"  type="slides, video">
<slides source="module6/module6_00" shot="0" start="3:5707" end="4:5306"> </slides>
</exercise>

<exercise id="1" title="Telling stories with visualization" type="slides,video">
<slides source="module6/module6_01" shot="1" start="0:003" end="07:12"> </slides>
</exercise>

<exercise id="2" title="True or False: Is it Effective?">

**True or False**       
*It's important to include as much information on a plot as possible.*


<choice id="1" >

<opt text="True" >

Sometimes removing categories can help communicate better and more effectively.

</opt>


<opt text="False"  correct="true">

Clever!

</opt>


</choice>

**True or False**       
*Data can convey different messages depending on how it's visualized.*

<choice id="2" >

<opt text="True"  correct="true">

It's important to be aware of this!

</opt>

<opt text="False" >

Depending on colour, size and presentation, data can be displayed to sway the audience with a certain message.

</opt>

</choice>

</exercise>


<exercise id="3" title="Which Graph is Effective?">

**Question 1**      
When comparing numeric values among categories, which visual channel is most effective in plotting?

<choice id="1" >
<opt text="Angle">

Angle can sometimes be difficult to compare, think about the exercise we did in Module 2. 

</opt>

<opt text="Colour" >

Categories are easily compared with colour but if we are trying to compare numeric values, colour may not be the best channel. 

</opt>

<opt text="Volume" >

We saw in a previous exercise in Module 2 that volume is not easily to assess all the time. 

</opt>


<opt text="Position" correct="true">

You got it!

</opt>

</choice>


**Question 2**      
Which plot is most effective in answer the question "Which countries do most NHL hockey players originate from?

#### Plot A


<center>
<img src="/module5/hockey1.svg" width="60%"></img>
</center>


#### Plot B 


<center>
<img src="/module5/hockey2.svg" width="60%"></img>
</center>



<choice id="2" >
<opt text="Plot A" >

Do we need to know all the categories?

</opt>

<opt text="Plot B" correct="true">

Nice!

</opt>

</choice>

</exercise>


<exercise id="4" title="Formatting Fun!">


**Instructions:**    
Be patient when running a coding exercise for the first time, it can take a few minutes. 

**When you see `____` in a coding exercise, replace it with what you assume to be the correct code. Run the code to see if you obtain the desired output
and submit it to validate if you were correct.**


The [penguins](https://www.kaggle.com/parulpandey/palmer-archipelago-antarctica-penguin-data) that we see time and time again is going to help us practice with formatting in this question.

<codeblock id="penguins">

</codeblock>


For this question let's create a stacked histogram of the values in the `culmen_depth_mm` column for different penguin species.

Remember is the previous module we discussed that the culmen is also sometimes referred to as the bill and is [upper ridge of a bird's beak](https://allisonhorst.github.io/palmerpenguins/articles/articles/art.html). 
Here is the diagram we showed you in an earlier module that was made by [Allison Horst](https://twitter.com/allison_horst).

<center>
<img src="/module3/penguin_culmen.jpg" width="60%"></img>
</center>

Tasks: 

Fill in the blanks in the code below so that the following gets accomplished:

- In a plot named `base`, use the data source `penguins_df` to make a histogram of the different quantities of penguin species in the data. 
- Map the species on the y-axis and the count on the x-axis. 
- In the base plot make sure to give a label to the x-axis. Since the species is categorical, do not set a label for the y-axis.
- Display the base plot and take a look at what it's communicating.
- Create text by using `mark_text()` and save this in an object named `text`. It should have the same x and y mapping as the base plot but this time you want to make sure the count is displayed on the side of each species bar. Make sure it's centered in alignment and located at `dx=10`.
- After observing the plot create and object named `penguin_title` using `.TitleParams()`. In this method, you will need to specify an insightful title, and subtitle, give the title a fontsize of 18, and set the subtitle colour to `firebrick`.
- Remove the grey box outlining the entire figure by setting the argument `strokeWidth` in the `.configure_view()` method.

<codeblock id="06_04">

- In the text plot, are you coding `.mark_text(align='center', dx=10)`?
- In the text plot, are you specifying `alt.Text('count()'`?
- for the titles formatting are you making sure to use the arguments `subtitle`, `fontSize` and `subtitleColor`?


</codeblock>

**Question**      

The base plot of the code above looks like this: 

<center>
<img src="/module5/base_plot.svg" width="60%"></img>
</center>


Which question can you now answer confidently using the formatted plot above, that you could not before with just the base plot?


<choice id="1" >
<opt text="Which penguin species is most prominent in the artic base on the data collected?" >

We could answer this question using the base plot since the position channel informed us on this. Comparing categories with the bars was still possible. 

</opt>

<opt text="How many Gentoo Penguins were observed in the data?" correct="true">

This would have been much harder to answer with our 

</opt>

<opt text="Which island has the most diverse penguin population?"  >

Neither plot, shows any information regarding the `island` column. 

</opt>

</choice>

</exercise>


<exercise id="5" title="Visualizing geographical data" type="slides,video">
<slides source="module6/module6_02" shot="1" start="0:003" end="07:12"> </slides>
</exercise>

<exercise id="6" title="True or False: Is it Effective?">

**True or False**       
*It's important to include as much information on a plot as possible.*


<choice id="1" >

<opt text="True" >

Sometimes removing categories can help communicate better and more effectively.

</opt>


<opt text="False"  correct="true">

Clever!

</opt>


</choice>

**True or False**       
*Data can convey different messages depending on how it's visualized.*

<choice id="2" >

<opt text="True"  correct="true">

It's important to be aware of this!

</opt>

<opt text="False" >

Depending on colour, size and presentation, data can be displayed to sway the audience with a certain message.

</opt>

</choice>

</exercise>


<exercise id="7" title="Which Graph is Effective?">

**Question 1**      
When comparing numeric values among categories, which visual channel is most effective in plotting?

<choice id="1" >
<opt text="Angle">

Angle can sometimes be difficult to compare, think about the exercise we did in Module 2. 

</opt>

<opt text="Colour" >

Categories are easily compared with colour but if we are trying to compare numeric values, colour may not be the best channel. 

</opt>

<opt text="Volume" >

We saw in a previous exercise in Module 2 that volume is not easily to assess all the time. 

</opt>


<opt text="Position" correct="true">

You got it!

</opt>

</choice>


**Question 2**      
Which plot is most effective in answer the question "Which countries do most NHL hockey players originate from?

#### Plot A


<center>
<img src="/module5/hockey1.svg" width="60%"></img>
</center>


#### Plot B 


<center>
<img src="/module5/hockey2.svg" width="60%"></img>
</center>



<choice id="2" >
<opt text="Plot A" >

Do we need to know all the categories?

</opt>

<opt text="Plot B" correct="true">

Nice!

</opt>

</choice>

</exercise>


<exercise id="8" title="Formatting Fun!">


**Instructions:**    
Be patient when running a coding exercise for the first time, it can take a few minutes. 

**When you see `____` in a coding exercise, replace it with what you assume to be the correct code. Run the code to see if you obtain the desired output
and submit it to validate if you were correct.**


The [penguins](https://www.kaggle.com/parulpandey/palmer-archipelago-antarctica-penguin-data) that we see time and time again is going to help us practice with formatting in this question.

<codeblock id="penguins">

</codeblock>


For this question let's create a stacked histogram of the values in the `culmen_depth_mm` column for different penguin species.

Remember is the previous module we discussed that the culmen is also sometimes referred to as the bill and is [upper ridge of a bird's beak](https://allisonhorst.github.io/palmerpenguins/articles/articles/art.html). 
Here is the diagram we showed you in an earlier module that was made by [Allison Horst](https://twitter.com/allison_horst).

<center>
<img src="/module3/penguin_culmen.jpg" width="60%"></img>
</center>

Tasks: 

Fill in the blanks in the code below so that the following gets accomplished:

- In a plot named `base`, use the data source `penguins_df` to make a histogram of the different quantities of penguin species in the data. 
- Map the species on the y-axis and the count on the x-axis. 
- In the base plot make sure to give a label to the x-axis. Since the species is categorical, do not set a label for the y-axis.
- Display the base plot and take a look at what it's communicating.
- Create text by using `mark_text()` and save this in an object named `text`. It should have the same x and y mapping as the base plot but this time you want to make sure the count is displayed on the side of each species bar. Make sure it's centered in alignment and located at `dx=10`.
- After observing the plot create and object named `penguin_title` using `.TitleParams()`. In this method, you will need to specify an insightful title, and subtitle, give the title a fontsize of 18, and set the subtitle colour to `firebrick`.
- Remove the grey box outlining the entire figure by setting the argument `strokeWidth` in the `.configure_view()` method.

<codeblock id="06_08">

- In the text plot, are you coding `.mark_text(align='center', dx=10)`?
- In the text plot, are you specifying `alt.Text('count()'`?
- for the titles formatting are you making sure to use the arguments `subtitle`, `fontSize` and `subtitleColor`?


</codeblock>

**Question**      

The base plot of the code above looks like this: 

<center>
<img src="/module5/base_plot.svg" width="60%"></img>
</center>


Which question can you now answer confidently using the formatted plot above, that you could not before with just the base plot?


<choice id="1" >
<opt text="Which penguin species is most prominent in the artic base on the data collected?" >

We could answer this question using the base plot since the position channel informed us on this. Comparing categories with the bars was still possible. 

</opt>

<opt text="How many Gentoo Penguins were observed in the data?" correct="true">

This would have been much harder to answer with our 

</opt>

<opt text="Which island has the most diverse penguin population?"  >

Neither plot, shows any information regarding the `island` column. 

</opt>

</choice>

</exercise>


<exercise id="9" title="Figure layouts" type="slides,video">
<slides source="module6/module6_03" shot="1" start="0:003" end="07:12"> </slides>
</exercise>


<exercise id="10" title="True or False: Is it Effective?">

**True or False**       
*It's important to include as much information on a plot as possible.*


<choice id="1" >

<opt text="True" >

Sometimes removing categories can help communicate better and more effectively.

</opt>


<opt text="False"  correct="true">

Clever!

</opt>


</choice>

**True or False**       
*Data can convey different messages depending on how it's visualized.*

<choice id="2" >

<opt text="True"  correct="true">

It's important to be aware of this!

</opt>

<opt text="False" >

Depending on colour, size and presentation, data can be displayed to sway the audience with a certain message.

</opt>

</choice>

</exercise>


<exercise id="11" title="Which Graph is Effective?">

**Question 1**      
When comparing numeric values among categories, which visual channel is most effective in plotting?

<choice id="1" >
<opt text="Angle">

Angle can sometimes be difficult to compare, think about the exercise we did in Module 2. 

</opt>

<opt text="Colour" >

Categories are easily compared with colour but if we are trying to compare numeric values, colour may not be the best channel. 

</opt>

<opt text="Volume" >

We saw in a previous exercise in Module 2 that volume is not easily to assess all the time. 

</opt>


<opt text="Position" correct="true">

You got it!

</opt>

</choice>


**Question 2**      
Which plot is most effective in answer the question "Which countries do most NHL hockey players originate from?

#### Plot A


<center>
<img src="/module5/hockey1.svg" width="60%"></img>
</center>


#### Plot B 


<center>
<img src="/module5/hockey2.svg" width="60%"></img>
</center>



<choice id="2" >
<opt text="Plot A" >

Do we need to know all the categories?

</opt>

<opt text="Plot B" correct="true">

Nice!

</opt>

</choice>

</exercise>


<exercise id="12" title="Formatting Fun!">


**Instructions:**    
Be patient when running a coding exercise for the first time, it can take a few minutes. 

**When you see `____` in a coding exercise, replace it with what you assume to be the correct code. Run the code to see if you obtain the desired output
and submit it to validate if you were correct.**


The [penguins](https://www.kaggle.com/parulpandey/palmer-archipelago-antarctica-penguin-data) that we see time and time again is going to help us practice with formatting in this question.

<codeblock id="penguins">

</codeblock>


For this question let's create a stacked histogram of the values in the `culmen_depth_mm` column for different penguin species.

Remember is the previous module we discussed that the culmen is also sometimes referred to as the bill and is [upper ridge of a bird's beak](https://allisonhorst.github.io/palmerpenguins/articles/articles/art.html). 
Here is the diagram we showed you in an earlier module that was made by [Allison Horst](https://twitter.com/allison_horst).

<center>
<img src="/module3/penguin_culmen.jpg" width="60%"></img>
</center>

Tasks: 

Fill in the blanks in the code below so that the following gets accomplished:

- In a plot named `base`, use the data source `penguins_df` to make a histogram of the different quantities of penguin species in the data. 
- Map the species on the y-axis and the count on the x-axis. 
- In the base plot make sure to give a label to the x-axis. Since the species is categorical, do not set a label for the y-axis.
- Display the base plot and take a look at what it's communicating.
- Create text by using `mark_text()` and save this in an object named `text`. It should have the same x and y mapping as the base plot but this time you want to make sure the count is displayed on the side of each species bar. Make sure it's centered in alignment and located at `dx=10`.
- After observing the plot create and object named `penguin_title` using `.TitleParams()`. In this method, you will need to specify an insightful title, and subtitle, give the title a fontsize of 18, and set the subtitle colour to `firebrick`.
- Remove the grey box outlining the entire figure by setting the argument `strokeWidth` in the `.configure_view()` method.

<codeblock id="06_12">

- In the text plot, are you coding `.mark_text(align='center', dx=10)`?
- In the text plot, are you specifying `alt.Text('count()'`?
- for the titles formatting are you making sure to use the arguments `subtitle`, `fontSize` and `subtitleColor`?


</codeblock>

**Question**      

The base plot of the code above looks like this: 

<center>
<img src="/module5/base_plot.svg" width="60%"></img>
</center>


Which question can you now answer confidently using the formatted plot above, that you could not before with just the base plot?


<choice id="1" >
<opt text="Which penguin species is most prominent in the artic base on the data collected?" >

We could answer this question using the base plot since the position channel informed us on this. Comparing categories with the bars was still possible. 

</opt>

<opt text="How many Gentoo Penguins were observed in the data?" correct="true">

This would have been much harder to answer with our 

</opt>

<opt text="Which island has the most diverse penguin population?"  >

Neither plot, shows any information regarding the `island` column. 

</opt>

</choice>

</exercise>



<exercise id="24" title="What Did We Just Learn?" type="slides, video">
<slides source="module6/module6_end" shot="0" start="04:5307" end="05:5911"></slides>
</exercise>
