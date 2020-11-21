---
type: slides
---

# Case Study: Pipelines

Notes: <br>

---

``` python
X_train_scaled.head()
```

```out
       longitude  latitude  housing_median_age  households  median_income  rooms_per_household  bedrooms_per_household  population_per_household
6051    0.908140 -0.743917           -0.526078    0.266135      -0.389736            -0.210591               -0.083813                  0.126398
20113  -0.002057  1.083123           -0.923283   -1.253312      -0.198924             4.726412               11.166631                 -0.050132
14289   1.218207 -1.352930            1.380504    0.542873      -0.635239            -0.273606               -0.025391                 -0.099240
13665   1.128188 -0.753286           -0.843842   -0.561467       0.714077             0.122307               -0.280310                  0.010183
14471   1.168196 -1.287344           -0.843842    2.500924      -1.059242            -0.640266               -0.190617                  0.126808
```

``` python
knn = KNeighborsRegressor()
knn.fit(X_train_scaled, y_train);
knn.score(X_train_scaled, y_train).round(3)
```

```out
0.798
```

Notes:

We left off with our scaled data and calculated our training score,
however in the last module we saw that cross-validation is a useful way
to get a realistic assessment of the model.

We don’t want to keep touching our test set like we have been doing, so
we really should be using cross-validation instead.

---

### How to carry out cross-validation?

``` python
knn = KNeighborsRegressor()
scores = cross_validate(knn, X_train_scaled, y_train, return_train_score=True)
pd.DataFrame(scores)
```

```out
   fit_time  score_time  test_score  train_score
0  0.008486    0.182278    0.696373     0.794236
1  0.008094    0.158972    0.684447     0.791467
2  0.008470    0.220749    0.695532     0.789436
3  0.008501    0.201372    0.679478     0.793243
4  0.009286    0.122095    0.680657     0.794820
```

Notes:

Let’s try cross-validation with transformed data.

**Is there a problem here?**

We are using our `X_train_scaled` in our `cross_validate()` function
which already has all our preprocessing done.

Let’s bring back the golden rule where ***Our test data should not
influence our training data*** and this applies also to our validation
data and that it also should not influence our training data.

Our first instinct to develop good habits is to split our data first
however when we use the `cross_validate()` function, since we are
scaling first and then splitting into training and validation,
information from our validation data is influencing our training data
now.

With imputation and scaling, we are scaling and imputing values based on
all the information in the data meaning the training data AND the
validation data and so we are not adhering to the golden rule anymore.

Every row in our `x_train_scaled` has now been influenced in a minor way
by every other row in `x_train_scaled`.

With scaling every row has been transformed based on all the data before
splitting between training and validation.

Here we said that we allowed information from the validation set to
**leak** into the training step.

We need to take care that we are keeping our validation data truly as
unseen data.

Before we look at the right approach to this, it’s important to look at
the wrong approaches and understand why we cannot perform
cross-validation in such ways.

---

### Bad methodology 1: Scaling the data separately

``` python
scaler = StandardScaler();
scaler.fit(X_train_imp);
X_train_scaled = scaler.transform(X_train_imp)
```

``` python
# Creating a separate object for scaling test data - Not a good idea.
scaler = StandardScaler();
scaler.fit(X_test_imp); # Calling fit on the test data - Yikes! 
```

```out
StandardScaler()
```

``` python
X_test_scaled = scaler.transform(X_test_imp) # Transforming the test data using the scaler fit on test data ... Bad! 
```

``` python
knn = KNeighborsRegressor()
knn.fit(X_train_scaled, y_train);
print("Training score: ", knn.score(X_train_scaled, y_train).round(2))
```

```out
Training score:  0.8
```

``` python
print("Test score: ", knn.score(X_test_scaled, y_test).round(2))
```

```out
Test score:  0.7
```

Notes:

The first mistake that often occurs is as follows.

We make our transformer, we fit it on the training data and then
transform the training data.

Next, we make a second transformer, fit it on the test data and then
transform our test data.

***What is wrong with this approach?***

Although we are keeping our test data separate from our training data,
by scaling the train and test splits separately, we are using two
different `StandardScaler` objects.

This is bad because we want to apply the same transformation on the
training and test splits.

The test data will have different values than the training data
producing a different transformation than the training data.

In summary, we should never fit on test data, whether it’s to build a
model or with a transforming, test data should never be exposed to the
`fit` function.

---

### Bad methodology 2: Scaling the data together

``` python
X_train_imp.shape, X_test_imp.shape
```

```out
((18576, 8), (2064, 8))
```

``` python
# Join the train and test sets back together
X_train_imp_df = pd.DataFrame(X_train_imp,columns=X_train.columns, index=X_train.index)
X_test_imp_df = pd.DataFrame(X_test_imp,columns=X_test.columns, index=X_test.index)
XX = pd.concat([X_train_imp_df, X_test_imp_df], axis = 0) ## Don't do it! 
XX.shape 
```

```out
(20640, 8)
```

``` python
scaler = StandardScaler()
scaler.fit(XX);
XX_scaled = scaler.transform(XX) 
XX_train, XX_test = XX_scaled[:18576], XX_scaled[18576:]
```

Notes:

The next mistake is when we scale the data together. So instead of
splitting our data, we are combining our training and testing and
scaling it together.

***What is wrong with this second approach?***

Here we are scaling the train and test splits together.

The golden rule says that the test data shouldn’t influence the training
in any way.

With this approach, we are using the information from the test split
when we `fit` the scalar and calculate the mean.

This means that the test data is being used when setting up the
transformations so, it’s **in violation** of the golden rule.

---

