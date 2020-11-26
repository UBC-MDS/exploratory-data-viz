---
title: 'Module 1: Machine Learning Terminology'
description:
  'In this module, we will explain the different branches of machine learning and introduce the steps needed to build a model by constructing baseline models.'
prev: module0
next: /module2
type: chapter
id: 1
---

<exercise id="0" title="Module Learning Outcomes"  type="slides, video">

<slides source="module1/module1_00" shot="0" start="3:5707" end="4:5306">
</slides>

</exercise>


<exercise id="1" title="What is Supervised Machine Learning?" type="slides,video">

<slides source="module1/module1_01" shot="1" start="0:003" end="07:12">
</slides>

</exercise>


<exercise id="2" title="Is it Machine Learning?">

**True or False: The following is an example of machine learning?**      
_Diagnosing cancer from magnetic resonance imaging_

<choice id="1" >
<opt text="True"  correct="true">

Great!

</opt>

<opt text="False">

Machine Learning can be use to attempt to diagnose cancer.

</opt>

</choice>

**True or False: The following is an example of machine learning?**       
_Classifying images containing animals_

<choice id="2">
<opt text="True" correct="true">

Nice work! 

</opt>

<opt text="False">

If you look at example 2, in the slides you'll see the code we used to do this. 

</opt>

</choice >

**True or False: The following is an example of machine learning?**       
_Blowing out a candle_

<choice  id="3">
<opt text="True" >

No quite sure how this would work, but never say never! Technology is progressing everyday. 

</opt>

<opt text="False" correct= "true">

I don't think we can use machine learning quite yet to do this. Maybe one day we will be able to! Who knows. 

</opt>

</choice>

</exercise>


<exercise id="3" title="Describing a Dataset">


**Instructions:**    
Running a coding exercise for the first time could take a bit of time for everything to load.  Be patient, it could take a few minutes. 

**When you see `____` in a coding exercise, replace it with what you assume to be the correct code.  Run it and see if you obtain the desired output.  Submit your code to validate if you were correct.**


_**Make sure you remove the hash (`#`) symbol in the coding portions of this question.  We have commented them so that the line won't execute and you can test your code after each step.**_


Let's make sure we understand all the components we use in a dataset for machine learning. The packages you need will be loaded for you. In this example we would be attempting to predict the country availability of candy bars, which makes the column `availability` the target.

- Print the `canbybar_df` object. 
- Save the dimensions of the dataframe in an object named `candybar_dim`.

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

**Question 3**     
Would this be considered classification or regression?

<choice  id="3">
<opt text="Classification" correct="true">

Great job!

</opt>

<opt text="Regression" >

What would we be predicting, a numerical value or categorical?

</opt>
</choice>
</exercise>


<exercise id="21" title="What Did We Just Learn?" type="slides, video">
<slides source="module1/module1_end" shot="0" start="04:5307" end="05:5911">
</slides>
</exercise>