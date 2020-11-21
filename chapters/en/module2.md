---
title: 'Module 2: Decision Trees'
description:
  'In this module, we will introduce the decision tree model. We will explain the structure of decision trees and the process it take to make predictions.'
prev: /module1
next: /module3
type: chapter
id: 2
---


<exercise id="0" title="Module Learning Outcomes"  type="slides, video">

<slides source="module2/module2_00" shot="0" start="05:5912" end="06:51">
</slides>

</exercise>


<exercise id="1" title=" Introducing Decision Trees" type="slides,video">

<slides source="module2/module2_01" shot="1" start="28:541" end="38:33">
</slides>

</exercise>


<exercise id="2" title= "Decision Tree - Trees">

**Question 1**      
What is the top node in a decision tree called? 

<choice id="1">

<opt text="truck">

Not quite. 

</opt>


<opt text= "branch" >
 
This appears further down the tree.

</opt>

<opt text="root" correct="true">

Nice work!

</opt>

<opt text="blossom">

That's a pretty name, but that's not what the top of the tree is called.

</opt>

</choice>



**Question 2**      
What are the nodes in a decision tree?

<choice id="2" >

<opt text="An <code>if</code>/<code>else</code> statement" correct="true">

Great!

</opt>

<opt text="An <code>if</code>/<code>elif</code>/<code>else</code> statement">

It is a Boolean decision, so only 2 outcomes are possible.

</opt>


<opt text="A <code>for</code> loop">

There is no loop involved here.

</opt>

<opt text="A function">

Not in this context. 

</opt>



</exercise>


<exercise id="3" title="Decision Tree Outcome">

What is the depth of this decision tree? 

<center>
<img src="/module2/Q3.png"  width = "100%" alt="404 image">
</center>
<br>
<br>

<choice id="1" >
<opt text="1" >

A depth of 1 would simply be the stump. 

</opt>

<opt text="2">

Perhaps think a bit *deeper* (hint hint). 

</opt>


<opt text="3" correct="true">

Nice work! 

</opt>

<opt text="4">

Not quite so deep. 

</opt>

</choice>

</exercise>



<exercise id="4" title="Building a Decision Tree Classifier" type="slides,video">

<slides source="module2/module2_04" shot="1" start="38:37" end="45:091">
</slides>

</exercise>


<exercise id="5" title="Predicting with a Decision Tree">

Using the following Decision tree for the next 2 questions:  


 <center>
<img src="/module2/Q3.png"  width = "100%" alt="404 image">
</center>


**Question 1**      
 Given the features:
 
 ```out
     yellow  sweet  berry  long  green  Mexico  seeds
0       0      1      0     0      1       0      1
 ```
 
What would the model predict? 
<br>

<choice  id="1">
<opt text="Banana" >

Is the fruit yellow? 

</opt>

<opt text="Orange" >

Isn't the fruit green?

</opt>

<opt text="Strawberry">

The fruit is not a berry. 

</opt>

<opt text="Kiwi" correct="true">

Great!

</opt>

</choice>


**Question 2**      
 Given the features:
 
 ```out
     yellow  sweet  berry  long  green  Mexico  seeds
0       1      0      0     0      0       0      1
 ```
 
What would the model predict?

<choice  id="2">
<opt text="Banana" >

Is the fruit long? 

</opt>

<opt text="Lemon"  correct="true">

Great!

</opt>

<opt text="Starfruit">

Is the fruit sweet? 

</opt>

<opt text="Kiwi">

Is the fruit yellow?

</opt>

</choice>

</exercise>

<exercise id="6" title="Decision Trees True/False">

**True or False**     
*`DecisionTreeClassifier` does not consider features in it's prediction just like `DummyClassifier`*


<choice id="1" >
<opt text="True"  >

What about how the predictions are made?

</opt>

<opt text="False" correct="true">

Decision trees make predictions based on the outcome from conditions determined by the features.

</opt>

</choice>

**True or False**     
*We need to `.fit` our decision tree model before we call `.predict`.*

<choice id="2">
<opt text="True" correct="true">

Nice work! 

</opt>

<opt text="False">

We must always train our model on the data before prediction.

</opt>

</choice >

**True or False**       
*Decision trees always give the correct answer for a single prediction..*

<choice id="3">
<opt text="True" >

Decision trees are not always 100% right.

</opt>

<opt text="False" correct="true">

Great!

</opt>

</choice>


</exercise>



<exercise id="7" title="Building a Decision Tree Classifier">

**Instructions:**    
Running a coding exercise for the first time could take a bit of time for everything to load.  Be patient, it could take a few minutes. 

**When you see `____` in a coding exercise, replace it with what you assume to be the correct code.  Run it and see if you obtain the desired output.  Submit your code to validate if you were correct.**

