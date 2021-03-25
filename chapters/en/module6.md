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
<slides source="module6/module6_00" shot="0" start="10:582" end=11:38"> </slides>
</exercise>

<exercise id="1" title="Telling Stories with Visualization" type="slides,video">
<slides source="module6/module6_01" shot="1" start="0:003" end="07:12"> </slides>
</exercise>

<exercise id="2" title="True or False: Once Upon a Time ...">

**True or False**       
*When telling a narrative for data analysis, it's important to adjust the technical verbiage for the respective reader.*


<choice id="1" >

<opt text="True" correct="true">

You got it!

</opt>


<opt text="False"  >

when explaining insights, it's important that we communicate it in a way that the audience understands.

</opt>


</choice>

**True or False**       
*Telling a narrative around data and data visualizations may sometimes lead to additional questions.*

<choice id="2" >

<opt text="True"  correct="true">

Right on!

</opt>

<opt text="False" >

Stories and narratives attempt to answer an initial question but can sometimes lead us down the path of "why?" or additional questions regarding what we discovered. 

</opt>

</choice>

</exercise>


<exercise id="3" title="...Happily Ever After: Narrative Components">

**Question**      
What in *NOT* an effective method to help make your story telling more effective?

<choice id="1" >
<opt text="Concentrating on the most exciting discoveries of your analysis and exagerate them." correct="true">

Yike! Never exagerate any of your findings. Remember the reading is trusting you to represent the data truthfully. 

</opt>

<opt text="Using striking visualizations to capture the audience's attention."  >

This can be effective  asking follow up questions can help tell a story.

</opt>

<opt text="Recaping the insignts discovered at the end of your analysis." >

This is a great thing to do to remind the reader what was covered. 

</opt>

<opt text="Preemptively covering topics or answering questions you think the reader may have about the data." >

It's a great idea to try and supply the ready with answers they may want. 

</opt>

</choice>

</exercise>



<exercise id="4" title="Analysis Narrative - Short Stories">

**Question 1**      
Take a look at the plot below that contains the data for hotel bookings and the number of days in advance they were booked. 

<center>
<img src="/module6/hotel.svg" width="70%"></img>
</center>

