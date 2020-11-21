---
title: 'Module 3: Splitting, Cross-Validation and the Fundamental Tradeoff'
description:
  'In this module, we  will introduce why and how we split our data as well as how cross-validation works on training data. We will also explain two important concepts in machine learning: the fundamental tradeoff and the golden rule. '
prev: /module2
next: /module4
type: chapter
id: 3
---

<exercise id="0" title="Module Learning Outcomes"  type="slides, video">

<slides source="module3/module3_00" shot="0" start="07:2828" end="08:0516">
</slides>

</exercise>

<exercise id="1" title="Splitting Data" type="slides,video">

<slides source="module3/module3_01" shot="1" start="80:571" end="94:51">
</slides>

</exercise>

<exercise id="2" title= "Splitting our data">

**Question 1**    
What are the 2 main groups we split our data into?

<choice id="1">

<opt text="Training and predicting data">

One of these may be right.

</opt>

<opt text= "Practice and testing data" >
 
One of these may be right.

</opt>

<opt text="Training and Testing data" correct="true">

Nice work!

</opt>

<opt text="Fitting and predicting data">

These are not the "official" names.

</opt>

</choice>


**Question 2**    
When do we split our data?

<choice id="2" >

<opt text="At the very beginning, before we explore our data." correct="true">

Great!

</opt>

<opt text="After we explore our data, but before we make our model.">

We must split our data before we do anything else.

</opt>

<opt text="After we train our model.">

This is a little too late. 

</opt>

<opt text="After we make any predictions.">

It's a better idea to do it as soon as possible.

</opt>

</choice>

**Question 3**   
Why do we split our data?

<choice id="3" >

<opt text="To increase our training accuracy." >

</opt>

<opt text="To help us generalize our model better." >

Getting warmer but not quite. 

</opt>

<opt text="To decreasing training time.">

Not quite but this may be a side effect. 

</opt>


<opt text="To help us assess how well our model generalizes." correct="true">

Great!

</opt>


</choice>

</exercise>

<exercise id="3" title="Decision Tree Outcome">

**True or False?**      
_If you don't set random_state, splitting your data is randomized and you will get different results each time._

<choice id="1" >
<opt text="True"  correct="true">

Great!

</opt>

<opt text="False">

`train_test_split()` splits the given data in a randomized manner. 

</opt>

</choice>

**True or False**      
*When using `train_test_split()`, you must specify both `test_size` and `train_size`.*

<choice id="2">
<opt text="True" >

You only need to specify one of these arguments. 

</opt>

<opt text="False" correct="true">

Nice work! 

</opt>

</choice >

</exercise>

<exercise id="4" title="Splitting Data in Action">

**Instructions:**    
Running a coding exercise for the first time could take a bit of time for everything to load.  Be patient, it could take a few minutes. 

**When you see `____` in a coding exercise, replace it with what you assume to be the correct code.  Run it and see if you obtain the desired output.  Submit your code to validate if you were correct.**

_**Make sure you remove the hash (`#`) symbol in the coding portions of this question.  We have commented them so that the line won't execute and you can test your code after each step.**_

Let's split our data using `train_test_split()` on our candy bars dataset.

Tasks:     

- Split the `X` and `y` dataframes into 4 objects: `X_train`, `X_test`, `y_train`, `y_test`. 
- Make the test set 0.2 (or the train set 0.8) and make sure to use `random_state=7`. 
- Build a model using `DecisionTreeClassifier()`. 
- Save this in an object named `model`. 
- Fit your model on the objects `X_train` and `y_train`.
- Evaluate the accuracy of the model using `.score()` on `X_train` and `y_train` save the values in an object named `train_score`.
- Repeat the above action but this time evaluate the accuracy of the model using `.score()` on `X_test` and `y_test` (which the model has never seen before) and save the values in an object named `test_score`. 

<codeblock id="03_04">

- Are you using `X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=7)`? 
- Are using `DecisionTreeClassifier()`?
- Are you using the model named `model`?
- Are you calling `.fit(X_train, y_train)` on your model?
- Are you scoring your model using `model.score(X_train, y_train)` and `model.score(X_test, y_test)`?

</codeblock>


**Question**    
On which split does the decision tree perform better?

<choice id="1" >
<opt text="Training Data"   correct="true">

Nice job! 

</opt>

<opt text="Testing Data">

Maybe take a closer look?

</opt>

</choice>

</exercise>

