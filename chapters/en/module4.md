---
title: 'Module 4: Similarity-Based Approaches to Supervised Learning'
description:
  'In this module, we will cover similarity-based models 𝑘-Nearest Neighbours (also known as 𝑘-NNs) and Support Vector Machines (SVMs with an RBF kernel).'
prev: /module3
next: /module5
type: chapter
id: 4
---

<exercise id="0" title="Module Learning Outcomes"  type="slides, video">

<slides source="module4/module4_00" shot="0" start="08:5423" end="09:3211">
</slides>

</exercise>

<exercise id="1" title="Terminology" type="slides,video">

<slides source="module4/module4_01" shot="2" start="0:002" end="6:28">
</slides>

</exercise>

<exercise id="2" title= "Dimension Questions">

Use the following dataframe named `garden` to answer the next two questions. 

```out
               
       seeds   shape  sweetness   water-content      weight    fruit_veg
0      1        0        35          84               100        fruit
1      0        0        23          75               120        fruit
2      1        1        15          90              1360         veg
3      1        1         7          96               600         veg
4      0        0        37          80                 5        fruit
5      0        0        45          78                40        fruit  
6      1        0        27          83               450         veg
7      1        1        18          73                 5         veg
8      1        1        32          80                76         veg
9      0        0        40          83                65        fruit
```

**Question 1**     
We are trying to predict if each example is either a fruit or a vegetable. 
What would be the dimension of feature vectors in this problem?

<choice id="1">

<opt text="1">

Have you tried counting the columns in `garden` that are not the `target`? 

</opt>

<opt text= "5" correct="true">
 
Fantastic!

</opt>

<opt text="6" >

Are you including the target column `fruit_veg`? Or maybe you included the index?

</opt>

<opt text="7">

You may be including the index and target column `fruit_veg`. 

</opt>

</choice>

**Question 2**   
Which of the following would be the feature vector for example 0. 

<choice id="2" >

<opt text="<code>array([1,  0, 1, 1, 0, 0, 1, 1, 1, 0])<code>">

This is the values from the first column not values for the feature vector of example 0. 

</opt>

<opt text="<code>array([fruit,  fruit, veg, veg, fruit, fruit, veg, veg, veg, fruit])<code>">

This is only containing the values of the target.

</opt>

<opt text="<code>array([1, 0, 35, 84, 100])<code>" correct="true">

Nice work!

</opt>

<opt text="<code>array([1, 0, 35, 84, 100,  fruit])<code>">

Close but you have the target value in the feature vector.

</opt>

</choice>

</exercise>

<exercise id="3" title="True and False Terminology">

**True or False**     
_Analogy-based models find examples from the test set that are most similar to the test example we are predicting._

<choice id="1" >
<opt text="True"  >

These types of models find examples that are most similar to the text example in the *training* set. 

</opt>

<opt text="False" correct="true">

Great! They are finding examples in the training set, most similar to the test example. 

</opt>

</choice>

**True or False**     
*Feature vectors can only be of length 3 since we cannot visualize past that.*

<choice id="2">
<opt text="True" >

Feature vectors have no max value.

</opt>

<opt text="False" correct="true">

Nice work! 

</opt>

</choice >

**True or False**     
*A dataset with 10 dimensions is considered low dimensional.*

<choice id="3">
<opt text="True" correct="true">

Well done!

</opt>

<opt text="False" >

Dimensions up to 1000 are considered "low". 

</opt>

</choice >

</exercise>

<exercise id="4" title="Distances" type="slides,video">
<slides source="module4/module4_04" shot="2" start="06:3324" end="11:18">
</slides>

</exercise>

<exercise id="5" title= "Calculating Distances">


**Question 1**      
Given the following 2 feature vectors, what is the Euclidean distance between the following two feature vectors?

```
u = np.array([5, 0, 22, -11])
v = np.array([-1, 0, 19, -9])
```

<choice id="1">

<opt text="49"  >

You forgot to square root!

</opt>

<opt text="7" correct="true">

Great!

</opt>

<opt text="6">

Not quite there.

</opt>

<opt text="36">

Close but you have the target value in the feature vector.

</opt>

</choice>

**Question 2**    
We have collected a third vector `w`. 

```
u = np.array([5, 0, 22, -11])
v = np.array([-1, 0, 19, -9])
w = np.array([0, 1, 17, -4])
```

Which two vectors are most similar among `u`, `v`, and `w`?

<choice id="2" >

<opt text="u and w"  >

