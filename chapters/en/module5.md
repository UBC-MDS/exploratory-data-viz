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


<exercise id="5" title="True or False: Titles and Formatting (T/F)?">

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


<exercise id="6" title="Multiple Choices for Titles and Labels">

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



<choice id="2" >
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



<choice id="3" >
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

<exercise id="7" title="Formatting Fun!">


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

Fill in the blanks in the code below so that the following gets accomplished:

- In a plot named `base`, use the data source `penguins_df` to make a histogram of the different quantities of penguin species in the data. 
- Map the species on the y-axis and the count on the x-axis. 
- In the base plot make sure to give a label to the x axis. Since the species is categorical, do not set a label for the y-axis.
- Display the base plot and take a look at what it's communicating.
- Create text by using `mark_text()` and save this in an object named `text`. It should have the same x and y mapping as the base plot but this time you want to make sure the count is displayed on the side of each species bar. Make sure it's centered in alignment and located at `dx=10`.
- After observing the plot create and object named `penguin_title` using `.TitleParams()`. In this method you will need to specify an insightful title, and subtitle, give the title a fontsize of 18, and set the subtitle colour to `firebrick`.
- Remove emove the grey box outlining the entire figure by setting the argument `strokeWidth` in the `.configure_view()` method. 

<codeblock id="05_07">

- Are you setting `alt.Y('species', title=None)` in the base plot?
- Are you setting `alt.X('count()', title='something')` in the base plot?
- In the text plot, are you coding `.mark_text(align='center', dx=10)`?
- In the text plot, are you specifying `alt.Text('count()'`?
- for the titles formatting are you making sure to use the arguments `subtitle`, `fontSize` and `subtitleColor`?


</codeblock>


</exercise>

<exercise id="8" title="Defining and transforming axis ranges" type="slides,video">
<slides source="module5/module5_03" shot="1" start="0:003" end="07:12"> </slides>
</exercise>


<exercise id="9" title="True or False: Transformations">

**True or False**       
*Filtering and clipping clipping is approriate to see variation in certain areas of your data.*


<choice id="1" >

<opt text="True"  correct="true">

You've been paying attention here!

</opt>

<opt text="False" >

Sometimes we need to see values within a certain range to indentify any variable or relationships within the data. 

</opt>


</choice>

**True or False**       
*Large outliers in the data can mask trends within the data.*

<choice id="2" >

<opt text="True"  correct="true">

🎉.

</opt>

<opt text="False" >

Sometimes a large value can affect the scale on an axes and make it difficult to identify and relationships or trends occuring in the data.

</opt>

</choice>


**True or False**       
*Log transforming an axis is a good option to use if there is a large range to displayed and you don't want to to compress the smaller values into bottom of the graph and with all possible values.*

<choice id="3" >

<opt text="True">

The first part is true, however log transforming does not work with values of 0 which would result in a value of -<span>&#8734;</span>. 

</opt>

<opt text="False" correct="true">

You are on fire!

</opt>

</choice>

</exercise>


<exercise id="10" title="Transformations and presentations">

**Question 1**      
Which of the folowing arguments will exclude data from a plot?

<choice id="1" >
<opt text="<code>clip</code>"  correct="true">

Cool!

</opt>

<opt text="<code>scale</code>">

We can use `.Scale()` and the `domain` argument to specify the domain of the plot axes but that does not stop the data points from appearing. 

</opt>

<opt text="<code>domain</code>">

Although this specifies the domain for the plot, the data will still display with

</opt>


<opt text="<code>filter</code>">

This is not an argument with Altair. 

</opt>

</choice>


**Question 2**      
How do you add interactivity to a plot?


<choice id="2" >
<opt text="<code>interactive=True</code>" >

You would not add interactivity with this argument.

</opt>

<opt text="<code>.interactivity()</code>">

Close but not quite!

</opt>

<opt text="<code>.interactive()</code>"  correct="true">

Nice!