<exercise id="5" title="Train, Validation and Test Split" type="slides,video">

<slides source="module3/module3_05" shot="1" start="94:581" end="99:03">
</slides>

</exercise>

<exercise id="6" title= "Name that split!">

**Question 1**      
What data is trained on, predicted on and scored on? 

<choice id="1">

<opt text="Train"  correct="true">

Great! It's the only data that the model trains on.

</opt>

<opt text= "Validation" >
 
This doesn't see the training phase.

</opt>

<opt text="Test">

This is never trained on!

</opt>

<opt text="Deployment">

This should be kept far far away from training and scoring! 

</opt>

</choice>


**Question 2**     
What is scored multiple times and predicted multiple times but never is fitted?

<choice id="2" >

<opt text="Train" >

This data gets fitted, so it can't be training data.

</opt>

<opt text="Validate" correct="true">

Great!

</opt>

<opt text="Test">

It's a better idea to do it as soon as possible.

</opt>

<opt text="Deployment">

This is never scored. 

</opt>

</choice>

**Question 3**     
What is only ever scored once?

<choice id="3" >

<opt text="Train" >

This data gets scored many times.

</opt>

<opt text="Validate" >

This gets scored multiple times. 

</opt>

<opt text="Test" correct="true">

You got it!

</opt>

<opt text="Deployment">

This is never scored. 

</opt>

</choice>

</exercise>

<exercise id="7" title="Decision Tree Outcome">

**True or False**      
_Deployment data is used at the very end and only scored once._

<choice id="1" >
<opt text="True">  

Deployment data is used at the very end but it is never scored.

</opt>

<opt text="False" correct="true">

Nice job.

</opt>

</choice>

**True or False**    
_Validation data is used to help tune hyperparameters._

<choice id="2">
<opt text="True" correct="true">

Nailed it!

</opt>

<opt text="False" >

This is a prime reason for having a validation set. 

</opt>

</choice >

</exercise>

<exercise id="8" title="Cross Validation" type="slides,video">

<slides source="module3/module3_08" shot="1" start="99:091" end="109:022">
</slides>

</exercise>

<exercise id="9" title= "Cross Validation Questions">

**Question 1**   
We carry out cross-validation to avoid reusing the same validation set again and again. Let's say you do a 10-fold cross-validation on 1000 examples. For each fold, how many examples do you train on? 

<choice id="1">

<opt text="1000"  >

Remember that we leave a portion of the examples out to validate on. 

</opt>

<opt text= "100" >
 
This is how many examples are in 1 fold but not necessarily trained on.

</opt>

<opt text="900" correct="true">

Great!

</opt>

<opt text="10">

This is the number of folds, not examples. 

</opt>

</choice>


**Question 2**    
With a 10-fold cross-validation, you split 1000 examples into 10-folds. For each fold, when you are done, you add up the accuracies from each fold and divide by what?

<choice id="2" >

<opt text="1000"  >

This is the number of examples. We would get a very low score if we divided by this. 

</opt>

<opt text= "100" >
 
This is how many examples are in 1 fold.

</opt>

<opt text="900" >

This is the number of examples we are training on.

</opt>

<opt text="10" correct="true">

Nice!

</opt>

</choice>

**Question 3**    

```out
array([0.80952381, 0.80952381, 0.85714286, 0.85714286])
```

Given this output of `cross_val_score()`, what was the value of 𝑘?

<choice id="3" >

<opt text="0" >

There must have been some positive value for k.

</opt>

<opt text="1" >

How many items are there in the array?

</opt>

<opt text="4" correct="true">

Great work!

</opt>

<opt text="8" >

Not this time!

</opt>

</choice>

</exercise>

<exercise id="10" title="Cross Validation True or False">

**True or False?**     
_𝑘-fold cross-validation calls fit 𝑘 times and predict 𝑘 times._

<choice id="1" >
<opt text="True" correct="true">  

Fit and predict are both called k times!

</opt>

<opt text="False" >

How many times are fit and predict called on 1 fold - cross-validation?

</opt>

</choice>

**True or False**      
_The goal of cross-validation is to obtain a better estimate of test score than just using a single validation set._

<choice id="2">
<opt text="True" correct="true">

Nailed it!

</opt>

<opt text="False" >

We use cross validation to estimate our test score better. 

</opt>

</choice >

**True or False**       
_The main disadvantage of using a large 𝑘 in cross-validation is running time._