_**Make sure you remove the hash (`#`) symbol in the coding portions of this question.  We have commented them so that the line won't execute and you can test your code after each step.**_

Let's build a decision tree classifier using `DecisionTreeClassifier()`. 

Tasks:     

- Build a model using `DecisionTreeClassifier()` and make sure to set the `random_state` argument to 1. 
- Save this in an object named `model`. 
- Fit your model on the objects `X` and `y`.
- Predict on `X` and save the values in an object named `predicted`.
- Compare the `availability` column to the `predicted` column and answer the multiple-choice questions below. 

<codeblock id="02_07">

- Are using `DecisionTreeClassifier(random_state=1)`?
- Are you using the model named `model`?
- Are you calling `.fit(X,y)` on your model?

</codeblock>



**Question 1**     
Which of the following candy bars did the model incorrectly predict?

<choice id="1" >
<opt text="Twix"  >

Not this one!

</opt>

<opt text="Oh Henry" correct="true">

Great! The model predicted this one incorrectly.

</opt>

<opt text="Skor"  >

The model predicted `both` for this example which is the correct answer. 

</opt>


<opt text="Almond Joy"  >

This candy bar was correctly predicted by the model.

</opt>

</choice>

**Question 2**      
What should have been the correct prediction for the candy bar above?

<choice id="2">
<opt text="America" correct="true">

This is what the model predicted, not the true value. 

</opt>

<opt text="Canada">

Not quite, maybe take a closer look.

</opt>


<opt text="both" correct="true">

You got it!

</opt>

</choice >

**Question 3**      
How many in total did the model incorrectly predict? 

<choice id="3">
<opt text="1" >

There is more, take a closer look. 

</opt>

<opt text="2">

Maybe take a closer look, you may be missing one/some. 

</opt>

<opt text="3"  correct="true" >

Nice!

</opt>

<opt text="4" >

Did you find one that we didn't?

</opt>


</choice>

</exercise>


<exercise id="8" title="Decision Trees with Continuous Features" type="slides,video">

<slides source="module2/module2_08" shot="1" start="45:131" end="52:38">
</slides>

</exercise>

<exercise id="9" title="Decision Boundaries">

For the following questions, refer to this diagram:

 <center>
<img src="/module2/Q9.png"  width = "100%" alt="404 image">
</center>


**Question 1**      
What is the diagram displaying?

<choice  id="1">
<opt text="A decision branch" >

The branches are the connections between nodes.

</opt>

<opt text="A decision stump" correct="true">

Great!

</opt>

<opt text="A decision leaf">

Leaves are the outcomes of the decisions. 

</opt>

<opt text="A decision trunk" >

Not quite the right word. 

</opt>

</choice>


**Question 2**        
On which feature is the decision boundary splitting?
 
 <choice  id="2">
<opt text="<code>seeds</code>" >

Not this time!

</opt>

<opt text="<code>location</code>"  >

Location was not the splitting feature here!

</opt>

<opt text="<code>water Content</code>" correct="true">

You got it!

</opt>

<opt text="<code>sweetness</code>">

Maybe take a look at the diagram a bit closer. 

</opt>

</choice>


**Question 3**        
On what value of the above feature is the decision boundary splitting?
 
 <choice  id="3">
<opt text="<code>90</code>" >

Not quite. 

</opt>

<opt text="<code>water content</code>"  >

This is the feature it's splitting on, not the value. 

</opt>

<opt text="<code>92</code>">

Not this time. 

</opt>

<opt text="<code>96</code>"  correct="true">

Cool!

</opt>

</choice>

</exercise>


<exercise id="10" title="Decision Boundaries">

For the following questions, refer to this diagram below.

We are trying to predict a player’s position in this problem:

- Blue circles represent defense players
- Red triangles represent forward players

 <center>
<img src="/module2/hockey_q.png"  width = "60%" alt="404 image">
</center>



**Question 1**      
What are the two features used in this decision tree classifier? 

<choice  id="1">
<opt text="Height and Weight" >

One of these is correct. Take a look at the x-axis. 

</opt>

<opt text="Height and Experience">

One of these is correct. Take a look at the y-axis. 

</opt>

<opt text="Experience and Weight"  correct="true">

Great!

</opt>

<opt text="Age and Weight" >

One of these is correct. Take a look at the x-axis. 

</opt>

</choice>


**Question 2**       
What is the splitting value for the feature on the x-axis?
 
 <choice  id="2">
<opt text="9" >

This answer seems a little high.

</opt>

<opt text="6"  >

Not quite.

</opt>

<opt text="7.5" correct="true">

You got it!

</opt>

<opt text="4.5">

