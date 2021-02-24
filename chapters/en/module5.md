---
title: 'Module 5: Designing plots for communication'
description:
  'In this module we will be learning about how to design effective plots for communication purposes.'
prev: ../../module4
next: ../../module6
type: chapter
id: 5
---

<head>
    <base target="_blank">
</head>

<exercise id="0" title="Module Learning Outcomes"  type="slides, video">
<slides source="module5/module5_00" shot="0" start="3:5707" end="4:5306"> </slides>
</exercise>

<exercise id="1" title="Effective Figure Design" type="slides,video">
<slides source="module5/module5_01" shot="1" start="0:003" end="07:12"> </slides>
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


<exercise id="4" title="Descriptive Titles and Labels" type="slides,video">
<slides source="module5/module5_04" shot="1" start="0:003" end="07:12"> </slides>
</exercise>


<exercise id="5" title="True or False: Titles and Formatting (T/F)?">

**True or False**       
*All plots should have a subtitle that adds additional details*


<choice id="1" >

<opt text="True" >

Often it's not necessary to have a subtitle but they can help support the communication of the plot's insights.

</opt>


<opt text="False"  correct="true">

Clever!

</opt>


</choice>

**True or False**       
*Using Altair, we can split up a title or subtitle by adding `\n` to indicate a line break.*

<choice id="2" >

<opt text="True" >

This does work in other plotting tools, but in Altair, we separate our title and subtitle lines but putting strings as elements in a list. Each element in the list is indicative of a new line.

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

For axes such as time and some categorical labels, it's redundant to have labels. 
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

This is not exactly what we are trying to communicate with the plot we see above. We would more likely want to title it commenting on the large number of players originating from Canada.

</opt>

</choice>

</exercise>

<exercise id="7" title="Formatting Fun!">


**Instructions:**    
Be patient when running a coding exercise for the first time, it can take a few minutes. 

**When you see `____` in a coding exercise, replace it with what you assume to be the correct code. Run the code to see if you obtain the desired output
and submit it to validate if you were correct.**