<choice id="3">
<opt text="True" correct="true">

Nailed it!

</opt>

<opt text="False" >

Since we need to train multiple times and predict multiple times, it can be very time-consuming.

</opt>

</choice >

</exercise>

<exercise id="11" title="Cross Validation in Action">

**Instructions:**    
Running a coding exercise for the first time could take a bit of time for everything to load.  Be patient, it could take a few minutes. 

**When you see `____` in a coding exercise, replace it with what you assume to be the correct code.  Run it and see if you obtain the desired output.  Submit your code to validate if you were correct.**

_**Make sure you remove the hash (`#`) symbol in the coding portions of this question.  We have commented them so that the line won't execute and you can test your code after each step.**_

Let's use `cross_validate()` on a Pokémon dataset that we've used before in <a href="https://prog-learn.mds.ubc.ca/" target="_blank">Programming in Python for Data Science</a>.

Tasks:     

- Split the `X` and `y` dataframes into 4 objects: `X_train`, `X_test`, `y_train`, `y_test`. 
- Make the test set 0.2 (or the train set 0.8) and make sure to use `random_state=33` (the random state here is for testing purposes so we all get the same split). 
- Build a model using `DecisionTreeClassifier()`. 
- Save this in an object named `model`. 
- Cross-validate using `cross_val_score()` on the objects `X_train` and `y_train` and with 6 folds (`cv=6`) and save these scores in an object named `cv_scores`. 

<codeblock id="03_11">

- Are you using `X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=33)`? 
- Are using `DecisionTreeClassifier()`?
- Are you using the model named `model`?
- Are you cross-validating using `cross_val_score(model, X_train, y_train, cv=6)` on your model?

</codeblock>

</exercise>

<exercise id="12" title="Cross Validation in Action again!">

**Instructions:**    
Running a coding exercise for the first time could take a bit of time for everything to load.  Be patient, it could take a few minutes. 

**When you see `____` in a coding exercise, replace it with what you assume to be the correct code.  Run it and see if you obtain the desired output.  Submit your code to validate if you were correct.**

_**Make sure you remove the hash (`#`) symbol in the coding portions of this question.  We have commented them so that the line won't execute and you can test your code after each step.**_

Let's use `cross_validate()` on our Pokémon dataset that we saw in the previous exercises.  

Tasks:     

- Build a model using `DecisionTreeClassifier()`. 
- Save this in an object named `model`. 
- Cross-validate using `cross_validate()` on the objects `X_train` and `y_train` making sure to specify 10 folds and `return_train_score=True`.
- Convert the scores into a dataframe and save it in an object named `scores_df`.
- Calculate the mean value of each column and save this in an object named `mean_scores`. 

<codeblock id="03_12">

- Are using `DecisionTreeClassifier()`?
- Are you using the model named `model`?
- Are you cross-validating using `cross_validate(model, X_train, y_train, cv=10, return_train_score=True)` on your model?
- Are you saving your dataframe using `pd.DataFrame(scores)`?
- Are you using `.mean()` to calculate the mean of each column in `scores_df`?

</codeblock>

</exercise>

<exercise id="13" title="Underfitting and Overfitting" type="slides,video">

<slides source="module3/module3_13" shot="1" start="109:08" end="116:091">
</slides>

</exercise>

<exercise id="14" title= "Is it Overfitting or Underfitting?">

**Question 1**   
If our train accuracy is much higher than our test accuracy, is our model overfitting or underfitting? 

<choice id="1">

<opt text="Overfitting"  correct="true">

Great! 

</opt>

<opt text= "Underfitting" >
 
Underfitting would occur if our training accuracy was low. 

</opt>


</choice>


**Question 2**   
If our train accuracy and our test accuracy are both low and relatively similar in value, is our model overfitting or underfitting? 

<choice id="2" >

<opt text="Overfitting"  >

Since our train accuracy is still quite low, this would not be overfitting. 

</opt>

<opt text= "Underfitting" correct="true">
 
Great!

</opt>

</choice>

**Question 3**     
If our model is using a Dummy Classifier for a classification problem with the `strategy=most_frequent`, is our model more likely overfitting or underfitting?

<choice id="3" >

<opt text="Overfitting"  >

We are using a model that isn't complex and could be improved, this may be pointing to underfitting. 

</opt>

<opt text= "Underfitting" correct="true">
 
Great!

</opt>

</choice>

</exercise>

<exercise id="15" title="Overfitting and Underfitting True or False">