This answer seems a little low. 

</opt>

</choice>


**Question 3**      
What is the splitting value for the feature on the y-axis?
 
 <choice  id="3">
<opt text="175.5" correct="true">

Nice.

</opt>

<opt text="120.5"  >

This answer is a bit low.

</opt>

<opt text="210">

This answer is a little high.

</opt>

<opt text="200.5"  >

This answer is a little high.

</opt>

</choice>

</exercise>

<exercise id="11" title="Decision Boundaries">

Use the plot below to answer the following questions.

 <center>
<img src="/module2/hockey_q.png"  width = "60%" alt="404 image">
</center>

We are trying to predict a player's position in this problem:

- Blue circles represent defense players
- Red triangles represent forward players


**Question**       
Given this plot, which tree diagram is best represented by the decision boundaries? 

A)  <center>
<img src="/module2/module_hockey2.png"  width = "50%" alt="404 image">
</center>


B)  <center>
<img src="/module2/module_hockey.png"  width = "40%" alt="404 image">
</center>



<choice  id="3">
<opt text="A" >

What is the depth of the tree in the diagram and how many boundaries (lines) can you count in the plot?

</opt>

<opt text="B" correct="true" >

Nice work!

</opt>

</choice>

</exercise>



<exercise id="12" title="Parameters and Hyperparameters" type="slides,video">

<slides source="module2/module2_12" shot="1" start="52:431" end="64:08">
</slides>

</exercise>

<exercise id="13" title= "Feature Splitting">

**Question 1**   
Who chooses the features that are split on at each node?

<choice id="1">
<opt text= "Data scientists/model builders" >
 
Where would we input this information?  

</opt>

<opt text="The model" correct="true">

Great!

</opt>

</choice>

**Question 2**    
What is the depth of a decision stump? 

<choice id="2">
<opt text= "1" correct="true">
 
You have been paying attention! Nice work! 

</opt>

<opt text="5" >

This depth would not be considered a stump. 

</opt>

<opt text="Whatever you set it as" >

Decision stumps are what make up a decision tree, stumps are not a hyperparameter.

</opt>
</choice>

</exercise>

<exercise id="14" title= "Parameter or Hyperparameter">

For the following statements, state if it corresponds to a Parameter or Hyperparameter.


**Question 1**     
*The builder of the model can set them.*

<choice id="1">
<opt text= "Parameters" >
 
Maybe review the notes a bit.

</opt>

<opt text="Hyperparameters" correct="true">

Great.

</opt>

</choice>


**Question 2**     
*They get set during the training phase.*

<choice id="2">
<opt text= "Parameters" correct="true">
 
Nice.

</opt>

<opt text="Hyperparameters" >

We set hyperparameters before training but not parameters.

</opt>

</choice>


</exercise>


<exercise id="15" title="Playing with Hyperparameters">

**Instructions:**    
Running a coding exercise for the first time could take a bit of time for everything to load.  Be patient, it could take a few minutes. 

**When you see `____` in a coding exercise, replace it with what you assume to be the correct code.  Run it and see if you obtain the desired output.  Submit your code to validate if you were correct.**

_**Make sure you remove the hash (`#`) symbol in the coding portions of this question.  We have commented them so that the line won't execute and you can test your code after each step.**_

Let's build a decision tree classifier using `DecisionTreeClassifier()` but this time, let's set some different hyperparameters.

Tasks:     

- Build a decision tree classifier and make sure to set the argument `random_state` to 1. 
- Set the `max_depth` of the tree to 8 and the `min_samples_split` to 4. 
- Save the model in an object named `hyper_tree`. 
- Fit your model on the objects `X` and `y`.
- Save the accuracy of the model rounded to 2 decimal places in a variable named `tree_score` and display it.

<codeblock id="02_15">

- Are using `DecisionTreeClassifier(max_depth=8, min_samples_split=4, random_state=1)`?
- Are you using the model named `hyper_tree`?
- Are you calling `.fit(X,y)` on your model?
- Are you using `.score(X,y)` and rounding to 2 decimal places by using `round()`?

</codeblock>



**Question 1**      
Will increasing the value of `max_depth` increase or decrease the accuracy of the model?

<choice id="1" >
<opt text="Increase"  correct="true">

Increasing the depth of the tree will increase the accuracy of the model.

</opt>

<opt text="Decrease" >

Maybe test it out above and see what happens?

</opt>

<opt text="Either increase or decrease"  >

Maybe test it out above and see what happens?

</opt>


</choice>

**Question 2**      
Will increasing the value of `min_samples_split` increase or decrease the accuracy of the model?

<choice id="2" >
<opt text="Increase" >

Maybe test it out above and see what happens?

