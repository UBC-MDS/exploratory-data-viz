---
type: slides
---

# Decision Tree Regressor

Notes: <br>

---

``` python
regression_df = pd.read_csv("data/quiz2-grade-toy-regression.csv")
regression_df
```

```out
   ml_experience  class_attendance  lab1  lab2  lab3  lab4  quiz1  quiz2
0              1                 1    92    93    84    91     92     90
1              1                 0    94    90    80    83     91     84
2              0                 0    78    85    83    80     80     82
3              0                 1    91    94    92    91     89     92
4              0                 1    77    83    90    92     85     90
5              1                 0    70    73    68    74     71     75
6              1                 0    80    88    89    88     91     91
```

Notes:

We saw previously that we can use decision trees for classification
problems but we can also use this decision tree algorithm for regression
problems.

We can also use the decision tree algorithm for regression problems.

Instead of using Gini (which we briefly mentioned this in previous
slides), we can use
<a href="https://scikit-learn.org/stable/modules/tree.html#mathematical-formulation" target="_blank">some
other criteria</a> for splitting. (A common one is mean squared error
(MSE) which we will discuss shortly)

`scikit-learn` supports regression using decision trees with
`DecisionTreeRegressor()` and the `.fit()` and `.predict()` paradigm
that is similar to classification.

Just like when we talked about the baseline Dummy regressor, `.score()`
for regression returns somethings called an
<a href="https://scikit-learn.org/stable/modules/generated/sklearn.metrics.r2_score.html#sklearn.metrics.r2_score" target="_blank">
𝑅2 </a>.

The maximum 𝑅2 is 1 for perfect predictions.

It can be negative which is very bad (worse than DummyRegressor).

---

``` python
X = regression_df.drop(columns=["quiz2"])
X.head()
```

```out
   ml_experience  class_attendance  lab1  lab2  lab3  lab4  quiz1
0              1                 1    92    93    84    91     92
1              1                 0    94    90    80    83     91
2              0                 0    78    85    83    80     80
3              0                 1    91    94    92    91     89
4              0                 1    77    83    90    92     85
```

``` python
y = regression_df["quiz2"]
y.head()
```

```out
0    90
1    84
2    82
3    92
4    90
Name: quiz2, dtype: int64
```

Notes:

Before we do anything, let’s bring in our regression data this time it’s
going to be the quiz2 dataset however instead of predicting quiz2 a
categorical variable (A+ or Not A+) we have continuous values instead.

We split our data into our `X` and `Y` objects as we’ve previously been
doing.

---

``` python
from sklearn.tree import DecisionTreeRegressor
```

``` python
depth = 4
reg_model = DecisionTreeRegressor(max_depth=depth)
reg_model.fit(X, y);
```

Notes:

**Decision Tree Regressor** is built using `DecisionTreeRegressor()` and
a similar `.fit()` and `.predict()` paradigms as classification.

Instead of importing `DecisionTreeClassifier`, we import
`DecisionTreeRegressor`.

We follow the same steps as before and can even set hyperparameters as
we did in classification.

Here when we build our model, we are specifying a `max_depth` of 4.

This means our decision tree is going to be constrained to a depth of 4.

---

<center>

<img src="/module2/module2_16a.png"  width = "68%" alt="404 image" />

</center>

Notes:

And here is the tree it produces.

We can see all the decision boundaries and splitting values.

Our leaves used to contain a categorical value for prediction, but this
time we see our leaves are predicting numerical values.

---

``` python
X.loc[[0]]
```

```out
   ml_experience  class_attendance  lab1  lab2  lab3  lab4  quiz1
0              1                 1    92    93    84    91     92
```

``` python
reg_model.predict(X.loc[[0]])
```

```out
array([90.])
```

Notes:

Here we take a single example.

This example has `class_attendance` and `ml_experience` equal to 1 and
then the numerical values for labs 1-4 and `quiz2`.

When we predict on this single example, we can see that our model
outputs a value of 90.

---

``` python
predicted_grades = reg_model.predict(X)
regression_df = regression_df.assign(predicted_quiz2 = predicted_grades)
print("R^2 score on the training data:" + str(round(reg_model.score(X,y), 3)))
```

```out
R^2 score on the training data:1.0
```

``` python
regression_df.head()
```

```out
   ml_experience  class_attendance  lab1  lab2  lab3  lab4  quiz1  quiz2  predicted_quiz2
0              1                 1    92    93    84    91     92     90             90.0
1              1                 0    94    90    80    83     91     84             84.0
2              0                 0    78    85    83    80     80     82             82.0
3              0                 1    91    94    92    91     89     92             92.0
4              0                 1    77    83    90    92     85     90             90.0
```

Notes:

Let’s see how well this model does predicting on the entire data.

Now we are using `.score()` on the entire data that we’ve trained on.

We can compare the predicted value versus the true quiz2 grade in this
dataframe and we see our model has predicted every example correctly.

This is confirmed when we see that the score is 1.0.

We talked in Module 1 about how we use a measurement called 𝑅2 to
measure the score of regression models. An 𝑅2 score of 1.0, means the
model perfectly predicts the outcome of every observation.

This is quite different from what we were getting with a Dummy
Classifier which had an 𝑅2 value of 0.

---

# Let’s apply what we learned\!

Notes: <br>
