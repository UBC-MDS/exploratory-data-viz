---
title: "Module 6: Preprocessing Categorical Variables"
description:
  "This module will teach you different encoding methods for categorical variables (ordinal and one-hot encoding) and appropriately set them up. We will also introduce ColumnTransformer and CountVectorizer from the sklearn library and show you how to implement them."
prev: /module5
next: /module7
type: chapter
id: 6
---

<exercise id="0" title="Module Learning Outcomes"  type="slides, video">

<slides source="module6/module6_00" shot="0" start="11:4921" end="12:4509">
</slides>

</exercise>



<exercise id="1" title="Categorical Variables: Ordinal Encoding" type="slides,video">

<slides source="module6/module6_01" shot="3" start="00:002" end="94:51">
</slides>

</exercise>

<exercise id="2" title= "Categorical Variables">

```
           name    colour    location    seed   shape  sweetness   water-content  weight
0         apple       red     canada    True   round     True          84         100
1        banana    yellow     mexico   False    long     True          75         120
2    cantaloupe    orange      spain    True   round     True          90        1360
3  dragon-fruit   magenta      china    True   round    False          96         600
4    elderberry    purple    austria   False   round     True          80           5
5           fig    purple     turkey   False    oval    False          78          40
6         guava     green     mexico    True    oval     True          83         450
7   huckleberry      blue     canada    True   round     True          73           5
8          kiwi     brown      china    True   round     True          80          76
9         lemon    yellow     mexico   False    oval    False          83          65

```

**Question 1**    

What would be the unique values givent to th values in the column `location`, in we transformed it with ordinal encoding?

<choice id="1">

<opt text="<code>[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]</code>">

There are multiples of some of these values

</opt>

<opt text= "<code>[0, 1, 2, 3, 4, 5]</code>"  correct="true">
 
Nice!

</opt>

<opt text="<code>[1, 2, 3, 4, 5, 6]</code>">

Do we start labelling at 1?

</opt>

<opt text="<code>[0, 1, 2, 3, 4, 5, 6]</code>">

Do we have 7 unique values?

</opt>

</choice>


**Question 2**    

Does it make sense to be doing ordinal transformations on this column?

<choice id="2" >

<opt text="Yes" >

Is yellow more red than green?

</opt>

<opt text="No" correct="true">

Good work!

</opt>

</choice>

</exercise>

<exercise id="3" title="True or False: Ordinal Encoding">

**True or False?**     
Whenever we have categorical values, we should use ordinal encoding.

<choice id="1" >
<opt text="True" >

Do all categorical has an order to them? For example if we had fruit, is a kiwi closer to a banana than a strawberry?

</opt>

<opt text="False" correct="true">

Great!

</opt>

</choice>

**True or False**      
If we include categorical values in our feature table, `sklearn` will throw an error.

<choice id="2">
<opt text="True" correct="true" >

Nice work! 

</opt>

<opt text="False">

Do categorical variables make sense to `sklearn`?

</opt>

</choice >

</exercise>

<exercise id="4" title="">

**Instructions:**    
Running a coding exercise for the first time could take a bit of time for everything to load.  Be patient, it could take a few minutes. 

**When you see `____` in a coding exercise, replace it with what you assume to be the correct code.  Run it and see if you obtain the desired output.  Submit your code to validate if you were correct.**

_**Make sure you remove the hash (`#`) symbol in the coding portions of this question.  We have commented them so that the line won't execute and you can test your code after each step.**_


Tasks:     


<codeblock id="">

- Are you ...?

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

<exercise id="5" title="Categorical Variables: One-Hot Encoding" type="slides,video">

<slides source="module6/module6_05" shot="3" start="00:002" end="94:51">
</slides>

</exercise>


<exercise id="6" title= "One-Hot Encoding Questions">

**Question**     
If we one hot encoded the `shape` column, what datatype would be the output of after using `transform`?

<choice id="1">

<opt text="NumPy array" correct="true">

You got it!

</opt>

<opt text= " Pandas Dataframe" >
 
Do we get labels with the output?

</opt>

<opt text="Pandas Series" >

Are we getting multiple columns in the output?

</opt>

<opt text="Dictionary">

Not quite. 

</opt>

</choice>

</exercise>

<exercise id="7" title= "One-Hot Encoding - Output">

