---
title: 'Module 4: Visualizing Distributions and Exploratory Data Analysis'
description:
  'In this module we will be learning about how to visualize two dimensional and categorical distributions of data as well as how to perform exploratory data analysis.'
prev: ../../module3
next: ../../module5
type: chapter
id: 4
---

<exercise id="0" title="Module Learning Outcomes"  type="slides, video">
<slides source="module4/module4_00" shot="0" start="3:5707" end="4:5306"> </slides>
</exercise>

<exercise id="1" title="Visualizing Multidimensional Distributions" type="slides,video">
<slides source="module4/module4_01" shot="2" start="0:003" end="09:17"> </slides>
</exercise>

<exercise id="2" title="True or False: Plotting Multiple Numerical Columns">

**True or False**       
*Using a scatterplot to visualize the relationship between 2 numeric columns will always result in overplotting.*


<choice id="1" >

<opt text="True" >

Sometimes using a scatterplot helps avoid overplotting but in other cases, it can still cause saturated areas and no meaningful insights will be able to be observed.

</opt>


<opt text="False"  correct="true">

You've been paying attention!

</opt>


</choice>

**True or False**       
*We can use density plots to examine the distributions between 2 numeric columns using Altair*

<choice id="2" >

<opt text="True"  >

Altair currently cannot be used to create 2D density plots, but can be done using a plotting package called Seaborn. 

</opt>

<opt text="False" correct="true">

You are on a roll!

</opt>

</choice>

</exercise>


<exercise id="3" title="Which Plot Is It?">

**Question 1**      
If we are interested in visualizing the relationship between two **numeric/quantitative** columns, which plot type is most appropriate?

<choice id="1" >
<opt text="Histogram">

This can be used to visualize a single numeric column's distribution.

</opt>

<opt text="Violin plot" >

This can be used to visualize a single numeric column's distribution.

</opt>

<opt text="boxplot" >

This can be used to visualize a single numeric column's distribution.

</opt>


<opt text="Scatterplot" correct="true">

You got it!

</opt>

</choice>


**Question 2**      
Which plots are most ideal for visualizing the relationship between 2 numeric column distributions where overplotting is an issue?


<choice id="2" >
<opt text="A single heatmap" correct="true">

Nailed it! 

</opt>

<opt text="A single barplot">

This can be used to visualize categorical “distributions”.

</opt>

<opt text="A single bubble plot">

This doesn't quite show the distributions of the columns well. 

</opt>


<opt text="Scatter plot">

This one is less informative if overplotting is present. 

</opt>

</choice>

</exercise>


<exercise id="4" title="Graph Analysis">

Look at the plot below and answer the following questions.  