**True or False**      
_All models will either overfit or underfit._

<choice id="2">
<opt text="True">

Not all models will overfit or underfit. 

</opt>

<opt text="False"  correct="true">

Nailed it!

</opt>

</choice >

**True or False**       
_More "complicated" models are more likely to overfit than "simple" ones._

<choice id="3">
<opt text="True" correct="true">

Great!

</opt>

<opt text="False"  >

As we add complexity to our model, it is more likely to overfit. 

</opt>

</choice >

</exercise>


<exercise id="16" title="Overfitting/Underfitting in Action!">

**Instructions:**    
Running a coding exercise for the first time could take a bit of time for everything to load.  Be patient, it could take a few minutes. 

**When you see `____` in a coding exercise, replace it with what you assume to be the correct code.  Run it and see if you obtain the desired output.  Submit your code to validate if you were correct.**

_**Make sure you remove the hash (`#`) symbol in the coding portions of this question.  We have commented them so that the line won't execute and you can test your code after each step.**_

Let's examine our validation scores and training scores a bit more carefully and assess if our model is underfitting or overfitting.

This time we are looking at a new data set that contains the basketball players in the NBA. We are only going to use the players with a position of Guard (G) or Forward (F).  We will be using features height, weight and salary to try to predict the player's position, Guard or Forward.  

Let's take a quick look at it before diving in. 

<codeblock id="basketball">

</codeblock>

Tasks:     

- Cross-validate using `cross_validate()` on the objects `X_train` and `y_train` making sure to specify 10 folds and `return_train_score=True`.
- Convert the scores into a dataframe and save it in an object named `scores_df`.
- Calculate the mean value of each column and save this in an object named `mean_scores`. 
- Answer the question below.

<codeblock id="03_16">

- Are you cross-validating using `cross_validate(model, X_train, y_train, cv=10, return_train_score=True)` on your model?
- Are you saving your dataframe using `pd.DataFrame(scores)`?
- Are you using `.mean()` to calculate the mean of each column in `scores_df`?

</codeblock>


**Question**    
Is this model overfitting or underfitting?

<choice id="1" >
<opt text="Overfitting"   correct="true">

Nice job! 

</opt>

<opt text="Underfitting">

Is the training score higher or lower?

</opt>

</choice>

</exercise>

<exercise id="17" title="Fundamental Tradeoff and the Golden Rule" type="slides,video">

<slides source="module3/module3_17" shot="1" start="116:141" end="125:12">
</slides>

</exercise>

<exercise id="18" title= "Quick Questions on Tradeoff and Golden Rule">

**Question 1**    
If we are hyperparameter tuning, which depth would you select for this model given the graph below? 

<center><img src="/module3/Q16_2.png"  width = "80%" alt="404 image" /></center>

<choice id="1">

<opt text="1"  >

Where is the cross-validation score the highest?

</opt>

<opt text= "4" >
 
Where is the cross-validation score the highest?

</opt>

<opt text= "6" correct="true">
 
Great!

</opt>

<opt text= "19" >
 
Where is the cross-validation score the highest?

</opt>

</choice>


**Question 2**   
Fill in the Blank: 

The ______________ data cannot influence the training phase in any way.

<choice id="2" >

<opt text="Training"  >

This actually must be used in the training phase. 

</opt>

<opt text= "Test" correct="true">
 
Great!

</opt>

</choice>

</exercise>

<exercise id="19" title="Training and Testing Questions">

**Question 1**   

The fundamental tradeoff of ML states that as model complexity increases ...

<choice id="1" >

<opt text="Test score decreases."  >

Actually the test score is not taken into consideration here. 

</opt>

<opt text= "Train score decreases.">
 
 Quite the oposite in fact!

</opt>

<opt text= "Train score increases." correct="true">
 
Great!

</opt>

<opt text= "Test score increases." >
 
Try not to think about the the test score here. 

</opt>

</choice>

**Question 2**     
*In supervised learning, the training score is _________ higher than the validation score.*

<choice id="2">
<opt text="Always" >

Although this is the case often, validation score can be higher.

</opt>

<opt text="Ususally"  correct="true">

Nice work! Sometimes and often but not always!

</opt>

<opt text="Sometimes">

Maybe a bit more than sometimes.

</opt>


<opt text="Never" >

We've seen cases where this true!

</opt>

</choice >

</exercise>

<exercise id="20" title="Picking your Hyperparameter">