</opt>

<opt text="<code>.active()</code>">

You are right that it's a method but not the correct one. 

</opt>


</choice>

</exercise>

<exercise id="11" title="Using Transformations in Action!">


**Instructions:**    
Be patient when running a coding exercise for the first time, it can take a few minutes. 

**When you see `____` in a coding exercise, replace it with what you assume to be the correct code. Run the code to see if you obtain the desired output
and submit it to validate if you were correct.**


This variation of the [Phillipino dataset originally from Kaggle](https://www.kaggle.com/grosvenpaul/family-income-and-expenditure) shows the income and expenditure (in PHP) of residents in the Philippine.

<codeblock id="income_exp">

</codeblock>


First let's just plot the income vs education expenditure with no transformations. Let's make sure we are formatting the axes correctly and determine if we can make any conclusions regarding the relationship between the two variables.

Tasks: 

Fill in the blanks in the code below so that the following gets accomplished:

- In a plot named `income_plot`, use the data source `income_df` to make a scatterplot. 
- Map the `tot_income` on the x-axis and `education_expenditure` on the y-axis. 
- Set the opacity of the points to 0.5 and size to 10.
- Make sure to give the x and y-axis labels (with units) and the plot a title.
- The x and y-axis values should have SI-units. 

<codeblock id="05_11a">

- Are you setting `alt.X('tot_income', axis=alt.Axis(format='s'), title='Income (PHP)'))`?
- Are you setting `alt.Y('education_expenditure', axis=alt.Axis(format='s'), title='Education expenditure (PHP)')`?
- Are you using `.mark_circle()`?
- Are you setting `opacity=0.5, size=10` within `.mark_circle()`?

</codeblock>

It's difficult to draw any clear conclusion on the relationship between these two variables. It might be helpful to transform these axes. 

**Question**      
Which type of transformation do you think would be best fitting here?


<choice id="1" >
<opt text="Logarithmic" >

Are you sure? Some people may spend 0 PHP on education.

</opt>

<opt text="Symmetric Logarithmic" correct="true">

You got it! `Symlog` is best here since some people spend 0 PHP on education. 

</opt>

<opt text="Exponential"  >

Maybe it's a good idea to refer to the notes. 

</opt>

<opt text="Absolute Value">

It doesn't make sense to have negative income or expenditures in this situation. 

</opt>

</choice>


Let's transform the axes now!

Tasks: 

Fill in the blanks in the code below so that the following gets accomplished:

- In a new plot named `income_log_plot` create a new scatter plot similarly to what we did before. 
- Map the `tot_income` on the x-axis and `education_expenditure` on the y-axis. 
- Set the opacity of the points to 0.5 and size to 10.
- Make sure to give the x and y-axis labels (with units) and the plot a title.
- The x and y-axis values should have SI-units. 
- **This time, transform both the x and y-axes with the appropriate transformation we answered from the multiple choice question above.** 

<codeblock id="05_11b">

- Are you setting `alt.X('tot_income', axis=alt.Axis(format='s'), title='Income (PHP)'), scale=alt.Scale(type='symlog'))`?
- Are you setting `alt.Y('education_expenditure', axis=alt.Axis(format='s'), title='Education expenditure (PHP)', scale=alt.Scale(type='symlog'))`?
- Are you using `.mark_circle()`?
- Are you setting `opacity=0.5, size=10` within `.mark_circle()`?

</codeblock>


**Question**      
What type of relationship is there between income and education expenditure now?


<choice id="2" >
<opt text="Positive" correct="true">

There appears to be an upward slope between the datapoints. 

</opt>

<opt text="Negative" >

Are you sure here?

</opt>

<opt text="No Relationship"  >

There appears to be some sort of relationship between the variables!

</opt>

</choice>

</exercise>

<exercise id="12" title="Effective Use of Colour for Categorical Data" type="slides,video">
<slides source="module5/module5_04" shot="1" start="0:003" end="07:12"> </slides>
</exercise>


<exercise id="13" title="True or False: These Statement are Either Black or White">


**True or False**       
*It's important to set your work apart and demonstate creativity by creating your own colour scheme.*


<choice id="1" >

<opt text="True">

It's often better to use colour schemes designed by experts in a way to be easy to tell apart and in most cases also suitable for people with color vision deficiencies.

</opt>

<opt text="False"  correct="true">

🎉.

</opt>


</choice>

**True or False**       
*Adding an additional channel like "shape" to an exisiting column mapping, is often recommended to help people with color vision deficiences.*

<choice id="2" >

<opt text="True"  correct="true">

Yes! If you want to add a colour mapping of a column, it's often a good idea to add the same mapping to an additional channel. 

</opt>

<opt text="False" >

Is using only a colour mapping inclusive to people who can't interprete them?   

</opt>

</choice>

</exercise>


<exercise id="14" title="Transformations and presentations">

**Question 1**      
When is it a good idea to use custom colour schemes?

<choice id="1" >
<opt text="When colours are already naturally associated with certain categories or values."  correct="true">

Cool!

</opt>

<opt text="When it helps demonstrates your creativity and coding ability.">

Using custom colours may actually do the oposite in this case.

</opt>

<opt text="When you don't like the pre-existing colour schemes.">

There's gotta be at least one scheme you like!

</opt>


<opt text="When you want to colour coordinate with your company's logos.">

I can understand this one but not necessarily the number one reason.

</opt>

</choice>


**Question 2**      
A around how many colour hues is it a good rule of thumb to reconsider colour as an effective channel to represent your data?


<choice id="2" >
<opt text="3" >

Maybe a little higher.

</opt>

<opt text="5" correct="true">
Nice :)!