</opt>

<opt text="Decrease"  correct="true">

Increasing the minimum number of samples needed to split on a feature will decrease the accuracy.

</opt>

<opt text="Either increase or decrease"  >

Maybe test it out above and see what happens?

</opt>


</choice>

**Question 3**       
Will increasing the value of `max_depth` and `min_samples_split` increase or decrease the accuracy of the model?

<choice id="3" >
<opt text="Increase" >

Are we 100% sure? Increasing `max_depth` will increase the accuracy but increasing `min_samples_split` will decrease it. 

</opt>

<opt text="Decrease" >

Are we 100% sure? Increasing `max_depth` will increase the accuracy but increasing `min_samples_split` will decrease it. 

</opt>

<opt text="Either increase or decrease"   correct="true">

Right! It's hard to say since increasing `max_depth` will increase the accuracy but increasing `min_samples_split` will decrease it.

</opt>

</choice>

</exercise>


<exercise id="16" title="Decision Tree Regressor" type="slides,video">

<slides source="module2/module2_16" shot="1" start="64:10" end="69:37">
</slides>

</exercise>

<exercise id="17" title= "Regression with Decision Tree True or False">

**True or False**       
*`.score()` is calculated in the same way for regressions problems as for classification problems.*
  

<choice id="1">
<opt text= "True" >
 
`.score()` for regression problems returns something called an $R^2$ score.

</opt>

<opt text="False" correct="true">

Great!

</opt>

</choice>

**True or False**     
*The same hyperparameters can be used for `DecisionTreeRegressor()`.*

<choice id="2">
<opt text= "True" correct="true">
 
You have been paying attention! Nice work! 

</opt>

<opt text="False" >

If you look at the documentation, you'll be able to see that they do have the same hyperparameters. 

</opt>

</choice>

</exercise>


<exercise id="18" title="Building a Decision Tree Regressor">

**Instructions:**    
Running a coding exercise for the first time could take a bit of time for everything to load.  Be patient, it could take a few minutes. 

**When you see `____` in a coding exercise, replace it with what you assume to be the correct code.  Run it and see if you obtain the desired output.  Submit your code to validate if you were correct.**

_**Make sure you remove the hash (`#`) symbol in the coding portions of this question.  We have commented them so that the line won't execute and you can test your code after each step.**_

Let's build a decision tree regressor using `DecisionTreeRegressor()` and let's set some different hyperparameters.

Tasks:     

- Build a model using `DecisionTreeRegressor()` and make sure to set the argument `random_state` to 1. 
- Set the `max_depth` of the tree to 5.  
- Save your model in an object named `reg_tree`.
- Fit your model on the objects `X` and `y` and then predict on `X`. 
- Save the R^2 score of the model rounded to 2 decimal places in a variable named `tree_score`.

<codeblock id="02_18">

- Are using `DecisionTreeRegressor(random_state=1, max_depth=5)`?
- Are you using the model named `reg_tree`?
- Are you calling `.fit(X,y)` on your model?
- Are you using `.score(X,y)` and rounding to 2 decimal places by using `round()`?

</codeblock>

**Question**     
Given the value of the regression model's score, which model does better?

<choice id="1" >
<opt text="Dummy Regressor"  >

The Dummy Regressor gave a $R^2$ value of 0.0. 

</opt>

<opt text="Decision Tree" correct="true">

You got it!

</opt>

</choice>

</exercise>

<exercise id="19" title="Generalization" type="slides,video">

<slides source="module2/module2_19" shot="1" start="69:441" end="80:50">
</slides>

</exercise>

<exercise id="20" title= "Generalization Practice Questions">


**Question 1**   
Is it always a good idea to have the most precise/complex model?

<choice id="1">
<opt text= "Yes, it will predict the best in all cases." >
 
Complex models have the best scores for the data that it has seen but what about unseen data?

</opt>

<opt text="Yes, precise models result in the highest accuracy">

Precise models have the highest accuracy for the data that it has seen but what about unseen data?

</opt>

<opt text="No, it may not generalize well to other unseen data." correct="true">

Great!

</opt>

<opt text="No, you want a model with low accuracy">

You are on the right track but you still want a model that does its job well. 

</opt>

</choice>

**Question 2**   
Does increasing the depth of a tree make the tree more or less generalized?

<choice id="2">
<opt text= "More generalized" >
 
Increasing the depth increases the number of decision boundaries. Does this make the model more generalized then?

</opt>

<opt text="Less generalized" correct="true">

Nice!

</choice>

</exercise>


<exercise id="21" title="What Did We Just Learn?" type="slides, video">
<slides source="module2/module2_end" shot="0" start="06:5223" end="07:2827">
</slides>
</exercise>

