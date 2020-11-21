---
type: slides
---

# Case Study: Preprocessing with Scaling

Notes: <br>

---

``` python
knn_unscaled = KNeighborsClassifier();
knn_unscaled.fit(X_train, y_train)
print('Train score: ', (knn_unscaled.score(X_train, y_train).round(2)))
print('Test score: ', (knn_unscaled.score(X_test, y_test).round(2)))
```

``` out
KNeighborsClassifier()
Train score:  0.71
Test score:  0.45
```

``` python
knn_scaled = KNeighborsClassifier();
knn_scaled.fit(X_train_scaled, y_train)
print('Train score: ', (knn_scaled.score(X_train_scaled, y_train).round(2)))
print('Test score: ', (knn_scaled.score(X_test_scaled, y_test).round(2)))
```

``` out
KNeighborsClassifier()
Train score:  0.94
Test score:  0.89
```

Notes:

We’ve seen why scaling is important when we were using our basketball
dataset in the first section of this module.

In this section, we are going to dive a little deeper into the process
and the transformer options.

We had our basketball dataset and we saw the training and testing scores
before scaling with 𝑘-NN and we saw how these results improved when we
scaled our features.

---

## Scaling

<center>

<img src="/module5/scaling-data.png"  width = "75%" alt="404 image" />

</center>

<a href="https://amueller.github.io/COMS4995-s19/slides/aml-05-preprocessing/#8" target="_blank">Attribution</a>

Notes:

This problem affects a large number of ML methods.

There are several approaches to this problem.

This diagram shows the original data with each feature on an axis and
the 4 diagrams on the right show how the data is transformed with
different scaling methods.

We are going to concentrate on the two named `MinMaxScaler` and
`StandardScaler`.

---

| Approach        | What it does                     | How to update 𝑋 (but see below\!)                      | sklearn implementation                                                                                                                                                            |
| --------------- | -------------------------------- | ------------------------------------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Normalization   | sets range to \[0,1\]            | `X -= np.min(X, axis=0)`<br>`X /= np.max(X, axis=0)`   | <a href="https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.MinMaxScaler.html" target="_blank">`MinMaxScaler()`</a>                                          |
| Standardization | sets sample mean to 0, s.d. to 1 | `X -= np.mean(X, axis=0)`<br>`X /=  np.std(X, axis=0)` | <a href="https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.StandardScaler.html#sklearn.preprocessing.StandardScaler" target="_blank">`StandardScaler()`</a> |

There are all sorts of articles on this: see
<a href="http://www.dataminingblog.com/standardization-vs-normalization/" target="_blank">here</a>
and
<a href="https://medium.com/@rrfd/standardize-or-normalize-examples-in-python-e3f174b65dfc" target="_blank">here</a>.

Notes:

In terms of terminology, **Normalization** is the term we use when we
use the `MinMaxScaler()` function and **Standardization** with
`StandardScaler()` which we saw before.

Normalization converts all the values so they lie between the values 0
and 1. Standardization will set the sample mean to 0 and distribute the
values around the mean with a standard deviation of 1.

---

``` python
pd.DataFrame(X_train_imp, columns=X_train.columns, index=X_train.index).head()
```

```out
       longitude  latitude  housing_median_age  households  median_income  rooms_per_household  bedrooms_per_household  population_per_household
6051     -117.75     34.04                22.0       602.0         3.1250             4.897010                1.056478                  4.318937
20113    -119.57     37.94                17.0        20.0         3.4861            17.300000                6.500000                  2.550000
14289    -117.13     32.74                46.0       708.0         2.6604             4.738701                1.084746                  2.057910
13665    -117.31     34.02                18.0       285.0         5.2139             5.733333                0.961404                  3.154386
14471    -117.23     32.88                18.0      1458.0         1.8580             3.817558                1.004801                  4.323045
```

``` python
from sklearn.preprocessing import StandardScaler
```

``` python
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train_imp)
X_test_scaled = scaler.transform(X_test_imp)
pd.DataFrame(X_train_scaled, columns=X_train.columns, index=X_train.index).head()
```