Refer to the dataframe to answer the following question.
```
           name   colour location   seed  shape  sweetness  water_content  weight
0         apple      red   canada   True  round       True             84     100
1        banana   yellow   mexico  False   long       True             75     120
2    cantaloupe   orange    spain   True  round       True             90    1360
3  dragon-fruit  magenta    china   True  round      False             96     600
4    elderberry   purple  austria  False  round       True             80       5
5           fig   purple   turkey  False   oval      False             78      40
6         guava    green   mexico   True   oval       True             83     450
7   huckleberry     blue   canada   True  round       True             73       5
8          kiwi    brown    china   True  round       True             80      76
9         lemon   yellow   mexico  False   oval      False             83      65
```

<br>

**Question**   
Which of the following outputs in the result of one-hot encoding the shape column?

A) 

```
array([[0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 1, 1, 0, 0, 1],
       [1, 0, 1, 1, 1, 0, 0, 1, 1, 0]])
```

B)

```
array([[0, 0, 1],
       [1, 0, 0],
       [0, 0, 1],
       [0, 0, 1],
       [0, 0, 1],
       [0, 1, 0],
       [0, 1, 0],
       [0, 0, 1],
       [0, 0, 1],
       [0, 1, 0]])
```

C)

```
array([[0, 1, 0, 0, 0, 0],
       [0, 0, 0, 1, 0, 0],
       [0, 0, 0, 0, 1, 0],
       [0, 0, 1, 0, 0, 0],
       [1, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 1],
       [0, 0, 0, 1, 0, 0],
       [0, 1, 0, 0, 0, 0],
       [0, 0, 1, 0, 0, 0],
       [0, 0, 0, 1, 0, 0]])
```

D) 

```
array([[0],
       [5],
       [0],
       [3],
       [0],
       [0],
       [3],
       [0],
       [5],
       [3],
       [1],
       [4],
       [3],
       [2]])

```


<choice id="1" >

<opt text="A"  >

Are you sure it's the correct dimensions?

</opt>

<opt text="B" correct="true">

Great!

</opt>

<opt text="C">

How many unique values are there in the column `seed` 

</opt>

<opt text="D">

This is a single column. Are you sure that's what you want?

</opt>

</choice>

</exercise>

<exercise id="8" title="One Hot encoding True or False">

**True or False**     
_One-hot encoding a column with 5 unique categories will produce 5 new transformed columns._

<choice id="1" >
<opt text="True"  correct="true">

Yes! We are transforming the data into new columns!

</opt>

<opt text="False" >

How is our data transforming?

</opt>

</choice>

**True or False**     
_The unique values in the new transformed columns after one-hot encoding because all possible integer or float values. ._

<choice id="2" >
<opt text="True"  >

How many options are there for each columns? Does it become a binary value now?

</opt>

<opt text="False" correct="true">

Great! The values become binary and only two possible values are in the columns now; 0, or 1. 

</opt>

</choice>

</exercise>

<exercise id="9" title='You Try It: One Hot Encoding'>

**Instructions:**    
Running a coding exercise for the first time could take a bit of time for everything to load.  Be patient, it could take a few minutes. 

**When you see `____` in a coding exercise, replace it with what you assume to be the correct code.  Run it and see if you obtain the desired output.  Submit your code to validate if you were correct.**

_**Make sure you remove the hash (`#`) symbol in the coding portions of this question.  We have commented them so that the line won't execute and you can test your code after each step.**_

Let's take a look at a modified version of our basketball player dataset.  

First, let's take a look at if and/or where we are missing any values.

Tasks:     

- Use `.describe()` or `.info()` to find if there are any values missing from the dataset. 
- Using some of the skills we learned in the previous <a href="https://prog-learn.mds.ubc.ca/en/module8" target="_blank">course</a> find the number of rows that contains missing values and save the total number of examples with missing values in an object named `num_nan`.       
*Hint: `.any(axis=1)` may come in handy here.* 

<codeblock id="05_09">

- Are you using `X_train.info()`?
- Are you using `X_train.isnull().any(axis=1).sum()`?

</codeblock>


Now that we've identified the columns with missing values, let's use `SimpleImputer` to replace the missing value. 

Tasks:     
- Import the necessary library.
- Using `SimpleImputer`, replace the null values in the training and testing dataset with the median value in each column.
- Save your transformed data in objects named `train_X_imp` and `test_X_imp` respectively. 
- Transform `X_train_imp` into a dataframe using the column and index labels from `X_train` and save it as `X_train_imp_df`.
- Check if `X_train_imp_df`  still has missing values.


</exercise>


<exercise id="10" title="ColumnTransformer" type="slides,video">

<slides source="module6/module6_10" shot="3" start="00:002" end="94:51">
</slides>

</exercise>

<exercise id="11" title= "Transforming Columns with ColumnTransformer">


