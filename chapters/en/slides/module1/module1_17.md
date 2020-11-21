---
type: slides
---

# Dummy Regression

Notes:

Let’s build a baseline model for our regression problem.

---

### Building a baseline regression model

<br> <br> <br> Baseline model:

**Averge target value**: always predicts the mean of the training set.

Notes:

Let’s build a ***baseline*** simple machine learning algorithm based on
simple rules of thumb.

For a regression problem, we are going to build a baseline model that
always predicts the mean target value in the training set.

---

## Data

``` python
classification_df = pd.read_csv("data/quiz2-grade-toy-regression.csv")
classification_df.head()
```

```out
   ml_experience  class_attendance  lab1  lab2  lab3  lab4  quiz1  quiz2
0              1                 1    92    93    84    91     92     90
1              1                 0    94    90    80    83     91     84
2              0                 0    78    85    83    80     80     82
3              0                 1    91    94    92    91     89     92
4              0                 1    77    83    90    92     85     90
```

Notes:

To demonstrate this we are going to bring in our toy regression dataset.

As a reminder, the task here is to protect our `quiz2` score.

---

## 1\. Create 𝑋 and 𝑦

𝑋 → Feature vectors <br> 𝑦 → Target

``` python
X = classification_df.drop(columns=["quiz2"])
y = classification_df["quiz2"]
```

Notes:

Just like before, we separate our data into the feature table and the
target, also known as 𝑋 and 𝑦.

---

## 2\. Create a regressor object

  - `import` the appropriate regressor, in this case, `DummyRegressor`.
  - Create an object of the regressor.

<!-- end list -->

``` python
from sklearn.dummy import DummyRegressor

dummy_reg = DummyRegressor(strategy="mean")
```

Notes:

Next, we create our regressor object.

This time instead of importing `DummyClassifier()`, we import
`DummyRegessor` which will be used to create our baseline regression
model.

We specify in the `strategy` argument `mean`. With this strategy, the
model will predict the mean target value in the training data.

Here we are naming our model `dummy_reg`.

---

## 3\. Fit the regressor

``` python
dummy_reg.fit(X, y)
```

Notes:

The next step is fitting our regressor.

As usual, we call fit on our dummy regressor and we pass `X` and `y`
into `fit()`.

Our dummy regressor is a very simple model and all it is going to learn
here is the mean prediction from the training data.

---

## 4\. Predict the target of given examples

We can predict the mean of examples by calling `predict` on the
classifier object.

``` python
single_obs = X.loc[[2]]
single_obs
```

```out
   ml_experience  class_attendance  lab1  lab2  lab3  lab4  quiz1
2              0                 0    78    85    83    80     80
```

``` python
dummy_reg.predict(single_obs)
```

```out
array([86.28571429])
```

Notes:

Now that we have trained our regressor, we can use it to predict targets
for new examples.

First, let’s try to predict the target value for a single observation.

When we call `predict` on `dummy_reg` with this observation. We get a
prediction of 86.285.

---

``` python
X
```

```out
   ml_experience  class_attendance  lab1  lab2  lab3  lab4  quiz1
0              1                 1    92    93    84    91     92
1              1                 0    94    90    80    83     91
2              0                 0    78    85    83    80     80
3              0                 1    91    94    92    91     89
4              0                 1    77    83    90    92     85
5              1                 0    70    73    68    74     71
6              1                 0    80    88    89    88     91
```

``` python
dummy_reg.predict(X)
```

```out
array([86.28571429, 86.28571429, 86.28571429, 86.28571429, 86.28571429, 86.28571429, 86.28571429])
```

Notes:

We can predict on the full dataset `X` and when we do so, we get the
value of 86.285 for every example. This makes sense because the
prediction is the mean of the target column.

---

## 5\. Scoring your model

In the regression setting, `.score()` gives the R^2 of the model,
i.e. the coefficient of determination of the prediction.

``` python
print("The accuracy of the model on the training data:", (dummy_reg.score(X, y)).round(3))
```

```out
The accuracy of the model on the training data: 0.0
```

Notes:

Now let’s try to assess our model.

In the case of regression, `score` gives something called an R^2 to
assess our model.

We will not be going into that much detail on it now but the best
possible score for any model is 1.0 and for dummy classifiers, it is
around 0.

This can also be a negative (because the model can be arbitrarily worse)

---

# Let’s apply what we learned\!

Notes: <br>
