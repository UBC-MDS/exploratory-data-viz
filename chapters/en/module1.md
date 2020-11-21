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


<exercise id="3" title="Types of Machine Learning" type="slides,video">

<slides source="module1/module1_03" shot="1" start="07:171" end="12:371">
</slides>

</exercise>



<exercise id="4" title=" Supervised vs. Unsupervised Learning">

**Given the following scenarios, would each example be considered supervised learning or unsupervised learning?**

**Example:**   
_Finding groups of similar properties in a real estate data set._

<choice id="1" >
<opt text="Supervised Learning">

Is there a "true number" of groups of similar properties? Are the groups known and defined?

</opt>

<opt text="Unsupervised Learning" correct="true">

Good job! This is an unsupervised learning example.

</opt>

</choice>

**Example:**    
_Predicting real estate prices based on house features (number of rooms,past sales, etc.)._

<choice id="2">
<opt text="Supervised Learning" correct="true">

Nice work! Since we have examples with known value of real estate prices, we can use this predict real estate prices for homes we don't know the price on. 

</opt>

<opt text="Unsupervised Learning">

Do we have true corresponding values of what we are predicting with?

</opt>

</choice >

**Example:**   
_Detecting credit card fraud based on examples of fraudulent transactions._

<choice  id="3">
<opt text="Supervised Learning" correct= "true">

Great! Since we have examples with labels of "fraudulent" or "not fraudulent", we can detect if transactions with similar features to our examples are of the same nature. 

</opt>

<opt text="Unsupervised Learning" >

Do we have examples of the true corresponding value of what we are predicting?

</opt>

</choice>

**Example:**   
_Identifying groups of animals given features such as "number of legs", "wings/no wings", "fur/no fur", etc._

<choice  id="4">
<opt text="Supervised Learning">

We are grouping animals together based on similarity. 

</opt>

<opt text="Unsupervised Learning"  correct="true">

Nice work.


</opt>
</choice>

**Example:**   
_Grouping articles on different topics from different news sources (something like Google News app)._


<choice  id="5">
<opt text="Supervised Learning">

Here we do not have a clear "correct" answer and therefor this is an example of unsupervised learning. 

</opt>

<opt text="Unsupervised Learning"  correct= "true">

Grouping is also called *clustering* which is an example of unsupervised learning. 

</opt>

</choice>

</exercise>



<exercise id="5" title="Classification vs. Regression" type="slides,video">

<slides source="module1/module1_05" shot="1" start="12:443" end="15:062">
</slides>

</exercise>

<exercise id="6" title="Classification vs. Regression">


**Example:**       
_Predicting the price of a house based on features  such as  number of rooms and the year built._

<choice id="1">
<opt text="Classification">

Is the prediction a categorical or a numerical value?

</opt>

<opt text="Regression" correct="true">

Good job! We are predicting a numerical value and therefore this is an example of regression.

</opt>

</choice>

**Example:**     
_Predicting if a house will sell or not based on features like the price of the house, number of rooms, etc._

<choice  id="2">
<opt text="Classification" correct="true">

Good job! We are predicting a categorical value (Sell/Not Sell) and therefore this is an example of classification.

</opt>

<opt text="Regression" >

Is the prediction a categorical or a numerical value?

</opt>

</choice>

**Example:**       
_Predicting your grade in this course based on your grade in Programming in Python for Data Science._

<choice  id="3">
<opt text="Classification">

Is the prediction a categorical or a numerical value?

</opt>

<opt text="Regression" correct="true">

Good job! We are predicting a numerical value (percent grade) and therefore this is an example of regression.

</opt>
</choice>

**Example:**       
_Predicting a cereal's manufacturer given the nutritional information._

<choice  id="4">
<opt text="Classification" correct="true">

Good job! We are predicting a categorical value and therefore this is an example of classification.

</opt>

<opt text="Regression">

Is the prediction a categorical or a numerical value?

</opt>
</choice>
</exercise>


<exercise id="7" title=" Classification vs. Regression Target">

```out
           name     calories     sugar   water-content  weight  shape
0         apple       100         3.0          84         100   round
1        banana       120         4.0          75         120   long
2    cantaloupe       130         5.0          90        1360   round
3  dragon-fruit        70         1.5          96         600   round
4    elderberry       110         2.5          80           5   round 
5           fig        40         2.0          78          40   oval  
6         guava        90         3.0          83         450   oval
7   huckleberry        85         4.0          73           5   round
8          kiwi        60         4.5          80          76   round
9         lemon        50         1.0          83          65   oval
```

