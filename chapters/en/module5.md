---
title: 'Module 5: Designing plots for communication'
description:
  'In this module we will be learning about how to design effective plots for communication purposes.'
prev: ../../module4
next: ../../module6
type: chapter
id: 5
---

<exercise id="0" title="Module Learning Outcomes"  type="slides, video">
<slides source="module5/module5_00" shot="0" start="3:5707" end="4:5306"> </slides>
</exercise>

<exercise id="1" title="Effective figure design" type="slides,video">
<slides source="module5/module5_01" shot="1" start="0:003" end="07:12"> </slides>
</exercise>


<exercise id="2" title="True or False: Is it Effective?">

**True or False**       
*It's important to imclude as much information on a plot as possible.*


<choice id="1" >

<opt text="True" >

Sometimes removing categories can help commmunicate better and more effectively.

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
When comparing categories, which visual channel is most effective in plotting?

<choice id="1" >
<opt text="Angles">

This can be used to visualize a single column's distribution.

</opt>

<opt text="Colours" >

This can be used to visualize a single column's distribution.

</opt>

<opt text="Volume" >

This can be used to visualize a single column's distribution.

</opt>


<opt text="Positions" correct="true">

You got it!

</opt>

</choice>


**Question 2**      
Which plot is most effective in answer the question "Which countries do most NHL hockey players originate from?

#### Plot A


<center>
<img src="/module5/hockey1.svg" width="50%"></img>
</center>


#### Plot B 


<center>
<img src="/module5/hockey2.svg" width="50%"></img>
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


<exercise id="4" title="Descriptive titles and labels" type="slides,video">
<slides source="module5/module5_02" shot="1" start="0:003" end="07:12"> </slides>
</exercise>


<exercise id="5" title="True or False: Is it Effective?">

**True or False**       
*All plots should have a subtitle that adds additional details*


<choice id="1" >

<opt text="True" >

Often it's not necessary to have a subtitle but they can be helpful in supporting the communication of the plot's insights.

</opt>


<opt text="False"  correct="true">

Clever!

</opt>


</choice>

**True or False**       
*Using Altair, we can split up a title or subtitle by adding `\n` to indicate a line break.*

<choice id="2" >

<opt text="True" >

This does work in other plotting tools, but in Altair we separate our title and subtitle lines but putting strings as elements in a list. Each element in the list is indicative of a new line.

</opt>

<opt text="False"  correct="true">

🎉 

</opt>

</choice>


**True or False**       
*Not very axis and legend needs to have a title.*

<choice id="3" >

<opt text="True"  correct="true">

You got it!

</opt>

<opt text="False" >

For axis such as time and some categorical labels, it's redundant to have labels. 
</opt>

</choice>

</exercise>


<exercise id="6" title="Which graph is effective?">

**Question 1**      
When aligning your titles, which argument would you use in `.TitleParams()`?

<choice id="1" >
<opt text="<code>alignment</code>">

I think your argument should be called something else.

</opt>

<opt text="<code>position</code>">

I think your argument should be called something else.

</opt>

<opt text="<code>align</code>">

I think your argument should be called something else.

</opt>


<opt text="<code>anchor</code>" correct="true">

You got it!

</opt>

</choice>


**Question 2**      
Which title is most appropriate for the plot below?


<center>
<img src="/module5/hockey3.svg" width="50%"></img>
</center>



<choice id="3" >
<opt text="<code>full</code>">

Not quite. Maybe take a look at slide 11.

</opt>

<opt text="<code>s</code>" correct="true">

Nice work!

</opt>

<opt text="<code>SI-units</code>">

Although this is the correct name, it's not the value we assign to the `format` argument

</opt>

<opt text="<code>SI</code>">

Close but not quite here.

</opt>


</choice>


**Question 3**      
To display the full number in the axis tick values instead of scientific notation, we can set `format` in `.Axis()` to which of the following )?


<center>
<img src="/module5/hockey3.svg" width="50%"></img>
</center>



<choice id="2" >
<opt text="NHL hockey player nationality" >

This isn't explaining any insights from the plot.

</opt>

<opt text="birth_country vs frequency in NHL" >

Referencing the column names isn't explaining any insights from the plot.

</opt>

<opt text="Majority of NHL hockey players originate from Canada" correct="true">

Nice!

</opt>

<opt text="Hockey Players in the NLH originate from all around the world" >

This is not exactly pertaining to the plot we see above. We would more likely want to title it commenting on the large number of players originating from Canada.

</opt>

</choice>

</exercise>

<exercise id="7" title="Titles and Texts with penguins">


**Instructions:**    
Be patient when running a coding exercise for the first time, it can take a few minutes. 

**When you see `____` in a coding exercise, replace it with what you assume to be the correct code. Run the code to see if you obtain the desired output
and submit it to validate if you were correct.**


The [penguins](https://www.kaggle.com/parulpandey/palmer-archipelago-antarctica-penguin-data) that we seen time and time again is going to help us practice with formatting in this question.

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


<codeblock id="05_07">

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

<exercise id="8" title="Defining and transforming axis ranges" type="slides,video">
<slides source="module5/module5_03" shot="1" start="0:003" end="07:12"> </slides>
</exercise>

<exercise id="12" title="Effective use of color for categorical data" type="slides,video">
<slides source="module5/module5_04" shot="1" start="0:003" end="07:12"> </slides>
</exercise>

<exercise id="15" title="Effective use of color for quantitative data" type="slides,video">
<slides source="module5/module5_05" shot="1" start="0:003" end="07:12"> </slides>
</exercise>

<exercise id="19" title="Using color to highlight data" type="slides,video">
<slides source="module5/module5_06" shot="1" start="0:003" end="07:12"> </slides>
</exercise>

<exercise id="25" title="What Did We Just Learn?" type="slides, video">
<slides source="module5/module5_end" shot="0" start="04:5307" end="05:5911"></slides>
</exercise>