(Attribution: These plots were created using [a Kaggle dataset](https://www.kaggle.com/jessemostipak/hotel-booking-demand?select=hotel_bookings.csv) where the data was originally obtained from the article [Hotel Booking Demand Datasets](https://www.sciencedirect.com/science/article/pii/S2352340918315191), written by Nuno Antonio, Ana Almeida, and Luis Nunes for Data in Brief, Volume 22, February 2019.)


Which of the following is the best narrative approach to the visualization above?


<choice id="1" >
<opt text="Due to the majority of single stays being business related, it's clear that single guest stays need less advanced booking time then bookings with multiple guests.">

This narrative is jumping to conclusions regarding the single stays being business related. We have no information on that displayed here.

</opt>

<opt text="In comparison to single and many guest bookings, the distribution of bookings for couples has a much longer right tail. This is likely due to parents needing more time to organize for child care accomodation for their children when they go on vacation together. "  >

Again this seems to be jumping to conclusions on a very specific reason that may not be accurate.

</opt>

<opt text="Looking at the hotel bookings from single guests, it appears that they require less advance notice for their stays. This leads us to further questions regarding the nature of the booking. Are they booked through travel agents or by a corporate company? How long are they stays on average?" correct="true">

You got it!

</opt>

<opt text="Single guest bookings generally are booked far less in advance than multiple guest bookings." >

This is just an observation here, there doesn't seem to be any story telling or narrative to keep the readers engagement.

</opt>

</choice>


**Question 2**      

We then follow up on our dataset and decide to answer some questions that were brought to light. Are most bookings for a single guest business related? This lead up to make the following visualizations. 





<img src="/module6/hotelsing.svg" width="80%"></img>





<img src="/module6/hotelmult.svg" width="80%"></img>


Which narrative is more suitable to explain the plots above?



<choice id="2" >
<opt text="After plotting the booking method for single guest stays, we can confirm that a large porportion of the bookings were done corporately. This explains the distribution in the previous question and why single guest stays are booked less time in advance." >

Do we need to know all the categories?

</opt>

<opt text="Now that we can see the porportion of booking methods more clearly, it appears that less than 20% of single guest stays, are booked through a corporate setting. Other reasons beside business that might reflect the need for less time in advance to book could be that it's easier to book for single individuals as it requires less scheduling alignment. Single individuals may also be more flexible since they have less arrangements to make with other responsibilities such as childcare." correct="true">

Nice!

</opt>

</choice>

</exercise>


<exercise id="5" title="Visualizing geographical data" type="slides,video">
<slides source="module6/module6_02" shot="1" start="0:003" end="07:12"> </slides>
</exercise>

<exercise id="6" title="True or False: Getting Geo With It!">

**True or False**       
*If we are interested in certain contries, Altair gives up the ability to display these locations zoomed in.*


<choice id="1" >

<opt text="True" >

Sometimes removing categories can help communicate better and more effectively.

</opt>


<opt text="False"  correct="true">

Clever!

</opt>


</choice>

**True or False**       
*With Altair geographical visualizations, we are restricted to chloropleth maps.*

<choice id="2" >

<opt text="True"  >

If we have the necessary columns (such as `latitude` and `longitude`) we can use different channels and are less restricted in our visualizations. 

</opt>

<opt text="False" correct="true">

Depending on which columns we have, (such as `latitude` and `longitude`) we can use different visualization channels!

</opt>

</choice>

</exercise>


<exercise id="7" title="Where Are We, With Geography?">

**Question 1**      
Below we see a map showing the location of all the airports in the USA. 
<br>
[**Attribution**](https://altair-viz.github.io/gallery/airports.html)

Which of the following projections types would have been used to create this plot?


<iframe src="/module6/airports.html" width="100%" height="580px">
</iframe>

<choice id="1" >
<opt text="<code>FlatUsa</code>">

Not quite. We made this one up and is not a type of projection. 

</opt>

<opt text="<code>albers</code>">

This is a U.S.-centric configuration of "conicEqualArea" and would not produce a map as clear as the one above.

</opt>

<opt text="<code>equalEarth</code>">

This type is use with the `countries` feature type and focuses on correctly representing the relative areas of all landmasses.

</opt>


<opt text="<code>albersUsa" correct="true">

🎉 !

</opt>

</choice>


**Question 2**      
Which of the following methods is needed for all map visualizations?

<choice id="2" >
<opt text="<code>.project()</code>">

This isn't needed since if omitted, the default projection of `mercator` will result. 

</opt>

<opt text="<code>.mark_geoshape()</code>" correct="true">

Nice!

</opt>


<opt text="<code>.LookupData()</code>">

This is only needed if we need 2 data sources.

</opt>


<opt text="<code>.transform_lookup()</code>">

This is only needed if we need 2 data sources.

</opt>

</choice>

</exercise>


<exercise id="8" title="Geography with Gapminder">


**Instructions:**    
Be patient when running a coding exercise for the first time, it can take a few minutes. 

**When you see `____` in a coding exercise, replace it with what you assume to be the correct code. Run the code to see if you obtain the desired output
and submit it to validate if you were correct.**


We were introduced to the Gapminder dataset in previous modules as well as the assignments as although we have data about the world, we have yet to actually plot is as a map! 

We have altered this dataset a bit to only include data from 2018 (there should only be 1 row for each country now) and we also added a new `id` column which contains the [ISO 3166-1 numeric code](https://en.wikipedia.org/wiki/ISO_3166-1_numeric) for each country. 

<codeblock id="gapminder_codes">

</codeblock>


We have looked at various statistics in the passed, but for this question, let's look at each country's average life expectancy.
We want to visualize all the countries and if they are above of below the global average life expectancy of 72 years (in 2018).
This might help us see clearly if there are any particular geographical location that are higher or lower than the global average.

Tasks: 

Fill in the blanks in the code below so that the following gets accomplished:

- Load 2 sources of data; the `gapminder_codes.csv` data that contains all the global statistics, and the `countries` TopoJSON file from the `vega_datasets` library. Name each data source `gapminder_df`and `world_df` respectively. 
- In a plot named `world_plot`, use the data source `world_df` to make a "geo_shape" visualization that maps the `life_expectancy` of each country to a colour channel. Use a [colour scheme](https://vega.github.io/vega/docs/schemes/) you find appropriate (we recommend a diverging scheme) with the domain midpoint at the global average (72 years) and assign the `life_expectancy` and  `country` to a tooltip channel. 
- In order to combine the two sources, you will need to use `transform_lookup()` to lookup the two columns `life_expectancy` and  `country` from the `gapminder_df` data using `id` as the connecting column.
- Finally makesure that your are projecting using an `equalEarth` map appearance. 

<codeblock id="06_08">

- In the text plot, are you using `.mark_geoshape()`?
- In the text plot, are you specifying ` alt.Color("life_expectancy:Q", scale=alt.Scale(scheme="redblue", domainMid=72))`?
- Are you setting the tooltip channel to `tooltip=[alt.Tooltip("country:N", title="Country"),alt.Tooltip("life_expectancy:Q", title="Life Expectancy (years)")]`?
- Are you setting `lookup="id"` and `from_=alt.LookupData(gapminder_df, "id", ["life_expectancy", 'country'])` within `.transform_lookup()`?
- Are you setting `type="equalEarth"` within `.project()`?


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
<slides source="module6/module6_end" shot="0" start="11:38" end="12:27"></slides>
</exercise>
