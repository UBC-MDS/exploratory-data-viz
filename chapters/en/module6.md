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

when explaining insights, it's important that we communicate them in a way that the audience understands.

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
What is *NOT* an effective method to help make your storytelling more effective?

<choice id="1" >
<opt text="Concentrating on the most exciting discoveries of your analysis and exagerate them." correct="true">

Yikes! Never exaggerate any of your findings. Remember the reading is trusting you to represent the data truthfully. 

</opt>

<opt text="Using striking visualizations to capture the audience's attention."  >

This can be effective since and follow-up questions can help tell a story.

</opt>

<opt text="Recaping the insights discovered at the end of your analysis." >

This is a great thing to do to remind the reader of what was covered. 

</opt>

<opt text="Preemptively covering topics or answering questions you think the reader may have about the data." >

It's a great idea to try and supply the ready with answers they may want. 

</opt>

</choice>

</exercise>



<exercise id="4" title="Analysis Narrative - Short Stories">

**Question 1**      
Take a look at the plot below that visualizes hotel bookings data, in particular the number of guests and the number of days rooms were booked in advance.

<center>
<img src="/module6/hotel.svg" width="70%"></img>
</center>

(Attribution: These plots were created using [a Kaggle dataset](https://www.kaggle.com/jessemostipak/hotel-booking-demand?select=hotel_bookings.csv) where the data was originally obtained from the article [Hotel Booking Demand Datasets](https://www.sciencedirect.com/science/article/pii/S2352340918315191), written by Nuno Antonio, Ana Almeida, and Luis Nunes for Data in Brief, Volume 22, February 2019.)


Which of the following is the best narrative approach to the visualization above?


<choice id="1" >
<opt text="Due to the majority of single stays being business related, it's clear that single guest stays need less advanced booking time then bookings with multiple guests.">

This narrative is jumping to conclusions regarding the single stays being business-related. We have no information on that displayed here.

</opt>

<opt text="In comparison to single and many guest bookings, the distribution of bookings for couples has a much longer right tail. This is likely due to parents needing more time to organize for child care accomodation for their children when they go on vacation together. "  >

Again this seems to be jumping to conclusions on a very specific reason that may not be accurate.

</opt>

<opt text="Looking at the hotel bookings from single guests, the distribution appears to have a large peak at values less than 50 days in advance. This leads us to further questions regarding the nature of the booking. Are they booked through travel agents or by a corporate company? How long are they stays on average?" correct="true">

You got it!

</opt>

<opt text="Single guest bookings generally are booked far less in advance than multiple guest bookings." >

This is just an observation here, there doesn't seem to be any storytelling or narrative to keep the readers' engagement.

</opt>

</choice>


**Question 2**      

We then follow up on our dataset and decide to answer some questions that were brought to light. Are most bookings for a single guest business-related? This leads up to make the following visualizations. 





<img src="/module6/hotelsing.svg" width="80%"></img>





<img src="/module6/hotelmult.svg" width="80%"></img>


Which narrative is more suitable to explain the plots above?



<choice id="2" >
<opt text="After plotting the booking method for single guest stays, we can confirm that a large porportion of the bookings were done corporately. This explains the distribution in the previous question and why single guest stays are booked less time in advance." >

Do we need to know all the categories?

</opt>

<opt text="Now that we can see the porportion of booking methods more clearly, it appears that a much large  porportion of single guest stays, are booked through a corporate setting than for multiple guest bookings. However, it is possible that the data is underestimating the the number of business-related bookings for single guest travel stays, as not all business-stays need to be booked via corporate booking services but without additional data, we cannot confirm this." correct="true">

Nice!

</opt>

</choice>

</exercise>


<exercise id="5" title="Visualizing geographical data" type="slides,video">
<slides source="module6/module6_02" shot="1" start="0:003" end="07:12"> </slides>
</exercise>

<exercise id="6" title="True or False: Getting Geo With It!">

**True or False**       
*If we want to look more closely at certain countries instead of the whole globe, Altair uses the `scale` argument to zoom in to our desire geographical area.*


<choice id="1" >

<opt text="True" correct="true">

Killing it here!

</opt>


<opt text="False"  >

We can use the arguments `scale` and `translate` to zoom and pan closer into a map. 

</opt>


</choice>

**True or False**       
*With Altair geographical visualizations, we are restricted to choropleth maps.*

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

Which of the following projection types would have been used to create this plot?


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

This type is used with the `countries` feature type and focuses on correctly representing the relative areas of all landmasses.

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




We were introduced to the Gapminder dataset in previous modules as well as the assignments as although we have data about the world, we have yet to actually plot it as a map! 

We have altered this dataset a bit to only include data from 2018 (there should only be 1 row for each country now) and we also added a new `id` column which contains the [ISO 3166-1 numeric code](https://en.wikipedia.org/wiki/ISO_3166-1_numeric) for each country. 

<codeblock id="gapminder_codes">

</codeblock>


Before we start plotting the data from the `gapminder_df`, let's first make sure we know how to make a map of the world without any statistics. 

Tasks: 

Fill in the blanks in the code below so that the following gets accomplished:

- Load the `countries` TopoJSON file from the `vega_datasets` library and save it as an object named `world_df` respectively. 
-  In a plot named `world_plot`, use the data source `world_df` to make a `.geo_shape()` visualization with a projection type of `equalEarth`. Make sure the plot has the height and width dimensions of 580 and 400 respectively. 

<codeblock id="06_08a">

- Are you using the method `.topo_feature()` to load in the lada and selecting `countries`? 
- In the plot, are you using `.mark_geoshape()`?
- Are you setting `type="equalEarth"` within `.project()`?
- We are 

</codeblock>

Great we have a map! What if we want to add some statistics though? We have looked at various statistics in the past, but for this question, let's look at each country's population density.
We want to visualize all the countries and if they are above or below the global median of  life expectancy of 72 years (in 2018).
This might help us see clearly if there are any particular geographical locations that are higher or lower than the global average.

Tasks: 

Fill in the blanks in the code below so that the following gets accomplished:

- Load 2 sources of data; the `gapminder_codes.csv` data that contains all the global statistics, and the `countries` TopoJSON file from the `vega_datasets` library. Name each data source `gapminder_df`and `world_df` respectively. 
- In a plot named `pop_dense_plot`, use the data source `world_df` to make a `.geo_shape()` visualization that maps the `pop_density` of each country to a colour channel. Use a [colour scheme](https://vega.github.io/vega/docs/schemes/) you find appropriate (we recommend a diverging scheme) with the domain midpoint at the global median (81).
- In order to combine the two sources, you will need to use `transform_lookup()` to lookup the two columns `pop_density` from the `gapminder_df` data using `id` as the connecting column.
- Finally, make sure that you are zooming in with a scale of 80 and panning to , respectively. 

<codeblock id="06_08b">

- In the plot, are you using `.mark_geoshape()`?
- In the plot, are you specifying ` alt.Color('pop_density:Q', scale=alt.Scale(scheme='blueorange', domainMid=81))`?
- Are you setting `lookup='id'` and `from_=alt.LookupData(gapminder_df, "id", ['pop_density'])` within `.transform_lookup()`?
- Are you setting `scale=80` within `.project()`?


</codeblock>

**Question**      

Looking at the plot above, which narrative is most appropriate?


<choice id="1" >
<opt text="Countries from Europe and parts of Asia and Africa appear to have population densities above the global average. This could be due to higher populations or less land area. In comparison, Canada (our home and native land) has a relatively low population density."  correct="true">

Nice

</opt>

<opt text="Although countries in South America appear to have the lowest population density globally, it's appears they also have the greatest range of densities spanning from as low as 2 all the way over 1000." >

We cannot jump to this conclusion without seeing any evidence of it!It's not clear that there is a large range of population densities for countries in South America.

</opt>

<opt text="Countries in Oceania appear to have the most countries with the highest population densities. That being said, these countries also tend to be farming countries and responsible to the export of grains and food products."  >

We cannot jump to this conclusion without seeing any evidence of it! This statement was completely fabricated.

</opt>

</choice>

</exercise>


<exercise id="9" title="Figure layouts" type="slides,video">
<slides source="module6/module6_03" shot="1" start="0:003" end="07:12"> </slides>
</exercise>


<exercise id="10" title="True or False: Concatenating Plots">

**True or False**       
*Using `alt.hconcat()` and `&` will both arrange plots side by side horizontally.*


<choice id="1" >

<opt text="True" >

 `&` concatenates plots vertically.

</opt>


<opt text="False"  correct="true">

🏅

</opt>


</choice>

**True or False**       
*When concatenating plots, each visualization in the presentation should have its own separate title.*

<choice id="2" >

<opt text="True"  >

When plotting for communication, sometimes having a single title for multiple plots communicates your insights most effectively. 

</opt>

<opt text="False" correct="true">

Nice. 

</opt>

</choice>

</exercise>


<exercise id="11" title="Lay it All Out!">

Bringing back the hotel data that we saw from exercise 4, We've made a couple of different layouts with 3 visualizations. 

(Attribution: These plots were created using [a Kaggle dataset](https://www.kaggle.com/jessemostipak/hotel-booking-demand?select=hotel_bookings.csv) where the data was originally obtained from the article [Hotel Booking Demand Datasets](https://www.sciencedirect.com/science/article/pii/S2352340918315191), written by Nuno Antonio, Ana Almeida, and Luis Nunes for Data in Brief, Volume 22, February 2019.)

**Question 1**      
Looking at the presentation below which code will produce the layout shown?

<center>
<img src="/module6/layout1.svg" width="80%"></img>
</center>

<choice id="1" >

<opt text="<code>plot_A | plot_B & plot_C</code>">

Remember that the `&` operator has a higher priority than `|`!

</opt>

<opt text="<code>plot_A | (plot_B & plot_C)</code>" >

Maybe switch up where the brackets should be?

</opt>


<opt text="<code>(plot_A | plot_B) & plot_C</code>" correct="true">

Nailed it!

</opt>


<opt text="<code>(plot_A & plot_B) | plot_C</code>">

I think you got the symbols mixed up!

</opt>

</choice>


**Question 2**      
How would we combine the plots `plot_A`, `plot_B` and  `plot_C` to create the layout below?     
(*Hint: Two options are possible!*)

<center>
<img src="/module6/layout2.svg" width="80%"></img>
</center>

<choice id="2" >
<opt text="<code>plot_A | plot_B & plot_C</code>" correct="true">

Good work! We could also have done <code>plot_A | (plot_B & plot_C)</code>

</opt>

<opt text="<code>plot_A | (plot_B & plot_C)</code>"  correct="true">

Nice! code>plot_A | plot_B & plot_C</code> could also work too since the `&` operator has higher priority than `|`!

</opt>


<opt text="<code>plot_A & (plot_B | plot_C)</code>">

I think you are mixing up your symbols!

</opt>


<opt text="<code>(plot_A | plot_B) & plot_C</code>">

Check if you've got brackets in the right place!

</opt>

</choice>

</exercise>


<exercise id="12" title="Placing Penguins Properly">


**Instructions:**    
Be patient when running a coding exercise for the first time, it can take a few minutes. 

**When you see `____` in a coding exercise, replace it with what you assume to be the correct code. Run the code to see if you obtain the desired output
and submit it to validate if you were correct.**


We've worked with the penguin dataset quite a lot in this course and it only makes sense now to combine some of the plots we've made already into one combined presentation. 

<codeblock id="penguins">

</codeblock>

Here we have 4 plots that we have made in the previous modules (or similar to these) that we want to combine together so that the first plots lies at the top of the presentation followed by a second row that contains 2 plots side by side and end with a bottom row with the last plot.
It should appear something like this: 

<center>
<img src="/module6/penguin_layout.svg" width="70%"></img>
</center>

Tasks: 

Fill in the blanks in the code below so that the following gets accomplished:

- From the given plots `mass_density_plot`, `masss_boxplot`, `penguin_heatmap` and `culmen_facet_plot`, arrange them so they look like the image above. 

<codeblock id="06_12">

- Are you specifying `culmen_facet_plot` first and combining `mass_boxplot` and  `penguin_heatmap` together with brackets followed by `mass_density_plot`?
- Are you using the `&` operator to stack charts vertically and `|` to align them side by side?


</codeblock>

</exercise>



<exercise id="24" title="What Did We Just Learn?" type="slides, video">
<slides source="module6/module6_end" shot="0" start="11:38" end="12:27"></slides>
</exercise>