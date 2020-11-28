---
title: 'Module 1: Why Visualize Data?'
description:
  'In this module we will be learning about the importance of data visualization and how a grammar of graphics can help us effectively visualize data.'
prev: ../../module0
next: ../../module2
type: chapter
id: 1
---

<exercise id="0" title="Module Learning Outcomes"  type="slides, video">

<slides source="module1/module1_00" shot="0" start="3:5707" end="4:5306">
</slides>

</exercise>


<exercise id="1" title="What is Data Visualization?" type="slides,video">

<slides source="module1/module1_01" shot="1" start="0:003" end="07:12">
</slides>

</exercise>

<exercise id="2" title="Why Visualize Data?">

**True or False: It is easier for humans to interpret plots than raw numbers.**

<choice id="1" >
<opt text="True"  correct="true"></opt>
<opt text="False"></opt>
</choice>

**True or False: Statistical summaries can be misleading.**

<choice id="2" >
<opt text="True"  correct="true"></opt>
<opt text="False"></opt>
</choice>

</exercise>

<!--
**Question 1**

How many example did the model of this matrix correctly label as "Guard"?

<choice id="1">

<opt text="19">

This is the number of example the model correctly predicted as **Forward**.

</opt>

<opt text= "3">
 
This is the number of examples the model predicted **Guard** when the true label was **Forward**.

</opt>

<opt text="4">

This is the number of examples the model predicted **Forward** when the true label was **Guard**.

</opt>

<opt text="26"  correct="true">

Nice!

</opt>

</choice>


**Question 2**

If **Forward** is the positve label, how many ***false positive*** values?

<choice id="2" >

<opt text="19">

This is the number of example true positives. 

</opt>

<opt text= "3">
 
This is the number of false negatives! 

</opt>

<opt text="4"  correct="true">

Great! This is the number of examples the model predicted **Forward** (positive) when the true label was **Guard** (negative) .

</opt>

<opt text="26" >

This the the number of true negatives. 

</opt>

</choice>


</exercise>


<exercise id="3" title="Question Title Here">

Running a coding exercise for the first time could take a bit of time for everything to load.  Be patient, it could take a few minutes. 

**When you see `____` in a coding exercise, replace it with what you assume to be the correct code.  Run it and see if you obtain the desired output.  Submit your code to validate if you were correct.**

_**Make sure you remove the hash (`#`) symbol in the coding portions of this question.  We have commented them so that the line won't execute and you can test your code after each step.**_

We've seen our basketball dataset before and predicted using `SVC` with it before but this time we are going to have a look at how well our model does by building a confusion matrix. 

Tasks:   
- Import the plotting confusion matrix library. 
- Build a pipeline naed `pipe_bb` that preprocesses with `preprocessor` and builds an `SVC()` model with default hyperparameters. 
- Fit the pipeline on `X_train` and `y_train`. 
- Next, build a confusion matrix using `plot_confusion_matrix` and calling `pipe_bb` and the **test** set. Pick any colour you like with `cmap`. You can find the colour options <a href=" https://matplotlib.org/3.1.0/tutorials/colors/colormaps.html" target="_blank">here</a>.

<codeblock id="01_03">

- Are you using `.shape` to find the dimensions? 

</codeblock>



**Question 1**       
How many features does the data have?

<choice  id="1">
<opt text="8">

This is not the number of features.

</opt>

<opt text="9" correct="true">

Yes! Good job!

</opt>

<opt text="25">

This is not the number of features.

</opt>

<opt text="10">

We don't include the index or the target as a feature.

</opt>
</choice>



**Question 2**      
 How many examples does the data have?

<choice  id="2">

<opt text="9">

This is the total number of columns, not the number of examples.

</opt>

<opt text="8" >

This is the not the number of examples.

</opt>

<opt text="25" correct="true">

Well done!

</opt>

<opt text="26">
This is not the number of examples.

</opt>
</choice>
</exercise>

-->


<exercise id="3" title="What Did We Just Learn?" type="slides, video">
<slides source="module1/module1_end" shot="0" start="04:5307" end="05:5911">
</slides>
</exercise>