The distance between `u` and `w` is 10. Have you checked the other yet?
</opt>

<opt text="u and v" correct="true">

The distance between `u` and `v` is 7. Have you checked the other yet?

</opt>

<opt text="v and w" correct="true">

Nice work!

</opt>

<opt text="They are equally distanced from one another">

The distance between `u` and `w` is 10 and the distance between `u` and `v` is 7 so they cannot be the same distance from one another.

</opt>

</choice>

</exercise>

<exercise id="6" title="Distance True or False">

**True or False**     
_Euclidean distance will always have a positive value.._

<choice id="1" >
<opt text="True"  correct="true">

Yes! We are squaring all the differences which means that distance can only be a positive value. 

</opt>

<opt text="False" >

Take a look at the equation we use to calculate Euclidean distance. 

</opt>

</choice>

</exercise>

<exercise id="7" title='Calculating Euclidean Distance Step by Step'>

**Instructions:**    
Running a coding exercise for the first time could take a bit of time for everything to load.  Be patient, it could take a few minutes. 

**When you see `____` in a coding exercise, replace it with what you assume to be the correct code.  Run it and see if you obtain the desired output.  Submit your code to validate if you were correct.**

_**Make sure you remove the hash (`#`) symbol in the coding portions of this question.  We have commented them so that the line won't execute and you can test your code after each step.**_

Let's calculate the Euclidean distance between 2 examples in the Pokémon dataset without using Scikit-learn. 

Tasks:     

- Subtract the first two pokemon feature vectors and save the result in an object named `sub_pk`.
- Square the difference and save it in an object named `sq_sub_pk`.
- Sum the squared difference from each dimension and save the result in an object named `sss_pk`.
- Finally, take the square root of the entire calculation and save it in an object named `pk_distance`.

<codeblock id="04_07">

- Are you importing `sqrt` from the `math` library?
- Are you using `X.iloc[1] - X.iloc[0]` to subtract the first 2 Pokémon feature vectors?
- Are you using `**2` to square the difference??
- Are you using `.sum()` to sum the differences?
- Are you using `sqrt()` to square root the sum of squared differences?

</codeblock>

</exercise>

<exercise id="8" title='Calculating Euclidean Distance with Scikit-learn'>

**Instructions:**    
Running a coding exercise for the first time could take a bit of time for everything to load.  Be patient, it could take a few minutes. 

**When you see `____` in a coding exercise, replace it with what you assume to be the correct code.  Run it and see if you obtain the desired output.  Submit your code to validate if you were correct.**

_**Make sure you remove the hash (`#`) symbol in the coding portions of this question.  We have commented them so that the line won't execute and you can test your code after each step.**_

This time, let's calculate the Euclidean distance between 2 examples in the Pokémon dataset using Scikit-learn. 

Tasks:     

- Import the necessary library.
- Calculate the Euclidean distance of the first 2 Pokémon and save it in an object named pk_distance.

<codeblock id="04_08">

- Are you importing `euclidean_distances` from `sklearn.metrics.pairwise` 
- Are you making sure to use `euclidean_distances(X.iloc[:2])`
- Are you selecting the right value from the array using `[0,1]`
</codeblock>

</exercise>

<exercise id="9" title="Finding the Nearest Neighbour" type="slides,video">
<slides source="module4/module4_09" shot="2" start="11:22" end="17:0708">
</slides>

</exercise>

<exercise id="10" title= "Finding Neighbours Questions">

**Question 1**    
In the slides we calculated distances between all points in the training data using `sklearn`'s `euclidean_distances` function. What would happen if we didn't use `fill_diagonal()`?

<choice id="1">

<opt text="We would get the farthest example from the one we are trying to find instead of the closest.">

Not quite. 

</opt>

<opt text= "We would get itself as the closest example."  correct="true" >
 
Right, there is 0 distance from a point to itself. 

</opt>

<opt text="We would obtain the mean distance from all points to the current one." >

Unfortunately, the mean has nothing to do with why we fill the diagonals in.

</opt>

<opt text="We would get 0 examples." >

We would get an example but it would be the wrong one.

</opt>

</choice>

**Question 2**     
How many dimension does the input vector for `kneighbors()` need to be?

<choice id="2" >

<opt text="1" >

1d vectors will result in an error. 

</opt>

<opt text="2" correct="true">

Great!

</opt>

<opt text="3">

This will throw an error. 

</opt>

<opt text="It must be a pandas dataframe">

Close but you have the target value in the feature vector.

