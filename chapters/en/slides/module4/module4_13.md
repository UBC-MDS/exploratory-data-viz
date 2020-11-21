---
type: slides
---

# 𝑘 -Nearest Neighbours (𝑘-NNs) Classifier

Notes: <br>

Now that we have learned how to find similar examples, how can we use
this idea in a predictive model?

---

<br> <br>

<center>

<img src="/module4/scatter.png"  width = "50%" alt="404 image" />

</center>

Notes:

Let’s demonstrate this using some toy data for binary classification.

We have two features in our toy example; feature 1 and feature 2.

We have two targets; 0 represented with blue points and 1 represented
with orange points.

We want to predict the point in gray.

Based on what we have been doing so far, we can find the closest example
to this gray point and use its class as the class for our grey point.

---

<br> <br>

<center>

<img src="/module4/scatter_k1.png"  width = "50%" alt="404 image" />

</center>

Notes:

In this particular case, we will predict orange as the class for our
query point.

---

<br> <br>

<center>

<img src="/module4/scatter_k3.png"  width = "50%" alt="404 image" />

</center>

Notes:

Now you might be thinking that it may not be a great idea to make this
decision based only on one nearest example.

What if we consider more than one nearest example and let them vote on
the target of the query example.

In our toy example, we can consider the three closest points and let
them vote.

Now our prediction changes.

Before our prediction was orange with only one nearest point and with
three nearest points, now our prediction is blue.

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

Let’s look at how we can do this using Sklearn.

Let’s go back to our cities data. Here we are only considering thirty
examples from our cities data.

We are sampling 1 point from our data and that is the point represented
with the green triangle.

---

<center>

<img src="/module4/point.png"  width = "60%" alt="404 image" />

</center>

``` python
from sklearn.neighbors import KNeighborsClassifier

neigh = KNeighborsClassifier(n_neighbors=1)
neigh.fit(X_train, y_train);
neigh.predict(one_city.drop(columns=["country"]))
```

```out
array(['Canada'], dtype=object)
```

Notes:

Our goal is to find the class for this green triangle example.

As usual, we will import the necessary libraries (here we are importing
the `KneighborsClassifier` function) then we create our class object.

We create our class object with only one neighbour. We can do this by
passing one as the value for this `n_neighbors` argument.

We fit the classifier on our training data and we predict the single
green triangle city.

Our prediction here is Canada since the closest point to the green
triangle is a city with the class “Canada”.

---

<center>

<img src="/module4/point.png"  width = "60%" alt="404 image" />

</center>

``` python
neigh = KNeighborsClassifier(n_neighbors=3)
neigh.fit(X_train, y_train);
neigh.predict(one_city.drop(columns=["country"]))
```

```out
array(['Canada'], dtype=object)
```

Notes:

Now, what if we consider the nearest 3 neighbours?

We can do this by passing three to the `n_neighbors` argument.

We fit on the model.

Using `predict` on our new model still gives us a classification of
“Canada”.

---

<center>

<img src="/module4/point.png"  width = "60%" alt="404 image" />

</center>

``` python
neigh = KNeighborsClassifier(n_neighbors=9)
neigh.fit(X_train, y_train);
neigh.predict(one_city.drop(columns=["country"]))
```

```out
array(['USA'], dtype=object)
```

Notes:

When we change our model to consider the nearest 9 neighbours, our
prediction changes\!

It now predicts “USA” since the majority of the 9 nearest points are
“USA” cities.

---

``` python
model = KNeighborsClassifier(n_neighbors=1)
model.fit(X_train, y_train);
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

Let’s score our model with 1 neighbour.

We create our model and fit it.

We see that with one neighbour we get the perfect score of 1.0 on the
training data.

But our test score is much lower. When we score our model 0.714
accuracy.

---

# Let’s apply what we learned\!

Notes: <br>
