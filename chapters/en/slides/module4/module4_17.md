---
type: slides
---

# Choosing K (n\_neighbors)

Notes: <br>

We saw that the prediction of over query pointing changes with different
values for the `n_neighbors` argument.

So, a natural question is *how do we pick `n_neighbors`?*.

What happens when we change this hyperparameter?

Are we likely to be overfitting or underfitting with higher or lower
values of `n_neighbors`?

---

``` python
cities_df = pd.read_csv("data/canada_usa_cities.csv")
X = cities_df.drop(columns=["country"])
y = cities_df["country"]
X_train, X_test, y_train, y_test = train_test_split( X, y, test_size=0.1, random_state=123)
```

``` python
model = KNeighborsClassifier(n_neighbors=1)
model.fit(X_train, y_train.to_numpy());
```

``` python
model.score(X_train,y_train)
```

```out
1.0
```

Notes:

Let’s examine this using our cities data.

As usual, we create our `X` and `y` objects as well as our training and
test splits.

We create our `KNeighborsClassifier` object with `n_neighbors=1` and
training the model.

When we score it, we get an accuracy of 1 on the training data.

---

``` python
k = 1
knn1 = KNeighborsClassifier(n_neighbors=k)
scores = cross_validate(knn1, X_train, y_train, return_train_score = True)
pd.DataFrame(scores)
```

```out
   fit_time  score_time  test_score  train_score
0  0.002151    0.003102    0.710526          1.0
1  0.002047    0.004153    0.684211          1.0
2  0.002056    0.003417    0.842105          1.0
3  0.002830    0.003512    0.702703          1.0
4  0.002067    0.003255    0.837838          1.0
```

``` python
k = 100
knn100 = KNeighborsClassifier(n_neighbors=k)
scores = cross_validate(knn100, X_train, y_train, return_train_score = True)
pd.DataFrame(scores)
```

```out
   fit_time  score_time  test_score  train_score
0  0.002761    0.003340    0.605263     0.600000
1  0.002082    0.003742    0.605263     0.600000
2  0.002438    0.003654    0.605263     0.600000
3  0.002087    0.003082    0.594595     0.602649
4  0.001990    0.003453    0.594595     0.602649
```

Notes:

Let’s carry out cross-validation with 𝑘=1.

These are our cross-validation results.

What we see here is in each fold our training score always produces a
perfect accuracy of 1.0.

Our validation score for each fold is much lower than the training
score.

The gap between the training and validation sets seems to be high and so
it is likely that our model is overfitting.

Let’s seen now what happens when 𝑘=100.

Now, we see that our training scores are much lower and our validation
scores are also lower.

The gap between the training and validation sets seem to be lower. This
looks like our model is underfitting now.

---

<img src="/module4/module4_17/unnamed-chunk-7-1.png" width="1536" />

Notes:

If we plot these two models with 𝑘=1 on the left and 𝑘=100 on the right.

The left plot shows a much more complex model where it is much more
specific and attempts to get every example correct.

The plot on right is plotting a simpler model and we can see more
training examples are being predicted incorrectly.

---

### How to choose `n_neighbors`?

``` python
results_dict = {"n_neighbors": list(), "mean_train_score": list(), "mean_cv_score": list()}

for k in range(1,50,5):
    knn = KNeighborsClassifier(n_neighbors=k)
    scores = cross_validate(knn, X_train, y_train, return_train_score = True)
    results_dict["n_neighbors"].append(k)
    results_dict["mean_cv_score"].append(np.mean(scores["test_score"]))
    results_dict["mean_train_score"].append(np.mean(scores["train_score"]))

results_df = pd.DataFrame(results_dict)
results_df
```

```out
   n_neighbors  mean_train_score  mean_cv_score
0            1          1.000000       0.755477
1            6          0.831135       0.792603
2           11          0.819152       0.802987
3           16          0.801863       0.782219
4           21          0.777934       0.766430
5           26          0.755364       0.723613
6           31          0.743391       0.707681
7           36          0.728777       0.707681
8           41          0.706128       0.681223
9           46          0.694155       0.660171
```

Notes:

In our toy problem with 𝑘=1, we saw the model was overfitting yet when
𝑘=100, the model was underfitting.

So, the question is how do we pick 𝑘?

  - The answer lies in hyperparameter optimization.

Here we are looping over different values of 𝑘 ( `n_neighbors`) and
performing cross-validation on each one.

---

<br>

<center>

<img src="/module4/K_plot.png" alt="A caption" width="80%" />

</center>

Notes:

In this graph we’ve plotted, `n_neighbors` is on the x-axis and the
model accuracy is on the y-axis.

We can see there is a sweet spot where the gap between the validation
and training scores is the lowest. Here it’s when `n_neighbors` is 11.

---

``` python
sorted_results_df = results_df.sort_values("mean_cv_score", ascending = False)
sorted_results_df
```

```out
   n_neighbors  mean_train_score  mean_cv_score
2           11          0.819152       0.802987
1            6          0.831135       0.792603
3           16          0.801863       0.782219
4           21          0.777934       0.766430
0            1          1.000000       0.755477
5           26          0.755364       0.723613
6           31          0.743391       0.707681
7           36          0.728777       0.707681
8           41          0.706128       0.681223
9           46          0.694155       0.660171
```

``` python
best_k = sorted_results_df.iloc[0,0]
best_k
```

```out
11
```

Notes:

We can find the most optimal `n_neighbors` value by sorting our results
on the mean validation score.

This shows the best validation score occurs when `n_neighbors=11`.

---

``` python
knn = KNeighborsClassifier(n_neighbors=best_k)
knn.fit(X_train, y_train);
print("Test accuracy:", round(knn.score(X_test, y_test), 3))
```

```out
Test accuracy: 0.905
```

Notes:

Now that we know the best scoring hyperparameter value, we are ready to
assess our model on the test set.

We recreate our model with `n_neighbors=11`, fit the model and score it
on the test set.

Our training accuracy is 0.905 which is higher than the validation mean
accuracy we had earlier.

This is surprising and could be due to having a small dataset.

---

### Curse of dimensionality

<br>

  - 𝑘 -NN usually works well when the number of dimensions is small.

<br> <br>

<center>

<img src="/module4/skull.png" alt="A caption" width="60%" />

</center>

Notes:

In the previous module, we discussed one of the most important problems
in machine learning which was overfitting the second most important
problem in machine learning is the ***curse of dimensionality***.

This problem affects most models but this problem is especially bad for
𝑘-NN.

𝑘-NN works well then the number of dimensions is small but things fall
apart fairly quickly as the number of dimensions goes up.

If there are many irrelevant features, 𝑘-NN is hopelessly confused
because all of them contribute to finding similarities between examples.

With enough irrelevant features, the accidental similarity between
features wipe out any meaningful similarity and 𝑘-NN becomes is no
better than random guessing.

---

### Other useful arguments of `KNeighborsClassifier`

<center>

<img src="/module4/knn.png" alt="A caption" width="80%" />

</center>

<a href="https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.KNeighborsClassifier.html" target="_blank">**Attribution**
</a>

Notes:

Another useful hyperparameter is `weight`.

So far, when predicting labels, we have been giving equal weight to all
the nearby examples.

We can change that using this `weight` hyperparameter.

We can tell it to weigh the examples higher if they are closer to the
query point.

---

# Let’s apply what we learned\!

Notes: <br>