``` python
knn = KNeighborsRegressor()
knn.fit(XX_train, y_train);
print('Train score: ', (knn.score(XX_train, y_train).round(2))) # Misleading score
```

```out
Train score:  0.8
```

``` python
print('Test score: ', (knn.score(XX_test, y_test).round(2))) # Misleading score
```

```out
Test score:  0.71
```

Notes:

These values are showing misleading scores because of this bad approach.

---

<br> <br>

### So, what can we do?

We can create a
<a href="ttps://scikit-learn.org/stable/modules/generated/sklearn.pipeline.Pipeline.html" target="_blank">scikit-learn
Pipeline</a>\!

Pipelines allow us to define a “pipeline” of transformers with a final
estimator.

Notes:

To get around these issues, we introduce a new tool called
**pipelines**.

---

## Let’s see it in action

``` python
from sklearn.pipeline import Pipeline
```

``` python
pipe = Pipeline([
        ("imputer", SimpleImputer(strategy="median")),
        ("scaler", StandardScaler()),
        ("reg", KNeighborsRegressor())
])
```

Notes:

A **pipeline** is a sklearn function that contains a sequence of steps.

Essentially we give it all the actions we want to do with our data such
as transformers and models and the pipeline will execute them in steps.

In this example, we instruct the pipeline to first do imputation using
`SimpleImputer()` using a strategy of “median”, next to scale our data
using `StandardScaler` and then build a `KNeighborsRegressor`.

The last step should be a **model/classifier/regressor**.

All the earlier steps should be **transformers**.

This will help obey the golden rule.

---

``` python
pipe.fit(X_train, y_train)
```

```out
Pipeline(steps=[('imputer', SimpleImputer(strategy='median')),
                ('scaler', StandardScaler()), ('reg', KNeighborsRegressor())])
```

What’s happening:

``` python
imputer.fit(X_train)
X_train_imp = imputer.transform(X_train)
scaler.fit(X_train_imp)
X_train_imp_scaled = scaler.transform(X_train_imp)
knn.fit(X_train_imp_scaled)
```

Notes:

When we call `pipe.fit(X_train, y_train)`, multiple steps are occurring.

Notice that we are passing `X_train` and **not** the imputed or scaled
data here.

  - Fit `SimpleImputer` on `X_train`.
  - Transform `X_train` using the fit `SimpleImputer` to create
    `X_train_imp`.
  - Fit `StandardScaler` on `X_train_imp`.
  - Transform `X_train_imp` using the fit `StandardScaler` to create
    `X_train_imp_scaled`.
  - Fit the model (`KNeighborsRegressor` in our case) on
    `X_train_imp_scaled`.

---

``` python
pipe.predict(X_train) 
```

```out
array([126500., 117380., 187700., ..., 259500., 308120.,  60860.])
```

``` python
X_train_imp = imputer.transform(X_train)
X_train_imp_scaled = scaler.transform(X_train_imp)
knn.predict(X_train_imp_scaled)
```

Notes:

Then when we are passing original data to `predict` the following steps
are carrying out:

  - Transform `X_train` using the fit `SimpleImputer` to create
    `X_train_imp`.
  - Transform `X_train_imp` using the fit `StandardScaler` to create
    `X_train_imp_scaled`.
  - Predict using the fit model (`KNeighborsRegressor` in our case) on
    `X_train_imp_scaled`.

It is not fitting any of the data this time.

One thing that is awesome with pipelines is that we can’t make the
mistakes we showed earlier.

---

<center>

<img src="/module5/pipeline.png" width = "70%" alt="404 image" />

</center>

<a href="https://amueller.github.io/COMS4995-s20/slides/aml-04-preprocessing/#18" target="_blank">Attribution</a>

Notes:

Here is a schematic assuming we have two transformers `T1` (in our
example, imputation) and `T2` (in our example, standardization).

We call fit on the train split and score on the test split, it’s clean.

We can’t accidentally re-fit the preprocessor on the test data like we
did last time.

It automatically makes sure the same transformations are applied to
train and test.

When we call `pipe.fit()` we are fitting ***and*** transforming our
data.

---

``` python
scores_processed = cross_validate(pipe, X_train, y_train, return_train_score=True)
pd.DataFrame(scores_processed)
```

```out
   fit_time  score_time  test_score  train_score
0  0.024251    0.207057    0.693883     0.792395
1  0.021954    0.183063    0.685017     0.789108
2  0.022043    0.189623    0.694409     0.787796
3  0.022782    0.190466    0.677055     0.792444
4  0.022356    0.151298    0.714494     0.823421
```

Notes:

Remember what cross-validation does - it calls `fit` and `score`.

Now we’re calling fit on the pipeline, not just the 𝑘-NN regressor.

So, the transformers and the 𝑘-NN model are refits again on each fold.

The pipeline applies the `fit_transform` on the train portion of the
data and only `transform` on the validation portion in each fold.

This is how to avoid the Golden Rule violation\!

---

``` python
pd.DataFrame(scores_processed).mean()
```

```out
fit_time       0.022677
score_time     0.184301
test_score     0.692972
train_score    0.797033
dtype: float64
```

``` python
dummy = DummyRegressor(strategy="median")
scores = cross_validate(dummy, X_train, y_train, return_train_score=True)
pd.DataFrame(scores).mean()
```

```out
fit_time       0.001234
score_time     0.000540
test_score    -0.055115
train_score   -0.054611
dtype: float64
```

Notes:

And we can also see that the preprocessed scores are much better than
our dummy regressor which has negative ones\!

We can trust here now that the scores are not influenced but the
training data and all our steps were done efficiently and easily too.

---

# Let’s apply what we learned\!

Notes: <br>