<?xml version="1.0" encoding="utf-8"?>
<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" version="1.1" class="marks" width="614" height="364" viewBox="0 0 614 364"><rect width="614" height="364" fill="white"/><g fill="none" stroke-miterlimit="10" transform="translate(51,27)"><g class="mark-group role-frame root" role="graphics-object" aria-roledescription="group mark container"><g transform="translate(0,0)"><path class="background" aria-hidden="true" d="M0.5,0.5h400v300h-400Z" stroke="#ddd"/><g><g class="mark-rect role-mark marks" role="graphics-object" aria-roledescription="rect mark container"><path aria-label="Count of Records: 7; Defense Score: 45 – 50; Attack Score: 45 – 50" role="graphics-symbol" aria-roledescription="rect mark" d="M71.61111111111111,225.5h8.888888888888886v8.333333333333343h-8.888888888888886Z" fill="rgb(37, 139, 187)"/><path aria-label="Count of Records: 10; Defense Score: 60 – 65; Attack Score: 60 – 65" role="graphics-symbol" aria-roledescription="rect mark" d="M98.27777777777777,200.50000000000003h8.8888888888889v8.333333333333286h-8.8888888888889Z" fill="rgb(28, 49, 133)"/><path aria-label="Count of Records: 6; Defense Score: 120 – 125; Attack Score: 100 – 105" role="graphics-symbol" aria-roledescription="rect mark" d="M204.94444444444443,133.83333333333331h8.888888888888914v8.333333333333343h-8.888888888888914Z" fill="rgb(55, 168, 193)"/><path aria-label="Count of Records: 8; Defense Score: 40 – 45; Attack Score: 50 – 55" role="graphics-symbol" aria-roledescription="rect mark" d="M62.72222222222222,217.16666666666666h8.888888888888893v8.333333333333343h-8.888888888888893Z" fill="rgb(33, 106, 173)"/><path aria-label="Count of Records: 3; Defense Score: 55 – 60; Attack Score: 60 – 65" role="graphics-symbol" aria-roledescription="rect mark" d="M89.38888888888889,200.50000000000003h8.888888888888886v8.333333333333286h-8.888888888888886Z" fill="rgb(180, 225, 182)"/><path aria-label="Count of Records: 3; Defense Score: 75 – 80; Attack Score: 100 – 105" role="graphics-symbol" aria-roledescription="rect mark" d="M124.94444444444444,133.83333333333331h8.888888888888872v8.333333333333343h-8.888888888888872Z" fill="rgb(180, 225, 182)"/><path aria-label="Count of Records: 5; Defense Score: 65 – 70; Attack Score: 45 – 50" role="graphics-symbol" aria-roledescription="rect mark" d="M107.16666666666667,225.5h8.888888888888872v8.333333333333343h-8.888888888888872Z" fill="rgb(89, 189, 192)"/><path aria-label="Count of Records: 3; Defense Score: 80 – 85; Attack Score: 60 – 65" role="graphics-symbol" aria-roledescription="rect mark" d="M133.83333333333331,200.50000000000003h8.888888888888914v8.333333333333286h-8.888888888888914Z" fill="rgb(180, 225, 182)"/><path aria-label="Count of Records: 4; Defense Score: 35 – 40; Attack Score: 30 – 35" role="graphics-symbol" aria-roledescription="rect mark" d="M53.833333333333336,250.5h8.888888888888886v8.333333333333371h-8.888888888888886Z" fill="rgb(134, 208, 187)"/><path aria-label="Count of Records: 1; Defense Score: 55 – 60; Attack Score: 20 – 25" role="graphics-symbol" aria-roledescription="rect mark" d="M89.38888888888889,267.16666666666663h8.888888888888886v8.333333333333371h-8.888888888888886Z" fill="rgb(239, 249, 189)"/><path aria-label="Count of Records: 5; Defense Score: 50 – 55; Attack Score: 45 – 50" role="graphics-symbol" aria-roledescription="rect mark" d="M80.5,225.5h8.888888888888886v8.333333333333343h-8.888888888888886Z" fill="rgb(89, 189, 192)"/><path aria-label="Count of Records: 4; Defense Score: 30 – 35; Attack Score: 35 – 40" role="graphics-symbol" aria-roledescription="rect mark" d="M44.94444444444444,242.16666666666669h8.888888888888893v8.333333333333314h-8.888888888888893Z" fill="rgb(134, 208, 187)"/><path aria-label="Count of Records: 1; Defense Score: 50 – 55; Attack Score: 25 – 30" role="graphics-symbol" aria-roledescription="rect mark" d="M80.5,258.83333333333337h8.888888888888886v8.333333333333258h-8.888888888888886Z" fill="rgb(239, 249, 189)"/><path aria-label="Count of Records: 1; Defense Score: 40 – 45; Attack Score: 150 – 155" role="graphics-symbol" aria-roledescription="rect mark" d="M62.72222222222222,50.499999999999986h8.888888888888893v8.333333333333343h-8.888888888888893Z" fill="rgb(239, 249, 189)"/><path aria-label="Count of Records: 7; Defense Score: 40 – 45; Attack Score: 45 – 50" role="graphics-symbol" aria-roledescription="rect mark" d="M62.72222222222222,225.5h8.888888888888893v8.333333333333343h-8.888888888888893Z" fill="rgb(37, 139, 187)"/><path aria-label="Count of Records: 4; Defense Score: 80 – 85; Attack Score: 80 – 85" role="graphics-symbol" aria-roledescription="rect mark" d="M133.83333333333331,167.16666666666669h8.888888888888914v8.333333333333286h-8.888888888888914Z" fill="rgb(134, 208, 187)"/><path aria-label="Count of Records: 4; Defense Score: 35 – 40; Attack Score: 55 – 60" role="graphics-symbol" aria-roledescription="rect mark" d="M53.833333333333336,208.83333333333331h8.888888888888886v8.333333333333343h-8.888888888888886Z" fill="rgb(134, 208, 187)"/><path aria-label="Count of Records: 9; Defense Score: 70 – 75; Attack Score: 70 – 75" role="graphics-symbol" aria-roledescription="rect mark" d="M116.05555555555554,183.83333333333334h8.8888888888889v8.333333333333314h-8.8888888888889Z" fill="rgb(35, 74, 158)"/><path aria-label="Count of Records: 4; Defense Score: 30 – 35; Attack Score: 60 – 65" role="graphics-symbol" aria-roledescription="rect mark" d="M44.94444444444444,200.50000000000003h8.888888888888893v8.333333333333286h-8.888888888888893Z" fill="rgb(134, 208, 187)"/><path aria-label="Count of Records: 5; Defense Score: 65 – 70; Attack Score: 90 – 95" role="graphics-symbol" aria-roledescription="rect mark" d="M107.16666666666667,150.5h8.888888888888872v8.333333333333343h-8.888888888888872Z" fill="rgb(89, 189, 192)"/><path aria-label="Count of Records: 5; Defense Score: 40 – 45; Attack Score: 60 – 65" role="graphics-symbol" aria-roledescription="rect mark" d="M62.72222222222222,200.50000000000003h8.888888888888893v8.333333333333286h-8.888888888888893Z" fill="rgb(89, 189, 192)"/><path aria-label="Count of Records: 3; Defense Score: 65 – 70; Attack Score: 95 – 100" role="graphics-symbol" aria-roledescription="rect mark" d="M107.16666666666667,142.16666666666666h8.888888888888872v8.333333333333343h-8.888888888888872Z" fill="rgb(180, 225, 182)"/><path aria-label="Count of Records: 6; Defense Score: 40 – 45; Attack Score: 55 – 60" role="graphics-symbol" aria-roledescription="rect mark" d="M62.72222222222222,208.83333333333331h8.888888888888893v8.333333333333343h-8.888888888888893Z" fill="rgb(55, 168, 193)"/><path aria-label="Count of Records: 6; Defense Score: 50 – 55; Attack Score: 85 – 90" role="graphics-symbol" aria-roledescription="rect mark" d="M80.5,158.83333333333334h8.888888888888886v8.333333333333343h-8.888888888888886Z" fill="rgb(55, 168, 193)"/><path aria-label="Count of Records: 3; Defense Score: 90 – 95; Attack Score: 75 – 80" role="graphics-symbol" aria-roledescription="rect mark" d="M151.61111111111111,175.49999999999997h8.888888888888886v8.333333333333371h-8.888888888888886Z" fill="rgb(180, 225, 182)"/><path aria-label="Count of Records: 3; Defense Score: 65 – 70; Attack Score: 60 – 65" role="graphics-symbol" aria-roledescription="rect mark" d="M107.16666666666667,200.50000000000003h8.888888888888872v8.333333333333286h-8.888888888888872Z" fill="rgb(180, 225, 182)"/><path aria-label="Count of Records: 3; Defense Score: 85 – 90; Attack Score: 90 – 95" role="graphics-symbol" aria-roledescription="rect mark" d="M142.72222222222223,150.5h8.888888888888886v8.333333333333343h-8.888888888888886Z" fill="rgb(180, 225, 182)"/><path aria-label="Count of Records: 4; Defense Score: 55 – 60; Attack Score: 70 – 75" role="graphics-symbol" aria-roledescription="rect mark" d="M89.38888888888889,183.83333333333334h8.888888888888886v8.333333333333314h-8.888888888888886Z" fill="rgb(134, 208, 187)"/><path aria-label="Count of Records: 4; Defense Score: 40 – 45; Attack Score: 40 – 45" role="graphics-symbol" aria-roledescription="rect mark" d="M62.72222222222222,233.83333333333334h8.888888888888893v8.333333333333343h-8.888888888888893Z" fill="rgb(134, 208, 187)"/><path aria-label="Count of Records: 3; Defense Score: 75 – 80; Attack Score: 65 – 70" role="graphics-symbol" aria-roledescription="rect mark" d="M124.94444444444444,192.16666666666666h8.888888888888872v8.333333333333371h-8.888888888888872Z" fill="rgb(180, 225, 182)"/><path aria-label="Count of Records: 1; Defense Score: 20 – 25; Attack Score: 45 – 50" role="graphics-symbol" aria-roledescription="rect mark" d="M27.166666666666668,225.5h8.88888888888889v8.333333333333343h-8.88888888888889Z" fill="rgb(239, 249, 189)"/><path aria-label="Count of Records: 5; Defense Score: 45 – 50; Attack Score: 70 – 75" role="graphics-symbol" aria-roledescription="rect mark" d="M71.61111111111111,183.83333333333334h8.888888888888886v8.333333333333314h-8.888888888888886Z" fill="rgb(89, 189, 192)"/><path aria-label="Count of Records: 3; Defense Score: 35 – 40; Attack Score: 45 – 50" role="graphics-symbol" aria-roledescription="rect mark" d="M53.833333333333336,225.5h8.888888888888886v8.333333333333343h-8.888888888888886Z" fill="rgb(180, 225, 182)"/><path aria-label="Count of Records: 5; Defense Score: 70 – 75; Attack Score: 80 – 85" role="graphics-symbol" aria-roledescription="rect mark" d="M116.05555555555554,167.16666666666669h8.8888888888889v8.333333333333286h-8.8888888888889Z" fill="rgb(89, 189, 192)"/><path aria-label="Count of Records: 2; Defense Score: 55 – 60; Attack Score: 50 – 55" role="graphics-symbol" aria-roledescription="rect mark" d="M89.38888888888889,217.16666666666666h8.888888888888886v8.333333333333343h-8.888888888888886Z" fill="rgb(216, 240, 180)"/><path aria-label="Count of Records: 4; Defense Score: 70 – 75; Attack Score: 65 – 70" role="graphics-symbol" aria-roledescription="rect mark" d="M116.05555555555554,192.16666666666666h8.8888888888889v8.333333333333371h-8.8888888888889Z" fill="rgb(134, 208, 187)"/><path aria-label="Count of Records: 2; Defense Score: 85 – 90; Attack Score: 80 – 85" role="graphics-symbol" aria-roledescription="rect mark" d="M142.72222222222223,167.16666666666669h8.888888888888886v8.333333333333286h-8.888888888888886Z" fill="rgb(216, 240, 180)"/><path aria-label="Count of Records: 2; Defense Score: 80 – 85; Attack Score: 95 – 100" role="graphics-symbol" aria-roledescription="rect mark" d="M133.83333333333331,142.16666666666666h8.888888888888914v8.333333333333343h-8.888888888888914Z" fill="rgb(216, 240, 180)"/><path aria-label="Count of Records: 5; Defense Score: 50 – 55; Attack Score: 55 – 60" role="graphics-symbol" aria-roledescription="rect mark" d="M80.5,208.83333333333331h8.888888888888886v8.333333333333343h-8.888888888888886Z" fill="rgb(89, 189, 192)"/><path aria-label="Count of Records: 7; Defense Score: 60 – 65; Attack Score: 65 – 70" role="graphics-symbol" aria-roledescription="rect mark" d="M98.27777777777777,192.16666666666666h8.8888888888889v8.333333333333371h-8.8888888888889Z" fill="rgb(37, 139, 187)"/><path aria-label="Count of Records: 3; Defense Score: 30 – 35; Attack Score: 55 – 60" role="graphics-symbol" aria-roledescription="rect mark" d="M44.94444444444444,208.83333333333331h8.888888888888893v8.333333333333343h-8.888888888888893Z" fill="rgb(180, 225, 182)"/><path aria-label="Count of Records: 6; Defense Score: 60 – 65; Attack Score: 100 – 105" role="graphics-symbol" aria-roledescription="rect mark" d="M98.27777777777777,133.83333333333331h8.8888888888889v8.333333333333343h-8.8888888888889Z" fill="rgb(55, 168, 193)"/><path aria-label="Count of Records: 6; Defense Score: 35 – 40; Attack Score: 35 – 40" role="graphics-symbol" aria-roledescription="rect mark" d="M53.833333333333336,242.16666666666669h8.888888888888886v8.333333333333314h-8.888888888888886Z" fill="rgb(55, 168, 193)"/><path aria-label="Count of Records: 7; Defense Score: 45 – 50; Attack Score: 50 – 55" role="graphics-symbol" aria-roledescription="rect mark" d="M71.61111111111111,217.16666666666666h8.888888888888886v8.333333333333343h-8.888888888888886Z" fill="rgb(37, 139, 187)"/><path aria-label="Count of Records: 2; Defense Score: 75 – 80; Attack Score: 80 – 85" role="graphics-symbol" aria-roledescription="rect mark" d="M124.94444444444444,167.16666666666669h8.888888888888872v8.333333333333286h-8.888888888888872Z" fill="rgb(216, 240, 180)"/><path aria-label="Count of Records: 1; Defense Score: 35 – 40; Attack Score: 80 – 85" role="graphics-symbol" aria-roledescription="rect mark" d="M53.833333333333336,167.16666666666669h8.888888888888886v8.333333333333286h-8.888888888888886Z" fill="rgb(239, 249, 189)"/><path aria-label="Count of Records: 2; Defense Score: 60 – 65; Attack Score: 105 – 110" role="graphics-symbol" aria-roledescription="rect mark" d="M98.27777777777777,125.49999999999999h8.8888888888889v8.333333333333329h-8.8888888888889Z" fill="rgb(216, 240, 180)"/><path aria-label="Count of Records: 2; Defense Score: 80 – 85; Attack Score: 110 – 115" role="graphics-symbol" aria-roledescription="rect mark" d="M133.83333333333331,117.16666666666666h8.888888888888914v8.333333333333329h-8.888888888888914Z" fill="rgb(216, 240, 180)"/><path aria-label="Count of Records: 9; Defense Score: 65 – 70; Attack Score: 65 – 70" role="graphics-symbol" aria-roledescription="rect mark" d="M107.16666666666667,192.16666666666666h8.888888888888872v8.333333333333371h-8.888888888888872Z" fill="rgb(35, 74, 158)"/><path aria-label="Count of Records: 5; Defense Score: 95 – 100; Attack Score: 95 – 100" role="graphics-symbol" aria-roledescription="rect mark" d="M160.5,142.16666666666666h8.888888888888886v8.333333333333343h-8.888888888888886Z" fill="rgb(89, 189, 192)"/><path aria-label="Count of Records: 1; Defense Score: 15 – 20; Attack Score: 20 – 25" role="graphics-symbol" aria-roledescription="rect mark" d="M18.27777777777778,267.16666666666663h8.88888888888889v8.333333333333371h-8.88888888888889Z" fill="rgb(239, 249, 189)"/><path aria-label="Count of Records: 2; Defense Score: 65 – 70; Attack Score: 50 – 55" role="graphics-symbol" aria-roledescription="rect mark" d="M107.16666666666667,217.16666666666666h8.888888888888872v8.333333333333343h-8.888888888888872Z" fill="rgb(216, 240, 180)"/><path aria-label="Count of Records: 5; Defense Score: 50 – 55; Attack Score: 80 – 85" role="graphics-symbol" aria-roledescription="rect mark" d="M80.5,167.16666666666669h8.888888888888886v8.333333333333286h-8.888888888888886Z" fill="rgb(89, 189, 192)"/><path aria-label="Count of Records: 7; Defense Score: 70 – 75; Attack Score: 100 – 105" role="graphics-symbol" aria-roledescription="rect mark" d="M116.05555555555554,133.83333333333331h8.8888888888889v8.333333333333343h-8.8888888888889Z" fill="rgb(37, 139, 187)"/><path aria-label="Count of Records: 4; Defense Score: 80 – 85; Attack Score: 130 – 135" role="graphics-symbol" aria-roledescription="rect mark" d="M133.83333333333331,83.83333333333334h8.888888888888914v8.333333333333329h-8.888888888888914Z" fill="rgb(134, 208, 187)"/><path aria-label="Count of Records: 3; Defense Score: 35 – 40; Attack Score: 75 – 80" role="graphics-symbol" aria-roledescription="rect mark" d="M53.833333333333336,175.49999999999997h8.888888888888886v8.333333333333371h-8.888888888888886Z" fill="rgb(180, 225, 182)"/><path aria-label="Count of Records: 2; Defense Score: 50 – 55; Attack Score: 90 – 95" role="graphics-symbol" aria-roledescription="rect mark" d="M80.5,150.5h8.888888888888886v8.333333333333343h-8.888888888888886Z" fill="rgb(216, 240, 180)"/><path aria-label="Count of Records: 2; Defense Score: 65 – 70; Attack Score: 105 – 110" role="graphics-symbol" aria-roledescription="rect mark" d="M107.16666666666667,125.49999999999999h8.888888888888872v8.333333333333329h-8.888888888888872Z" fill="rgb(216, 240, 180)"/><path aria-label="Count of Records: 1; Defense Score: 35 – 40; Attack Score: 40 – 45" role="graphics-symbol" aria-roledescription="rect mark" d="M53.833333333333336,233.83333333333334h8.888888888888886v8.333333333333343h-8.888888888888886Z" fill="rgb(239, 249, 189)"/><path aria-label="Count of Records: 2; Defense Score: 65 – 70; Attack Score: 70 – 75" role="graphics-symbol" aria-roledescription="rect mark" d="M107.16666666666667,183.83333333333334h8.888888888888872v8.333333333333314h-8.888888888888872Z" fill="rgb(216, 240, 180)"/><path aria-label="Count of Records: 4; Defense Score: 100 – 105; Attack Score: 80 – 85" role="graphics-symbol" aria-roledescription="rect mark" d="M169.38888888888889,167.16666666666669h8.888888888888886v8.333333333333286h-8.888888888888886Z" fill="rgb(134, 208, 187)"/><path aria-label="Count of Records: 2; Defense Score: 115 – 120; Attack Score: 95 – 100" role="graphics-symbol" aria-roledescription="rect mark" d="M196.05555555555554,142.16666666666666h8.888888888888886v8.333333333333343h-8.888888888888886Z" fill="rgb(216, 240, 180)"/><path aria-label="Count of Records: 1; Defense Score: 130 – 135; Attack Score: 120 – 125" role="graphics-symbol" aria-roledescription="rect mark" d="M222.72222222222223,100.50000000000001h8.888888888888857v8.333333333333329h-8.888888888888857Z" fill="rgb(239, 249, 189)"/><path aria-label="Count of Records: 2; Defense Score: 55 – 60; Attack Score: 85 – 90" role="graphics-symbol" aria-roledescription="rect mark" d="M89.38888888888889,158.83333333333334h8.888888888888886v8.333333333333343h-8.888888888888886Z" fill="rgb(216, 240, 180)"/><path aria-label="Count of Records: 1; Defense Score: 180 – 185; Attack Score: 75 – 80" role="graphics-symbol" aria-roledescription="rect mark" d="M311.61111111111114,175.49999999999997h8.888888888888857v8.333333333333371h-8.888888888888857Z" fill="rgb(239, 249, 189)"/><path aria-label="Count of Records: 1; Defense Score: 70 – 75; Attack Score: 35 – 40" role="graphics-symbol" aria-roledescription="rect mark" d="M116.05555555555554,242.16666666666669h8.8888888888889v8.333333333333314h-8.8888888888889Z" fill="rgb(239, 249, 189)"/><path aria-label="Count of Records: 1; Defense Score: 95 – 100; Attack Score: 60 – 65" role="graphics-symbol" aria-roledescription="rect mark" d="M160.5,200.50000000000003h8.888888888888886v8.333333333333286h-8.888888888888886Z" fill="rgb(239, 249, 189)"/><path aria-label="Count of Records: 2; Defense Score: 55 – 60; Attack Score: 90 – 95" role="graphics-symbol" aria-roledescription="rect mark" d="M89.38888888888889,150.5h8.888888888888886v8.333333333333343h-8.888888888888886Z" fill="rgb(216, 240, 180)"/><path aria-label="Count of Records: 2; Defense Score: 45 – 50; Attack Score: 85 – 90" role="graphics-symbol" aria-roledescription="rect mark" d="M71.61111111111111,158.83333333333334h8.888888888888886v8.333333333333343h-8.888888888888886Z" fill="rgb(216, 240, 180)"/><path aria-label="Count of Records: 1; Defense Score: 70 – 75; Attack Score: 110 – 115" role="graphics-symbol" aria-roledescription="rect mark" d="M116.05555555555554,117.16666666666666h8.8888888888889v8.333333333333329h-8.8888888888889Z" fill="rgb(239, 249, 189)"/><path aria-label="Count of Records: 5; Defense Score: 55 – 60; Attack Score: 45 – 50" role="graphics-symbol" aria-roledescription="rect mark" d="M89.38888888888889,225.5h8.888888888888886v8.333333333333343h-8.888888888888886Z" fill="rgb(89, 189, 192)"/><path aria-label="Count of Records: 3; Defense Score: 80 – 85; Attack Score: 70 – 75" role="graphics-symbol" aria-roledescription="rect mark" d="M133.83333333333331,183.83333333333334h8.888888888888914v8.333333333333314h-8.888888888888914Z" fill="rgb(180, 225, 182)"/><path aria-label="Count of Records: 4; Defense Score: 75 – 80; Attack Score: 105 – 110" role="graphics-symbol" aria-roledescription="rect mark" d="M124.94444444444444,125.49999999999999h8.888888888888872v8.333333333333329h-8.888888888888872Z" fill="rgb(134, 208, 187)"/><path aria-label="Count of Records: 1; Defense Score: 100 – 105; Attack Score: 65 – 70" role="graphics-symbol" aria-roledescription="rect mark" d="M169.38888888888889,192.16666666666666h8.888888888888886v8.333333333333371h-8.888888888888886Z" fill="rgb(239, 249, 189)"/><path aria-label="Count of Records: 1; Defense Score: 180 – 185; Attack Score: 95 – 100" role="graphics-symbol" aria-roledescription="rect mark" d="M311.61111111111114,142.16666666666666h8.888888888888857v8.333333333333343h-8.888888888888857Z" fill="rgb(239, 249, 189)"/><path aria-label="Count of Records: 3; Defense Score: 80 – 85; Attack Score: 65 – 70" role="graphics-symbol" aria-roledescription="rect mark" d="M133.83333333333331,192.16666666666666h8.888888888888914v8.333333333333371h-8.888888888888914Z" fill="rgb(180, 225, 182)"/><path aria-label="Count of Records: 1; Defense Score: 160 – 165; Attack Score: 45 – 50" role="graphics-symbol" aria-roledescription="rect mark" d="M276.05555555555554,225.5h8.888888888888914v8.333333333333343h-8.888888888888914Z" fill="rgb(239, 249, 189)"/><path aria-label="Count of Records: 3; Defense Score: 90 – 95; Attack Score: 105 – 110" role="graphics-symbol" aria-roledescription="rect mark" d="M151.61111111111111,125.49999999999999h8.888888888888886v8.333333333333329h-8.888888888888886Z" fill="rgb(180, 225, 182)"/><path aria-label="Count of Records: 2; Defense Score: 115 – 120; Attack Score: 130 – 135" role="graphics-symbol" aria-roledescription="rect mark" d="M196.05555555555554,83.83333333333334h8.888888888888886v8.333333333333329h-8.888888888888886Z" fill="rgb(216, 240, 180)"/><path aria-label="Count of Records: 3; Defense Score: 50 – 55; Attack Score: 30 – 35" role="graphics-symbol" aria-roledescription="rect mark" d="M80.5,250.5h8.888888888888886v8.333333333333371h-8.888888888888886Z" fill="rgb(180, 225, 182)"/><path aria-label="Count of Records: 3; Defense Score: 70 – 75; Attack Score: 50 – 55" role="graphics-symbol" aria-roledescription="rect mark" d="M116.05555555555554,217.16666666666666h8.8888888888889v8.333333333333343h-8.8888888888889Z" fill="rgb(180, 225, 182)"/><path aria-label="Count of Records: 1; Defense Score: 80 – 85; Attack Score: 40 – 45" role="graphics-symbol" aria-roledescription="rect mark" d="M133.83333333333331,233.83333333333334h8.888888888888914v8.333333333333343h-8.888888888888914Z" fill="rgb(239, 249, 189)"/><path aria-label="Count of Records: 2; Defense Score: 85 – 90; Attack Score: 105 – 110" role="graphics-symbol" aria-roledescription="rect mark" d="M142.72222222222223,125.49999999999999h8.888888888888886v8.333333333333329h-8.888888888888886Z" fill="rgb(216, 240, 180)"/><path aria-label="Count of Records: 2; Defense Score: 95 – 100; Attack Score: 50 – 55" role="graphics-symbol" aria-roledescription="rect mark" d="M160.5,217.16666666666666h8.888888888888886v8.333333333333343h-8.888888888888886Z" fill="rgb(216, 240, 180)"/><path aria-label="Count of Records: 1; Defense Score: 110 – 115; Attack Score: 80 – 85" role="graphics-symbol" aria-roledescription="rect mark" d="M187.16666666666666,167.16666666666669h8.888888888888886v8.333333333333286h-8.888888888888886Z" fill="rgb(239, 249, 189)"/><path aria-label="Count of Records: 1; Defense Score: 50 – 55; Attack Score: 120 – 125" role="graphics-symbol" aria-roledescription="rect mark" d="M80.5,100.50000000000001h8.888888888888886v8.333333333333329h-8.888888888888886Z" fill="rgb(239, 249, 189)"/><path aria-label="Count of Records: 3; Defense Score: 75 – 80; Attack Score: 55 – 60" role="graphics-symbol" aria-roledescription="rect mark" d="M124.94444444444444,208.83333333333331h8.888888888888872v8.333333333333343h-8.888888888888872Z" fill="rgb(180, 225, 182)"/><path aria-label="Count of Records: 3; Defense Score: 95 – 100; Attack Score: 65 – 70" role="graphics-symbol" aria-roledescription="rect mark" d="M160.5,192.16666666666666h8.888888888888886v8.333333333333371h-8.888888888888886Z" fill="rgb(180, 225, 182)"/><path aria-label="Count of Records: 1; Defense Score: 120 – 125; Attack Score: 90 – 95" role="graphics-symbol" aria-roledescription="rect mark" d="M204.94444444444443,150.5h8.888888888888914v8.333333333333343h-8.888888888888914Z" fill="rgb(239, 249, 189)"/><path aria-label="Count of Records: 2; Defense Score: 95 – 100; Attack Score: 85 – 90" role="graphics-symbol" aria-roledescription="rect mark" d="M160.5,158.83333333333334h8.888888888888886v8.333333333333343h-8.888888888888886Z" fill="rgb(216, 240, 180)"/><path aria-label="Count of Records: 1; Defense Score: 120 – 125; Attack Score: 130 – 135" role="graphics-symbol" aria-roledescription="rect mark" d="M204.94444444444443,83.83333333333334h8.888888888888914v8.333333333333329h-8.888888888888914Z" fill="rgb(239, 249, 189)"/><path aria-label="Count of Records: 2; Defense Score: 5 – 10; Attack Score: 5 – 10" role="graphics-symbol" aria-roledescription="rect mark" d="M0.5,292.1666666666667h8.88888888888889v8.333333333333314h-8.88888888888889Z" fill="rgb(216, 240, 180)"/><path aria-label="Count of Records: 1; Defense Score: 115 – 120; Attack Score: 55 – 60" role="graphics-symbol" aria-roledescription="rect mark" d="M196.05555555555554,208.83333333333331h8.888888888888886v8.333333333333343h-8.888888888888886Z" fill="rgb(239, 249, 189)"/><path aria-label="Count of Records: 4; Defense Score: 100 – 105; Attack Score: 125 – 130" role="graphics-symbol" aria-roledescription="rect mark" d="M169.38888888888889,92.16666666666667h8.888888888888886v8.333333333333343h-8.888888888888886Z" fill="rgb(134, 208, 187)"/><path aria-label="Count of Records: 2; Defense Score: 70 – 75; Attack Score: 40 – 45" role="graphics-symbol" aria-roledescription="rect mark" d="M116.05555555555554,233.83333333333334h8.8888888888889v8.333333333333343h-8.8888888888889Z" fill="rgb(216, 240, 180)"/><path aria-label="Count of Records: 3; Defense Score: 85 – 90; Attack Score: 75 – 80" role="graphics-symbol" aria-roledescription="rect mark" d="M142.72222222222223,175.49999999999997h8.888888888888886v8.333333333333371h-8.888888888888886Z" fill="rgb(180, 225, 182)"/><path aria-label="Count of Records: 3; Defense Score: 35 – 40; Attack Score: 50 – 55" role="graphics-symbol" aria-roledescription="rect mark" d="M53.833333333333336,217.16666666666666h8.888888888888886v8.333333333333343h-8.888888888888886Z" fill="rgb(180, 225, 182)"/><path aria-label="Count of Records: 3; Defense Score: 55 – 60; Attack Score: 80 – 85" role="graphics-symbol" aria-roledescription="rect mark" d="M89.38888888888889,167.16666666666669h8.888888888888886v8.333333333333286h-8.888888888888886Z" fill="rgb(180, 225, 182)"/><path aria-label="Count of Records: 2; Defense Score: 55 – 60; Attack Score: 95 – 100" role="graphics-symbol" aria-roledescription="rect mark" d="M89.38888888888889,142.16666666666666h8.888888888888886v8.333333333333343h-8.888888888888886Z" fill="rgb(216, 240, 180)"/><path aria-label="Count of Records: 1; Defense Score: 120 – 125; Attack Score: 155 – 160" role="graphics-symbol" aria-roledescription="rect mark" d="M204.94444444444443,42.16666666666665h8.888888888888914v8.333333333333336h-8.888888888888914Z" fill="rgb(239, 249, 189)"/><path aria-label="Count of Records: 1; Defense Score: 95 – 100; Attack Score: 100 – 105" role="graphics-symbol" aria-roledescription="rect mark" d="M160.5,133.83333333333331h8.888888888888886v8.333333333333343h-8.888888888888886Z" fill="rgb(239, 249, 189)"/><path aria-label="Count of Records: 1; Defense Score: 55 – 60; Attack Score: 10 – 15" role="graphics-symbol" aria-roledescription="rect mark" d="M89.38888888888889,283.8333333333333h8.888888888888886v8.333333333333371h-8.888888888888886Z" fill="rgb(239, 249, 189)"/><path aria-label="Count of Records: 1; Defense Score: 105 – 110; Attack Score: 155 – 160" role="graphics-symbol" aria-roledescription="rect mark" d="M178.27777777777777,42.16666666666665h8.888888888888886v8.333333333333336h-8.888888888888886Z" fill="rgb(239, 249, 189)"/><path aria-label="Count of Records: 1; Defense Score: 80 – 85; Attack Score: 85 – 90" role="graphics-symbol" aria-roledescription="rect mark" d="M133.83333333333331,158.83333333333334h8.888888888888914v8.333333333333343h-8.888888888888914Z" fill="rgb(239, 249, 189)"/><path aria-label="Count of Records: 1; Defense Score: 60 – 65; Attack Score: 130 – 135" role="graphics-symbol" aria-roledescription="rect mark" d="M98.27777777777777,83.83333333333334h8.8888888888889v8.333333333333329h-8.8888888888889Z" fill="rgb(239, 249, 189)"/><path aria-label="Count of Records: 4; Defense Score: 70 – 75; Attack Score: 60 – 65" role="graphics-symbol" aria-roledescription="rect mark" d="M116.05555555555554,200.50000000000003h8.8888888888889v8.333333333333286h-8.8888888888889Z" fill="rgb(134, 208, 187)"/><path aria-label="Count of Records: 1; Defense Score: 100 – 105; Attack Score: 40 – 45" role="graphics-symbol" aria-roledescription="rect mark" d="M169.38888888888889,233.83333333333334h8.888888888888886v8.333333333333343h-8.888888888888886Z" fill="rgb(239, 249, 189)"/><path aria-label="Count of Records: 2; Defense Score: 125 – 130; Attack Score: 60 – 65" role="graphics-symbol" aria-roledescription="rect mark" d="M213.83333333333334,200.50000000000003h8.888888888888886v8.333333333333286h-8.888888888888886Z" fill="rgb(216, 240, 180)"/><path aria-label="Count of Records: 4; Defense Score: 90 – 95; Attack Score: 80 – 85" role="graphics-symbol" aria-roledescription="rect mark" d="M151.61111111111111,167.16666666666669h8.888888888888886v8.333333333333286h-8.888888888888886Z" fill="rgb(134, 208, 187)"/><path aria-label="Count of Records: 1; Defense Score: 105 – 110; Attack Score: 115 – 120" role="graphics-symbol" aria-roledescription="rect mark" d="M178.27777777777777,108.83333333333334h8.888888888888886v8.333333333333314h-8.888888888888886Z" fill="rgb(239, 249, 189)"/><path aria-label="Count of Records: 1; Defense Score: 85 – 90; Attack Score: 135 – 140" role="graphics-symbol" aria-roledescription="rect mark" d="M142.72222222222223,75.5h8.888888888888886v8.333333333333343h-8.888888888888886Z" fill="rgb(239, 249, 189)"/><path aria-label="Count of Records: 1; Defense Score: 65 – 70; Attack Score: 110 – 115" role="graphics-symbol" aria-roledescription="rect mark" d="M107.16666666666667,117.16666666666666h8.888888888888872v8.333333333333329h-8.888888888888872Z" fill="rgb(239, 249, 189)"/><path aria-label="Count of Records: 1; Defense Score: 100 – 105; Attack Score: 85 – 90" role="graphics-symbol" aria-roledescription="rect mark" d="M169.38888888888889,158.83333333333334h8.888888888888886v8.333333333333343h-8.888888888888886Z" fill="rgb(239, 249, 189)"/><path aria-label="Count of Records: 1; Defense Score: 90 – 95; Attack Score: 100 – 105" role="graphics-symbol" aria-roledescription="rect mark" d="M151.61111111111111,133.83333333333331h8.888888888888886v8.333333333333343h-8.888888888888886Z" fill="rgb(239, 249, 189)"/><path aria-label="Count of Records: 6; Defense Score: 45 – 50; Attack Score: 60 – 65" role="graphics-symbol" aria-roledescription="rect mark" d="M71.61111111111111,200.50000000000003h8.888888888888886v8.333333333333286h-8.888888888888886Z" fill="rgb(55, 168, 193)"/><path aria-label="Count of Records: 5; Defense Score: 65 – 70; Attack Score: 80 – 85" role="graphics-symbol" aria-roledescription="rect mark" d="M107.16666666666667,167.16666666666669h8.888888888888872v8.333333333333286h-8.888888888888872Z" fill="rgb(89, 189, 192)"/><path aria-label="Count of Records: 3; Defense Score: 95 – 100; Attack Score: 130 – 135" role="graphics-symbol" aria-roledescription="rect mark" d="M160.5,83.83333333333334h8.888888888888886v8.333333333333329h-8.888888888888886Z" fill="rgb(180, 225, 182)"/><path aria-label="Count of Records: 1; Defense Score: 70 – 75; Attack Score: 150 – 155" role="graphics-symbol" aria-roledescription="rect mark" d="M116.05555555555554,50.499999999999986h8.8888888888889v8.333333333333343h-8.8888888888889Z" fill="rgb(239, 249, 189)"/><path aria-label="Count of Records: 6; Defense Score: 100 – 105; Attack Score: 100 – 105" role="graphics-symbol" aria-roledescription="rect mark" d="M169.38888888888889,133.83333333333331h8.888888888888886v8.333333333333343h-8.888888888888886Z" fill="rgb(55, 168, 193)"/><path aria-label="Count of Records: 2; Defense Score: 100 – 105; Attack Score: 105 – 110" role="graphics-symbol" aria-roledescription="rect mark" d="M169.38888888888889,125.49999999999999h8.888888888888886v8.333333333333329h-8.888888888888886Z" fill="rgb(216, 240, 180)"/><path aria-label="Count of Records: 1; Defense Score: 30 – 35; Attack Score: 45 – 50" role="graphics-symbol" aria-roledescription="rect mark" d="M44.94444444444444,225.5h8.888888888888893v8.333333333333343h-8.888888888888893Z" fill="rgb(239, 249, 189)"/><path aria-label="Count of Records: 6; Defense Score: 60 – 65; Attack Score: 75 – 80" role="graphics-symbol" aria-roledescription="rect mark" d="M98.27777777777777,175.49999999999997h8.8888888888889v8.333333333333371h-8.8888888888889Z" fill="rgb(55, 168, 193)"/><path aria-label="Count of Records: 5; Defense Score: 30 – 35; Attack Score: 30 – 35" role="graphics-symbol" aria-roledescription="rect mark" d="M44.94444444444444,250.5h8.888888888888893v8.333333333333371h-8.888888888888893Z" fill="rgb(89, 189, 192)"/><path aria-label="Count of Records: 9; Defense Score: 50 – 55; Attack Score: 50 – 55" role="graphics-symbol" aria-roledescription="rect mark" d="M80.5,217.16666666666666h8.888888888888886v8.333333333333343h-8.888888888888886Z" fill="rgb(35, 74, 158)"/><path aria-label="Count of Records: 1; Defense Score: 30 – 35; Attack Score: 20 – 25" role="graphics-symbol" aria-roledescription="rect mark" d="M44.94444444444444,267.16666666666663h8.888888888888893v8.333333333333371h-8.888888888888893Z" fill="rgb(239, 249, 189)"/><path aria-label="Count of Records: 2; Defense Score: 50 – 55; Attack Score: 35 – 40" role="graphics-symbol" aria-roledescription="rect mark" d="M80.5,242.16666666666669h8.888888888888886v8.333333333333314h-8.888888888888886Z" fill="rgb(216, 240, 180)"/><path aria-label="Count of Records: 4; Defense Score: 70 – 75; Attack Score: 90 – 95" role="graphics-symbol" aria-roledescription="rect mark" d="M116.05555555555554,150.5h8.8888888888889v8.333333333333343h-8.8888888888889Z" fill="rgb(134, 208, 187)"/><path aria-label="Count of Records: 2; Defense Score: 80 – 85; Attack Score: 90 – 95" role="graphics-symbol" aria-roledescription="rect mark" d="M133.83333333333331,150.5h8.888888888888914v8.333333333333343h-8.888888888888914Z" fill="rgb(216, 240, 180)"/><path aria-label="Count of Records: 7; Defense Score: 55 – 60; Attack Score: 55 – 60" role="graphics-symbol" aria-roledescription="rect mark" d="M89.38888888888889,208.83333333333331h8.888888888888886v8.333333333333343h-8.888888888888886Z" fill="rgb(37, 139, 187)"/><path aria-label="Count of Records: 1; Defense Score: 15 – 20; Attack Score: 40 – 45" role="graphics-symbol" aria-roledescription="rect mark" d="M18.27777777777778,233.83333333333334h8.88888888888889v8.333333333333343h-8.88888888888889Z" fill="rgb(239, 249, 189)"/><path aria-label="Count of Records: 2; Defense Score: 25 – 30; Attack Score: 25 – 30" role="graphics-symbol" aria-roledescription="rect mark" d="M36.05555555555556,258.83333333333337h8.888888888888886v8.333333333333258h-8.888888888888886Z" fill="rgb(216, 240, 180)"/><path aria-label="Count of Records: 2; Defense Score: 15 – 20; Attack Score: 30 – 35" role="graphics-symbol" aria-roledescription="rect mark" d="M18.27777777777778,250.5h8.88888888888889v8.333333333333371h-8.88888888888889Z" fill="rgb(216, 240, 180)"/><path aria-label="Count of Records: 1; Defense Score: 65 – 70; Attack Score: 20 – 25" role="graphics-symbol" aria-roledescription="rect mark" d="M107.16666666666667,267.16666666666663h8.888888888888872v8.333333333333371h-8.888888888888872Z" fill="rgb(239, 249, 189)"/><path aria-label="Count of Records: 2; Defense Score: 85 – 90; Attack Score: 40 – 45" role="graphics-symbol" aria-roledescription="rect mark" d="M142.72222222222223,233.83333333333334h8.888888888888886v8.333333333333343h-8.888888888888886Z" fill="rgb(216, 240, 180)"/><path aria-label="Count of Records: 4; Defense Score: 70 – 75; Attack Score: 75 – 80" role="graphics-symbol" aria-roledescription="rect mark" d="M116.05555555555554,175.49999999999997h8.8888888888889v8.333333333333371h-8.8888888888889Z" fill="rgb(134, 208, 187)"/><path aria-label="Count of Records: 1; Defense Score: 105 – 110; Attack Score: 95 – 100" role="graphics-symbol" aria-roledescription="rect mark" d="M178.27777777777777,142.16666666666666h8.888888888888886v8.333333333333343h-8.888888888888886Z" fill="rgb(239, 249, 189)"/><path aria-label="Count of Records: 5; Defense Score: 95 – 100; Attack Score: 80 – 85" role="graphics-symbol" aria-roledescription="rect mark" d="M160.5,167.16666666666669h8.888888888888886v8.333333333333286h-8.888888888888886Z" fill="rgb(89, 189, 192)"/><path aria-label="Count of Records: 2; Defense Score: 50 – 55; Attack Score: 20 – 25" role="graphics-symbol" aria-roledescription="rect mark" d="M80.5,267.16666666666663h8.888888888888886v8.333333333333371h-8.888888888888886Z" fill="rgb(216, 240, 180)"/><path aria-label="Count of Records: 2; Defense Score: 80 – 85; Attack Score: 50 – 55" role="graphics-symbol" aria-roledescription="rect mark" d="M133.83333333333331,217.16666666666666h8.888888888888914v8.333333333333343h-8.888888888888914Z" fill="rgb(216, 240, 180)"/><path aria-label="Count of Records: 2; Defense Score: 115 – 120; Attack Score: 100 – 105" role="graphics-symbol" aria-roledescription="rect mark" d="M196.05555555555554,133.83333333333331h8.888888888888886v8.333333333333343h-8.888888888888886Z" fill="rgb(216, 240, 180)"/><path aria-label="Count of Records: 3; Defense Score: 75 – 80; Attack Score: 75 – 80" role="graphics-symbol" aria-roledescription="rect mark" d="M124.94444444444444,175.49999999999997h8.888888888888872v8.333333333333371h-8.888888888888872Z" fill="rgb(180, 225, 182)"/><path aria-label="Count of Records: 3; Defense Score: 40 – 45; Attack Score: 35 – 40" role="graphics-symbol" aria-roledescription="rect mark" d="M62.72222222222222,242.16666666666669h8.888888888888893v8.333333333333314h-8.888888888888893Z" fill="rgb(180, 225, 182)"/><path aria-label="Count of Records: 2; Defense Score: 70 – 75; Attack Score: 55 – 60" role="graphics-symbol" aria-roledescription="rect mark" d="M116.05555555555554,208.83333333333331h8.8888888888889v8.333333333333343h-8.8888888888889Z" fill="rgb(216, 240, 180)"/><path aria-label="Count of Records: 1; Defense Score: 55 – 60; Attack Score: 75 – 80" role="graphics-symbol" aria-roledescription="rect mark" d="M89.38888888888889,175.49999999999997h8.888888888888886v8.333333333333371h-8.888888888888886Z" fill="rgb(239, 249, 189)"/><path aria-label="Count of Records: 4; Defense Score: 45 – 50; Attack Score: 65 – 70" role="graphics-symbol" aria-roledescription="rect mark" d="M71.61111111111111,192.16666666666666h8.888888888888886v8.333333333333371h-8.888888888888886Z" fill="rgb(134, 208, 187)"/><path aria-label="Count of Records: 3; Defense Score: 85 – 90; Attack Score: 85 – 90" role="graphics-symbol" aria-roledescription="rect mark" d="M142.72222222222223,158.83333333333334h8.888888888888886v8.333333333333343h-8.888888888888886Z" fill="rgb(180, 225, 182)"/><path aria-label="Count of Records: 1; Defense Score: 110 – 115; Attack Score: 65 – 70" role="graphics-symbol" aria-roledescription="rect mark" d="M187.16666666666666,192.16666666666666h8.888888888888886v8.333333333333371h-8.888888888888886Z" fill="rgb(239, 249, 189)"/><path aria-label="Count of Records: 4; Defense Score: 40 – 45; Attack Score: 85 – 90" role="graphics-symbol" aria-roledescription="rect mark" d="M62.72222222222222,158.83333333333334h8.888888888888893v8.333333333333343h-8.888888888888893Z" fill="rgb(134, 208, 187)"/><path aria-label="Count of Records: 3; Defense Score: 80 – 85; Attack Score: 75 – 80" role="graphics-symbol" aria-roledescription="rect mark" d="M133.83333333333331,175.49999999999997h8.888888888888914v8.333333333333371h-8.888888888888914Z" fill="rgb(180, 225, 182)"/><path aria-label="Count of Records: 3; Defense Score: 55 – 60; Attack Score: 30 – 35" role="graphics-symbol" aria-roledescription="rect mark" d="M89.38888888888889,250.5h8.888888888888886v8.333333333333371h-8.888888888888886Z" fill="rgb(180, 225, 182)"/><path aria-label="Count of Records: 1; Defense Score: 90 – 95; Attack Score: 65 – 70" role="graphics-symbol" aria-roledescription="rect mark" d="M151.61111111111111,192.16666666666666h8.888888888888886v8.333333333333371h-8.888888888888886Z" fill="rgb(239, 249, 189)"/><path aria-label="Count of Records: 2; Defense Score: 140 – 145; Attack Score: 90 – 95" role="graphics-symbol" aria-roledescription="rect mark" d="M240.5,150.5h8.888888888888886v8.333333333333343h-8.888888888888886Z" fill="rgb(216, 240, 180)"/><path aria-label="Count of Records: 1; Defense Score: 105 – 110; Attack Score: 75 – 80" role="graphics-symbol" aria-roledescription="rect mark" d="M178.27777777777777,175.49999999999997h8.888888888888886v8.333333333333371h-8.888888888888886Z" fill="rgb(239, 249, 189)"/><path aria-label="Count of Records: 1; Defense Score: 225 – 230; Attack Score: 125 – 130" role="graphics-symbol" aria-roledescription="rect mark" d="M391.6111111111111,92.16666666666667h8.888888888888914v8.333333333333343h-8.888888888888914Z" fill="rgb(239, 249, 189)"/><path aria-label="Count of Records: 5; Defense Score: 75 – 80; Attack Score: 120 – 125" role="graphics-symbol" aria-roledescription="rect mark" d="M124.94444444444444,100.50000000000001h8.888888888888872v8.333333333333329h-8.888888888888872Z" fill="rgb(89, 189, 192)"/><path aria-label="Count of Records: 3; Defense Score: 85 – 90; Attack Score: 95 – 100" role="graphics-symbol" aria-roledescription="rect mark" d="M142.72222222222223,142.16666666666666h8.888888888888886v8.333333333333343h-8.888888888888886Z" fill="rgb(180, 225, 182)"/><path aria-label="Count of Records: 1; Defense Score: 140 – 145; Attack Score: 150 – 155" role="graphics-symbol" aria-roledescription="rect mark" d="M240.5,50.499999999999986h8.888888888888886v8.333333333333343h-8.888888888888886Z" fill="rgb(239, 249, 189)"/><path aria-label="Count of Records: 1; Defense Score: 225 – 230; Attack Score: 10 – 15" role="graphics-symbol" aria-roledescription="rect mark" d="M391.6111111111111,283.8333333333333h8.888888888888914v8.333333333333371h-8.888888888888914Z" fill="rgb(239, 249, 189)"/><path aria-label="Count of Records: 1; Defense Score: 115 – 120; Attack Score: 180 – 185" role="graphics-symbol" aria-roledescription="rect mark" d="M196.05555555555554,0.5h8.888888888888886v8.333333333333337h-8.888888888888886Z" fill="rgb(239, 249, 189)"/><path aria-label="Count of Records: 2; Defense Score: 75 – 80; Attack Score: 130 – 135" role="graphics-symbol" aria-roledescription="rect mark" d="M124.94444444444444,83.83333333333334h8.888888888888872v8.333333333333329h-8.888888888888872Z" fill="rgb(216, 240, 180)"/><path aria-label="Count of Records: 1; Defense Score: 120 – 125; Attack Score: 50 – 55" role="graphics-symbol" aria-roledescription="rect mark" d="M204.94444444444443,217.16666666666666h8.888888888888914v8.333333333333343h-8.888888888888914Z" fill="rgb(239, 249, 189)"/><path aria-label="Count of Records: 4; Defense Score: 80 – 85; Attack Score: 100 – 105" role="graphics-symbol" aria-roledescription="rect mark" d="M133.83333333333331,133.83333333333331h8.888888888888914v8.333333333333343h-8.888888888888914Z" fill="rgb(134, 208, 187)"/><path aria-label="Count of Records: 3; Defense Score: 95 – 100; Attack Score: 55 – 60" role="graphics-symbol" aria-roledescription="rect mark" d="M160.5,208.83333333333331h8.888888888888886v8.333333333333343h-8.888888888888886Z" fill="rgb(180, 225, 182)"/><path aria-label="Count of Records: 2; Defense Score: 35 – 40; Attack Score: 65 – 70" role="graphics-symbol" aria-roledescription="rect mark" d="M53.833333333333336,192.16666666666666h8.888888888888886v8.333333333333371h-8.888888888888886Z" fill="rgb(216, 240, 180)"/><path aria-label="Count of Records: 3; Defense Score: 45 – 50; Attack Score: 55 – 60" role="graphics-symbol" aria-roledescription="rect mark" d="M71.61111111111111,208.83333333333331h8.888888888888886v8.333333333333343h-8.888888888888886Z" fill="rgb(180, 225, 182)"/><path aria-label="Count of Records: 1; Defense Score: 140 – 145; Attack Score: 80 – 85" role="graphics-symbol" aria-roledescription="rect mark" d="M240.5,167.16666666666669h8.888888888888886v8.333333333333286h-8.888888888888886Z" fill="rgb(239, 249, 189)"/><path aria-label="Count of Records: 2; Defense Score: 90 – 95; Attack Score: 90 – 95" role="graphics-symbol" aria-roledescription="rect mark" d="M151.61111111111111,150.5h8.888888888888886v8.333333333333343h-8.888888888888886Z" fill="rgb(216, 240, 180)"/><path aria-label="Count of Records: 3; Defense Score: 120 – 125; Attack Score: 120 – 125" role="graphics-symbol" aria-roledescription="rect mark" d="M204.94444444444443,100.50000000000001h8.888888888888914v8.333333333333329h-8.888888888888914Z" fill="rgb(180, 225, 182)"/><path aria-label="Count of Records: 6; Defense Score: 60 – 65; Attack Score: 95 – 100" role="graphics-symbol" aria-roledescription="rect mark" d="M98.27777777777777,142.16666666666666h8.8888888888889v8.333333333333343h-8.8888888888889Z" fill="rgb(55, 168, 193)"/><path aria-label="Count of Records: 1; Defense Score: 35 – 40; Attack Score: 20 – 25" role="graphics-symbol" aria-roledescription="rect mark" d="M53.833333333333336,267.16666666666663h8.888888888888886v8.333333333333371h-8.888888888888886Z" fill="rgb(239, 249, 189)"/><path aria-label="Count of Records: 1; Defense Score: 35 – 40; Attack Score: 60 – 65" role="graphics-symbol" aria-roledescription="rect mark" d="M53.833333333333336,200.50000000000003h8.888888888888886v8.333333333333286h-8.888888888888886Z" fill="rgb(239, 249, 189)"/><path aria-label="Count of Records: 2; Defense Score: 105 – 110; Attack Score: 80 – 85" role="graphics-symbol" aria-roledescription="rect mark" d="M178.27777777777777,167.16666666666669h8.888888888888886v8.333333333333286h-8.888888888888886Z" fill="rgb(216, 240, 180)"/><path aria-label="Count of Records: 1; Defense Score: 10 – 15; Attack Score: 10 – 15" role="graphics-symbol" aria-roledescription="rect mark" d="M9.38888888888889,283.8333333333333h8.88888888888889v8.333333333333371h-8.88888888888889Z" fill="rgb(239, 249, 189)"/><path aria-label="Count of Records: 3; Defense Score: 75 – 80; Attack Score: 85 – 90" role="graphics-symbol" aria-roledescription="rect mark" d="M124.94444444444444,158.83333333333334h8.888888888888872v8.333333333333343h-8.888888888888872Z" fill="rgb(180, 225, 182)"/><path aria-label="Count of Records: 2; Defense Score: 85 – 90; Attack Score: 115 – 120" role="graphics-symbol" aria-roledescription="rect mark" d="M142.72222222222223,108.83333333333334h8.888888888888886v8.333333333333314h-8.888888888888886Z" fill="rgb(216, 240, 180)"/><path aria-label="Count of Records: 2; Defense Score: 115 – 120; Attack Score: 75 – 80" role="graphics-symbol" aria-roledescription="rect mark" d="M196.05555555555554,175.49999999999997h8.888888888888886v8.333333333333371h-8.888888888888886Z" fill="rgb(216, 240, 180)"/><path aria-label="Count of Records: 4; Defense Score: 50 – 55; Attack Score: 60 – 65" role="graphics-symbol" aria-roledescription="rect mark" d="M80.5,200.50000000000003h8.888888888888886v8.333333333333286h-8.888888888888886Z" fill="rgb(134, 208, 187)"/><path aria-label="Count of Records: 1; Defense Score: 150 – 155; Attack Score: 160 – 165" role="graphics-symbol" aria-roledescription="rect mark" d="M258.27777777777777,33.83333333333335h8.888888888888857v8.3333333333333h-8.888888888888857Z" fill="rgb(239, 249, 189)"/><path aria-label="Count of Records: 3; Defense Score: 130 – 135; Attack Score: 90 – 95" role="graphics-symbol" aria-roledescription="rect mark" d="M222.72222222222223,150.5h8.888888888888857v8.333333333333343h-8.888888888888857Z" fill="rgb(180, 225, 182)"/><path aria-label="Count of Records: 1; Defense Score: 90 – 95; Attack Score: 130 – 135" role="graphics-symbol" aria-roledescription="rect mark" d="M151.61111111111111,83.83333333333334h8.888888888888886v8.333333333333329h-8.888888888888886Z" fill="rgb(239, 249, 189)"/><path aria-label="Count of Records: 2; Defense Score: 75 – 80; Attack Score: 110 – 115" role="graphics-symbol" aria-roledescription="rect mark" d="M124.94444444444444,117.16666666666666h8.888888888888872v8.333333333333329h-8.888888888888872Z" fill="rgb(216, 240, 180)"/><path aria-label="Count of Records: 5; Defense Score: 60 – 65; Attack Score: 85 – 90" role="graphics-symbol" aria-roledescription="rect mark" d="M98.27777777777777,158.83333333333334h8.8888888888889v8.333333333333343h-8.8888888888889Z" fill="rgb(89, 189, 192)"/><path aria-label="Count of Records: 1; Defense Score: 80 – 85; Attack Score: 160 – 165" role="graphics-symbol" aria-roledescription="rect mark" d="M133.83333333333331,33.83333333333335h8.888888888888914v8.3333333333333h-8.888888888888914Z" fill="rgb(239, 249, 189)"/><path aria-label="Count of Records: 4; Defense Score: 50 – 55; Attack Score: 70 – 75" role="graphics-symbol" aria-roledescription="rect mark" d="M80.5,183.83333333333334h8.888888888888886v8.333333333333314h-8.888888888888886Z" fill="rgb(134, 208, 187)"/><path aria-label="Count of Records: 6; Defense Score: 70 – 75; Attack Score: 85 – 90" role="graphics-symbol" aria-roledescription="rect mark" d="M116.05555555555554,158.83333333333334h8.8888888888889v8.333333333333343h-8.8888888888889Z" fill="rgb(55, 168, 193)"/><path aria-label="Count of Records: 1; Defense Score: 110 – 115; Attack Score: 150 – 155" role="graphics-symbol" aria-roledescription="rect mark" d="M187.16666666666666,50.499999999999986h8.888888888888886v8.333333333333343h-8.888888888888886Z" fill="rgb(239, 249, 189)"/><path aria-label="Count of Records: 3; Defense Score: 40 – 45; Attack Score: 30 – 35" role="graphics-symbol" aria-roledescription="rect mark" d="M62.72222222222222,250.5h8.888888888888893v8.333333333333371h-8.888888888888893Z" fill="rgb(180, 225, 182)"/><path aria-label="Count of Records: 1; Defense Score: 60 – 65; Attack Score: 70 – 75" role="graphics-symbol" aria-roledescription="rect mark" d="M98.27777777777777,183.83333333333334h8.8888888888889v8.333333333333314h-8.8888888888889Z" fill="rgb(239, 249, 189)"/><path aria-label="Count of Records: 3; Defense Score: 55 – 60; Attack Score: 35 – 40" role="graphics-symbol" aria-roledescription="rect mark" d="M89.38888888888889,242.16666666666669h8.888888888888886v8.333333333333314h-8.888888888888886Z" fill="rgb(180, 225, 182)"/><path aria-label="Count of Records: 8; Defense Score: 50 – 55; Attack Score: 40 – 45" role="graphics-symbol" aria-roledescription="rect mark" d="M80.5,233.83333333333334h8.888888888888886v8.333333333333343h-8.888888888888886Z" fill="rgb(33, 106, 173)"/><path aria-label="Count of Records: 5; Defense Score: 40 – 45; Attack Score: 70 – 75" role="graphics-symbol" aria-roledescription="rect mark" d="M62.72222222222222,183.83333333333334h8.888888888888893v8.333333333333314h-8.888888888888893Z" fill="rgb(89, 189, 192)"/><path aria-label="Count of Records: 2; Defense Score: 100 – 105; Attack Score: 50 – 55" role="graphics-symbol" aria-roledescription="rect mark" d="M169.38888888888889,217.16666666666666h8.888888888888886v8.333333333333343h-8.888888888888886Z" fill="rgb(216, 240, 180)"/><path aria-label="Count of Records: 3; Defense Score: 65 – 70; Attack Score: 85 – 90" role="graphics-symbol" aria-roledescription="rect mark" d="M107.16666666666667,158.83333333333334h8.888888888888872v8.333333333333343h-8.888888888888872Z" fill="rgb(180, 225, 182)"/><path aria-label="Count of Records: 3; Defense Score: 60 – 65; Attack Score: 40 – 45" role="graphics-symbol" aria-roledescription="rect mark" d="M98.27777777777777,233.83333333333334h8.8888888888889v8.333333333333343h-8.8888888888889Z" fill="rgb(180, 225, 182)"/><path aria-label="Count of Records: 1; Defense Score: 100 – 105; Attack Score: 160 – 165" role="graphics-symbol" aria-roledescription="rect mark" d="M169.38888888888889,33.83333333333335h8.888888888888886v8.3333333333333h-8.888888888888886Z" fill="rgb(239, 249, 189)"/><path aria-label="Count of Records: 1; Defense Score: 90 – 95; Attack Score: 45 – 50" role="graphics-symbol" aria-roledescription="rect mark" d="M151.61111111111111,225.5h8.888888888888886v8.333333333333343h-8.888888888888886Z" fill="rgb(239, 249, 189)"/><path aria-label="Count of Records: 4; Defense Score: 45 – 50; Attack Score: 90 – 95" role="graphics-symbol" aria-roledescription="rect mark" d="M71.61111111111111,150.5h8.888888888888886v8.333333333333343h-8.888888888888886Z" fill="rgb(134, 208, 187)"/><path aria-label="Count of Records: 1; Defense Score: 20 – 25; Attack Score: 50 – 55" role="graphics-symbol" aria-roledescription="rect mark" d="M27.166666666666668,217.16666666666666h8.88888888888889v8.333333333333343h-8.88888888888889Z" fill="rgb(239, 249, 189)"/><path aria-label="Count of Records: 1; Defense Score: 60 – 65; Attack Score: 90 – 95" role="graphics-symbol" aria-roledescription="rect mark" d="M98.27777777777777,150.5h8.8888888888889v8.333333333333343h-8.8888888888889Z" fill="rgb(239, 249, 189)"/><path aria-label="Count of Records: 1; Defense Score: 60 – 65; Attack Score: 120 – 125" role="graphics-symbol" aria-roledescription="rect mark" d="M98.27777777777777,100.50000000000001h8.8888888888889v8.333333333333329h-8.8888888888889Z" fill="rgb(239, 249, 189)"/><path aria-label="Count of Records: 1; Defense Score: 40 – 45; Attack Score: 20 – 25" role="graphics-symbol" aria-roledescription="rect mark" d="M62.72222222222222,267.16666666666663h8.888888888888893v8.333333333333371h-8.888888888888893Z" fill="rgb(239, 249, 189)"/><path aria-label="Count of Records: 1; Defense Score: 135 – 140; Attack Score: 45 – 50" role="graphics-symbol" aria-roledescription="rect mark" d="M231.6111111111111,225.5h8.888888888888914v8.333333333333343h-8.888888888888914Z" fill="rgb(239, 249, 189)"/><path aria-label="Count of Records: 1; Defense Score: 125 – 130; Attack Score: 85 – 90" role="graphics-symbol" aria-roledescription="rect mark" d="M213.83333333333334,158.83333333333334h8.888888888888886v8.333333333333343h-8.888888888888886Z" fill="rgb(239, 249, 189)"/><path aria-label="Count of Records: 2; Defense Score: 125 – 130; Attack Score: 105 – 110" role="graphics-symbol" aria-roledescription="rect mark" d="M213.83333333333334,125.49999999999999h8.888888888888886v8.333333333333329h-8.888888888888886Z" fill="rgb(216, 240, 180)"/><path aria-label="Count of Records: 1; Defense Score: 100 – 105; Attack Score: 70 – 75" role="graphics-symbol" aria-roledescription="rect mark" d="M169.38888888888889,183.83333333333334h8.888888888888886v8.333333333333314h-8.888888888888886Z" fill="rgb(239, 249, 189)"/><path aria-label="Count of Records: 1; Defense Score: 225 – 230; Attack Score: 140 – 145" role="graphics-symbol" aria-roledescription="rect mark" d="M391.6111111111111,67.16666666666666h8.888888888888914v8.333333333333343h-8.888888888888914Z" fill="rgb(239, 249, 189)"/><path aria-label="Count of Records: 2; Defense Score: 55 – 60; Attack Score: 40 – 45" role="graphics-symbol" aria-roledescription="rect mark" d="M89.38888888888889,233.83333333333334h8.888888888888886v8.333333333333343h-8.888888888888886Z" fill="rgb(216, 240, 180)"/><path aria-label="Count of Records: 4; Defense Score: 85 – 90; Attack Score: 100 – 105" role="graphics-symbol" aria-roledescription="rect mark" d="M142.72222222222223,133.83333333333331h8.888888888888886v8.333333333333343h-8.888888888888886Z" fill="rgb(134, 208, 187)"/><path aria-label="Count of Records: 2; Defense Score: 75 – 80; Attack Score: 70 – 75" role="graphics-symbol" aria-roledescription="rect mark" d="M124.94444444444444,183.83333333333334h8.888888888888872v8.333333333333314h-8.888888888888872Z" fill="rgb(216, 240, 180)"/><path aria-label="Count of Records: 2; Defense Score: 75 – 80; Attack Score: 45 – 50" role="graphics-symbol" aria-roledescription="rect mark" d="M124.94444444444444,225.5h8.888888888888872v8.333333333333343h-8.888888888888872Z" fill="rgb(216, 240, 180)"/><path aria-label="Count of Records: 1; Defense Score: 20 – 25; Attack Score: 90 – 95" role="graphics-symbol" aria-roledescription="rect mark" d="M27.166666666666668,150.5h8.88888888888889v8.333333333333343h-8.88888888888889Z" fill="rgb(239, 249, 189)"/><path aria-label="Count of Records: 1; Defense Score: 70 – 75; Attack Score: 140 – 145" role="graphics-symbol" aria-roledescription="rect mark" d="M116.05555555555554,67.16666666666666h8.8888888888889v8.333333333333343h-8.8888888888889Z" fill="rgb(239, 249, 189)"/><path aria-label="Count of Records: 2; Defense Score: 35 – 40; Attack Score: 70 – 75" role="graphics-symbol" aria-roledescription="rect mark" d="M53.833333333333336,183.83333333333334h8.888888888888886v8.333333333333314h-8.888888888888886Z" fill="rgb(216, 240, 180)"/><path aria-label="Count of Records: 4; Defense Score: 100 – 105; Attack Score: 120 – 125" role="graphics-symbol" aria-roledescription="rect mark" d="M169.38888888888889,100.50000000000001h8.888888888888886v8.333333333333329h-8.888888888888886Z" fill="rgb(134, 208, 187)"/><path aria-label="Count of Records: 1; Defense Score: 140 – 145; Attack Score: 85 – 90" role="graphics-symbol" aria-roledescription="rect mark" d="M240.5,158.83333333333334h8.888888888888886v8.333333333333343h-8.888888888888886Z" fill="rgb(239, 249, 189)"/><path aria-label="Count of Records: 1; Defense Score: 35 – 40; Attack Score: 25 – 30" role="graphics-symbol" aria-roledescription="rect mark" d="M53.833333333333336,258.83333333333337h8.888888888888886v8.333333333333258h-8.888888888888886Z" fill="rgb(239, 249, 189)"/><path aria-label="Count of Records: 1; Defense Score: 45 – 50; Attack Score: 100 – 105" role="graphics-symbol" aria-roledescription="rect mark" d="M71.61111111111111,133.83333333333331h8.888888888888886v8.333333333333343h-8.888888888888886Z" fill="rgb(239, 249, 189)"/><path aria-label="Count of Records: 2; Defense Score: 60 – 65; Attack Score: 115 – 120" role="graphics-symbol" aria-roledescription="rect mark" d="M98.27777777777777,108.83333333333334h8.8888888888889v8.333333333333314h-8.8888888888889Z" fill="rgb(216, 240, 180)"/><path aria-label="Count of Records: 1; Defense Score: 110 – 115; Attack Score: 110 – 115" role="graphics-symbol" aria-roledescription="rect mark" d="M187.16666666666666,117.16666666666666h8.888888888888886v8.333333333333329h-8.888888888888886Z" fill="rgb(239, 249, 189)"/><path aria-label="Count of Records: 2; Defense Score: 65 – 70; Attack Score: 55 – 60" role="graphics-symbol" aria-roledescription="rect mark" d="M107.16666666666667,208.83333333333331h8.888888888888872v8.333333333333343h-8.888888888888872Z" fill="rgb(216, 240, 180)"/><path aria-label="Count of Records: 1; Defense Score: 85 – 90; Attack Score: 120 – 125" role="graphics-symbol" aria-roledescription="rect mark" d="M142.72222222222223,100.50000000000001h8.888888888888886v8.333333333333329h-8.888888888888886Z" fill="rgb(239, 249, 189)"/><path aria-label="Count of Records: 1; Defense Score: 105 – 110; Attack Score: 70 – 75" role="graphics-symbol" aria-roledescription="rect mark" d="M178.27777777777777,183.83333333333334h8.888888888888886v8.333333333333314h-8.888888888888886Z" fill="rgb(239, 249, 189)"/><path aria-label="Count of Records: 1; Defense Score: 75 – 80; Attack Score: 40 – 45" role="graphics-symbol" aria-roledescription="rect mark" d="M124.94444444444444,233.83333333333334h8.888888888888872v8.333333333333343h-8.888888888888872Z" fill="rgb(239, 249, 189)"/><path aria-label="Count of Records: 1; Defense Score: 50 – 55; Attack Score: 95 – 100" role="graphics-symbol" aria-roledescription="rect mark" d="M80.5,142.16666666666666h8.888888888888886v8.333333333333343h-8.888888888888886Z" fill="rgb(239, 249, 189)"/><path aria-label="Count of Records: 1; Defense Score: 20 – 25; Attack Score: 15 – 20" role="graphics-symbol" aria-roledescription="rect mark" d="M27.166666666666668,275.5h8.88888888888889v8.333333333333314h-8.88888888888889Z" fill="rgb(239, 249, 189)"/><path aria-label="Count of Records: 3; Defense Score: 75 – 80; Attack Score: 60 – 65" role="graphics-symbol" aria-roledescription="rect mark" d="M124.94444444444444,200.50000000000003h8.888888888888872v8.333333333333286h-8.888888888888872Z" fill="rgb(180, 225, 182)"/><path aria-label="Count of Records: 1; Defense Score: 75 – 80; Attack Score: 165 – 170" role="graphics-symbol" aria-roledescription="rect mark" d="M124.94444444444444,25.50000000000001h8.888888888888872v8.33333333333334h-8.888888888888872Z" fill="rgb(239, 249, 189)"/><path aria-label="Count of Records: 1; Defense Score: 90 – 95; Attack Score: 40 – 45" role="graphics-symbol" aria-roledescription="rect mark" d="M151.61111111111111,233.83333333333334h8.888888888888886v8.333333333333343h-8.888888888888886Z" fill="rgb(239, 249, 189)"/><path aria-label="Count of Records: 1; Defense Score: 130 – 135; Attack Score: 70 – 75" role="graphics-symbol" aria-roledescription="rect mark" d="M222.72222222222223,183.83333333333334h8.888888888888857v8.333333333333314h-8.888888888888857Z" fill="rgb(239, 249, 189)"/><path aria-label="Count of Records: 1; Defense Score: 60 – 65; Attack Score: 150 – 155" role="graphics-symbol" aria-roledescription="rect mark" d="M98.27777777777777,50.499999999999986h8.8888888888889v8.333333333333343h-8.8888888888889Z" fill="rgb(239, 249, 189)"/><path aria-label="Count of Records: 1; Defense Score: 45 – 50; Attack Score: 20 – 25" role="graphics-symbol" aria-roledescription="rect mark" d="M71.61111111111111,267.16666666666663h8.888888888888886v8.333333333333371h-8.888888888888886Z" fill="rgb(239, 249, 189)"/><path aria-label="Count of Records: 2; Defense Score: 80 – 85; Attack Score: 120 – 125" role="graphics-symbol" aria-roledescription="rect mark" d="M133.83333333333331,100.50000000000001h8.888888888888914v8.333333333333329h-8.888888888888914Z" fill="rgb(216, 240, 180)"/><path aria-label="Count of Records: 2; Defense Score: 85 – 90; Attack Score: 60 – 65" role="graphics-symbol" aria-roledescription="rect mark" d="M142.72222222222223,200.50000000000003h8.888888888888886v8.333333333333286h-8.888888888888886Z" fill="rgb(216, 240, 180)"/><path aria-label="Count of Records: 1; Defense Score: 105 – 110; Attack Score: 100 – 105" role="graphics-symbol" aria-roledescription="rect mark" d="M178.27777777777777,133.83333333333331h8.888888888888886v8.333333333333343h-8.888888888888886Z" fill="rgb(239, 249, 189)"/><path aria-label="Count of Records: 1; Defense Score: 100 – 105; Attack Score: 95 – 100" role="graphics-symbol" aria-roledescription="rect mark" d="M169.38888888888889,142.16666666666666h8.888888888888886v8.333333333333343h-8.888888888888886Z" fill="rgb(239, 249, 189)"/><path aria-label="Count of Records: 1; Defense Score: 130 – 135; Attack Score: 145 – 150" role="graphics-symbol" aria-roledescription="rect mark" d="M222.72222222222223,58.83333333333333h8.888888888888857v8.333333333333329h-8.888888888888857Z" fill="rgb(239, 249, 189)"/><path aria-label="Count of Records: 3; Defense Score: 80 – 85; Attack Score: 55 – 60" role="graphics-symbol" aria-roledescription="rect mark" d="M133.83333333333331,208.83333333333331h8.888888888888914v8.333333333333343h-8.888888888888914Z" fill="rgb(180, 225, 182)"/><path aria-label="Count of Records: 2; Defense Score: 100 – 105; Attack Score: 75 – 80" role="graphics-symbol" aria-roledescription="rect mark" d="M169.38888888888889,175.49999999999997h8.888888888888886v8.333333333333371h-8.888888888888886Z" fill="rgb(216, 240, 180)"/><path aria-label="Count of Records: 1; Defense Score: 150 – 155; Attack Score: 145 – 150" role="graphics-symbol" aria-roledescription="rect mark" d="M258.27777777777777,58.83333333333333h8.888888888888857v8.333333333333329h-8.888888888888857Z" fill="rgb(239, 249, 189)"/><path aria-label="Count of Records: 1; Defense Score: 200 – 205; Attack Score: 100 – 105" role="graphics-symbol" aria-roledescription="rect mark" d="M347.1666666666667,133.83333333333331h8.888888888888857v8.333333333333343h-8.888888888888857Z" fill="rgb(239, 249, 189)"/><path aria-label="Count of Records: 1; Defense Score: 150 – 155; Attack Score: 75 – 80" role="graphics-symbol" aria-roledescription="rect mark" d="M258.27777777777777,175.49999999999997h8.888888888888857v8.333333333333371h-8.888888888888857Z" fill="rgb(239, 249, 189)"/><path aria-label="Count of Records: 2; Defense Score: 100 – 105; Attack Score: 130 – 135" role="graphics-symbol" aria-roledescription="rect mark" d="M169.38888888888889,83.83333333333334h8.888888888888886v8.333333333333329h-8.888888888888886Z" fill="rgb(216, 240, 180)"/><path aria-label="Count of Records: 1; Defense Score: 90 – 95; Attack Score: 150 – 155" role="graphics-symbol" aria-roledescription="rect mark" d="M151.61111111111111,50.499999999999986h8.888888888888886v8.333333333333343h-8.888888888888886Z" fill="rgb(239, 249, 189)"/><path aria-label="Count of Records: 1; Defense Score: 160 – 165; Attack Score: 180 – 185" role="graphics-symbol" aria-roledescription="rect mark" d="M276.05555555555554,0.5h8.888888888888914v8.333333333333337h-8.888888888888914Z" fill="rgb(239, 249, 189)"/><path aria-label="Count of Records: 1; Defense Score: 100 – 105; Attack Score: 180 – 185" role="graphics-symbol" aria-roledescription="rect mark" d="M169.38888888888889,0.5h8.888888888888886v8.333333333333337h-8.888888888888886Z" fill="rgb(239, 249, 189)"/><path aria-label="Count of Records: 1; Defense Score: 90 – 95; Attack Score: 95 – 100" role="graphics-symbol" aria-roledescription="rect mark" d="M151.61111111111111,142.16666666666666h8.888888888888886v8.333333333333343h-8.888888888888886Z" fill="rgb(239, 249, 189)"/><path aria-label="Count of Records: 3; Defense Score: 105 – 110; Attack Score: 105 – 110" role="graphics-symbol" aria-roledescription="rect mark" d="M178.27777777777777,125.49999999999999h8.888888888888886v8.333333333333329h-8.888888888888886Z" fill="rgb(180, 225, 182)"/><path aria-label="Count of Records: 4; Defense Score: 50 – 55; Attack Score: 75 – 80" role="graphics-symbol" aria-roledescription="rect mark" d="M80.5,175.49999999999997h8.888888888888886v8.333333333333371h-8.888888888888886Z" fill="rgb(134, 208, 187)"/><path aria-label="Count of Records: 1; Defense Score: 70 – 75; Attack Score: 120 – 125" role="graphics-symbol" aria-roledescription="rect mark" d="M116.05555555555554,100.50000000000001h8.8888888888889v8.333333333333329h-8.8888888888889Z" fill="rgb(239, 249, 189)"/><path aria-label="Count of Records: 1; Defense Score: 40 – 45; Attack Score: 25 – 30" role="graphics-symbol" aria-roledescription="rect mark" d="M62.72222222222222,258.83333333333337h8.888888888888893v8.333333333333258h-8.888888888888893Z" fill="rgb(239, 249, 189)"/><path aria-label="Count of Records: 1; Defense Score: 30 – 35; Attack Score: 65 – 70" role="graphics-symbol" aria-roledescription="rect mark" d="M44.94444444444444,192.16666666666666h8.888888888888893v8.333333333333371h-8.888888888888893Z" fill="rgb(239, 249, 189)"/><path aria-label="Count of Records: 1; Defense Score: 40 – 45; Attack Score: 125 – 130" role="graphics-symbol" aria-roledescription="rect mark" d="M62.72222222222222,92.16666666666667h8.888888888888893v8.333333333333343h-8.888888888888893Z" fill="rgb(239, 249, 189)"/><path aria-label="Count of Records: 1; Defense Score: 60 – 65; Attack Score: 165 – 170" role="graphics-symbol" aria-roledescription="rect mark" d="M98.27777777777777,25.50000000000001h8.8888888888889v8.33333333333334h-8.8888888888889Z" fill="rgb(239, 249, 189)"/><path aria-label="Count of Records: 1; Defense Score: 115 – 120; Attack Score: 40 – 45" role="graphics-symbol" aria-roledescription="rect mark" d="M196.05555555555554,233.83333333333334h8.888888888888886v8.333333333333343h-8.888888888888886Z" fill="rgb(239, 249, 189)"/><path aria-label="Count of Records: 1; Defense Score: 165 – 170; Attack Score: 50 – 55" role="graphics-symbol" aria-roledescription="rect mark" d="M284.94444444444446,217.16666666666666h8.888888888888857v8.333333333333343h-8.888888888888857Z" fill="rgb(239, 249, 189)"/><path aria-label="Count of Records: 3; Defense Score: 45 – 50; Attack Score: 25 – 30" role="graphics-symbol" aria-roledescription="rect mark" d="M71.61111111111111,258.83333333333337h8.888888888888886v8.333333333333258h-8.888888888888886Z" fill="rgb(180, 225, 182)"/><path aria-label="Count of Records: 2; Defense Score: 70 – 75; Attack Score: 45 – 50" role="graphics-symbol" aria-roledescription="rect mark" d="M116.05555555555554,225.5h8.8888888888889v8.333333333333343h-8.8888888888889Z" fill="rgb(216, 240, 180)"/><path aria-label="Count of Records: 1; Defense Score: 55 – 60; Attack Score: 105 – 110" role="graphics-symbol" aria-roledescription="rect mark" d="M89.38888888888889,125.49999999999999h8.888888888888886v8.333333333333329h-8.888888888888886Z" fill="rgb(239, 249, 189)"/><path aria-label="Count of Records: 1; Defense Score: 45 – 50; Attack Score: 35 – 40" role="graphics-symbol" aria-roledescription="rect mark" d="M71.61111111111111,242.16666666666669h8.888888888888886v8.333333333333314h-8.888888888888886Z" fill="rgb(239, 249, 189)"/><path aria-label="Count of Records: 1; Defense Score: 65 – 70; Attack Score: 100 – 105" role="graphics-symbol" aria-roledescription="rect mark" d="M107.16666666666667,133.83333333333331h8.888888888888872v8.333333333333343h-8.888888888888872Z" fill="rgb(239, 249, 189)"/><path aria-label="Count of Records: 1; Defense Score: 30 – 35; Attack Score: 50 – 55" role="graphics-symbol" aria-roledescription="rect mark" d="M44.94444444444444,217.16666666666666h8.888888888888893v8.333333333333343h-8.888888888888893Z" fill="rgb(239, 249, 189)"/><path aria-label="Count of Records: 1; Defense Score: 40 – 45; Attack Score: 80 – 85" role="graphics-symbol" aria-roledescription="rect mark" d="M62.72222222222222,167.16666666666669h8.888888888888893v8.333333333333286h-8.888888888888893Z" fill="rgb(239, 249, 189)"/><path aria-label="Count of Records: 4; Defense Score: 40 – 45; Attack Score: 65 – 70" role="graphics-symbol" aria-roledescription="rect mark" d="M62.72222222222222,192.16666666666666h8.888888888888893v8.333333333333371h-8.888888888888893Z" fill="rgb(134, 208, 187)"/><path aria-label="Count of Records: 1; Defense Score: 90 – 95; Attack Score: 135 – 140" role="graphics-symbol" aria-roledescription="rect mark" d="M151.61111111111111,75.5h8.888888888888886v8.333333333333343h-8.888888888888886Z" fill="rgb(239, 249, 189)"/><path aria-label="Count of Records: 1; Defense Score: 50 – 55; Attack Score: 125 – 130" role="graphics-symbol" aria-roledescription="rect mark" d="M80.5,92.16666666666667h8.888888888888886v8.333333333333343h-8.888888888888886Z" fill="rgb(239, 249, 189)"/><path aria-label="Count of Records: 3; Defense Score: 60 – 65; Attack Score: 80 – 85" role="graphics-symbol" aria-roledescription="rect mark" d="M98.27777777777777,167.16666666666669h8.8888888888889v8.333333333333286h-8.8888888888889Z" fill="rgb(180, 225, 182)"/><path aria-label="Count of Records: 1; Defense Score: 85 – 90; Attack Score: 20 – 25" role="graphics-symbol" aria-roledescription="rect mark" d="M142.72222222222223,267.16666666666663h8.888888888888886v8.333333333333371h-8.888888888888886Z" fill="rgb(239, 249, 189)"/><path aria-label="Count of Records: 1; Defense Score: 115 – 120; Attack Score: 85 – 90" role="graphics-symbol" aria-roledescription="rect mark" d="M196.05555555555554,158.83333333333334h8.888888888888886v8.333333333333343h-8.888888888888886Z" fill="rgb(239, 249, 189)"/><path aria-label="Count of Records: 2; Defense Score: 105 – 110; Attack Score: 90 – 95" role="graphics-symbol" aria-roledescription="rect mark" d="M178.27777777777777,150.5h8.888888888888886v8.333333333333343h-8.888888888888886Z" fill="rgb(216, 240, 180)"/><path aria-label="Count of Records: 1; Defense Score: 115 – 120; Attack Score: 170 – 175" role="graphics-symbol" aria-roledescription="rect mark" d="M196.05555555555554,17.166666666666675h8.888888888888886v8.333333333333336h-8.888888888888886Z" fill="rgb(239, 249, 189)"/><path aria-label="Count of Records: 1; Defense Score: 85 – 90; Attack Score: 145 – 150" role="graphics-symbol" aria-roledescription="rect mark" d="M142.72222222222223,58.83333333333333h8.888888888888886v8.333333333333329h-8.888888888888886Z" fill="rgb(239, 249, 189)"/><path aria-label="Count of Records: 1; Defense Score: 115 – 120; Attack Score: 110 – 115" role="graphics-symbol" aria-roledescription="rect mark" d="M196.05555555555554,117.16666666666666h8.888888888888886v8.333333333333329h-8.888888888888886Z" fill="rgb(239, 249, 189)"/><path aria-label="Count of Records: 3; Defense Score: 90 – 95; Attack Score: 50 – 55" role="graphics-symbol" aria-roledescription="rect mark" d="M151.61111111111111,217.16666666666666h8.888888888888886v8.333333333333343h-8.888888888888886Z" fill="rgb(180, 225, 182)"/><path aria-label="Count of Records: 1; Defense Score: 110 – 115; Attack Score: 90 – 95" role="graphics-symbol" aria-roledescription="rect mark" d="M187.16666666666666,150.5h8.888888888888886v8.333333333333343h-8.888888888888886Z" fill="rgb(239, 249, 189)"/><path aria-label="Count of Records: 1; Defense Score: 105 – 110; Attack Score: 130 – 135" role="graphics-symbol" aria-roledescription="rect mark" d="M178.27777777777777,83.83333333333334h8.888888888888886v8.333333333333329h-8.888888888888886Z" fill="rgb(239, 249, 189)"/><path aria-label="Count of Records: 3; Defense Score: 65 – 70; Attack Score: 120 – 125" role="graphics-symbol" aria-roledescription="rect mark" d="M107.16666666666667,100.50000000000001h8.888888888888872v8.333333333333329h-8.888888888888872Z" fill="rgb(180, 225, 182)"/><path aria-label="Count of Records: 1; Defense Score: 115 – 120; Attack Score: 70 – 75" role="graphics-symbol" aria-roledescription="rect mark" d="M196.05555555555554,183.83333333333334h8.888888888888886v8.333333333333314h-8.888888888888886Z" fill="rgb(239, 249, 189)"/><path aria-label="Count of Records: 2; Defense Score: 130 – 135; Attack Score: 140 – 145" role="graphics-symbol" aria-roledescription="rect mark" d="M222.72222222222223,67.16666666666666h8.888888888888857v8.333333333333343h-8.888888888888857Z" fill="rgb(216, 240, 180)"/><path aria-label="Count of Records: 1; Defense Score: 125 – 130; Attack Score: 100 – 105" role="graphics-symbol" aria-roledescription="rect mark" d="M213.83333333333334,133.83333333333331h8.888888888888886v8.333333333333343h-8.888888888888886Z" fill="rgb(239, 249, 189)"/><path aria-label="Count of Records: 1; Defense Score: 130 – 135; Attack Score: 110 – 115" role="graphics-symbol" aria-roledescription="rect mark" d="M222.72222222222223,117.16666666666666h8.888888888888857v8.333333333333329h-8.888888888888857Z" fill="rgb(239, 249, 189)"/><path aria-label="Count of Records: 1; Defense Score: 110 – 115; Attack Score: 60 – 65" role="graphics-symbol" aria-roledescription="rect mark" d="M187.16666666666666,200.50000000000003h8.888888888888886v8.333333333333286h-8.888888888888886Z" fill="rgb(239, 249, 189)"/><path aria-label="Count of Records: 1; Defense Score: 125 – 130; Attack Score: 95 – 100" role="graphics-symbol" aria-roledescription="rect mark" d="M213.83333333333334,142.16666666666666h8.888888888888886v8.333333333333343h-8.888888888888886Z" fill="rgb(239, 249, 189)"/><path aria-label="Count of Records: 1; Defense Score: 95 – 100; Attack Score: 165 – 170" role="graphics-symbol" aria-roledescription="rect mark" d="M160.5,25.50000000000001h8.888888888888886v8.33333333333334h-8.888888888888886Z" fill="rgb(239, 249, 189)"/><path aria-label="Count of Records: 1; Defense Score: 145 – 150; Attack Score: 55 – 60" role="graphics-symbol" aria-roledescription="rect mark" d="M249.38888888888889,208.83333333333331h8.888888888888886v8.333333333333343h-8.888888888888886Z" fill="rgb(239, 249, 189)"/><path aria-label="Count of Records: 1; Defense Score: 135 – 140; Attack Score: 100 – 105" role="graphics-symbol" aria-roledescription="rect mark" d="M231.6111111111111,133.83333333333331h8.888888888888914v8.333333333333343h-8.888888888888914Z" fill="rgb(239, 249, 189)"/><path aria-label="Count of Records: 2; Defense Score: 105 – 110; Attack Score: 65 – 70" role="graphics-symbol" aria-roledescription="rect mark" d="M178.27777777777777,192.16666666666666h8.888888888888886v8.333333333333371h-8.888888888888886Z" fill="rgb(216, 240, 180)"/><path aria-label="Count of Records: 1; Defense Score: 130 – 135; Attack Score: 75 – 80" role="graphics-symbol" aria-roledescription="rect mark" d="M222.72222222222223,175.49999999999997h8.888888888888857v8.333333333333371h-8.888888888888857Z" fill="rgb(239, 249, 189)"/><path aria-label="Count of Records: 1; Defense Score: 70 – 75; Attack Score: 125 – 130" role="graphics-symbol" aria-roledescription="rect mark" d="M116.05555555555554,92.16666666666667h8.8888888888889v8.333333333333343h-8.8888888888889Z" fill="rgb(239, 249, 189)"/><path aria-label="Count of Records: 2; Defense Score: 110 – 115; Attack Score: 160 – 165" role="graphics-symbol" aria-roledescription="rect mark" d="M187.16666666666666,33.83333333333335h8.888888888888886v8.3333333333333h-8.888888888888886Z" fill="rgb(216, 240, 180)"/><path aria-label="Count of Records: 1; Defense Score: 120 – 125; Attack Score: 70 – 75" role="graphics-symbol" aria-roledescription="rect mark" d="M204.94444444444443,183.83333333333334h8.888888888888914v8.333333333333314h-8.888888888888914Z" fill="rgb(239, 249, 189)"/><path aria-label="Count of Records: 2; Defense Score: 95 – 100; Attack Score: 75 – 80" role="graphics-symbol" aria-roledescription="rect mark" d="M160.5,175.49999999999997h8.888888888888886v8.333333333333371h-8.888888888888886Z" fill="rgb(216, 240, 180)"/><path aria-label="Count of Records: 1; Defense Score: 90 – 95; Attack Score: 110 – 115" role="graphics-symbol" aria-roledescription="rect mark" d="M151.61111111111111,117.16666666666666h8.888888888888886v8.333333333333329h-8.888888888888886Z" fill="rgb(239, 249, 189)"/><path aria-label="Count of Records: 1; Defense Score: 85 – 90; Attack Score: 55 – 60" role="graphics-symbol" aria-roledescription="rect mark" d="M142.72222222222223,208.83333333333331h8.888888888888886v8.333333333333343h-8.888888888888886Z" fill="rgb(239, 249, 189)"/><path aria-label="Count of Records: 3; Defense Score: 80 – 85; Attack Score: 115 – 120" role="graphics-symbol" aria-roledescription="rect mark" d="M133.83333333333331,108.83333333333334h8.888888888888914v8.333333333333314h-8.888888888888914Z" fill="rgb(180, 225, 182)"/><path aria-label="Count of Records: 1; Defense Score: 130 – 135; Attack Score: 135 – 140" role="graphics-symbol" aria-roledescription="rect mark" d="M222.72222222222223,75.5h8.888888888888857v8.333333333333343h-8.888888888888857Z" fill="rgb(239, 249, 189)"/><path aria-label="Count of Records: 1; Defense Score: 60 – 65; Attack Score: 135 – 140" role="graphics-symbol" aria-roledescription="rect mark" d="M98.27777777777777,75.5h8.8888888888889v8.333333333333343h-8.8888888888889Z" fill="rgb(239, 249, 189)"/><path aria-label="Count of Records: 1; Defense Score: 95 – 100; Attack Score: 140 – 145" role="graphics-symbol" aria-roledescription="rect mark" d="M160.5,67.16666666666666h8.888888888888886v8.333333333333343h-8.888888888888886Z" fill="rgb(239, 249, 189)"/><path aria-label="Count of Records: 1; Defense Score: 55 – 60; Attack Score: 65 – 70" role="graphics-symbol" aria-roledescription="rect mark" d="M89.38888888888889,192.16666666666666h8.888888888888886v8.333333333333371h-8.888888888888886Z" fill="rgb(239, 249, 189)"/><path aria-label="Count of Records: 1; Defense Score: 75 – 80; Attack Score: 95 – 100" role="graphics-symbol" aria-roledescription="rect mark" d="M124.94444444444444,142.16666666666666h8.888888888888872v8.333333333333343h-8.888888888888872Z" fill="rgb(239, 249, 189)"/><path aria-label="Count of Records: 1; Defense Score: 75 – 80; Attack Score: 125 – 130" role="graphics-symbol" aria-roledescription="rect mark" d="M124.94444444444444,92.16666666666667h8.888888888888872v8.333333333333343h-8.888888888888872Z" fill="rgb(239, 249, 189)"/><path aria-label="Count of Records: 1; Defense Score: 90 – 95; Attack Score: 60 – 65" role="graphics-symbol" aria-roledescription="rect mark" d="M151.61111111111111,200.50000000000003h8.888888888888886v8.333333333333286h-8.888888888888886Z" fill="rgb(239, 249, 189)"/><path aria-label="Count of Records: 1; Defense Score: 60 – 65; Attack Score: 25 – 30" role="graphics-symbol" aria-roledescription="rect mark" d="M98.27777777777777,258.83333333333337h8.8888888888889v8.333333333333258h-8.8888888888889Z" fill="rgb(239, 249, 189)"/><path aria-label="Count of Records: 3; Defense Score: 85 – 90; Attack Score: 65 – 70" role="graphics-symbol" aria-roledescription="rect mark" d="M142.72222222222223,192.16666666666666h8.888888888888886v8.333333333333371h-8.888888888888886Z" fill="rgb(180, 225, 182)"/><path aria-label="Count of Records: 1; Defense Score: 45 – 50; Attack Score: 80 – 85" role="graphics-symbol" aria-roledescription="rect mark" d="M71.61111111111111,167.16666666666669h8.888888888888886v8.333333333333286h-8.888888888888886Z" fill="rgb(239, 249, 189)"/><path aria-label="Count of Records: 1; Defense Score: 105 – 110; Attack Score: 30 – 35" role="graphics-symbol" aria-roledescription="rect mark" d="M178.27777777777777,250.5h8.888888888888886v8.333333333333371h-8.888888888888886Z" fill="rgb(239, 249, 189)"/><path aria-label="Count of Records: 1; Defense Score: 115 – 120; Attack Score: 90 – 95" role="graphics-symbol" aria-roledescription="rect mark" d="M196.05555555555554,150.5h8.888888888888886v8.333333333333343h-8.888888888888886Z" fill="rgb(239, 249, 189)"/><path aria-label="Count of Records: 1; Defense Score: 85 – 90; Attack Score: 30 – 35" role="graphics-symbol" aria-roledescription="rect mark" d="M142.72222222222223,250.5h8.888888888888886v8.333333333333371h-8.888888888888886Z" fill="rgb(239, 249, 189)"/><path aria-label="Count of Records: 1; Defense Score: 145 – 150; Attack Score: 50 – 55" role="graphics-symbol" aria-roledescription="rect mark" d="M249.38888888888889,217.16666666666666h8.888888888888886v8.333333333333343h-8.888888888888886Z" fill="rgb(239, 249, 189)"/><path aria-label="Count of Records: 1; Defense Score: 130 – 135; Attack Score: 105 – 110" role="graphics-symbol" aria-roledescription="rect mark" d="M222.72222222222223,125.49999999999999h8.888888888888857v8.333333333333329h-8.888888888888857Z" fill="rgb(239, 249, 189)"/><path aria-label="Count of Records: 1; Defense Score: 45 – 50; Attack Score: 110 – 115" role="graphics-symbol" aria-roledescription="rect mark" d="M71.61111111111111,117.16666666666666h8.888888888888886v8.333333333333329h-8.888888888888886Z" fill="rgb(239, 249, 189)"/><path aria-label="Count of Records: 1; Defense Score: 65 – 70; Attack Score: 140 – 145" role="graphics-symbol" aria-roledescription="rect mark" d="M107.16666666666667,67.16666666666666h8.888888888888872v8.333333333333343h-8.888888888888872Z" fill="rgb(239, 249, 189)"/><path aria-label="Count of Records: 4; Defense Score: 60 – 65; Attack Score: 50 – 55" role="graphics-symbol" aria-roledescription="rect mark" d="M98.27777777777777,217.16666666666666h8.8888888888889v8.333333333333343h-8.8888888888889Z" fill="rgb(134, 208, 187)"/><path aria-label="Count of Records: 1; Defense Score: 45 – 50; Attack Score: 75 – 80" role="graphics-symbol" aria-roledescription="rect mark" d="M71.61111111111111,175.49999999999997h8.888888888888886v8.333333333333371h-8.888888888888886Z" fill="rgb(239, 249, 189)"/><path aria-label="Count of Records: 2; Defense Score: 105 – 110; Attack Score: 135 – 140" role="graphics-symbol" aria-roledescription="rect mark" d="M178.27777777777777,75.5h8.888888888888886v8.333333333333343h-8.888888888888886Z" fill="rgb(216, 240, 180)"/><path aria-label="Count of Records: 1; Defense Score: 90 – 95; Attack Score: 55 – 60" role="graphics-symbol" aria-roledescription="rect mark" d="M151.61111111111111,208.83333333333331h8.888888888888886v8.333333333333343h-8.888888888888886Z" fill="rgb(239, 249, 189)"/><path aria-label="Count of Records: 1; Defense Score: 70 – 75; Attack Score: 115 – 120" role="graphics-symbol" aria-roledescription="rect mark" d="M116.05555555555554,108.83333333333334h8.8888888888889v8.333333333333314h-8.8888888888889Z" fill="rgb(239, 249, 189)"/><path aria-label="Count of Records: 2; Defense Score: 90 – 95; Attack Score: 145 – 150" role="graphics-symbol" aria-roledescription="rect mark" d="M151.61111111111111,58.83333333333333h8.888888888888886v8.333333333333329h-8.888888888888886Z" fill="rgb(216, 240, 180)"/><path aria-label="Count of Records: 1; Defense Score: 60 – 65; Attack Score: 125 – 130" role="graphics-symbol" aria-roledescription="rect mark" d="M98.27777777777777,92.16666666666667h8.8888888888889v8.333333333333343h-8.8888888888889Z" fill="rgb(239, 249, 189)"/><path aria-label="Count of Records: 3; Defense Score: 90 – 95; Attack Score: 120 – 125" role="graphics-symbol" aria-roledescription="rect mark" d="M151.61111111111111,100.50000000000001h8.888888888888886v8.333333333333329h-8.888888888888886Z" fill="rgb(180, 225, 182)"/><path aria-label="Count of Records: 1; Defense Score: 95 – 100; Attack Score: 110 – 115" role="graphics-symbol" aria-roledescription="rect mark" d="M160.5,117.16666666666666h8.888888888888886v8.333333333333329h-8.888888888888886Z" fill="rgb(239, 249, 189)"/><path aria-label="Count of Records: 1; Defense Score: 110 – 115; Attack Score: 105 – 110" role="graphics-symbol" aria-roledescription="rect mark" d="M187.16666666666666,125.49999999999999h8.888888888888886v8.333333333333329h-8.888888888888886Z" fill="rgb(239, 249, 189)"/><path aria-label="Count of Records: 1; Defense Score: 50 – 55; Attack Score: 65 – 70" role="graphics-symbol" aria-roledescription="rect mark" d="M80.5,192.16666666666666h8.888888888888886v8.333333333333371h-8.888888888888886Z" fill="rgb(239, 249, 189)"/><path aria-label="Count of Records: 1; Defense Score: 125 – 130; Attack Score: 90 – 95" role="graphics-symbol" aria-roledescription="rect mark" d="M213.83333333333334,150.5h8.888888888888886v8.333333333333343h-8.888888888888886Z" fill="rgb(239, 249, 189)"/><path aria-label="Count of Records: 2; Defense Score: 90 – 95; Attack Score: 125 – 130" role="graphics-symbol" aria-roledescription="rect mark" d="M151.61111111111111,92.16666666666667h8.888888888888886v8.333333333333343h-8.888888888888886Z" fill="rgb(216, 240, 180)"/><path aria-label="Count of Records: 2; Defense Score: 70 – 75; Attack Score: 105 – 110" role="graphics-symbol" aria-roledescription="rect mark" d="M116.05555555555554,125.49999999999999h8.8888888888889v8.333333333333329h-8.8888888888889Z" fill="rgb(216, 240, 180)"/><path aria-label="Count of Records: 1; Defense Score: 120 – 125; Attack Score: 150 – 155" role="graphics-symbol" aria-roledescription="rect mark" d="M204.94444444444443,50.499999999999986h8.888888888888914v8.333333333333343h-8.888888888888914Z" fill="rgb(239, 249, 189)"/><path aria-label="Count of Records: 3; Defense Score: 90 – 95; Attack Score: 70 – 75" role="graphics-symbol" aria-roledescription="rect mark" d="M151.61111111111111,183.83333333333334h8.888888888888886v8.333333333333314h-8.888888888888886Z" fill="rgb(180, 225, 182)"/><path aria-label="Count of Records: 2; Defense Score: 95 – 100; Attack Score: 120 – 125" role="graphics-symbol" aria-roledescription="rect mark" d="M160.5,100.50000000000001h8.888888888888886v8.333333333333329h-8.888888888888886Z" fill="rgb(216, 240, 180)"/><path aria-label="Count of Records: 1; Defense Score: 120 – 125; Attack Score: 105 – 110" role="graphics-symbol" aria-roledescription="rect mark" d="M204.94444444444443,125.49999999999999h8.888888888888914v8.333333333333329h-8.888888888888914Z" fill="rgb(239, 249, 189)"/><path aria-label="Count of Records: 1; Defense Score: 65 – 70; Attack Score: 145 – 150" role="graphics-symbol" aria-roledescription="rect mark" d="M107.16666666666667,58.83333333333333h8.888888888888872v8.333333333333329h-8.888888888888872Z" fill="rgb(239, 249, 189)"/><path aria-label="Count of Records: 1; Defense Score: 60 – 65; Attack Score: 20 – 25" role="graphics-symbol" aria-roledescription="rect mark" d="M98.27777777777777,267.16666666666663h8.8888888888889v8.333333333333371h-8.8888888888889Z" fill="rgb(239, 249, 189)"/><path aria-label="Count of Records: 1; Defense Score: 150 – 155; Attack Score: 110 – 115" role="graphics-symbol" aria-roledescription="rect mark" d="M258.27777777777777,117.16666666666666h8.888888888888857v8.333333333333329h-8.888888888888857Z" fill="rgb(239, 249, 189)"/><path aria-label="Count of Records: 1; Defense Score: 50 – 55; Attack Score: 150 – 155" role="graphics-symbol" aria-roledescription="rect mark" d="M80.5,50.499999999999986h8.888888888888886v8.333333333333343h-8.888888888888886Z" fill="rgb(239, 249, 189)"/><path aria-label="Count of Records: 1; Defense Score: 115 – 120; Attack Score: 105 – 110" role="graphics-symbol" aria-roledescription="rect mark" d="M196.05555555555554,125.49999999999999h8.888888888888886v8.333333333333329h-8.888888888888886Z" fill="rgb(239, 249, 189)"/><path aria-label="Count of Records: 1; Defense Score: 85 – 90; Attack Score: 70 – 75" role="graphics-symbol" aria-roledescription="rect mark" d="M142.72222222222223,183.83333333333334h8.888888888888886v8.333333333333314h-8.888888888888886Z" fill="rgb(239, 249, 189)"/><path aria-label="Count of Records: 1; Defense Score: 115 – 120; Attack Score: 120 – 125" role="graphics-symbol" aria-roledescription="rect mark" d="M196.05555555555554,100.50000000000001h8.888888888888886v8.333333333333329h-8.888888888888886Z" fill="rgb(239, 249, 189)"/><path aria-label="Count of Records: 1; Defense Score: 75 – 80; Attack Score: 90 – 95" role="graphics-symbol" aria-roledescription="rect mark" d="M124.94444444444444,150.5h8.888888888888872v8.333333333333343h-8.888888888888872Z" fill="rgb(239, 249, 189)"/><path aria-label="Count of Records: 1; Defense Score: 150 – 155; Attack Score: 50 – 55" role="graphics-symbol" aria-roledescription="rect mark" d="M258.27777777777777,217.16666666666666h8.888888888888857v8.333333333333343h-8.888888888888857Z" fill="rgb(239, 249, 189)"/><path aria-label="Count of Records: 1; Defense Score: 180 – 185; Attack Score: 115 – 120" role="graphics-symbol" aria-roledescription="rect mark" d="M311.61111111111114,108.83333333333334h8.888888888888857v8.333333333333314h-8.888888888888857Z" fill="rgb(239, 249, 189)"/><path aria-label="Count of Records: 1; Defense Score: 60 – 65; Attack Score: 160 – 165" role="graphics-symbol" aria-roledescription="rect mark" d="M98.27777777777777,33.83333333333335h8.8888888888889v8.3333333333333h-8.8888888888889Z" fill="rgb(239, 249, 189)"/><path aria-label="Count of Records: 1; Defense Score: 120 – 125; Attack Score: 110 – 115" role="graphics-symbol" aria-roledescription="rect mark" d="M204.94444444444443,117.16666666666666h8.888888888888914v8.333333333333329h-8.888888888888914Z" fill="rgb(239, 249, 189)"/><path aria-label="Count of Records: 1; Defense Score: 90 – 95; Attack Score: 115 – 120" role="graphics-symbol" aria-roledescription="rect mark" d="M151.61111111111111,108.83333333333334h8.888888888888886v8.333333333333314h-8.888888888888886Z" fill="rgb(239, 249, 189)"/><path aria-label="Count of Records: 1; Defense Score: 30 – 35; Attack Score: 75 – 80" role="graphics-symbol" aria-roledescription="rect mark" d="M44.94444444444444,175.49999999999997h8.888888888888893v8.333333333333371h-8.888888888888893Z" fill="rgb(239, 249, 189)"/><path aria-label="Count of Records: 1; Defense Score: 30 – 35; Attack Score: 70 – 75" role="graphics-symbol" aria-roledescription="rect mark" d="M44.94444444444444,183.83333333333334h8.888888888888893v8.333333333333314h-8.888888888888893Z" fill="rgb(239, 249, 189)"/><path aria-label="Count of Records: 1; Defense Score: 60 – 65; Attack Score: 110 – 115" role="graphics-symbol" aria-roledescription="rect mark" d="M98.27777777777777,117.16666666666666h8.8888888888889v8.333333333333329h-8.8888888888889Z" fill="rgb(239, 249, 189)"/><path aria-label="Count of Records: 1; Defense Score: 60 – 65; Attack Score: 55 – 60" role="graphics-symbol" aria-roledescription="rect mark" d="M98.27777777777777,208.83333333333331h8.8888888888889v8.333333333333343h-8.8888888888889Z" fill="rgb(239, 249, 189)"/><path aria-label="Count of Records: 1; Defense Score: 75 – 80; Attack Score: 115 – 120" role="graphics-symbol" aria-roledescription="rect mark" d="M124.94444444444444,108.83333333333334h8.888888888888872v8.333333333333314h-8.888888888888872Z" fill="rgb(239, 249, 189)"/><path aria-label="Count of Records: 1; Defense Score: 150 – 155; Attack Score: 60 – 65" role="graphics-symbol" aria-roledescription="rect mark" d="M258.27777777777777,200.50000000000003h8.888888888888857v8.333333333333286h-8.888888888888857Z" fill="rgb(239, 249, 189)"/><path aria-label="Count of Records: 1; Defense Score: 80 – 85; Attack Score: 45 – 50" role="graphics-symbol" aria-roledescription="rect mark" d="M133.83333333333331,225.5h8.888888888888914v8.333333333333343h-8.888888888888914Z" fill="rgb(239, 249, 189)"/><path aria-label="Count of Records: 1; Defense Score: 80 – 85; Attack Score: 125 – 130" role="graphics-symbol" aria-roledescription="rect mark" d="M133.83333333333331,92.16666666666667h8.888888888888914v8.333333333333343h-8.888888888888914Z" fill="rgb(239, 249, 189)"/><path aria-label="Count of Records: 1; Defense Score: 45 – 50; Attack Score: 40 – 45" role="graphics-symbol" aria-roledescription="rect mark" d="M71.61111111111111,233.83333333333334h8.888888888888886v8.333333333333343h-8.888888888888886Z" fill="rgb(239, 249, 189)"/><path aria-label="Count of Records: 1; Defense Score: 140 – 145; Attack Score: 125 – 130" role="graphics-symbol" aria-roledescription="rect mark" d="M240.5,92.16666666666667h8.888888888888886v8.333333333333343h-8.888888888888886Z" fill="rgb(239, 249, 189)"/><path aria-label="Count of Records: 1; Defense Score: 110 – 115; Attack Score: 75 – 80" role="graphics-symbol" aria-roledescription="rect mark" d="M187.16666666666666,175.49999999999997h8.888888888888886v8.333333333333371h-8.888888888888886Z" fill="rgb(239, 249, 189)"/><path aria-label="Count of Records: 1; Defense Score: 130 – 135; Attack Score: 60 – 65" role="graphics-symbol" aria-roledescription="rect mark" d="M222.72222222222223,200.50000000000003h8.888888888888857v8.333333333333286h-8.888888888888857Z" fill="rgb(239, 249, 189)"/><path aria-label="Count of Records: 1; Defense Score: 65 – 70; Attack Score: 115 – 120" role="graphics-symbol" aria-roledescription="rect mark" d="M107.16666666666667,108.83333333333334h8.888888888888872v8.333333333333314h-8.888888888888872Z" fill="rgb(239, 249, 189)"/><path aria-label="Count of Records: 1; Defense Score: 135 – 140; Attack Score: 75 – 80" role="graphics-symbol" aria-roledescription="rect mark" d="M231.6111111111111,175.49999999999997h8.888888888888914v8.333333333333371h-8.888888888888914Z" fill="rgb(239, 249, 189)"/><path aria-label="Count of Records: 1; Defense Score: 125 – 130; Attack Score: 110 – 115" role="graphics-symbol" aria-roledescription="rect mark" d="M213.83333333333334,117.16666666666666h8.888888888888886v8.333333333333329h-8.888888888888886Z" fill="rgb(239, 249, 189)"/><path aria-label="Count of Records: 1; Defense Score: 30 – 35; Attack Score: 25 – 30" role="graphics-symbol" aria-roledescription="rect mark" d="M44.94444444444444,258.83333333333337h8.888888888888893v8.333333333333258h-8.888888888888893Z" fill="rgb(239, 249, 189)"/><path aria-label="Count of Records: 1; Defense Score: 130 – 135; Attack Score: 25 – 30" role="graphics-symbol" aria-roledescription="rect mark" d="M222.72222222222223,258.83333333333337h8.888888888888857v8.333333333333258h-8.888888888888857Z" fill="rgb(239, 249, 189)"/><path aria-label="Count of Records: 1; Defense Score: 85 – 90; Attack Score: 110 – 115" role="graphics-symbol" aria-roledescription="rect mark" d="M142.72222222222223,117.16666666666666h8.888888888888886v8.333333333333329h-8.888888888888886Z" fill="rgb(239, 249, 189)"/><path aria-label="Count of Records: 1; Defense Score: 135 – 140; Attack Score: 135 – 140" role="graphics-symbol" aria-roledescription="rect mark" d="M231.6111111111111,75.5h8.888888888888914v8.333333333333343h-8.888888888888914Z" fill="rgb(239, 249, 189)"/><path aria-label="Count of Records: 1; Defense Score: 35 – 40; Attack Score: 135 – 140" role="graphics-symbol" aria-roledescription="rect mark" d="M53.833333333333336,75.5h8.888888888888886v8.333333333333343h-8.888888888888886Z" fill="rgb(239, 249, 189)"/><path aria-label="Count of Records: 1; Defense Score: 130 – 135; Attack Score: 180 – 185" role="graphics-symbol" aria-roledescription="rect mark" d="M222.72222222222223,0.5h8.888888888888857v8.333333333333337h-8.888888888888857Z" fill="rgb(239, 249, 189)"/><path aria-label="Count of Records: 1; Defense Score: 50 – 55; Attack Score: 100 – 105" role="graphics-symbol" aria-roledescription="rect mark" d="M80.5,133.83333333333331h8.888888888888886v8.333333333333343h-8.888888888888886Z" fill="rgb(239, 249, 189)"/></g><g class="mark-group role-legend" role="graphics-symbol" aria-roledescription="legend" aria-label="Gradient legend titled 'Count of Records' for fill color with values from 1 to 10"><g transform="translate(418,0)"><path class="background" aria-hidden="true" d="M0,0h140v216h-140Z" pointer-events="none"/><g><g class="mark-group role-legend-entry"><g transform="translate(0,16)"><path class="background" aria-hidden="true" d="M0,0h0v0h0Z" pointer-events="none"/><g><g class="mark-rect role-legend-gradient" pointer-events="none"><path d="M0,0h16v200h-16Z" fill="url(#gradient_0)" stroke="#ddd" stroke-width="0" opacity="1"/></g><g class="mark-text role-legend-label" pointer-events="none"><text text-anchor="start" transform="translate(18,180.77777777777777)" font-family="sans-serif" font-size="10px" fill="#000" opacity="1">2</text><text text-anchor="start" transform="translate(18,136.33333333333334)" font-family="sans-serif" font-size="10px" fill="#000" opacity="1">4</text><text text-anchor="start" transform="translate(18,91.88888888888889)" font-family="sans-serif" font-size="10px" fill="#000" opacity="1">6</text><text text-anchor="start" transform="translate(18,47.44444444444444)" font-family="sans-serif" font-size="10px" fill="#000" opacity="1">8</text><text text-anchor="start" transform="translate(18,8)" font-family="sans-serif" font-size="10px" fill="#000" opacity="1">10</text></g></g><path class="foreground" aria-hidden="true" d="" pointer-events="none" display="none"/></g></g><g class="mark-text role-legend-title" pointer-events="none"><text text-anchor="start" transform="translate(0,9)" font-family="sans-serif" font-size="11px" font-weight="bold" fill="#000" opacity="1">Count
of
Records</text></g></g><path class="foreground" aria-hidden="true" d="" pointer-events="none" display="none"/></g></g><g class="mark-group role-title"><g transform="translate(200,-22)"><path class="background" aria-hidden="true" d="M0,0h0v0h0Z" pointer-events="none"/><g><g class="mark-text role-title-text" role="graphics-symbol" aria-roledescription="title" aria-label="Title text 'Pokemon Scores'" pointer-events="none"><text text-anchor="middle" transform="translate(0,10)" font-family="sans-serif" font-size="13px" font-weight="bold" fill="#000" opacity="1">Pokemon
Scores</text></g></g><path class="foreground" aria-hidden="true" d="" pointer-events="none" display="none"/></g></g><g class="mark-group role-axis" role="graphics-symbol" aria-roledescription="axis" aria-label="X-axis titled 'Defense Score' for a linear scale with values from 5 to 230"><g transform="translate(0.5,300.5)"><path class="background" aria-hidden="true" d="M0,0h0v0h0Z" pointer-events="none"/><g><g class="mark-rule role-axis-tick" pointer-events="none"><line transform="translate(0,0)" x2="0" y2="5" stroke="#888" stroke-width="1" opacity="1"/><line transform="translate(9,0)" x2="0" y2="5" stroke="#888" stroke-width="1" opacity="1"/><line transform="translate(18,0)" x2="0" y2="5" stroke="#888" stroke-width="1" opacity="1"/><line transform="translate(27,0)" x2="0" y2="5" stroke="#888" stroke-width="1" opacity="1"/><line transform="translate(36,0)" x2="0" y2="5" stroke="#888" stroke-width="1" opacity="1"/><line transform="translate(44,0)" x2="0" y2="5" stroke="#888" stroke-width="1" opacity="1"/><line transform="translate(53,0)" x2="0" y2="5" stroke="#888" stroke-width="1" opacity="1"/><line transform="translate(62,0)" x2="0" y2="5" stroke="#888" stroke-width="1" opacity="1"/><line transform="translate(71,0)" x2="0" y2="5" stroke="#888" stroke-width="1" opacity="1"/><line transform="translate(80,0)" x2="0" y2="5" stroke="#888" stroke-width="1" opacity="1"/><line transform="translate(89,0)" x2="0" y2="5" stroke="#888" stroke-width="1" opacity="1"/><line transform="translate(98,0)" x2="0" y2="5" stroke="#888" stroke-width="1" opacity="1"/><line transform="translate(107,0)" x2="0" y2="5" stroke="#888" stroke-width="1" opacity="1"/><line transform="translate(116,0)" x2="0" y2="5" stroke="#888" stroke-width="1" opacity="1"/><line transform="translate(124,0)" x2="0" y2="5" stroke="#888" stroke-width="1" opacity="1"/><line transform="translate(133,0)" x2="0" y2="5" stroke="#888" stroke-width="1" opacity="1"/><line transform="translate(142,0)" x2="0" y2="5" stroke="#888" stroke-width="1" opacity="1"/><line transform="translate(151,0)" x2="0" y2="5" stroke="#888" stroke-width="1" opacity="1"/><line transform="translate(160,0)" x2="0" y2="5" stroke="#888" stroke-width="1" opacity="1"/><line transform="translate(169,0)" x2="0" y2="5" stroke="#888" stroke-width="1" opacity="1"/><line transform="translate(178,0)" x2="0" y2="5" stroke="#888" stroke-width="1" opacity="1"/><line transform="translate(187,0)" x2="0" y2="5" stroke="#888" stroke-width="1" opacity="1"/><line transform="translate(196,0)" x2="0" y2="5" stroke="#888" stroke-width="1" opacity="1"/><line transform="translate(204,0)" x2="0" y2="5" stroke="#888" stroke-width="1" opacity="1"/><line transform="translate(213,0)" x2="0" y2="5" stroke="#888" stroke-width="1" opacity="1"/><line transform="translate(222,0)" x2="0" y2="5" stroke="#888" stroke-width="1" opacity="1"/><line transform="translate(231,0)" x2="0" y2="5" stroke="#888" stroke-width="1" opacity="1"/><line transform="translate(240,0)" x2="0" y2="5" stroke="#888" stroke-width="1" opacity="1"/><line transform="translate(249,0)" x2="0" y2="5" stroke="#888" stroke-width="1" opacity="1"/><line transform="translate(258,0)" x2="0" y2="5" stroke="#888" stroke-width="1" opacity="1"/><line transform="translate(267,0)" x2="0" y2="5" stroke="#888" stroke-width="1" opacity="1"/><line transform="translate(276,0)" x2="0" y2="5" stroke="#888" stroke-width="1" opacity="1"/><line transform="translate(284,0)" x2="0" y2="5" stroke="#888" stroke-width="1" opacity="1"/><line transform="translate(293,0)" x2="0" y2="5" stroke="#888" stroke-width="1" opacity="1"/><line transform="translate(302,0)" x2="0" y2="5" stroke="#888" stroke-width="1" opacity="1"/><line transform="translate(311,0)" x2="0" y2="5" stroke="#888" stroke-width="1" opacity="1"/><line transform="translate(320,0)" x2="0" y2="5" stroke="#888" stroke-width="1" opacity="1"/><line transform="translate(329,0)" x2="0" y2="5" stroke="#888" stroke-width="1" opacity="1"/><line transform="translate(338,0)" x2="0" y2="5" stroke="#888" stroke-width="1" opacity="1"/><line transform="translate(347,0)" x2="0" y2="5" stroke="#888" stroke-width="1" opacity="1"/><line transform="translate(356,0)" x2="0" y2="5" stroke="#888" stroke-width="1" opacity="1"/><line transform="translate(364,0)" x2="0" y2="5" stroke="#888" stroke-width="1" opacity="1"/><line transform="translate(373,0)" x2="0" y2="5" stroke="#888" stroke-width="1" opacity="1"/><line transform="translate(382,0)" x2="0" y2="5" stroke="#888" stroke-width="1" opacity="1"/><line transform="translate(391,0)" x2="0" y2="5" stroke="#888" stroke-width="1" opacity="1"/><line transform="translate(400,0)" x2="0" y2="5" stroke="#888" stroke-width="1" opacity="1"/></g><g class="mark-text role-axis-label" pointer-events="none"><text text-anchor="start" transform="translate(0,15)" font-family="sans-serif" font-size="10px" fill="#000" opacity="1">5</text><text text-anchor="middle" transform="translate(8.88888888888889,15)" font-family="sans-serif" font-size="10px" fill="#000" opacity="0">10</text><text text-anchor="middle" transform="translate(17.77777777777778,15)" font-family="sans-serif" font-size="10px" fill="#000" opacity="0">15</text><text text-anchor="middle" transform="translate(26.666666666666668,15)" font-family="sans-serif" font-size="10px" fill="#000" opacity="0">20</text><text text-anchor="middle" transform="translate(35.55555555555556,15)" font-family="sans-serif" font-size="10px" fill="#000" opacity="1">25</text><text text-anchor="middle" transform="translate(44.44444444444444,15)" font-family="sans-serif" font-size="10px" fill="#000" opacity="0">30</text><text text-anchor="middle" transform="translate(53.333333333333336,15)" font-family="sans-serif" font-size="10px" fill="#000" opacity="0">35</text><text text-anchor="middle" transform="translate(62.22222222222222,15)" font-family="sans-serif" font-size="10px" fill="#000" opacity="0">40</text><text text-anchor="middle" transform="translate(71.11111111111111,15)" font-family="sans-serif" font-size="10px" fill="#000" opacity="1">45</text><text text-anchor="middle" transform="translate(80,15)" font-family="sans-serif" font-size="10px" fill="#000" opacity="0">50</text><text text-anchor="middle" transform="translate(88.88888888888889,15)" font-family="sans-serif" font-size="10px" fill="#000" opacity="0">55</text><text text-anchor="middle" transform="translate(97.77777777777777,15)" font-family="sans-serif" font-size="10px" fill="#000" opacity="0">60</text><text text-anchor="middle" transform="translate(106.66666666666667,15)" font-family="sans-serif" font-size="10px" fill="#000" opacity="1">65</text><text text-anchor="middle" transform="translate(115.55555555555554,15)" font-family="sans-serif" font-size="10px" fill="#000" opacity="0">70</text><text text-anchor="middle" transform="translate(124.44444444444444,15)" font-family="sans-serif" font-size="10px" fill="#000" opacity="0">75</text><text text-anchor="middle" transform="translate(133.33333333333331,15)" font-family="sans-serif" font-size="10px" fill="#000" opacity="0">80</text><text text-anchor="middle" transform="translate(142.22222222222223,15)" font-family="sans-serif" font-size="10px" fill="#000" opacity="1">85</text><text text-anchor="middle" transform="translate(151.11111111111111,15)" font-family="sans-serif" font-size="10px" fill="#000" opacity="0">90</text><text text-anchor="middle" transform="translate(160,15)" font-family="sans-serif" font-size="10px" fill="#000" opacity="0">95</text><text text-anchor="middle" transform="translate(168.88888888888889,15)" font-family="sans-serif" font-size="10px" fill="#000" opacity="0">100</text><text text-anchor="middle" transform="translate(177.77777777777777,15)" font-family="sans-serif" font-size="10px" fill="#000" opacity="1">105</text><text text-anchor="middle" transform="translate(186.66666666666666,15)" font-family="sans-serif" font-size="10px" fill="#000" opacity="0">110</text><text text-anchor="middle" transform="translate(195.55555555555554,15)" font-family="sans-serif" font-size="10px" fill="#000" opacity="0">115</text><text text-anchor="middle" transform="translate(204.44444444444443,15)" font-family="sans-serif" font-size="10px" fill="#000" opacity="0">120</text><text text-anchor="middle" transform="translate(213.33333333333334,15)" font-family="sans-serif" font-size="10px" fill="#000" opacity="1">125</text><text text-anchor="middle" transform="translate(222.22222222222223,15)" font-family="sans-serif" font-size="10px" fill="#000" opacity="0">130</text><text text-anchor="middle" transform="translate(231.1111111111111,15)" font-family="sans-serif" font-size="10px" fill="#000" opacity="0">135</text><text text-anchor="middle" transform="translate(240,15)" font-family="sans-serif" font-size="10px" fill="#000" opacity="0">140</text><text text-anchor="middle" transform="translate(248.88888888888889,15)" font-family="sans-serif" font-size="10px" fill="#000" opacity="1">145</text><text text-anchor="middle" transform="translate(257.77777777777777,15)" font-family="sans-serif" font-size="10px" fill="#000" opacity="0">150</text><text text-anchor="middle" transform="translate(266.66666666666663,15)" font-family="sans-serif" font-size="10px" fill="#000" opacity="0">155</text><text text-anchor="middle" transform="translate(275.55555555555554,15)" font-family="sans-serif" font-size="10px" fill="#000" opacity="0">160</text><text text-anchor="middle" transform="translate(284.44444444444446,15)" font-family="sans-serif" font-size="10px" fill="#000" opacity="1">165</text><text text-anchor="middle" transform="translate(293.3333333333333,15)" font-family="sans-serif" font-size="10px" fill="#000" opacity="0">170</text><text text-anchor="middle" transform="translate(302.22222222222223,15)" font-family="sans-serif" font-size="10px" fill="#000" opacity="0">175</text><text text-anchor="middle" transform="translate(311.11111111111114,15)" font-family="sans-serif" font-size="10px" fill="#000" opacity="0">180</text><text text-anchor="middle" transform="translate(320,15)" font-family="sans-serif" font-size="10px" fill="#000" opacity="1">185</text><text text-anchor="middle" transform="translate(328.88888888888886,15)" font-family="sans-serif" font-size="10px" fill="#000" opacity="0">190</text><text text-anchor="middle" transform="translate(337.77777777777777,15)" font-family="sans-serif" font-size="10px" fill="#000" opacity="0">195</text><text text-anchor="middle" transform="translate(346.6666666666667,15)" font-family="sans-serif" font-size="10px" fill="#000" opacity="0">200</text><text text-anchor="middle" transform="translate(355.55555555555554,15)" font-family="sans-serif" font-size="10px" fill="#000" opacity="1">205</text><text text-anchor="middle" transform="translate(364.44444444444446,15)" font-family="sans-serif" font-size="10px" fill="#000" opacity="0">210</text><text text-anchor="middle" transform="translate(373.3333333333333,15)" font-family="sans-serif" font-size="10px" fill="#000" opacity="0">215</text><text text-anchor="middle" transform="translate(382.22222222222223,15)" font-family="sans-serif" font-size="10px" fill="#000" opacity="0">220</text><text text-anchor="middle" transform="translate(391.1111111111111,15)" font-family="sans-serif" font-size="10px" fill="#000" opacity="1">225</text><text text-anchor="end" transform="translate(400,15)" font-family="sans-serif" font-size="10px" fill="#000" opacity="0">230</text></g><g class="mark-rule role-axis-domain" pointer-events="none"><line transform="translate(0,0)" x2="400" y2="0" stroke="#888" stroke-width="1" opacity="1"/></g><g class="mark-text role-axis-title" pointer-events="none"><text text-anchor="middle" transform="translate(200,30)" font-family="sans-serif" font-size="11px" font-weight="bold" fill="#000" opacity="1">Defense
Score</text></g></g><path class="foreground" aria-hidden="true" d="" pointer-events="none" display="none"/></g></g><g class="mark-group role-axis" role="graphics-symbol" aria-roledescription="axis" aria-label="Y-axis titled 'Attack Score' for a linear scale with values from 5 to 185"><g transform="translate(0.5,0.5)"><path class="background" aria-hidden="true" d="M0,0h0v0h0Z" pointer-events="none"/><g><g class="mark-rule role-axis-tick" pointer-events="none"><line transform="translate(0,300)" x2="-5" y2="0" stroke="#888" stroke-width="1" opacity="1"/><line transform="translate(0,292)" x2="-5" y2="0" stroke="#888" stroke-width="1" opacity="1"/><line transform="translate(0,283)" x2="-5" y2="0" stroke="#888" stroke-width="1" opacity="1"/><line transform="translate(0,275)" x2="-5" y2="0" stroke="#888" stroke-width="1" opacity="1"/><line transform="translate(0,267)" x2="-5" y2="0" stroke="#888" stroke-width="1" opacity="1"/><line transform="translate(0,258)" x2="-5" y2="0" stroke="#888" stroke-width="1" opacity="1"/><line transform="translate(0,250)" x2="-5" y2="0" stroke="#888" stroke-width="1" opacity="1"/><line transform="translate(0,242)" x2="-5" y2="0" stroke="#888" stroke-width="1" opacity="1"/><line transform="translate(0,233)" x2="-5" y2="0" stroke="#888" stroke-width="1" opacity="1"/><line transform="translate(0,225)" x2="-5" y2="0" stroke="#888" stroke-width="1" opacity="1"/><line transform="translate(0,217)" x2="-5" y2="0" stroke="#888" stroke-width="1" opacity="1"/><line transform="translate(0,208)" x2="-5" y2="0" stroke="#888" stroke-width="1" opacity="1"/><line transform="translate(0,200)" x2="-5" y2="0" stroke="#888" stroke-width="1" opacity="1"/><line transform="translate(0,192)" x2="-5" y2="0" stroke="#888" stroke-width="1" opacity="1"/><line transform="translate(0,183)" x2="-5" y2="0" stroke="#888" stroke-width="1" opacity="1"/><line transform="translate(0,175)" x2="-5" y2="0" stroke="#888" stroke-width="1" opacity="1"/><line transform="translate(0,167)" x2="-5" y2="0" stroke="#888" stroke-width="1" opacity="1"/><line transform="translate(0,158)" x2="-5" y2="0" stroke="#888" stroke-width="1" opacity="1"/><line transform="translate(0,150)" x2="-5" y2="0" stroke="#888" stroke-width="1" opacity="1"/><line transform="translate(0,142)" x2="-5" y2="0" stroke="#888" stroke-width="1" opacity="1"/><line transform="translate(0,133)" x2="-5" y2="0" stroke="#888" stroke-width="1" opacity="1"/><line transform="translate(0,125)" x2="-5" y2="0" stroke="#888" stroke-width="1" opacity="1"/><line transform="translate(0,117)" x2="-5" y2="0" stroke="#888" stroke-width="1" opacity="1"/><line transform="translate(0,108)" x2="-5" y2="0" stroke="#888" stroke-width="1" opacity="1"/><line transform="translate(0,100)" x2="-5" y2="0" stroke="#888" stroke-width="1" opacity="1"/><line transform="translate(0,92)" x2="-5" y2="0" stroke="#888" stroke-width="1" opacity="1"/><line transform="translate(0,83)" x2="-5" y2="0" stroke="#888" stroke-width="1" opacity="1"/><line transform="translate(0,75)" x2="-5" y2="0" stroke="#888" stroke-width="1" opacity="1"/><line transform="translate(0,67)" x2="-5" y2="0" stroke="#888" stroke-width="1" opacity="1"/><line transform="translate(0,58)" x2="-5" y2="0" stroke="#888" stroke-width="1" opacity="1"/><line transform="translate(0,50)" x2="-5" y2="0" stroke="#888" stroke-width="1" opacity="1"/><line transform="translate(0,42)" x2="-5" y2="0" stroke="#888" stroke-width="1" opacity="1"/><line transform="translate(0,33)" x2="-5" y2="0" stroke="#888" stroke-width="1" opacity="1"/><line transform="translate(0,25)" x2="-5" y2="0" stroke="#888" stroke-width="1" opacity="1"/><line transform="translate(0,17)" x2="-5" y2="0" stroke="#888" stroke-width="1" opacity="1"/><line transform="translate(0,8)" x2="-5" y2="0" stroke="#888" stroke-width="1" opacity="1"/><line transform="translate(0,0)" x2="-5" y2="0" stroke="#888" stroke-width="1" opacity="1"/></g><g class="mark-text role-axis-label" pointer-events="none"><text text-anchor="end" transform="translate(-7,303)" font-family="sans-serif" font-size="10px" fill="#000" opacity="1">5</text><text text-anchor="end" transform="translate(-7,294.6666666666667)" font-family="sans-serif" font-size="10px" fill="#000" opacity="0">10</text><text text-anchor="end" transform="translate(-7,286.3333333333333)" font-family="sans-serif" font-size="10px" fill="#000" opacity="1">15</text><text text-anchor="end" transform="translate(-7,278)" font-family="sans-serif" font-size="10px" fill="#000" opacity="0">20</text><text text-anchor="end" transform="translate(-7,269.66666666666663)" font-family="sans-serif" font-size="10px" fill="#000" opacity="1">25</text><text text-anchor="end" transform="translate(-7,261.33333333333337)" font-family="sans-serif" font-size="10px" fill="#000" opacity="0">30</text><text text-anchor="end" transform="translate(-7,253)" font-family="sans-serif" font-size="10px" fill="#000" opacity="1">35</text><text text-anchor="end" transform="translate(-7,244.66666666666669)" font-family="sans-serif" font-size="10px" fill="#000" opacity="0">40</text><text text-anchor="end" transform="translate(-7,236.33333333333334)" font-family="sans-serif" font-size="10px" fill="#000" opacity="1">45</text><text text-anchor="end" transform="translate(-7,228)" font-family="sans-serif" font-size="10px" fill="#000" opacity="0">50</text><text text-anchor="end" transform="translate(-7,219.66666666666666)" font-family="sans-serif" font-size="10px" fill="#000" opacity="1">55</text><text text-anchor="end" transform="translate(-7,211.33333333333331)" font-family="sans-serif" font-size="10px" fill="#000" opacity="0">60</text><text text-anchor="end" transform="translate(-7,203.00000000000003)" font-family="sans-serif" font-size="10px" fill="#000" opacity="1">65</text><text text-anchor="end" transform="translate(-7,194.66666666666666)" font-family="sans-serif" font-size="10px" fill="#000" opacity="0">70</text><text text-anchor="end" transform="translate(-7,186.33333333333334)" font-family="sans-serif" font-size="10px" fill="#000" opacity="1">75</text><text text-anchor="end" transform="translate(-7,177.99999999999997)" font-family="sans-serif" font-size="10px" fill="#000" opacity="0">80</text><text text-anchor="end" transform="translate(-7,169.66666666666669)" font-family="sans-serif" font-size="10px" fill="#000" opacity="1">85</text><text text-anchor="end" transform="translate(-7,161.33333333333334)" font-family="sans-serif" font-size="10px" fill="#000" opacity="0">90</text><text text-anchor="end" transform="translate(-7,153)" font-family="sans-serif" font-size="10px" fill="#000" opacity="1">95</text><text text-anchor="end" transform="translate(-7,144.66666666666666)" font-family="sans-serif" font-size="10px" fill="#000" opacity="0">100</text><text text-anchor="end" transform="translate(-7,136.33333333333331)" font-family="sans-serif" font-size="10px" fill="#000" opacity="1">105</text><text text-anchor="end" transform="translate(-7,127.99999999999999)" font-family="sans-serif" font-size="10px" fill="#000" opacity="0">110</text><text text-anchor="end" transform="translate(-7,119.66666666666666)" font-family="sans-serif" font-size="10px" fill="#000" opacity="1">115</text><text text-anchor="end" transform="translate(-7,111.33333333333334)" font-family="sans-serif" font-size="10px" fill="#000" opacity="0">120</text><text text-anchor="end" transform="translate(-7,103.00000000000001)" font-family="sans-serif" font-size="10px" fill="#000" opacity="1">125</text><text text-anchor="end" transform="translate(-7,94.66666666666667)" font-family="sans-serif" font-size="10px" fill="#000" opacity="0">130</text><text text-anchor="end" transform="translate(-7,86.33333333333334)" font-family="sans-serif" font-size="10px" fill="#000" opacity="1">135</text><text text-anchor="end" transform="translate(-7,78)" font-family="sans-serif" font-size="10px" fill="#000" opacity="0">140</text><text text-anchor="end" transform="translate(-7,69.66666666666666)" font-family="sans-serif" font-size="10px" fill="#000" opacity="1">145</text><text text-anchor="end" transform="translate(-7,61.33333333333333)" font-family="sans-serif" font-size="10px" fill="#000" opacity="0">150</text><text text-anchor="end" transform="translate(-7,52.999999999999986)" font-family="sans-serif" font-size="10px" fill="#000" opacity="1">155</text><text text-anchor="end" transform="translate(-7,44.66666666666665)" font-family="sans-serif" font-size="10px" fill="#000" opacity="0">160</text><text text-anchor="end" transform="translate(-7,36.33333333333335)" font-family="sans-serif" font-size="10px" fill="#000" opacity="1">165</text><text text-anchor="end" transform="translate(-7,28.00000000000001)" font-family="sans-serif" font-size="10px" fill="#000" opacity="0">170</text><text text-anchor="end" transform="translate(-7,19.666666666666675)" font-family="sans-serif" font-size="10px" fill="#000" opacity="1">175</text><text text-anchor="end" transform="translate(-7,11.333333333333337)" font-family="sans-serif" font-size="10px" fill="#000" opacity="0">180</text><text text-anchor="end" transform="translate(-7,3)" font-family="sans-serif" font-size="10px" fill="#000" opacity="1">185</text></g><g class="mark-rule role-axis-domain" pointer-events="none"><line transform="translate(0,300)" x2="0" y2="-300" stroke="#888" stroke-width="1" opacity="1"/></g><g class="mark-text role-axis-title" pointer-events="none"><text text-anchor="middle" transform="translate(-35,150) rotate(-90) translate(0,-2)" font-family="sans-serif" font-size="11px" font-weight="bold" fill="#000" opacity="1">Attack
Score</text></g></g><path class="foreground" aria-hidden="true" d="" pointer-events="none" display="none"/></g></g></g><path class="foreground" aria-hidden="true" d="" display="none"/></g></g></g><defs><linearGradient id="gradient_0" x1="0" x2="0" y1="1" y2="0"><stop offset="0" stop-color="rgb(239, 249, 189)"/><stop offset="0.05555555555555555" stop-color="rgb(228, 245, 184)"/><stop offset="0.1111111111111111" stop-color="rgb(216, 240, 180)"/><stop offset="0.16666666666666666" stop-color="rgb(199, 233, 181)"/><stop offset="0.2222222222222222" stop-color="rgb(180, 225, 182)"/><stop offset="0.2777777777777778" stop-color="rgb(157, 217, 184)"/><stop offset="0.3333333333333333" stop-color="rgb(134, 208, 187)"/><stop offset="0.3888888888888889" stop-color="rgb(110, 199, 189)"/><stop offset="0.4444444444444444" stop-color="rgb(89, 189, 192)"/><stop offset="0.5" stop-color="rgb(69, 180, 194)"/><stop offset="0.5555555555555556" stop-color="rgb(55, 168, 193)"/><stop offset="0.6111111111111112" stop-color="rgb(43, 155, 191)"/><stop offset="0.6666666666666666" stop-color="rgb(37, 139, 187)"/><stop offset="0.7222222222222222" stop-color="rgb(33, 123, 181)"/><stop offset="0.7777777777777778" stop-color="rgb(33, 106, 173)"/><stop offset="0.8333333333333334" stop-color="rgb(34, 90, 165)"/><stop offset="0.8888888888888888" stop-color="rgb(35, 74, 158)"/><stop offset="0.9444444444444444" stop-color="rgb(32, 61, 146)"/><stop offset="1" stop-color="rgb(28, 49, 133)"/></linearGradient></defs></svg>

