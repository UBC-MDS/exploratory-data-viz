---
type: slides
---

# 𝑘 -Nearest Neighbours (𝑘-NNs) Classifier

Notes: <br>

---

Here is some toy data for binary classification. I want to predict the
point in grey.

<center>

<img src="/module4/scatter.png"  width = "50%" alt="404 image" />

</center>

Notes:

Now we know how to measure distance and find examples that are closest
to a point but how can that be translated into a predictive model?

Here is some toy data for binary classification.

We want to predict the point in grey.

An intuitive way to do this is predict the grey point using the same
label as the next “closest” point (𝑘 = 1) We would predict a target of 1
(orange) in this case

---

<center>

<img src="/module4/scatter_k1.png"  width = "50%" alt="404 image" />

</center>

Notes:

We would predict a target of 1 (orange) in this case.

---

<center>

<img src="/module4/scatter_k3.png"  width = "50%" alt="404 image" />

</center>

Notes:

We could also use the 3 closest points (𝑘 = 3) and let them **vote** on
the correct class.

We would predict a target of 0 (blue) in this case.

---

``` python
small_train_df = cities_df.sample(30, random_state=90)
X_train = small_train_df.drop(columns=["country"])
y_train = small_train_df["country"]
one_city = small_train_df.sample(1, random_state=44)
one_city
```

```out
     longitude  latitude country
144  -104.6173   50.4488  Canada
```

<center>

<img src="/module4/point.png"  width = "63%" alt="404 image" />

</center>

Notes:

Let’s return to a smaller version of our cities data now.

Here we have a single point we are calling `one_city`. It’s the green
triangle we see in the plot.

---

<center>

<img src="/module4/point.png"  width = "70%" alt="404 image" />

</center>

``` python
from sklearn.neighbors import KNeighborsClassifier

neigh = KNeighborsClassifier(n_neighbors=1)
neigh.fit(X_train, y_train.to_numpy());
neigh.predict(one_city.drop(columns=["country"]))
```

```out
array(['Canada'], dtype=object)
```

Notes:

If we predict the closest point where 𝑘 = 1, we would predict a target
of **Canada** (red) in this case.

---

<center>

<img src="/module4/point.png"  width = "70%" alt="404 image" />

</center>

``` python
neigh = KNeighborsClassifier(n_neighbors=3)
neigh.fit(X_train, y_train.to_numpy());
neigh.predict(one_city.drop(columns=["country"]))
```

```out
array(['Canada'], dtype=object)
```

Notes:

What about with the nearest 3 cities(𝑘 = 1)?

This is still predicting Canada since the majority of the 3 nearest
points to the green triangle are “Canadian”.

---

<center>

<img src="/module4/point.png"  width = "60%" alt="404 image" />

</center>

``` python
neigh = KNeighborsClassifier(n_neighbors=9)
neigh.fit(X_train, y_train.to_numpy());
neigh.predict(one_city.drop(columns=["country"]))
```

```out
array(['USA'], dtype=object)
```

Notes:

What about with the nearest 9 cities(𝑘 = 9)?

This is now predicting USA since the majority of the 9 nearest points
are “USA” cities.

---

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

``` python
model.score(X_test,y_test)
```

```out
0.7142857142857143
```

Note:

We can see how our model will predict both our training data and our
test set using the same `fit` and `score` that we saw with dummy
classifiers and decision trees.

Extra: The
<a href="https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.to_numpy.html" target="_blank">`.to_numpy()`
</a> tool can help get pandas dataframes into a 2 dimensional array
which is what `.score()` and `.fit()` need as inputs.

---

# Let’s apply what we learned\!

Notes: <br>
