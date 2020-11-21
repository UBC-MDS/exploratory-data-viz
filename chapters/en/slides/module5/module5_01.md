---
type: slides
---

# The importance of preprocessing

Notes: <br>

---

<br> <br>

### So far …

  - Models: Decision trees, 𝑘-NNs, SVMs with RBF kernel.
  - Fundamentals: Train-validation-test split, cross-validation, the
    fundamental tradeoff, the golden rule.

<br> <br>

### Now …

**Preprocessing**: Transforming input data into a format a machine
learning model can use and understand.

Notes:

So far we have seen:

  - Three ML models (decision trees, 𝑘-NNs, SVMs with RBF kernel)
  - ML fundamentals (train-validation-test split, cross-validation, the
    fundamental trade-off, the golden rule)

Are we ready to do machine learning on real-world datasets?

Very often real-world datasets need to be transformed or
***preprocessed*** before we use them to build ML models.

---

## Basketball dataset

``` python
bball_df = pd.read_csv('data/bball.csv')
bball_df.head()
```

```out
               full_name  rating jersey                  team position     b_day  height  weight      salary country  draft_year draft_round draft_peak          college
0           LeBron James      97    #23    Los Angeles Lakers        F  12/30/84    2.06   113.4  37436858.0     USA        2003           1          1              NaN
1          Kawhi Leonard      97     #2  Los Angeles Clippers        F  06/29/91    2.01   102.1  32742000.0     USA        2011           1         15  San Diego State
2  Giannis Antetokounmpo      96    #34       Milwaukee Bucks      F-G  12/06/94    2.11   109.8  25842697.0  Greece        2013           1         15              NaN
3           Kevin Durant      96     #7         Brooklyn Nets        F  09/29/88    2.08   104.3  37199000.0     USA        2007           1          2            Texas
4           James Harden      96    #13       Houston Rockets        G  08/26/89    1.96    99.8  38199000.0     USA        2009           1          3    Arizona State
```

``` python
bball_df = bball_df[(bball_df['position'] =='G') | (bball_df['position'] =='F')]
X = bball_df[['weight', 'height', 'salary']]
y =bball_df["position"]
X_train, X_test, y_train, y_test =train_test_split(X, y, test_size=0.20, random_state=123)
```

``` python
X_train.head()
```

```out
     weight  height     salary
152    79.4    1.88  1588231.0
337    82.1    1.91  2149560.0
130   106.6    2.03  6500000.0
340   106.1    2.08  2961120.0
50     96.2    1.93  4861207.0
```

Notes:

In module 3, we used a portion of the basketball dataset to predict a
player’s position using `DecisionTreeClassifier`.

Can we use a 𝑘-NN classifier for this task?

We are going to attempt to predict a player’s position (whether a
particular player is a point guard (‘G’) or a forward (‘F’)).

Right now, we are only going to be using the numeric columns `weight`
`height` and `salary` for our `X` object and our column `position` for
our `y`.

We will dive into categorical variables in module 6.

---

### Dummy Classifier

``` python
dummy = DummyClassifier(strategy="most_frequent")
scores = cross_validate(dummy, X_train, y_train, return_train_score=True)
print('Mean validation score', scores['test_score'].mean().round(2))
```

```out
Mean validation score 0.57
```

``` python
knn = KNeighborsClassifier()
scores = cross_validate(knn, X_train, y_train, return_train_score=True)
print('Mean validation score', scores['test_score'].mean().round(2))
```

```out
Mean validation score 0.5
```

Notes:

First, let’s see what scores we get if we simply predict the most
occurring position in the dataset using our dummy classifier.

We get a score of 0.57. Now if we build our 𝑘-NN classifier we determine
that it gets an even *worse* score of 0.50\!

Dummy classifiers are supposed to be a baseline and so why is it getting
a better score than a model that is actually doing machine learning?
What’s going on?

---

``` python
two_players = X_train.sample(2, random_state=42)
two_players
```

```out
     weight  height     salary
285    91.2    1.98  1882867.0
236   112.0    2.08  2000000.0
```

``` python
euclidean_distances(two_players)[1,0]
```

```out
117133.00184682972
```

``` python
two_players_subset = two_players[["salary"]]
two_players_subset
```

```out
        salary
285  1882867.0
236  2000000.0
```

``` python
euclidean_distances(two_players_subset)[1,0]
```

```out
117133.0
```

Notes:

Let’s have a look at just 2 players.

We can see the values in each column.

The values in the `weight` column are around 100, and the values in the
`height` column are around 2.

The salary column has values much higher at around 2 million.

Let’s now calculate the distance between the two players.

