---
type: slides
---

# Cross-validation

Notes: <br>

---

## Single split problems

<br> <br> <br>

<center>

<img src="/module3/train-valid-test-split.png"  width = "100%" alt="404 image" />

</center>

Notes:

We saw that it’s necessary to split our data into multiple different
sets/splits but is having a single train and validation split optimal?

The problem with having a single train/validation split is that now we
are using only a portion of our data for training and only a portion for
validation.

If our dataset is small we might end up with a tiny training and/or
validation set.

We might also be unlucky with our splits such that they don’t align well
or don’t well represent our test data.

It would be nice to have more data on which to train and validate.

---

## So what do we do?

### 𝑘-fold cross-validation

<center>

<img src="/module3/cross-validation.png"  width = "100%" alt="404 image" />

</center>

Notes:

Here we will introduce something called **cross-validation** or
***𝑘-fold cross-validation*** which attempts to get the best of both
worlds.

We still have the test set here at the bottom locked away that we will
not touch until the end.

Instead of splitting our training set and simply chopping it into train
and validation sets, we do something more complicated that allows us to
validate more accurately and not be over-reliant on the random dividing
into the training and validation sets.

Doing this could lead to us either being lucky or unlucky with the
splitting, causing extremely accurate or very poor scores.

Cross-validation consists of splitting the data into k-folds ( 𝑘\>2,
often 𝑘=10 ). In the picture below 𝑘=4.

Each “fold” gets a turn at being the validation set. And the other folds
are used as the training set.

Then we use a new fold as the validation set and the rest now become the
training set.

This is repeated until every fold has an opportunity to act as the
validation set.

Each round will produce a score so after 𝑘-fold cross-validation, it
will produce 𝑘 scores. We usually average over the 𝑘 results.

It’s better to notice the variation in the scores across folds.

We can get a more “robust” score on unseen data.

The main disadvantage here is that this as K increases the longer it
takes to run the code, which is a problem for bigger datasets / more
complex models.

---

## Cross-validation using scikit-learn

``` python
df = pd.read_csv("data/canada_usa_cities.csv")
X = df.drop(columns=["country"])
y = df["country"]
```

``` python
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=123)
```

Notes:

let’s bring in our Canadian/United States cities data and split it.

---

``` python
from sklearn.model_selection import cross_val_score

model = DecisionTreeClassifier(max_depth=4)
cv_score = cross_val_score(model, X_train, y_train, cv=5)
cv_score
```

```out
array([0.76470588, 0.82352941, 0.78787879, 0.78787879, 0.84848485])
```

Notes:

First, we import `cross_val_score` from `sklearn.model_selection` which
is gonna take care of the cross-validation for us.

Conveniently we don’t need to do the splitting into folds ourselves and
the functions we use from these libraries will help us with that.

We create our decision tree model.

We use `cross_val_score()` and specify the model and the training
features and target as arguments.

We also specify `cv` which determines the cross-validation splitting
strategy or how many “folds” there are.

Here we are saying there at 5 folds on the data.

For each fold, the model is fitted on the training portion and scores on
the validation portion.

The output of `cross_val_score()` is the validation score for each fold.

Typically an average of the scores can be taken to produce a single
measure of how the model is doing but it can be useful to look at the
individual scores to observe the variation among them.

If the scores are all quite different, that may make us question our
model more.

---

``` python
cv_scores = cross_val_score(model, X_train, y_train, cv=10)
cv_scores
```

```out
array([0.76470588, 0.82352941, 0.70588235, 0.94117647, 0.82352941, 0.82352941, 0.70588235, 0.9375    , 0.9375    , 0.9375    ])
```

``` python
cv_scores.mean()
```

```out
0.8400735294117647
```

Notes:

We can change the number of folds too. Now, when we change it to 10, we
get 10 different scores.

When we average these we get a mean score of 0.84.

---

``` python
from sklearn.model_selection import cross_validate
```

``` python
scores = cross_validate(model, X_train, y_train, cv=10, return_train_score=True)
scores
```