</opt>

</choice>

</exercise>

<exercise id="11" title="Nearest Neighbours True or False">

**True or False**     
_When finding the nearest neighbour in a dataset using `kneighbors()` from the `sklearn` library, we must `fit`  the data first._

<choice id="1" >
<opt text="True"  correct="true" >

Great work!

</opt>

<opt text="False" >

Take a look at the code in the lecture slides to refresh!

</opt>

</choice>

**True or False**     
_Calculating the distances between an example and a query point takes twice as long as calculating the distances between two examples._

<choice id="2" >
<opt text="True"  >

This is completely made up!

</opt>

<opt text="False" correct="true" >

Great work!

</opt>

</choice>

</exercise>

<exercise id="12" title='Calculating the Distance to a Query Point'>

**Instructions:**    
Running a coding exercise for the first time could take a bit of time for everything to load.  Be patient, it could take a few minutes. 

**When you see `____` in a coding exercise, replace it with what you assume to be the correct code.  Run it and see if you obtain the desired output.  Submit your code to validate if you were correct.**

_**Make sure you remove the hash (`#`) symbol in the coding portions of this question.  We have commented them so that the line won't execute and you can test your code after each step.**_

Let's calculate the closet Pokémon in the training set to a Snoodle (our made-up Pokémon)!

Snoodle	has the following feature vector. 

```out
[[53,  77,  43,  69,  80,  57,  5]]
```
Which Pokémon in the training set, most resembles a Snoodle?

Tasks:     

- Create a model and name it `nn` (make sure you are finding the single closest Pokémon).
- Train your model on `X_train`.
- Predict your Pokémon using `kneighbors` and save it in an object named `snoodles_neighbour`.
- Which Pokémon (the name) is Snoodle most similar to? Save it in an object named `snoodle_name`.

<codeblock id="04_12">

- Are you using ` NearestNeighbors(n_neighbors=1)`?
- Are you using `nn.fit(X_train)`?
- Are you using `nn.kneighbors(query_point)` ?
- Are you using `train_df.iloc[snoodles_neighbour[1].item()]['name']` to get the name of the closest Pokémon?

</codeblock>
</exercise>

<exercise id="13" title="𝑘-Nearest Neighbours (𝑘-NNs) Classifier" type="slides,video">
<slides source="module4/module4_13" shot="2" start="17:102" end="21:2605">
</slides>

</exercise>

<exercise id="14" title= "Classifying Examples by Hand">

Consider this toy dataset:

<center><img src="/module4/Q14.png"  width = "40%" alt="404 image" /></center>

**Question 1**   
If 𝑘=1 , what would you predict for &nbsp; &nbsp;   <img src="/module4/ans14.png"  width = "8%" alt="404 image" /> &nbsp;&nbsp;&nbsp;?

<choice id="1">

<opt text="0">

the point (2, 2) is the closest to (0, 0).
 
</opt>

<opt text= "1"  correct="true" >
 
Right, the point (2, 2) is the closest to (0, 0) and it is categorized as 1. 

</choice>

**Question 2**     
If  𝑘=3 , what would you predict for &nbsp; &nbsp;   <img src="/module4/ans14.png"  width = "8%" alt="404 image" /> &nbsp;&nbsp;&nbsp;?

<choice id="2" >

<opt text="0" correct="true">

Nice!

</opt>

<opt text= "1" >
 
The points (2, 2), (5, 2) and (4, 3) are the closest to (0, 0). Which label is more occurring?

</opt>

</choice>


</exercise>

<exercise id="15" title="𝑘-NN Classifiers True or False">

**True or False**     
_The classification of the closest neighbour to the test example always contributes the most to the prediction._

<choice id="1" >
<opt text="True">

Not always. You can select this as an option but it is not done like this by default.

</opt>

<opt text="False" correct="true" >

Great work!

</opt>

</choice>

**True or False**     
*The `n_neighbors` hyperparameter must be less than the number of examples in the training set.*

<choice id="2" >
<opt text="True" correct="true"  >

Nice work. 

</opt>

<opt text="False" >

You can't assign `n_neighbors` to a value greater than the possible number of examples in the training set. 

</opt>

</choice>

**True or False**     
_Similar to decision trees, 𝑘-NNs finds a small set of good features._

<choice id="3" >
<opt text="True"  >

𝑘-NNs use all the features!

</opt>

<opt text="False" correct="true" >

Great work!

</opt>

</choice>

</exercise>