The [penguins](https://www.kaggle.com/parulpandey/palmer-archipelago-antarctica-penguin-data) that we see time and time again is going to help us practice with formatting in this question.

<codeblock id="penguins">

</codeblock>


For this question let's create a stacked histogram of the values in the `culmen_depth_mm` column for different penguin species.

***([Culmen](https://allisonhorst.github.io/palmerpenguins/articles/articles/art.html): the upper ridge of a bird's beak)***

Tasks: 

Fill in the blanks in the code below so that the following gets accomplished:

- In a plot named `base`, use the data source `penguins_df` to make a histogram of the different quantities of penguin species in the data. 
- Map the species on the y-axis and the count on the x-axis. 
- In the base plot make sure to give a label to the x-axis. Since the species is categorical, do not set a label for the y-axis.
- Display the base plot and take a look at what it's communicating.
- Create text by using `mark_text()` and save this in an object named `text`. It should have the same x and y mapping as the base plot but this time you want to make sure the count is displayed on the side of each species bar. Make sure it's centered in alignment and located at `dx=10`.
- After observing the plot create and object named `penguin_title` using `.TitleParams()`. In this method, you will need to specify an insightful title, and subtitle, give the title a fontsize of 18, and set the subtitle colour to `firebrick`.
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
<slides source="module5/module5_08" shot="1" start="0:003" end="07:12"> </slides>
</exercise>


<exercise id="9" title="True or False: Transformations">

**True or False**       
*Filtering and clipping is appropriate to see a variation in certain areas of your data.*


<choice id="1" >

<opt text="True"  correct="true">

You've been paying attention here!

</opt>

<opt text="False" >

Sometimes we need to see values within a certain range to identify any variable or relationships within the data. 

</opt>


</choice>

**True or False**       
*Large outliers in the data can mask trends within the data.*

<choice id="2" >

<opt text="True"  correct="true">

🎉.

</opt>

<opt text="False" >

Sometimes a large value can affect the scale on an axis and make it difficult to identify and relationships or trends occurring in the data.

</opt>

</choice>


**True or False**       
*Log transforming an axis is a good option to use if there is a large range to displayed and you don't want to compress the smaller values into the bottom of the graph and with all possible values.*

<choice id="3" >

<opt text="True">

The first part is true, however, log transforming does not work with values of 0 which would result in a value of -<span>&#8734;</span>. 

</opt>

<opt text="False" correct="true">

You are on fire!

</opt>

</choice>

</exercise>


<exercise id="10" title="Transformations and Presentations">

**Question 1**      
Which of the following arguments will exclude data from a plot?

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


This variation of the [Phillipino dataset originally from Kaggle](https://www.kaggle.com/grosvenpaul/family-income-and-expenditure) shows the income and expenditure (in PHP) of residents in the Philippines.

<codeblock id="income_exp">

</codeblock>


First, let's just plot the income vs education expenditure with no transformations. Let's make sure we are formatting the axes correctly and determine if we can make any conclusions regarding the relationship between the two variables.

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
Which type of transformation do you think would be the best fitting here?


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

- In a new plot named `income_log_plot` create a new scatter plot similar to what we did before. 
- Map the `tot_income` on the x-axis and `education_expenditure` on the y-axis. 
- Set the opacity of the points to 0.5 and size to 10.
- Make sure to give the x and y-axis labels (with units) and the plot a title.
- The x and y-axis values should have SI-units. 
- **This time, transform both the x and y-axes with the appropriate transformation we answered from the multiple-choice question above.** 

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

There appears to be an upward slope between the data points. 

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
<slides source="module5/module5_12" shot="1" start="0:003" end="07:12"> </slides>
</exercise>


<exercise id="13" title="True or False: These Statement are Either Black or White">


**True or False**       
*It's important to set your work apart and demonstrate creativity by creating your own colour scheme.*


<choice id="1" >

<opt text="True">

It's often better to use colour schemes designed by experts in a way to be easy to tell apart and in most cases also suitable for people with color vision deficiencies.

</opt>

<opt text="False"  correct="true">

🎉.

</opt>


</choice>

**True or False**       
*Adding an additional channel like "shape" to an existing column mapping, is often recommended to help people with color vision deficiencies.*

<choice id="2" >

<opt text="True"  correct="true">

Yes! If you want to add a colour mapping of a column, it's often a good idea to add the same mapping to an additional channel. 

</opt>

<opt text="False" >

Is using strictly colour mapping inclusive to people who can't interpret them?   

</opt>

</choice>

</exercise>


<exercise id="14" title="Colour Coordination Questions">

**Question 1**      
When is it a good idea to use custom colour schemes?

<choice id="1" >
<opt text="When colours are already naturally associated with certain categories or values."  correct="true">

Cool!

</opt>

<opt text="When it helps demonstrates your creativity and coding ability.">

Using custom colours may do the opposite in this case.

</opt>

<opt text="When you don't like the pre-existing colour schemes.">

There's gotta be at least one scheme you like!

</opt>


<opt text="When you want to colour coordinate with your company's logos.">

I can understand this one but not necessarily the number one reason.

</opt>

</choice>


**Question 2**      
How many colours (approximately by a rule of thumb) should you begin to reconsider colour as an effective channel to represent your data?


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

20 colours is a lot!

</opt>


</choice>

</exercise>

<exercise id="15" title="Adding some Colour to Penguins">


**Instructions:**    
Be patient when running a coding exercise for the first time, it can take a few minutes. 

**When you see `____` in a coding exercise, replace it with what you assume to be the correct code. Run the code to see if you obtain the desired output
and submit it to validate if you were correct.**


We are about to talk our typically black and white [penguins](https://www.kaggle.com/parulpandey/palmer-archipelago-antarctica-penguin-data) and brighten these birds up a bit!  Using what we learned in the last 2 sections, let's identify if there are any relationships between the flipper and culmen length and the different species of Antarctic penguins. 

<codeblock id="penguins">

</codeblock>


Let's plot the `culmen_length_mm` and `flipper_length_mm` but this time, let's add a colour and shape channel to the species and explore if there are appears to be anything telling. 

Tasks: 

Fill in the blanks in the code below so that the following gets accomplished:


- In a plot named `colour_plot`, use the data source `penguins_df` to make a scatter plot (`mark_point`) with points that are size 10.
- Map the flipper length on the x-axis and the culmen length on the y-axis. 
- Map the penguin species to both a colour and a shape channel.
- Select a [desired colour scheme](https://vega.github.io/vega/docs/schemes/), and assign it to the colour channel. 
- In this plot, it might be a good idea to restrict the axis ranges. Select an appropriate domain for both the x and y-axis. 
- Make sure you are giving the channels all proper labels and the plot a title. 

<codeblock id="05_15">

- Are you using `mark_point(size=10)`?
- Are you setting `alt.X('flipper_length_mm', scale=alt.Scale(domain=[140, 240]), title="Flipper length (mm)")`?
- Are you setting `alt.X(''culmen_length_mm', scale=alt.Scale(domain=[25, 65]), title='Culmen length (mm)')`?
- In the  plot, are you coding ` alt.Color('species', title='Penguin species', scale=alt.Scale(scheme='desired-set-name'))`?
- Are you setting `alt.Shape('species')`?
- Are you setting a title in `properties()`?

</codeblock>

**Question**      
Which penguin species tend to have the shortest culmen length?


<choice id="1" >
<opt text="Adelie" correct="true">

Great!

</opt>

<opt text="Chintrap" >
Hmmm, maybe not this penguin species.

</opt>

<opt text="Gentoo">

Not this species!

</opt>


</choice>



</exercise>

<exercise id="16" title="Effective Use of Colour for Quantitative Data" type="slides,video">
<slides source="module5/module5_16" shot="1" start="0:003" end="07:12"> </slides>
</exercise>


<exercise id="17" title="True or False: Colouring in the Blank">

**True or False**       
*Some colour palettes and schemes may introduce a bias towards certain insights.*

<choice id="1" >

<opt text="True"  correct="true">

Got it!

</opt>

<opt text="False" >

It's important to be careful since using a palette potentially can cause a slight bias towards seeing groupings where there are none.

</opt>

</choice>


**True or False**       
*When using colour to communicate changes in quantitative data, it's better to use a scale with many different colours and hues.*


<choice id="2" >

<opt text="True">

It's often better to use a palette with few colours designed specifically to distinguish a scale or a single colour with different saturations.

</opt>

<opt text="False"  correct="true">

🎉.

</opt>


</choice>

</exercise>


<exercise id="18" title="Colouring by Numbers Questions">

**Question 1**      
If you are plotting data for a particular variable where there is no difference in importance between the high and low values, which colour should be assigned to the highest variable given the colours below?

<svg width="20" height="20" ><rect width="20" height="20" style="fill:#440154FF;stroke-width:2;stroke:rgb(0,0,0)" /></svg>  &nbsp; Indigo <br>
<svg width="20" height="20" ><rect width="20" height="20" style="fill:#30568CFF;stroke-width:2;stroke:rgb(0,0,0)" /></svg>  &nbsp; Blue <br>
<svg width="20" height="20" ><rect width="20" height="20" style="fill:#55C667FF;stroke-width:2;stroke:rgb(0,0,0)" /></svg>  &nbsp; Green <br>
<svg width="20" height="20" ><rect width="20" height="20" style="fill:#FDE725FF;stroke-width:2;stroke:rgb(0,0,0)" /></svg>  &nbsp; Yellow




<choice id="1" >
<opt text="💜- Indigo"  correct="true">

Cool! This is the darkest colour and thus has the largest contrast with the background which gets assigned to the highest values.

</opt>


<opt text="🔵 - Blue">

We need to assign the colour with the most contrast to the highest values. Is this the darkest colour?

</opt>
<opt text="✅ - Green">

We need to assign the colour with the most contrast to the highest values. Is this the darkest colour?

</opt>


<opt text="☀️- Yellow">

We need to assign the colour with the most contrast to the highest values. Is this the darkest colour?

</opt>

</choice>


**Question 2**      
Which colour scheme is most appropriate for quantitative data that has a natural midpoint? 


<choice id="2" >
<opt text="Sequential" >

Not quite. There is a better answer. 

</opt>

<opt text="Categorical" >
This is for categorical data! We asked for quantitative data!

</opt>

<opt text="Diverging" correct="true">

Passing with flying colours!

</opt>

<opt text="Rainbow">

There is no pot of gold at the end of this rainbow. 

</opt>

</choice>

</exercise>

<exercise id="19" title="Playing with Colour">


**Instructions:**    
Be patient when running a coding exercise for the first time, it can take a few minutes. 

**When you see `____` in a coding exercise, replace it with what you assume to be the correct code. Run the code to see if you obtain the desired output
and submit it to validate if you were correct.**


The University of British Columbia is based in Vancouver and we are lucky enough to have a relatively mild climate (mild climate, but rainy). This made us think of our country's wonderful capital Ottawa and how they are not so fortunate. This question will be using the data obtained from the [Governement of Canada](https://climate.weather.gc.ca/). The data we have collected is from 2008-2010.

<codeblock id="temperatures">

</codeblock>

 Let's observe and visualize the mean monthly temperature of Ottawa and see if there is any relationship between rainfall, the season and temperature. 

Tasks: 

Fill in the blanks in the code below so that the following gets accomplished:


- In a plot named `temp_plot`, use the data source `temps_df` to make a scatter plot (`mark_point`) with points that are size 50.
- Map the date on the x-axis and the total rainfall levels on the y-axis. 
- Map the mean temperature to a colour channel and select an appropriate [colour scheme](https://vega.github.io/vega/docs/schemes/). Is a diverging or sequential scheme more appropriate?
- Make sure you are giving the channels all proper labels and the plot a title. 
- In a plot named `line_plot`, make a line plot mapping the same variables but specify a line size of 1 and a grey colour. 

<codeblock id="05_19">

- Are you using `mark_point(size=50)`?
- Are you setting `alt.X('date', title="Date"))`?
- Are you setting `alt.Y('total_rain_mm',title='rainfall total for the month (mm)')`?
- In the  plot, are you coding `alt.Color('mean_temp', title=' Mean Temperature', scale=alt.Scale(scheme='blueorange'))`?
- Are you setting a title in `properties()`?
- In `line_plot` are you specifying `mark_line(size=1, color='grey')`?

</codeblock>

**Question**      
Do colder months tend to have higher or lower levels of rainfall?


<choice id="1" >
<opt text="Lower"" correct="true">

Cool as a cucumber! 

</opt>

<opt text="Higher" >

Maybe take a look at your graph?

</opt>

</choice>

Can you think of why this might occurs?

</exercise>

<exercise id="20" title="Using Colour to Highlight Data" type="slides,video">
<slides source="module5/module5_20" shot="1" start="0:003" end="07:12"> </slides>
</exercise>


<exercise id="21" title="True or False: Colouring in Black or White">

**True or False**       
*Within the colour channel, we can simply set `color='blue'` or `color='yellow'` if we want a specific plot colour.*

<choice id="1" >

<opt text="True"  >

When using a colour channel, we need to make sure that we use `alt.value('blue')` to specify a colour or Altair will think you are trying to add a variable to a colour channel instead of a static colour. 

</opt>

<opt text="False" correct="true">

Right! When using a colour channel, we need to make sure that we use `alt.value('blue')` to specify a colour. 

</opt>

</choice>


**True or False**       
*An entire aesthetic of a plot can be changed by styling multiple visual components at a time by applying a theme.*


<choice id="2" >

<opt text="True" correct="true">

🎉.

</opt>

<opt text="False">

Take a look at the last slide. This is a cool technique to know!

</opt>


</choice>

</exercise>


<exercise id="22" title="Texting and Selecting">

**Question 1**      
the `.condition()` Altair method acts like which of the following Python Syntax? 



<choice id="1" >
<opt text="A <code>for</code> loop"  >

Not a for loop. What does `.condition()` relate to?

</opt>

<opt text="An if-else statement" correct="true">

You are on a roll!

</opt>

<opt text="the assignment operator">

Nope. Think about the name of the method. 

</opt>

<opt text="A dictionary">

This is a data structure, think about an action that is occurring.

</opt>

</choice>


**Question 2**      
How would we format text on a graph so that it displays ***dollar*** values to 2 significant figures and removes any trailing zeros? <br>
Which of the following is most appropriate?


<choice id="2" >
<opt text="<code>format='$.2,d'</code>">

This will produce 2 significant figures and will round to the nearest integer.

</opt>

<opt text="<code>format='.2s-'</code>">

This is missing the dollar sign and the `s` is in the wrong location. We also do not use `-` for the removal of trailing zeros.

</opt>

<opt text="<code>format='$.2~s'</code>" correct="true">

🏆.

</opt>


<opt text="<code>format='.2~s'</code>">

You are close! You are missing the dollar sign!

</opt>

</choice>



</exercise>

<exercise id="23" title="Precipitation Contemplation">


**Instructions:**    
Be patient when running a coding exercise for the first time, it can take a few minutes. 

**When you see `____` in a coding exercise, replace it with what you assume to be the correct code. Run the code to see if you obtain the desired output
and submit it to validate if you were correct.**


Let's take a look again at the [Government of Canada](https://climate.weather.gc.ca/) data that contains the weather in Ottawa from 2008-2010.
We left off seeing that precipitation was higher in the hotter months.

<codeblock id="temperatures2">

</codeblock>

For the 3 years of data, Let's find out the total rainfall in each month. So between the years 2008 and 2010, how much precipitation was there in total during all the Januarys, Februarys, etc?  Remember that we will have to aggregate values here. 

Tasks: 

Fill in the blanks in the code below so that the following gets accomplished:


- In a plot named `rain_plot`, use the data source `temps_df` to make a bar plot.
- Map the month on the y-axis and the sum of all the precipitation for each month on the x-axis. Print your chart first and examine which month has the most precipitation.
- Color `rain_plot` by designating a different colour bar to the month with the highest rainfall.
- Make sure you are giving the x-axis an appropriate label and the plot a title. 
- In a second plot named `text_plot`, add text to each bar that shows the aggregate precipitation for each month and format it so it includes integer values only. Make sure it is aligned to the left and located 4 units to the right of the bar (use `dx` for this).  Set the text colour as black.

<codeblock id="05_23">

- Are you using `mark_bar()`?
- Are you setting `alt.X('sum(total_precipitate_mm)', title="Total precipitate per month (mm)")`?
- Are you setting `alt.Y('month', sort=list(month_name), title=None)`?
- Are you setting `color=alt.condition(alt.datum.month == 'September', alt.value('colour1'), alt.value('colour2')`?
- Are you setting a title in `.properties()`?
- In the text plot, are you coding `mark_text(align='left', dx=5)`?
- Are you setting ` text=alt.Text('sum(total_precipitate_mm)', format='d')`?
- Are you setting the colour to black using `color = alt.value('black')`? 

</codeblock>



**Question**      
Now we know the month with the highest rainfall collectively, what kind of plot would you expect for snowfall?

<choice id="1" >
<opt text="A similarly shaped plot" >

If it's raining, it's likely not snowing in Ottawa.

</opt>

<opt text="a plot that looks like the inverse of this one" correct="true">

Nice!

</opt>

<opt text="A uniform looking distribution (all similar argregated values)" >

Snow in July?

</opt>

</choice>


</exercise>

<exercise id="24" title="What Did We Just Learn?" type="slides, video">
<slides source="module5/module5_end" shot="0" start="04:5307" end="05:5911"></slides>
</exercise>