Refer to the dataframe to answer the following question.
```
       colour   location   seed    shape   sweetness  water_content  weight
0       red      canada    True              True          84         100
1     yellow     mexico    False   long      True          75         120
2     orange     spain     True              True          90           
3    magenta     china     True    round     False                    600
4     purple    austria    False             True          80         115
5     purple    turkey     False   oval      False         78         340
6     green     mexico     True    oval      True          83           
7      blue     canada     True    round     True          73         535
8     brown     china      True              True                    1743  
9     yellow    mexico     False   oval      False         83         265
```

<br>

**Question 1**   
How many categorical columns are there and how many numeric?

 

<choice id="1" >

<opt text="5 categoric columns and 3 numeric columns"  >

Are you sure it's the correct dimensions?

</opt>

<opt text="3 categoric columns and 5 numeric columns" >



</opt>

<opt text="5 categoric columns and 2 numeric columns" correct="true">

Great!

</opt>

<opt text="3 categoric columns and 4 numeric columns">

This is a single column. Are you sure that's what you want?

</opt>

</choice>


**Question 2**   
What transformations are being done to both numeric and categorical columns?

<choice id="2" >

<opt text="Scaling"  >

This is used on numeric columns.

</opt>

<opt text="Imputation" correct="true">

Great!

</opt>

<opt text="One-hot encoding">

This is only used on categorical columns.

</opt>

<opt text="Pipeline">

Pipeline isn't a transformer.

</opt>

</choice>

</exercise>

<exercise id="12" title="Transforming True or False">

**True or False**     
_If there are missing values in both numeric and categorical columns we can specify this in a single step in the main pipeline._

<choice id="1" >
<opt text="True"  >

We specify the transformation in each column type pipeline before we use them as inputs for `ColumnTransformer`. 

</opt>

<opt text="False" correct="true">

Nailed it!

</opt>

</choice>

**True or False**     
_If we do not specify `remainder="passthrough"` as an argument in `ColumnTransformer`, the columns not being transformed will be dropped ._

<choice id="2" >
<opt text="True"  correct="true">

You got it! Without this, any columns left alone will be removed from your features. 

</opt>

<opt text="False" >

Are you certain? Slide 7 has some information regarding this. 
</opt>

</choice>

</exercise>


<exercise id="13" title='You Try It: One Hot Encoding'>

**Instructions:**    
Running a coding exercise for the first time could take a bit of time for everything to load.  Be patient, it could take a few minutes. 

**When you see `____` in a coding exercise, replace it with what you assume to be the correct code.  Run it and see if you obtain the desired output.  Submit your code to validate if you were correct.**

_**Make sure you remove the hash (`#`) symbol in the coding portions of this question.  We have commented them so that the line won't execute and you can test your code after each step.**_

Let's take a look at a modified version of our basketball player dataset.  

First, let's take a look at if and/or where we are missing any values.

Tasks:     

- Use `.describe()` or `.info()` to find if there are any values missing from the dataset. 
- Using some of the skills we learned in the previous <a href="https://prog-learn.mds.ubc.ca/en/module8" target="_blank">course</a> find the number of rows that contains missing values and save the total number of examples with missing values in an object named `num_nan`.       
*Hint: `.any(axis=1)` may come in handy here.* 

<codeblock id="05_13">

- Are you using `X_train.info()`?
- Are you using `X_train.isnull().any(axis=1).sum()`?

</codeblock>


Now that we've identified the columns with missing values, let's use `SimpleImputer` to replace the missing value. 

Tasks:     
- Import the necessary library.
- Using `SimpleImputer`, replace the null values in the training and testing dataset with the median value in each column.
- Save your transformed data in objects named `train_X_imp` and `test_X_imp` respectively. 
- Transform `X_train_imp` into a dataframe using the column and index labels from `X_train` and save it as `X_train_imp_df`.
- Check if `X_train_imp_df`  still has missing values.


</exercise>


<exercise id="14" title="Make - Pipelines & Column Transformers" type="slides,video">

<slides source="module6/module6_14" shot="3" start="00:002" end="94:51">
</slides>

</exercise>


<exercise id="15" title= "Making pipelines">

Use the diagm below to answer the following questions.

```
Pipeline(steps=[('columntransformer',
                 ColumnTransformer(transformers=[('pipeline-1',
                                                  Pipeline(steps=[('simpleimputer',
                                                                   SimpleImputer(strategy='median')),
                                                                  ('standardscaler',
                                                                   StandardScaler())]),
                                                  ['water_content', 'weight',
                                                   'carbs']),
                                                 ('pipeline-2',
                                                  Pipeline(steps=[('simpleimputer',
                                                                   SimpleImputer(fill_value='missing',
                                                                                 strategy='constant')),
                                                                  ('onehotencoder',
                                                                   OneHotEncoder(handle_unknown='ignore'))]),
                                                  ['colour', 'location', 'seed',
                                                   'shape', 'sweetness',
                                                   'tropical'])])),
                ('decisiontreeclassifier', DecisionTreeClassifier())])
                
```  

