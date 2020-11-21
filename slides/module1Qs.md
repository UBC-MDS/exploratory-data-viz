

<exercise id="12" title="Fit or Predict">

**Do the following statements correspond to the `fit` or the `predict` function:**  

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
_At least for decision trees, this is where most of the hard work is done._

<choice id="2">
<opt text="Fit" correct="true">

Great job! Training is more intensive then predicting for decision trees. 

</opt>

<opt text="Predict" >

Where do we teach the model? 

</opt>
</choice>

**Statement:**   
_Only takes `X` as an argument._

<choice id="3">
<opt text="Fit">

We need to make sure we give the model the correct labels so it can _learn_. 

</opt>

<opt text="Predict" correct="true">

Great job!

</opt>
</choice>

**Statement:**  
_In scikit-learn, we can ignore its output._

<choice id="4">
<opt text="Fit" correct="true">
 
Great job!

</opt>

<opt text="Predict">

You may want to look at the slides and see what each function delivers as an output. 

</opt>
</choice>
</exercise>

<exercise id="13" title="Building Your Model">

Let's try training and prediction our own model. 

**Instructions:**

When you run a code exercise for the first time, it could take a bit of time for everything to load. 

**When you see `____` in a code exercise, replace it with what you assume to be the correct code. Run it and see if it you obtain the desired output. Submit your code to validate if you were correct.**

<codeblock id="01_13">

- Make sure you are using the correct functions 
- Are you using the model named `model`?

</codeblock>
</exercise>

<exercise id="14" title="Decision Tree Splitting Rules" type="slides">
<slides source="module1/module1_14">
</slides>
</exercise>

<exercise id="15" title="Calculating Gini Impurity">

Let's try calculating the Gini impurity  on our candybar dataset using the same `gini2` function from the module slides. The function has been imported for you. 

Let's make the split on the feature `peanuts` where anything greater than 0.5 is classified as `American`. Remember that you now have 2 groups and you need to calculate the impurity for both groups.  

* Don't forget to take into consideration the porportion of observations in each group!

**Instructions:**

When you run a code exercise for the first time, it could take a bit of time for everything to load. 

**When you see `____` in a code exercise, replace it with what you assume to be the correct code. Run it and see if it you obtain the desired output. Submit your code to validate if you were correct.**

The packages you need will be loaded for you. 
Save your Gini impurity as object `peanut_gini_impurity`

<codeblock id="01_15">

- Are you taking into consideration there are 2 gini calculations ( you will have to call `gini2 ` twice)?
- There are 6 observations of the 16 that have `peanuts` >= 0.5. Of those, 5 are of class `America` and 1 is of class `Canada`. 
- There are 10 observations of the 16 that have `peanuts` < 0.5. Of, those 3 are of class `America` and 7 is of class `Canada`.


</codeblock>
</exercise>

<exercise id="16" title="ML Model Parameters and Hyperparameters " type="slides">
<slides source="module1/module1_14">
</slides>
</exercise>


<exercise id="17" title= "Decision Tree - Trees">

**Question:**   
What is the maximum number of children a decision tree can have in a decision tree classifier?

<choice id="1">
<opt text= "1" >
 
Is this a decision then? 

</opt>

<opt text="2" correct="true">

Nice work!

</opt>

<opt text="There is no maximum">

Think about at each node, what are the posibilities?

</opt>

<opt text="0">

A node on decision tree needs can have 0 children but that's not the maximum. 

</opt>

</choice>

</exercise>

<exercise id="18" title= "Feature Split Selection">

Who choses the features that are split on at each node?

<choice id="1">
<opt text= "Data Scientist" >
 
Where would we input this information?  

</opt>

<opt text="Model" correct="true">

Great!

</opt>

</choice>

</exercise>

<exercise id="19" title= "Decision Stumps">

**Question:**   
What is the depth of a decision stump? 

<choice id="1">
<opt text= "1" correct="true">
 
You have been paying attention! Nice work! 

</opt>

<opt text="5" >

This is the default max depth of the decision tree classifier not the depth of a decision stump.

</opt>

<opt text="Whatever you set it as" >

Decision stumps are what make up a decision tree, stumps are not a hyperparameter

</opt>
</choice>
</exercise>

<exercise id="20" title= "Decision Tree True and False">

**Are the following Statements True or False**:

**Statement**    
_The standard decision tree algorithm finds the optimal tree given a data set._

<choice id="1">
<opt text= "True" >
 
For each node the model finds the optimal feature to split on but the nodes are chosen sequentially and it cannot choose the overall optimal tree. 

</opt>

<opt text="False" correct="true">

Great! Just because the model chooses the best feature to split on each node does not mean the total tree is the optimal one! 

</opt>

</choice>

**Statement:**     
_The same feature can be split on multiple times in a tree with depth > 1._

<choice id="2">
<opt text= "True" correct="true">
 
Super! There can be multiple threshold splits used for the same feature. 

</opt>

<opt text="False" >

There can be multiple threshold splits used for the same feature. 

</opt>

</choice>
</exercise>