<exercise id="16" title='Predicting with a 𝑘-NN-Classifier'>

**Instructions:**    
Running a coding exercise for the first time could take a bit of time for everything to load.  Be patient, it could take a few minutes. 

**When you see `____` in a coding exercise, replace it with what you assume to be the correct code.  Run it and see if you obtain the desired output.  Submit your code to validate if you were correct.**

_**Make sure you remove the hash (`#`) symbol in the coding portions of this question.  We have commented them so that the line won't execute and you can test your code after each step.**_

Let's try to classify some Pokémon from the Pokémon dataset. How well does our model do on the training data?

Tasks:     

- Create a `KNeighborsClassifier` model with `n_neighbors` equal to 5 and name it `model`.
- Train your model on `X_train` and `y_train` (Hint: you may want to use `.to_numpy()`).
- Score your model on the training set using `.score()` and save it in an object named `train_score`.
- Score your model on the test set using `.score()` and save it in an object named `test_score`.

<codeblock id="04_16">

- Are you importing `KNeighborsClassifier`?
- Are you using ` KNeighborsClassifier(n_neighbors=5)`?
- Are you using `model.fit(X_train, y_train.to_numpy())`?
- Are you using `model.score(X_train, y_train)` to find the training score?
- Are you using `model.score(X_test, y_test)` to find the test score?

</codeblock>
</exercise>

<exercise id="17" title="Choosing 𝑘 (n_neighbors)" type="slides,video">
<slides source="module4/module4_17" shot="2" start="21:2905" end="29:2625">
</slides>

</exercise>

<exercise id="18" title= "Choosing 𝑘 for Your Model">

Consider this graph:

<center><img src="/module4/Q18a.png"  width = "80%" alt="404 image" /></center>

**Question 1**     
What value of `n_neighbors` would you choose to train your model on? 

<choice id="1">

<opt text="0">

This is not a valid value for `n_neighbors`.
 
</opt>

<opt text= "1" >
 
Although this may have the highest training score, this does not have the highest cross-validation score. 

</opt>

<opt text= "12"  correct="true" >
 
Nice work. 

</opt>

<opt text= "16" >
 
Almost. There is a value with a higher score

</opt>

<opt text= "29">
 
You shouldn't pick the highest `n_neighbors` without the cv-score being the highest.  

</opt>

</choice>

**Question 2**     
At what of  𝑘 is the largest gap between the train and validation score?

<choice id="2">

<opt text="1" correct="true">

Training score is much higher than the validation score here!

</opt>

<opt text= "4" >
 
Are there values where the validation score is lower?

</opt>

<opt text= "17" >
 
Are there values where the validation score is lower and the training score is higher?

</opt>

<opt text= "29" >

The gap between validation score and training score is actually quite small here!

</opt>

</choice>

</exercise>

<exercise id="19" title="Curse of Dimensionality and Choosing 𝑘 True or False">

**True or False**     
_With  𝑘 -NN, setting the hyperparameter  𝑘  to larger values typically increase training score._

<choice id="1" >
<opt text="True">

Have you tried it out? It could be a good idea to see this in action!

</opt>

<opt text="False" correct="true" >

Great work!

</opt>

</choice>

**True or False**     
_𝑘 -NN may perform poorly in high-dimensional space (say, d > 100)._

<choice id="2" >
<opt text="True" correct="true"  >

Nice work. 

</opt>

<opt text="False" >

Having more features in some cases is less helpful to the model.

</opt>

</choice>

</exercise>

<exercise id="20" title='Hyperparameter Tuning'>

**Instructions:**    
Running a coding exercise for the first time could take a bit of time for everything to load.  Be patient, it could take a few minutes. 

**When you see `____` in a coding exercise, replace it with what you assume to be the correct code.  Run it and see if you obtain the desired output.  Submit your code to validate if you were correct.**

_**Make sure you remove the hash (`#`) symbol in the coding portions of this question.  We have commented them so that the line won't execute and you can test your code after each step.**_

In the last exercise, we classified some Pokémon from the Pokémon dataset but we were not using the model that could have been the best! Let's try hyperparameter tuning.

First, let's see which hyperparameter is the most optimal. 

Tasks:     

Fill in the code for  a `for` loop that does the following:
- iterates over the values 1-50 in increments of 5.
- Builds a  `KNeighborsClassifier` model with `n_neighbors` equal to each iteration.
- Uses `cross_validate` on the model with a `cv=10` and `return_train_score=True`.
- Appends the 𝑘 value to the `n_neighbors` list in the dictionary `results_dict`.
- Appends the `test_score` to the `mean_cv_score` list in the dictionary. 
- Appends the `train_score` to the `mean_train_score` list in the dictionary. 