Given the target column `shape`, does this represent a **Classification** or a **Regression** problem? 

<choice id="1">
<opt text="Classification" correct="true">

Nice job! 

</opt>

<opt text="Regression" >

Is the prediction a categorical or a numerical value?

</opt>

</choice>
</exercise>


<exercise id="8" title="Tabular Data and Terminology" type="slides, video">

<slides source="module1/module1_08" shot="1" start="15:13" end="18:2115">
</slides>

</exercise>



<exercise id="9" title="Terminology: Target">

Which is a synonym for ***targets***? 

<choice  id="1">

<opt text="Predictors" >

Not quite. You may want to have a read through of the definitions in this section. 

</opt>

<opt text="Records">

Not quite. You may want to have a read through of the definitions in this section. 

</opt>

<opt text="Outputs" correct="true">

Good job!

</opt>

<opt text="Independent variables">

Not quite. You may want to have a read through of the definitions in this section.

</opt>

</choice>
</exercise>

<exercise id="10" title="Terminology: Features">

Which is a synonym for ***feature***? 

<choice  id="1">
<opt text="testers" >

This, unfortunately, is not in the Machine learning vocabulary. 

</opt>

<opt text="Input" correct="true">

Input is a synonym for features! Well done. 

</opt>

<opt text="examples">

Example is not synonym for features. You may want to have a read through of the definitions in this section. 

</opt>

<opt text="row">

Row is not synonym for features. You may want to have a read through of the definitions in this section. 

</opt>

</choice>

</exercise>


<exercise id="11" title="Describing a Dataset">



**Instructions:**    
Running a coding exercise for the first time could take a bit of time for everything to load.  Be patient, it could take a few minutes. 

**When you see `____` in a coding exercise, replace it with what you assume to be the correct code.  Run it and see if you obtain the desired output.  Submit your code to validate if you were correct.**


_**Make sure you remove the hash (`#`) symbol in the coding portions of this question.  We have commented them so that the line won't execute and you can test your code after each step.**_


Let's make sure we understand all the components we use in a dataset for machine learning. The packages you need will be loaded for you. In this example we would be attempting to predict the country availability of candy bars, which makes the column `availability` the target.

- Print the `canbybar_df` object. 
- Save the dimensions of the dataframe in an object named `candybar_dim`.

<codeblock id="01_11">

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


<exercise id="12" title="Separating Our Data">

**Instructions:**    
Running a coding exercise for the first time could take a bit of time for everything to load.  Be patient, it could take a few minutes. 

**When you see `____` in a coding exercise, replace it with what you assume to be the correct code.  Run it and see if you obtain the desired output.  Submit your code to validate if you were correct.**

_**Make sure you remove the hash (`#`) symbol in the coding portions of this question.  We have commented them so that the line won't execute and you can test your code after each step.**_

Let's split up our the data in the candybars dataframe into our features and target. 
For this dataframe the features are the columns `chocolate` to `multi` and the target is the column `availability`.

Tasks:     

- Save the columns `chocolate` to `multi` in an object named `X`
- Since we are attempting to predict the country availability of candy bars, make the column `availability` the target and name the object `y`. 



<codeblock id="01_12">

- Are you using `.loc[]` to obtain the columns `chocolate` to `multi`?
- Are you select the column `availability` with single brackets?

</codeblock>
</exercise>




<exercise id="13" title="Baselines: Training a Model using Scikit-learn" type="slides, video">
<slides source="module1/module1_13" shot="1" start="18:2728" end="24:51">
</slides>
</exercise>

<exercise id="14" title="Fit or Predict">

**Do the following statements correspond to the `fit` or the `predict` stage:**  

**Statement:**      
_Is called first (before the other one)._

<choice id="1">
<opt text="Fit" correct="true">

Great job! Training on training data must be done before predicting on new data. 

</opt>

<opt text="Predict" >

How can the model predict without education first?

</opt>
</choice>

**Statement:**     
_Only takes `X` as an argument._

<choice id="2">
<opt text="Fit">

We need to make sure we give the model the correct labels so it can _learn_. 

</opt>

<opt text="Predict" correct="true">

Great job!

</opt>
</choice>

**Statement:**    
_In scikit-learn, we can ignore its output._

<choice id="3">
<opt text="Fit" correct="true">
 
Great job!

</opt>

<opt text="Predict">

You may want to look at the slides and see what each of these delivers as an output. 

</opt>
</choice>
</exercise>




<exercise id="15" title="First Step in Building a Model">