**Question 1**     

For which range of pokemon attack and defence scores do we have the most observations?

<choice id="1" >
<opt text="Pokemon with high defense and attack scores.">

This would correspond to the top right side of the plot. Is there a lot of saturation there? What colour is indicative of saturation?  

</opt>

<opt text="Pokemon with high defense and low attack scores." >

This would correspond to the bottom right side of the plot. Is there a lot of saturation there? What colour is indicative of saturation? 

</opt>

<opt text="Pokemon with low defense and high attack scores." >

This would correspond to the top left side of the plot. Is there a lot of saturation there? What colour is indicative of saturation? 

</opt>


<opt text="Pokemon with mid-low defense and  mid-low attack scores." correct="true">

You got it!

</opt>


</choice>


**Question 2**     

Which of the following marks is used to create the heatmap above?

<choice id="2" >


<opt text="<code>.mark_rect()</code>" correct="true">

Nice!

</opt>

<opt text="<code>.mark_rectangle()</code>">

Maybe consider a shortened version of `rectangle`?

</opt>


<opt text="<code>.mark_heatmap()</code>">

This mark isn't always used for heatmaps. 

</opt>


<opt text="<code>mark_hist()</code>">

I think we discovered that for histograms we use `.mark_bar()`.

</opt>



</choice>
</exercise>