We have given you code that wrangles this dictionary and transforms it into a state ready for plotting.

Finish off by filling in the blank to create a line graph that plots the train and validation scores for each value of k.      
(Note: we have edited the limits of the y-axis so it's easier to read)

<codeblock id="04_20a">

- Are you importing `KNeighborsClassifier`?
- Are you using ` KNeighborsClassifier(n_neighbors=11)`?
- Are you using `model.fit(X_train, y_train.to_numpy())`?
- Are you using `cross_validate(model, X_train, y_train, cv=10, return_train_score=True)`?
- Are you using `alt.Chart(results_df).mark_line()` to create your plot?

</codeblock>


**Question 1**    
What value would you pick for the hyperparameter `n_neighbors`?

<choice id="1" >
<opt text="1" >

There are other `n_neighbors` values that have a higher cross-validation score than at this value. 

</opt>

<opt text="11" correct="true">

Great! The CV score is highest at this value. 

</opt>

<opt text="24"   >

Are you sure this is the n_neighbors with the highest cross-validation score possible?

</opt>

<opt text="31">

Are you sure this is the n_neighbors with the highest cross-validation score possible?

</opt>

</choice>

Tasks:     

Now that we have found a suitable value for `n_neighbors`, let’s build a new model with this hyperparameter value. How well does your model do on the test data?

Tasks:     

- Build a model using `KNeighborsClassifier()` using the optimal `n_neighbors`. 
- Save this in an object named `model`. 
- Fit your model on the objects `X_train` and `y_train`.
- Evaluate the test score of the model using `.score()` on `X_test` and `y_test` and save the values in an object named `test_score` rounded to 4 decimal places.

<codeblock id="04_20b">

- Are using `KNeighborsClassifier(n_neighbors=11)`?
- Are you using the model named `model`?
- Are you calling `.fit(X_train, y_train)` on your model?
- Are you scoring your model using `model.score(X_test, y_test)`?
- Are you rounding to 4 decimal places?
- Are you calculating `test_score` as  `round(model.score(X_test, y_test), 4)` )

</codeblock>

</exercise>

<exercise id="21" title="𝑘 -Nearest Neighbours Regressor" type="slides,video">
<slides source="module4/module4_21" shot="2" start="29:3123" end="35:1328">
</slides>

</exercise>

<exercise id="22" title= "Regression Questions">

Consider this toy dataset:

<center><img src="/module4/Q14.png"  width = "40%" alt="404 image" /></center>

**Question 1**      
If  𝑘=3 , what would you predict for &nbsp; &nbsp;   <img src="/module4/ans14.png"  width = "8%" alt="404 image" /> &nbsp;&nbsp;&nbsp; if we were doing regression rather than classification?

<choice id="1">

<opt text="0">

The points (2, 2), (5, 2) and (4, 3) are the closest to (0, 0) and so we must take the average of all the values. 
 
</opt>

<opt text= "1"  >
 
The points (2, 2), (5, 2) and (4, 3) are the closest to (0, 0) and so we must take the average of all the values.

</opt>

<opt text= "1/3"  correct="true" >
 
You got it!

</opt>

<opt text= "3">
 
We must take the average of the 3 nearest examples. 

</opt>

</choice>

**Question 2**  

**True or False**     
_𝑘-NN with Regression can only be done in a 1-dimensional space._

<choice id="2" >

<opt text="True"  >

𝑘-NN can be done with just as many dimensions as classification

</opt>

<opt text="False" correct="true"  >

Nice work. 

</opt>

</choice>


</exercise>

<exercise id="23" title='Building a 𝑘-NN-Regressor'>

**Instructions:**    
Running a coding exercise for the first time could take a bit of time for everything to load.  Be patient, it could take a few minutes. 

**When you see `____` in a coding exercise, replace it with what you assume to be the correct code.  Run it and see if you obtain the desired output.  Submit your code to validate if you were correct.**

_**Make sure you remove the hash (`#`) symbol in the coding portions of this question.  We have commented them so that the line won't execute and you can test your code after each step.**_

Let's bring in this Pokémon dataset again, but this time we are not going to be predicting a Pokémon’s capture rate (`capture_rt`) instead of its `legendary` classification.

We did the same process of cross validation and scoring as we did before but we obtain this plot: 