</opt>

<opt text="10">

Can you differential between 10 different colours easily?

</opt>

<opt text="20">

20 colours seems like a lot!

</opt>


</choice>

</exercise>

<exercise id="15" title="Colouring Between the Lines!">


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

Fill in the blanks in the code below so that the following gets accomplished:


- In a plot named `base`, use the data source `penguins_df` to make a histogram of the different quantities of penguin species in the data. 
- Map the species on the y-axis and the count on the x-axis. 
- In the base plot make sure to give a label to the x axis. Since the species is categorical, do not set a label for the y-axis.
- Display the base plot and take a look at what it's communicating.
- Create text by using `mark_text()` and save this in an object named `text`. It should have the same x and y mapping as the base plot but this time you want to make sure the count is displayed on the side of each species bar. Make sure it's centered in alignment and located at `dx=10`.
- After observing the plot create and object named `penguin_title` using `.TitleParams()`. In this method you will need to specify an insightful title, and subtitle, give the title a fontsize of 18, and set the subtitle colour to `firebrick`.
- Remove emove the grey box outlining the entire figure by setting the argument `strokeWidth` in the `.configure_view()` method. 

<codeblock id="05_07">

- Are you setting `alt.Y('species', title=None)` in the base plot?
- Are you setting `alt.X('count()', title='something')` in the base plot?
- In the text plot, are you coding `.mark_text(align='center', dx=10)`?
- In the text plot, are you specifying `alt.Text('count()'`?
- for the titles formatting are you making sure to use the arguments `subtitle`, `fontSize` and `subtitleColor`?


</codeblock>


</exercise>

<exercise id="16" title="Effective use of color for quantitative data" type="slides,video">
<slides source="module5/module5_05" shot="1" start="0:003" end="07:12"> </slides>
</exercise>


<exercise id="20" title="Using color to highlight data" type="slides,video">
<slides source="module5/module5_06" shot="1" start="0:003" end="07:12"> </slides>
</exercise>


<exercise id="25" title="What Did We Just Learn?" type="slides, video">
<slides source="module5/module5_end" shot="0" start="04:5307" end="05:5911"></slides>
</exercise>