Below is the output of `y.value_counts()`.  
```out
Position
Forward     13
Defense      7
Goalie       2
dtype: int64
```



In this scenario, what would a `DummyClassifier(strategy='most_frequent')` model predict on the observation: 
```
   No.  Age  Height  Weight  Experience     Salary
1   83   34     191     210          11  3200000.0
```


<choice  id="1">
<opt text="Forward" correct="true">

Great job!

</opt>

<opt text="Defense" >

We are using the strategy `most_frequent` which predicts the most frequently occuring value. 

</opt>

<opt text="Goalie">

We are using the strategy `most_frequent` which predicts the most frequently occuring value. 

</opt>

<opt text="Player" >

We are using the strategy `most_frequent` which predicts the most frequently occuring value. 

</opt>

</choice>

</exercise>



<exercise id="16" title="Building a Model">

**Instructions:**    
Running a coding exercise for the first time could take a bit of time for everything to load.  Be patient, it could take a few minutes. 

**When you see `____` in a coding exercise, replace it with what you assume to be the correct code.  Run it and see if you obtain the desired output.  Submit your code to validate if you were correct.**

_**Make sure you remove the hash (`#`) symbol in the coding portions of this question.  We have commented them so that the line won't execute and you can test your code after each step.**_

Let's build a baseline model by using `DummyClassifier()`. 

Tasks:     

- Build a baseline model using  `DummyClassifier()`  and `most_frequent` for the `strategy` argument. Save this in an object named `model`. 
- Fit your model and then predict on the target column. 
- What is the accuracy of the model to 2 decimal places? Save this in the object `accuracy`.

<codeblock id="01_16">

- Are using `DummyClassifier(strategy="most_frequent")`?
- Are you using the model named `model`?
- Are you calling `.fit(X,y)` on your model?
- Are you using `model.score(X,y)` to find the accuracy?

</codeblock>
</exercise>

<exercise id="17" title="Baselines: Dummy Regression" type="slides, video">
<slides source="module1/module1_17" shot="1" start="24:582" end="28:4718">
</slides>
</exercise>


<exercise id="18" title="Dummy Regressors">

When using a regression model, which of the following is not a possible return value from `.score(X,y)` ? 

<choice  id="1">
<opt text="0.0" >

This is a possible value. This is expected when using a dummy classifier with a `mean` strategy. 

</opt>

<opt text="1.0" >

1.0 is the highest possible value. 

</opt>

<opt text="-0.1">

Negative values are a possible score when using regression classifiers.

</opt>

<opt text="1.5" correct="true">

Great! 1.0 is the highest possible value.

</opt>

</choice>

</exercise>

<exercise id="19" title="Dummy Regressor Scores">

Below are the values for `y` that were used to train  `DummyRegressor(strategy='mean')`:
```out
Grade
0     75
1     80
2     90
3     95
4     85
dtype: int64
```

What value will the model predict for every example?



<choice  id="1">
<opt text="80">

Is this the average of all the values?

</opt>

<opt text="90" >

Maybe try calculating the average of all the values.

</opt>

<opt text="85"  correct="true">

Great! It will predict the average of all the values. 

</opt>

<opt text="95" >

This is too high. Have you tried calculating the average of all the values?

</opt>

</choice>

</exercise>



<exercise id="20" title="Building a Dummy Regressor">

**Instructions:**    
Running a coding exercise for the first time could take a bit of time for everything to load.  Be patient, it could take a few minutes. 

**When you see `____` in a coding exercise, replace it with what you assume to be the correct code.  Run it and see if you obtain the desired output.  Submit your code to validate if you were correct.**

_**Make sure you remove the hash (`#`) symbol in the coding portions of this question.  We have commented them so that the line won't execute and you can test your code after each step.**_

Let's build a baseline model by using `DummyRegressor()`. 

Tasks:     

- Build a baseline model using the `DummyRegressor()`  and `mean` for the `strategy` argument. Save this in an object named `model`. 
- Fit your model and then predict on the target column. 
- What is the accuracy of the model to 2 decimal places? Save this in the object `accuracy`.

<codeblock id="01_20">

- Are using `DummyRegressor(strategy='mean')`?
- Are you using the model named `model`?
- Are you calling `.fit(X,y)` on your model?
- Are you using `model.score(X,y)` to find the accuracy?

</codeblock>
</exercise>


<exercise id="21" title="What Did We Just Learn?" type="slides, video">
<slides source="module1/module1_end" shot="0" start="04:5307" end="05:5911">
</slides>
</exercise>