**Question 1**   
How many columns are being transformed in the first pipeline?
 

<choice id="1" >

<opt text="0"  >

Are you counting the right thing? Look above `pipeline-2`.

</opt>

<opt text="2" >


Are you counting the right thing? Look above `pipeline-2`.

</opt>

<opt text="3" correct="true">

Great! They are ` ['water_content', 'weight', 'carbs']

</opt>

<opt text="6">

Are you counting the columns for `pipeline-2` by accident?

</opt>

</choice>


**Question 2**   
Which pipeline is transforming the categorical columns?

<choice id="2" >

<opt text="pipeline-1"  >

This is using `StandardScaler` so it is likely transforming numeric columns. Also pipeline-2 is using `OneHotEncoder`.

</opt>

<opt text="pipeline-2" correct="true">

Great!

</opt>

</choice>



**Question 3**   
What model is the pipeline fitting on?

<choice id="3" >

<opt text="<code>SVC</code>"  >

This is used on numeric columns.

</opt>

<opt text="<code>KNeighborsClassifier</code>" >



</opt>

<opt text="<code>DummyClassifier</code>">

This is only used on categorical columns.

</opt>

<opt text="<code>DecisionTreeClassifier</code>" correct="true">

Great!

</opt>

</choice>

</exercise>

<exercise id="16" title="Transforming True or False">

**True or False**     
_`Pipeline()` is the same as `make_pipeline()` but  `make_pipeline()` requires you to name the steps._

<choice id="1" >
<opt text="True"  >

`Pipeline()` requires you to name the steps whereas `make_pipeline()` does not. 

</opt>

<opt text="False" correct="true">

Nailed it! It's the other way round! `Pipeline()` requires you to name the steps. 

</opt>

</choice>

**True or False**     
_`make_pipeline()` can be called before `make_column_transformer`._

<choice id="2" >
<opt text="True"  correct="true">

Nice work!

</opt>

<opt text="False" >

We can first make seperate transformation pipelines for our different columns and then we can use `make_column_transformer`. 

</opt>

</choice>

</exercise>


<exercise id="17" title='You Try It: One Hot Encoding'>

**Instructions:**    
Running a coding exercise for the first time could take a bit of time for everything to load.  Be patient, it could take a few minutes. 

**When you see `____` in a coding exercise, replace it with what you assume to be the correct code.  Run it and see if you obtain the desired output.  Submit your code to validate if you were correct.**

_**Make sure you remove the hash (`#`) symbol in the coding portions of this question.  We have commented them so that the line won't execute and you can test your code after each step.**_

Let's take a look at a modified version of our basketball player dataset.  

First, let's take a look at if and/or where we are missing any values.

Tasks:     

- Use `.describe()` or `.info()` to find if there are any values missing from the dataset. 
- Using some of the skills we learned in the previous <a href="https://prog-learn.mds.ubc.ca/en/module8" target="_blank">course</a> find the number of rows that contains missing values and save the total number of examples with missing values in an object named `num_nan`.       
*Hint: `.any(axis=1)` may come in handy here.* 

<codeblock id="05_13">

- Are you using `X_train.info()`?
- Are you using `X_train.isnull().any(axis=1).sum()`?

</codeblock>


Now that we've identified the columns with missing values, let's use `SimpleImputer` to replace the missing value. 

Tasks:     
- Import the necessary library.
- Using `SimpleImputer`, replace the null values in the training and testing dataset with the median value in each column.
- Save your transformed data in objects named `train_X_imp` and `test_X_imp` respectively. 
- Transform `X_train_imp` into a dataframe using the column and index labels from `X_train` and save it as `X_train_imp_df`.
- Check if `X_train_imp_df`  still has missing values.


</exercise>



<exercise id="18" title="Handeling Categorical Features: Binary, Ordinal and more" type="slides,video">

<slides source="module6/module6_18" shot="3" start="00:002" end="94:51">
</slides>

</exercise>





<exercise id="22" title="Text Data" type="slides,video">

<slides source="module6/module6_22" shot="3" start="00:002" end="94:51">
</slides>

</exercise>




<exercise id="30" title="What Did We Just Learn?" type="slides, video">
<slides source="module6/module6_end" shot="0" start="12:4510" end="13:2010">
</slides>