<center><img src="/module4/Q23.png"  width = "90%" alt="404 image" /></center>

This model didn't end up having a clear best score when we hyperparameter tuned but in the end, we decided to use `n_neighbors=12`.

Let's build a `KNeighborsRegressor` with this hyperparameter value and see how well your model does on the test data.

Tasks:     

- Build a model using `KNeighborsRegressor()` using the optimal `n_neighbors`. 
- Save this in an object named `model`. 
- Fit your model on the objects `X_train` and `y_train`.
- Evaluate the test score of the model using `.score()` on `X_test` and `y_test` and save the values in an object named `test_score` rounded to 4 decimal places.

<codeblock id="04_23b">

- Are using `KNeighborsRegressor(n_neighbors=11)`?
- Are you using the model named `model`?
- Are you calling `.fit(X_train, y_train)` on your model?
- Are you scoring your model using `model.score(X_test, y_test)`?
- Are you rounding to 4 decimal places?
- Are you calculating `test_score` as  `round(model.score(X_test, y_test), 4)` )

</codeblock>

</exercise>

<exercise id="24" title="Support Vector Machines (SVMs) with RBF Kernel" type="slides,video">
<slides source="module4/module4_24" shot="2" start="35:1610" end="41:0523">
</slides>

</exercise>

<exercise id="25" title= "Testing your SVM RBF  Knowledge">

These two boundary plots were made using SVM with an RBF kernel and the other with K-Nearest Neighbours. 
<center><img src="/module4/Q25.png"  width = "90%" alt="404 image" /></center>

<br>

**Question 1**    
Which plot more likely visualizes the boundaries of the SVM model?

<choice id="1">

<opt text="Left">

Which plot has smoother boundaries?
 
</opt>

<opt text= "Right"  correct="true" >
 
Nice

</choice>


</exercise>

<exercise id="26" title="SVM True or False">

**True or False**      
_In Scikit Learn’s SVC classifier, large values of gamma tend to result in higher training score but probably lower validation score._

<choice id="1" >
<opt text="True" correct="true">

Great work!

</opt>

<opt text="False"  >

As we increase gamma, since our model is becoming more complex, our training score should increase. Since the model is more specific to the training data, the test score may decrease.

</opt>

</choice>

**True or False**     
_If we increase both `gamma` and `C`, we can't be certain if the model becomes more complex our less complex._

<choice id="2" >
<opt text="True"  >

Increasing both `C` and `gamma` makes the model more complex in both cases so the model will be increasing in complexity. 

</opt>

<opt text="False" correct="true" >

Great work. 

</opt>

</choice>

</exercise>

<exercise id="27" title='Predicting with an SVM Classifier'>

**Instructions:**    
Running a coding exercise for the first time could take a bit of time for everything to load.  Be patient, it could take a few minutes. 

**When you see `____` in a coding exercise, replace it with what you assume to be the correct code.  Run it and see if you obtain the desired output.  Submit your code to validate if you were correct.**

_**Make sure you remove the hash (`#`) symbol in the coding portions of this question.  We have commented them so that the line won't execute and you can test your code after each step.**_

We've used K-Nearest Neighbours to classify Pokémon from the Pokémon dataset so now let's try to do the same thing with an RBF kernel!

Tasks:     

- Create an `SVM` model with `gamma` equal to 0.1 and `C` equal to 10 then name the model `model`.
- Train your model on `X_train` and `y_train` (Hint: you may want to use `.to_numpy()`).
- Score your model on the training set using `.score()` and save it in an object named `train_score`.
- Score your model on the test set using `.score()` and save it in an object named `test_score`.

<codeblock id="04_27">

- Are you importing `SVM`?
- Are you using ` SVM(gamma=0.1, C=10)`?
- Are you using `model.fit(X_train, y_train.to_numpy())`?
- Are you using `model.score(X_train, y_train)` to find the training score?
- Are you using `model.score(X_test, y_test)` to find the test score?

</codeblock>

**Question**    
Does this model give similar results to 𝑘-NN?

<choice id="1" >
<opt text="Yes"  correct="true">

We got around .9 with 𝑘-NN as well!

</opt>

<opt text="No">

We got a score around 0.9 with 𝑘-NN .

</opt>x

</choice>

</exercise>

<exercise id="28" title="What Did We Just Learn?" type="slides, video">
<slides source="module4/module4_end" shot="0" start="09:3212" end="10:0720">
</slides>
</exercise>