<exercise id="5" title="Fire and Ice: Heatmaps with Antarctic Penguins">


**Instructions:**    
Be patient when running a coding exercise for the first time, it can take a few minutes. 

**When you see `____` in a coding exercise, replace it with what you assume to be the correct code. Run the code to see if you obtain the desired output
and submit it to validate if you were correct.**


Let's now look at our [penguins](https://www.kaggle.com/parulpandey/palmer-archipelago-antarctica-penguin-data) previous modules and see which penguins are more abundant. Are there penguins that have a greater flipper length  (`flipper_length_mm`) but with a smaller body mass (`body_mass_g`)? Does the mass of a penguin have a relationship to its flipper length?

Let's take a look!

<codeblock id="penguins">

</codeblock>


Create a heatmap between `flipper_length_mm` and `body_mass_g` and answer the questions below.


Tasks: 

Fill in the blanks in the code below so that the following gets accomplished.

- Create a heatmap and assign it to an object named `penguin_heatmap`. 
- Map `flipper_length_mm` on the x-axis and `body_mass_g` on the y-axis. Distinguish the penguin `count()` using the color channel.
- Make sure to set the `maxbins` argument to 30. 
- Set the dimensions to a width of 250 and a height of 200.
- Give it an appropriate title and axis labels. 


<codeblock id="04_05">