**Instructions:**    
Running a coding exercise for the first time could take a bit of time for everything to load.  Be patient, it could take a few minutes. 

**When you see `____` in a coding exercise, replace it with what you assume to be the correct code.  Run it and see if you obtain the desired output.  Submit your code to validate if you were correct.**

_**Make sure you remove the hash (`#`) symbol in the coding portions of this question.  We have commented them so that the line won't execute and you can test your code after each step.**_

Let's take a look at the basketball dataset we saw in exercise 16. We will again be using features height, weight and salary and a target column `position`..  This time , however, let's cross-validate on different values for max_depth so we can set this hyperparameter and build a final model that best generalizes on our test set. 

First let's see which hyperparameter is the most optimal. 

Tasks:     

- Fill in the code below. 
- We are first loading in our `bball.csv` dataset and assigning our features to `X` and our target `position` to an object named `y`. 
- Fill in the code so that it split the dataset into `X_train`, `X_test`, `y_train`, `y_test`. Make sure to use a 20% test set and a `random_state=33` so we can verify you solution.
- Next, fill in the code so that a `for` loop does the following:

  1. iterates over the values 1-20.
    - Builds a decision tree classifier with a `max_depth` equal to each iteration.
    - Uses `cross_validate` on the model with a `cv=10` and `return_train_score=True`.
    - Appends the depth value to the `depth` list in the dictionary `results_dict`.
    - Appends the `test_score` to the `mean_cv_score` list in the dictionary. 
    - Appends the `train_score` to the `mean_train_score` list in the dictionary. 
- We have given you code that wrangles this dictionary and transforms it into a state ready for plotting.
- Finish off by filling in the blank to create a line graph that plots the train and validation scores for each depth value. 
(Note: we have edited the limits of the y-axis so it's easier to read)

<codeblock id="03_20a">

- Are you using `train_test_split()` to split the data?
- Are you splitting with either `test_size=0.2` or `train_size=0.8`? 
- Are you setting your `random_state=33` inside `train_test_split()`?
- Are you using `DecisionTreeClassifier(max_depth=depth)` to build the model?
- Are you using `cross_validate(model, X_train, y_train, cv=10, return_train_score=True)`?
- Are you using `alt.Chart(results_df).mark_line()` to create your plot?

</codeblock>

**Question 1**    
To which depth would you set your `max_depth` hyperparameter?

<choice id="1" >
<opt text="1" >

There are other depth values that have a higher cross-validation score that at this value. 

</opt>

<opt text="4" correct="true">

Nice work. This is where the score is at the highest for the validation set. 

</opt>

<opt text="8"   >

Are you sure this is the depth with the highest cross-validation score possible?

</opt>

<opt text="17">

Are you sure this is the depth with the highest cross-validation score possible?

</opt>

</choice>


**Question 2**    
Are we obeying the golden rule of machine learing?

<choice id="2" >
<opt text="Yes" correct="true">

Yes, the test data have not influenced the training in anyway!

</opt>

<opt text="No" >

Have we touched the test data yet?

</opt>


</choice>


Now that we have found a suitable value for max_depth let's build a new model and let this hyperparameter value. How well does your model do on the test data?

Tasks:     

- Build a model using `DecisionTreeClassifier()` using the optimal `max_depth`. 
- Save this in an object named `model`. 
- Fit your model on the objects `X_train` and `y_train`.
- Evaluate the test score of the model using `.score()` on `X_test` and `y_test` and save the values in an object named `test_score` rounded to 4 decimal places.

<codeblock id="03_20b">

- Are using `DecisionTreeClassifier(max_depth=5)`?
- Are you using the model named `model`?
- Are you calling `.fit(X_train, y_train)` on your model?
- Are you scoring your model using `model.score(X_test, y_test)`?
- Are you rounding to 4 decimal places?
- Are you calculating `test_score` as  `round(model.score(X_test, y_test), 4)` )

</codeblock>


**Question 1**    
Is the test score comparable with the cross-validation score that we obtained in the first part?

<choice id="3" >
<opt text="Yes"   correct="true">

Nice job! 

</opt>

<opt text="No">

Wouldn't you say within 3% is comparable here?

</opt>

</choice>

</exercise>


<exercise id="21" title="What Did We Just Learn?" type="slides, video">
<slides source="module3/module3_end" shot="0" start="08:0517" end="08:5423">
</slides>
</exercise>

