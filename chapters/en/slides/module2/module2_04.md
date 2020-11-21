---
type: slides
---

# Decision Tree Classifiers

Notes: <br>

---

<center>

<img src="/module2/lingo_tree.png"  width = "100%" alt="404 image">

</center>

Notes:

Now we know the structure of decision trees, let’s build a decision tree
models, specifically a classifier.

We can use the exact same steps we did with our dummy classifier model
to build decision tree models with Scikit learn.

---

``` python
from sklearn.tree import DecisionTreeClassifier
```

``` python
model = DecisionTreeClassifier()
```

``` python
new_example
```

```out
   ml_experience  class_attendance  lab1  lab2  lab3  lab4  quiz1
0              1                 0     1     1     0     0      0
```

``` python
model.predict(new_example)
```

``` out
NotFittedError: This DecisionTreeClassifier instance is not fitted yet. Call 'fit' with appropriate arguments before using this estimator.

Detailed traceback: 
  File "<string>", line 1, in <module>
  File "/usr/local/lib/python3.8/site-packages/sklearn/tree/_classes.py", line 426, in predict
    check_is_fitted(self)
  File "/usr/local/lib/python3.8/site-packages/sklearn/utils/validation.py", line 72, in inner_f
    return f(**kwargs)
  File "/usr/local/lib/python3.8/site-packages/sklearn/utils/validation.py", line 1019, in check_is_fitted
    raise NotFittedError(msg % {'name': type(estimator).__name__})
```

Notes:

We can use the same steps we used when building a baseline model, to
build a decision tree model with `scikit-learn`.

Recall that `scikit-learn` uses the term `fit` for training or learning
and uses `predict` for prediction.

We must import the function from the `sklearn.tree` library and then we
can create a decision tree using the `DecisionTreeClassifier()`
function.

Is our new model ready to predict now that we have made our decision
tree model?

Let’s see what happens when we try to predict the quiz2 mark of a new
example.

We get an error\! We forgot the crucial step of fitting our model.

---

``` python
X_binary.head()
```

```out
   ml_experience  class_attendance  lab1  lab2  lab3  lab4  quiz1
0              1                 1     1     1     0     1      1
1              1                 0     1     1     0     0      1
2              0                 0     0     0     0     0      0
3              0                 1     1     1     1     1      0
4              0                 1     0     0     1     1      0
```

``` python
y.head()
```

```out
0        A+
1    not A+
2    not A+
3        A+
4        A+
Name: quiz2, dtype: object
```

``` python
model.fit(X_binary, y);
```

Notes:

We need to make sure that we `fit` our model before we `predict`. In the
decision tree algorithm, the fitting stage is where the model learns
about the data and sets the if-else statements.

Here are the features saved in an object named `X_binary` and our target
labels is `y`. Now we can `fit` our model.

---

<center>

<img src="/module2/dt_quiz2.png"  width = "70%" alt="404 image" />

</center>

Notes:

Let’s take a look at what our tree looks like.

We can see all the nodes of the tree and what the root condition is.

In this case, our root condition is whether or not `lab4` is greater or
equal to 0.5.

Since we are using binary data, if `lab4` equals 0 for an example, then
it’s going to be going down the left branch and if it equal `1` it will
go down the right branch.

---

``` python
new_example
```

```out
   ml_experience  class_attendance  lab1  lab2  lab3  lab4  quiz1
0              1                 0     1     1     0     0      0
```

<center>

<img src="/module2/dt_quiz2.png"  width = "50%" alt="404 image" />

</center>

Notes:

Using this tree, and the rules it’s set, let’s try and predict the
outcome of the example `new_example`.

Starting with `lab4` we can go down the left branch since it has a value
of 0 and the condition is true.`class_attendence` equals 0 so again we
go down the left branch.

`lab3` and `quiz1` are also both 0 and so we take the left branch at
each of these nodes leaving us at a leave with a prediction value of
‘Not A+\`.

---

``` python
(model.predict(new_example)[0])
```

```out
'not A+'
```

``` python
model.score(X_binary, y)
```

```out
0.9047619047619048
```

Notes:

We can check how accurate our model is using `.score()`.

This model predicts on data it’s already seen with 90% accuracy.

---

### How does predict work?

``` python
observation
```

```out
   ml_experience  class_attendance  lab1  lab2  lab3  lab4  quiz1
0              1                 0     1     1     0     1      1
```

<center>

<img src="/module2/predict2_slow.gif"  width = "70%" alt="404 image" />

</center>

Notes:

Let’s try again with a new tree and the animation below.

Let’s start at the top of the tree and ask binary questions at each node
and follow the appropriate path in the tree.

Here we go down the right branch from the root of the tree since
`class_attendence` does not equal 1, next we take the left branch at the
next node since `quiz1==1` is true and that drops us off at the leaf
where the model would predict `quiz2` to be an A+.

The model only considers the features which are in the learned tree and
ignores all other features.

---

### How does fit work

  - Which features are most useful for classification?
  - Minimize **impurity** at each question/node
  - Common criteria to minimize impurity
      - Gini Index
      - Information gain
      - Cross entropy

Notes:

We aren’t going to go into this in much detail, but the fitting of a
decision tree has a lot to do with important features (which columns
contribute the most to the decision-making process) and minimizing the
“impurity”.

We don’t need to worry about this for this course.

---

# Let’s apply what we learned\!

Notes: <br>