- Are you using `.mark_rect()`?
- Are you setting `alt.X('flipper_length_mm', bin=alt.Bin(maxbins=30)`?
- Are you setting `alt.Y('body_mass_g', bin=alt.Bin(maxbins=30)`?
- Are you using a color channel and setting it to `counts()`?
- Are you setting a title using `.properties(title= 'title')`?
- Are you setting `width=250` and `height=200` in `.properties()`?

</codeblock>


**Question 1**      

What kind of relationship is there between flipper length and penguin mass?

<choice id="1" >
<opt text="A positive linear relationship" correct="true">

There is a clear upward sloping line!

</opt>

<opt text="A negative linear relationship" >

Is there a downward slopping line formed from the data?

</opt>

<opt text="No clear relationship" >

Are there any obvious shapes being formed from the data?

</opt>

</choice>


**Question 2**      

What flipper length and mass are most common among the penguins in our data (with the given bin size)?

<choice id="2" >
<opt text="Flipper length between 185-200mm and mass between 4600-5200g" >

Are there any intervals of flipper length that contains a darker blue? The darker the colour, the more counts of penguins in the given interval range.

</opt>

<opt text="Flipper length between 185-200mm and mass between 3200-4000g" correct="true">

Nice, this is right!

</opt>

<opt text="Flipper length between 205-220mm and mass between 3200-4000g" >