We can see the distance between player 285 and 236 is 117133.00184683.

What happens if we only consider the `salary` column though?

It looks like we get almost the same distance\!

The distance is completely dominated by the feature with larger values.

The features with smaller values are being ignored.

Does it matter?

  - Yes\! The scale is based on how data was collected.
  - Features on a smaller scale can be highly informative and there is
    no good reason to ignore them.
  - We want our model to be robust and not sensitive to the scale.

Was this a problem for decision trees?

  - No. In decision trees we ask questions on one feature at a time.

So, what do we do about this?

Well, we have to scale the columns so they are all using a similar range
of values\!

Luckily Sklearn has tools called ***transformers*** for this.

---

## Transformers: Scaling example

``` python
from sklearn.preprocessing import StandardScaler
```

``` python
scaler = StandardScaler()   # Create feature transformer object
scaler.fit(X_train); # Fitting the transformer on the train split
```

```out
StandardScaler()
```

``` python
X_train_scaled = scaler.transform(X_train) # Transforming the train split
X_test_scaled = scaler.transform(X_test) # Transforming the test split
pd.DataFrame(X_train_scaled, columns = X_train.columns).head()
```

```out
     weight    height    salary
0 -1.552775 -1.236056 -0.728809
1 -1.257147 -0.800950 -0.670086
2  1.425407  0.939473 -0.214967
3  1.370661  1.664650 -0.585185
4  0.286690 -0.510879 -0.386408
```

Notes:

One form of preprocessing we can do is ***scaling*** we will talk about
this in more detail to come but for now just take a look at the tools we
are using.

We’ll be using `sklearn`’s
[`StandardScaler`](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.StandardScaler.html),
which is a `transformer`.

For now, try to only focus on the syntax.

We’ll talk about scaling in a bit.

1.  Create a feature transformer object. This is done in a similar way
    to how we create a model. Transformers accepts hyperparameters as
    well.
2.  Fitting the transformer on the train split.
3.  Transform the train split using `.transform()`.
4.  Then transform the test split.

`sklearn` uses `fit` and `transform` paradigms for feature
transformations. (In model building it was `fit` and `predict` or
`score`)

We `fit` the transformer on the train split and then `transform` the
train split as well as the test split.

`transform` replaces `predict` here.

We can now see that our values in our `X_train` have been scales so they
are now all on the same scale.

The `salary` values are no longer greater than the values in the
`height` and `weight` columns.

---

## Sklearn’s *predict* vs *transform*

``` python
model.fit(X_train, y_train)
X_train_predictions = model.predict(X_train)
```

``` python
transformer.fit(X_train, [y_train])
X_train_transformed = transformer.transform(X_train)
```

or

``` python
X_train_transformed = transformer.fit_transform(X_train)
```

Notes:

Let’s solidify this new concept of `transform`.

Suppose we have a named `model` which is either a classification or
regression model.

We can compare `predict` it with `transformer` which is a transformer
used to change the input representation to scale numeric features.

We do similar steps by calling `fit` first, followed by `transform` on
our training data just like we did `fit` and then `predict` in
classification and regression.

We can pass `y_train` in `fit` but it’s usually ignored. It allows us to
pass it just to be consistent with the usual usage of `sklearn`’s `fit`
method.

We can also carry out fitting and transforming in one call using
`.fit_transform()`, but we must be mindful to use it only on the train
split and **not** on the test split.

---

``` python
knn_unscaled = KNeighborsClassifier()
knn_unscaled.fit(X_train, y_train);
print('Train score: ', (knn_unscaled.score(X_train, y_train).round(2)))
```

``` python
print('Test score: ', (knn_unscaled.score(X_test, y_test).round(2)))
```

``` out
Train score:  0.71
Test score:  0.45
```

``` python
knn_scaled = KNeighborsClassifier()
knn_scaled.fit(X_train_scaled, y_train);
print('Train score: ', (knn_scaled.score(X_train_scaled, y_train).round(2)))
```

``` python
print('Test score: ', (knn_scaled.score(X_test_scaled, y_test).round(2)))
```

``` out
Train score:  0.94
Test score:  0.89
```

Notes:

Let’s check whether scaling makes any difference for 𝑘-NNs.

The scores with scaled data are now much better compared to the unscaled
data in the case of 𝑘-NNs.

We can see now that 𝑘-NN is doing better than the Dummy Classifier when
we scaled our features.

We are not carrying out cross-validation here for a reason that we’ll
look into soon.

We are being a bit sloppy here by using the test set several times for
teaching purposes.

But when we build any ML models, we should only assess the test set
once.

---

# Let’s apply what we learned\!

Notes: <br>