```out
       longitude  latitude  housing_median_age  households  median_income  rooms_per_household  bedrooms_per_household  population_per_household
6051    0.908140 -0.743917           -0.526078    0.266135      -0.389736            -0.210591               -0.083813                  0.126398
20113  -0.002057  1.083123           -0.923283   -1.253312      -0.198924             4.726412               11.166631                 -0.050132
14289   1.218207 -1.352930            1.380504    0.542873      -0.635239            -0.273606               -0.025391                 -0.099240
13665   1.128188 -0.753286           -0.843842   -0.561467       0.714077             0.122307               -0.280310                  0.010183
14471   1.168196 -1.287344           -0.843842    2.500924      -1.059242            -0.640266               -0.190617                  0.126808
```

Notes:

Let’s bring in our imputed data that we processed in the last slide deck
from the California housing dataset.

At this point, we’ve already imputed the missing data with median values
using `SimpleImputer()` and we have not yet transformed it with scaling
which we will do now.

We’ve seen the `StandardScaler()` function earlier but let’s see what
the transformed data looks like.

Now we can compare our training score with scaled and unscaled data and
see a noticeable difference between the two\!

Any negative values represent values that are lower than the calculated
feature mean and anything positive and greater than 0 will are values
greater than the original column mean.

---

**Unscaled data**

``` python
knn = KNeighborsRegressor()
knn.fit(X_train_imp, y_train);
print(knn.score(X_train_imp, y_train).round(3))
```

``` python
print(knn.score(X_test_imp, y_test).round(3))
```

``` out
0.561
0.32
```

**Scaled data**

``` python
knn = KNeighborsRegressor()
knn.fit(X_train_scaled, y_train);
print(knn.score(X_train_scaled, y_train).round(3))
```

``` python
print(knn.score(X_test_scaled, y_test).round(3))
```

``` out
0.798
0.712
```

Notes:

What about our training scores?

Just using scaled column values increases the training score by around
30% and the test score increases by around 40%.

---

``` python
from sklearn.preprocessing import MinMaxScaler
```

``` python
scaler = MinMaxScaler()
X_train_scaled = scaler.fit_transform(X_train_imp)
X_test_scaled = scaler.transform(X_test_imp)
pd.DataFrame(X_train_scaled, columns=X_train.columns, index=X_train.index).head()
```

```out
       longitude  latitude  housing_median_age  households  median_income  rooms_per_household  bedrooms_per_household  population_per_household
6051    0.657371  0.159405            0.411765    0.098832       0.181039             0.028717                0.021437                  0.002918
20113   0.476096  0.573858            0.313725    0.003124       0.205942             0.116642                0.182806                  0.001495
14289   0.719124  0.021254            0.882353    0.116264       0.148998             0.027594                0.022275                  0.001099
13665   0.701195  0.157279            0.333333    0.046703       0.325099             0.034645                0.018619                  0.001981
14471   0.709163  0.036132            0.333333    0.239599       0.093661             0.021064                0.019905                  0.002922
```

Notes:

Let’s now explore `MinMaxScaler`.

Note that this time we are using `fit_transform()` syntax. This means we
are fitting and immediately transforming the data. We can use this for
`StandardScaler()` as well, it just `sklearn` compressing 2 lines of
code into a single one.

In both transformation methods fit is recording certain calculations in
order to convert the data.

For instance, in standardization, during the fit stage, the transforming
is learning the mean and standard deviation whereas in normalization,
during `fit`, the transforming is learning the minimum and maximum
values.

Looking at the data after transforming it with `MinMaxScaler()` we see
this time there are no negative values and they all are between 0 and 1.

---

**Unscaled data**

``` python
knn = KNeighborsRegressor()
knn.fit(X_train_imp, y_train);
print(knn.score(X_train_imp, y_train).round(3))
```

``` python
print(knn.score(X_test_imp, y_test).round(3))
```

``` out
0.561
0.32
```

**Scaled data**

``` python
knn = KNeighborsRegressor()
knn.fit(X_train_scaled, y_train);
print(knn.score(X_train_scaled, y_train).round(3))
```

``` python
print(knn.score(X_test_scaled, y_test).round(3))
```

``` out
0.801
0.723
```

Notes:

Again, similar to `StandardScaler` there is a big difference in the KNN
training performance after scaling the data.

But we saw in module 3 that the training score doesn’t tell us much.

We should look at the cross-validation score.

Let’s take a look at that in the next section.

---

# Let’s apply what we learned\!

Notes: <br>