This flipper length interval may be a bit high. 

</opt>

<opt text="Flipper length between 205-220mm and mass between 4600-5200" >

These intervals seem rather high? Maybe inspect flipper length and mass that are lower in value.
</opt>

</choice>

</exercise>

<exercise id="6" title="Visualizing Categorical Distributions" type="slides,video">
<slides source="module4/module4_06" shot="2" start="9:2501" end="22:1100"> </slides>
</exercise>

<exercise id="7" title="Return of the Pokemon">


**Instructions:**
Be patient when running a coding exercise for the first time, it can take a few minutes. 

**When you see `____` in a coding exercise, replace it with what you assume to be the correct code. Run the code to see if you obtain the desired output
and submit it to validate if you were correct.**

We are going to explore the different types of pokemon. You may remember this dataset from the previous Programming in Python for Data Science course. 
This time we are going to take a look at the different generations and pokemon types and see which ones are most prominent. 

For those less familiar with Pokemon, a Pokemon's generation is determined by the ara it was introduced. For example the first generation spans Pokemon characters that were released in video games from 1996-1999. The 7th generation are Pokemon introduced from games released between 2016-2019.

According to [Wikipedia](https://en.wikipedia.org/wiki/Gameplay_of_Pok%C3%A9mon#Pok%C3%A9mon_types), A Pokémon's type is *"an elemental attribute determining the strengths and weaknesses of each Pokémon and its moves. Pokémon take double damage from attacking moves of types they are weak to and half damage from moves they resist. These type matchups offset one another in rock–paper–scissors-style relationships."*


<codeblock id="pokemon">

</codeblock>


Instead of a heatmap, let's make a plot that produces circles whose colour and size change based on the count of the Pokemon for each generation and type. 

Tasks: 

- Create a heatmap and assign it to an object named `pokemon_cicleplot`. 
- Map `gen` on the x-axis and make sure to specify that it is an ordinal ('O') value.  
- Map  `type` on the y-axis.
- Assign a `Size` and `Colour` channel to the `count()` of the pokemon. 
- Give it an appropriate title and axis labels. 


<codeblock id="04_07">

- Are you using `.mark_cicle()`?
- Are you setting `alt.X('gen:O')`?
- Are you setting `alt.Y('type')`?
- Are you using a color channel and setting it to `counts()`?
- Are you setting a title using `.properties(title= 'title')`?

- Are you setting `width=250` and `height=200` in `.properties()`?


</codeblock>


**Question 1**      

Which generation and pokemon type is most occurring in the dataset?

<choice id="1" >
<opt text="Water Pokemon from Generation 1" correct="true">

You caught em all! 

</opt>

<opt text="Water Pokemon from Generation 3" >

Right type but wrong generation!

</opt>

<opt text="Normal Pokemon from Generation 1" >

Take a look at the size and colour of the circles.

</opt>


<opt text="Bug Pokemon from Generation 5" >

Take a look at the size and colour of the circles.

</opt>

</choice>


**Question 2**      

Which generation has no dragon Pokemon?

<choice id="2" >
<opt text="Generation 1" >

This generation has no steel Pokemon. 

</opt>

<opt text="Generation 2" correct="true">

You caught em all! 

</opt>

<opt text="Generation 7" >

This generation has no ice Pokemon.

</opt>


<opt text="Generation 6" >

This generation has no ground Pokemon.

</opt>

</choice>
</exercise>


<exercise id="8" title="Exploratory Data Analysis" type="slides,video">
<slides source="module4/module4_08" shot="2" start="22:2100" end="39:4924"> </slides>
</exercise>


<exercise id="9" title="True or False: Exploratory Data Analysis (EDA)">

**True or False**       
*We start EDA by displaying a few rows from the data.*


<choice id="1" >

<opt text="True" correct="true">

Perfect! Let's see what we are dealing with! 

</opt>


<opt text="False">

It's important to see what our data looks like! 

</opt>

</choice>

**True or False**       
*EDA visualizations are less concerned about plotting details such as axis labels and titles.*

<choice id="2" >

<opt text="True" correct="true">

Perfect!

</opt>

<opt text="False" >

Are you sure? *Fun Fact*: Co-creator of this course, Hayley Boyce once **lost** marks for having plots that were "too pretty"" in her EDA. 

</opt>

</choice>

</exercise>


<exercise id="10" title="Exploring EDA">

**Question 1**      
Which of the following is not a part of EDA?

<choice id="1" >
<opt text="Obtaining statistics of the data.">

Statistics can help complement and paint a supportive picture of your data.

</opt>

<opt text="Understanding the missing values from your data." >

It's important to have an idea of what values are missing from your data and ideally be able to explain why.  

</opt>

<opt text="Visualizing the data" >

Visualizing the data is a crucial part of communicating information about the data.

</opt>

<opt text="Creating a predictive model from the data" correct="true">

This is not a formal part of exploratory data analysis.

</opt>

</choice>


**Question 2**      
Which code will help us create multiple plots, that maps every numeric column to a specified axis?


<choice id="2" >

<opt text="<code>.repeat()</code>">
You've half right, we specifically said every *numeric* column though.

</opt>

<opt text="<code>.repeated()</code> and the argument <code>type='numeric'</code>">

I think your argument should be called something else.

</opt>

<opt text="<code>.repeat()</code> and the argument <code>type='quantitative'</code>" correct="true">

Nice!

</opt>

<opt text="The argument <code>map='numeric'</code>">

You are extremely close, but no past tense is needed.

</opt>

</choice>


</exercise>

<exercise id="11" title="Plotting Numeric Columns with Penguins">


**Instructions:**    
Be patient when running a coding exercise for the first time, it can take a few minutes. 

**When you see `____` in a coding exercise, replace it with what you assume to be the correct code. Run the code to see if you obtain the desired output
and submit it to validate if you were correct.**


It's been a hot second since we used the [penguins](https://www.kaggle.com/parulpandey/palmer-archipelago-antarctica-penguin-data) data and seen it's one second too long and we missed it, we are welcoming it back. 

<codeblock id="penguins">

</codeblock>


Let's plot all the distributions of the numeric columns from the dataset.

Tasks: 

Fill in the blanks in the code below so that the following gets accomplished.

- Use the data source `penguins_df` to make a histogram for each of the numeric columns.
- Assign the plot to an object named `numeric_histograms`. 
- Plot the counts of each column on the y-axis and the values of each numeric column of the x-axis.
- Make sure to set the `maxbins` argument to something appropriate (30 or 40). 
- Set width to 150 and height to 150 and display the plots in 2 columns and 2 rows.


<codeblock id="04_11">

- Are you setting `alt.X(alt.repeat(), type='quantitative', bin=alt.Bin(maxbins=30)`?
- Are you setting `alt.Y('count()')`?
- Are you setting the height and width in `properties()`?
- Are you using `.repeat()` and setting `numeric_cols` as the first argument and `columns=2` or `rows=2`?

</codeblock>


**Question**      

Do any of the distributions look bimodal (2 bell shapes)?

<choice id="1" >
<opt text="Yes" correct='true'>

The 2 bumps suggest bimodality. The `culmen_length_mm` and `flipper_length_mm` distributions both appear to be bimodal. 

</opt>

<opt text="No">

Do you see 2 "bumps" in any of the plots? Maybe look at the `culmen_length_mm` and `flipper_length_mm` distributions. 

</opt>


</choice>
</exercise>


<exercise id="12" title="Exploratory Data Analysis on Categorial Data" type="slides,video">
<slides source="module4/module4_12" shot="2" start="39:5810" end="44:3200"> </slides>
</exercise>


<exercise id="13" title="Repeating Categorical Columns Quick Questions!">

**Question 1: True or False**       
*Repeating charts is the same as facetting them.*

<choice id="2" >

<opt text="True">

Killed it!

</opt>

<opt text="False"  correct="true">

Not quite. We can facet on a categorical dataframe column and repeat a plot mapping many categorical columns making them 2 distinct actions.

</opt>

</choice>

**Question 2**      
When we want to repeat categorical column values, what value *can* we use in the `type` argument?


<choice id="2" >

<opt text="<code>'qualitative'</code>">
I can understand the confusion since quantitative was used for numeric columns but that's because Altair recognizes them with a tag of Q for quantitative.

</opt>

<opt text="<code>'object'</code>">

This is a pandas dtype and not a reconizable Altair type.

</opt>

<opt text="<code>'nominal'</code>" correct="true">

Nice!

</opt>

<opt text="<code>'categorical'</code>">

Altair doesn't recognize this as a type. 

</opt>

</choice>


</exercise>

<exercise id="14" title="Plotting Repeated Categorical Columns with Penguins">


**Instructions:**    
Be patient when running a coding exercise for the first time, it can take a few minutes. 

**When you see `____` in a coding exercise, replace it with what you assume to be the correct code. Run the code to see if you obtain the desired output
and submit it to validate if you were correct.**


Are you getting bored of this [penguins](https://www.kaggle.com/parulpandey/palmer-archipelago-antarctica-penguin-data) data yet? Don't worry, we will spice it up soon, but let finish off this module with it. 

<codeblock id="penguins">

</codeblock>


Let's count combinations of the different categoricals, so we can get a bit of a better idea about where our data lies. 

Tasks: 

Fill in the blanks in the code below so that the following gets accomplished.

- Use the data source `penguins_df` to make a circle plots for each pair of categorical columns.
- Assign the plot to an object named `categorical_plots`. 
- Map and repeat every categorical column on both the x and y axis.
- Map the counts to both a `Color` and `Size` channel and indicate that no title should be assigned.
- Make sure to give the size and colour channels independent scales. 


<codeblock id="04_14">

- Are you using `.mark_circle()`?
- Are you setting `alt.X(alt.repeat('column'), type='nominal')`?
- Are you setting `alt.Y('count()')`?
- Are you chaining `repeat(row=cat_cols, column=cat_cols)` after `.encode()`?
- Are you setting `color='independent'` and `size='independent'` in `.resolve_scale()`?

</codeblock>


**Question 1**      

Are their approximately the same number of female and male penguins for each penguin species?

<choice id="1" >
<opt text="Yes" correct='true'>

If you look at the circle size and colours of each species in the `sex` vs `species` plot (top right), they are approximately equal. 

</opt>

<opt text="No">

Are you comparing the circle size and colours of each species in the `sex` vs `species` plot (top right)?

</opt>

</choice>


**Question 2**      

What species of penguins and from what island are most prominent in our data?

<choice id="2" >
<opt text="The Adelie species on Biscoe island are most prominent penguin in the data.">

Although the Adelie species are present on Biscoe island, they are not the most occuring in our data.

</opt>


<opt text="The Gentoo species on Biscoe island are most prominent penguin in the data." correct='true'>

Nice work!

</opt>

<opt text="The Chinstrap species on Dream island are most prominent penguin in the data.">

This is the second most occuring penguin in the data but not the first.

</opt>

<opt text="The Gentoo species on Dream island are most prominent penguin in the data.">

There are no records of Gentoo penguins on Dream island in the data.

</opt>

</choice>

</exercise>


<exercise id="15" title="What Did We Just Learn?" type="slides, video">
<slides source="module4/module4_end" shot="0" start="04:5307" end="05:5911">
</slides>
</exercise>