```out
{'fit_time': array([0.00230122, 0.00208592, 0.00180292, 0.00210714, 0.00196314, 0.001858  , 0.00211215, 0.00190091, 0.00172687, 0.00183606]), 'score_time': array([0.00177097, 0.00138998, 0.00141501, 0.00142288, 0.00138092, 0.00139499, 0.00138974, 0.00145197, 0.00130105, 0.00167704]), 'test_score': array([0.76470588, 0.82352941, 0.70588235, 0.94117647, 0.82352941, 0.82352941, 0.70588235, 0.9375    , 0.9375    , 0.9375    ]), 'train_score': array([0.91333333, 0.90666667, 0.90666667, 0.9       , 0.90666667, 0.91333333, 0.92      , 0.90066225, 0.90066225, 0.90066225])}
```

Notes:

We just talked about `cross_val_score()` which is the simpler
scikit-learn function for cross-validation.

`cross_validate()` is a more informative function for cross-validation.

Let us access training and validation scores.

We call `cross_validate()` with the argument `return_train_score` which
will output the training score as well as the other information.

The output of \``cross_validate()` is a dictionary so we change it to a
pandas dataframe to make it easier to read.

The 10 rows are the 10 folds of cross-validation.

The `test_score` column is the “validation score” which is the same
thing that is outputted from the `cross_val_score()` function.

The new training score is output since we set the argument
`return_train_score` to True and then we have the fit and score time it
takes to execute.

---

``` python
scores
```

```out
{'fit_time': array([0.00230122, 0.00208592, 0.00180292, 0.00210714, 0.00196314, 0.001858  , 0.00211215, 0.00190091, 0.00172687, 0.00183606]), 'score_time': array([0.00177097, 0.00138998, 0.00141501, 0.00142288, 0.00138092, 0.00139499, 0.00138974, 0.00145197, 0.00130105, 0.00167704]), 'test_score': array([0.76470588, 0.82352941, 0.70588235, 0.94117647, 0.82352941, 0.82352941, 0.70588235, 0.9375    , 0.9375    , 0.9375    ]), 'train_score': array([0.91333333, 0.90666667, 0.90666667, 0.9       , 0.90666667, 0.91333333, 0.92      , 0.90066225, 0.90066225, 0.90066225])}
```

``` python
pd.DataFrame(scores)
```

```out
   fit_time  score_time  test_score  train_score
0  0.002301    0.001771    0.764706     0.913333
1  0.002086    0.001390    0.823529     0.906667
2  0.001803    0.001415    0.705882     0.906667
3  0.002107    0.001423    0.941176     0.900000
4  0.001963    0.001381    0.823529     0.906667
5  0.001858    0.001395    0.823529     0.913333
6  0.002112    0.001390    0.705882     0.920000
7  0.001901    0.001452    0.937500     0.900662
8  0.001727    0.001301    0.937500     0.900662
9  0.001836    0.001677    0.937500     0.900662
```

Notes:

`scores` is returned as a dictionary but it’s much easier to understand
if we convert it to a dataframe.

---

``` python
pd.DataFrame(scores).mean()
```

```out
fit_time       0.001969
score_time     0.001459
test_score     0.840074
train_score    0.906865
dtype: float64
```

``` python
cross_val_score(model, X_train, y_train, cv=10).mean()
```

```out
0.8400735294117647
```

``` python
pd.DataFrame(scores).std()
```

```out
fit_time       0.000178
score_time     0.000146
test_score     0.094993
train_score    0.006822
dtype: float64
```

Notes:

We can calculate the mean cross-validation score by taking the mean of
the `test_score` column.

This is the same as taking the mean of the output from
`cross_val_score()`.

Normally we calculate the mean cross-validation score but sometimes it
would be useful to look at the range and standard deviation of the folds
as it helps assess how consistent the model is.

---

### Our typical supervised learning set up is as follows:

<br>

1.  Given training data with `X` and `y`.
2.  We split our data into `X_train, y_train, X_test, y_test`.
3.  Hyperparameter optimization using cross-validation on `X_train` and
    `y_train`.
4.  We assess the best model using `X_test` and `y_test`.
5.  The **test score** tells us how well our model generalizes.
6.  If the **test score** is reasonable, we deploy the model.

Notes:

This brings us to our standard set of steps or workflow for supervised
learning.

1.  We are given the dataset with our `X` and `y`.
2.  We split our data into our `X_train`, `y_train`, `X_test`,
    y\_test\`.
3.  We try different models and hyperparameter optimization.
4.  We then build the best model based on the results.
5.  When we have our favourite model, we assess our model with our
    `X_test`, y\_test\`.
6.  If we are happy with these scores, we deploy our model into
    practice.

---

# Let’s apply what we learned\!

Notes: <br>
