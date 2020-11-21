---
type: slides
---

# Decision trees with continuous features

Notes: <br>

---

``` python
classification_df = pd.read_csv("data/quiz2-grade-toy-classification.csv")
classification_df.head(3)
```

```out
   ml_experience  class_attendance  lab1  lab2  lab3  lab4  quiz1   quiz2
0              1                 1    92    93    84    91     92      A+
1              1                 0    94    90    80    83     91  not A+
2              0                 0    78    85    83    80     80  not A+
```

``` python
X = classification_df.drop(columns=["quiz2"])
X.head(3)
```

```out
   ml_experience  class_attendance  lab1  lab2  lab3  lab4  quiz1
0              1                 1    92    93    84    91     92
1              1                 0    94    90    80    83     91
2              0                 0    78    85    83    80     80
```

``` python
y = classification_df["quiz2"]
y.head(3)
```

```out
0        A+
1    not A+
2    not A+
Name: quiz2, dtype: object
```

Notes:

We’ve seen how decision trees work when our data is binary but that’s
not always going to be the case.

In fact, even for our quiz to toy classification dataset, we had to
transform it into binary data.

Here we see our labs 1 to 4 and quiz 1 are all numeric values from 0 to
100 and they’re not binary. How does our model handle this?

As usual, let’s split up our classification dataset frame into the `X`
object which is our features and our `Y` object which is our target
column.

---

``` python
from sklearn.tree import DecisionTreeClassifier
```

``` python
model = DecisionTreeClassifier()
model.fit(X, y)
```

```out
DecisionTreeClassifier()
```

Notes:

Just like we saw in the previous sections, we have to import our
decision tree classifier from the `scikit learn.tree` library.

We build our model which is a decision tree classifier and we fit our
data on our `X` and `y` objects.

---

<center>

<img src="/module2/module2_08a.png"  width = "65%" alt="404 image" />

</center>

Notes:

Now we can see what the decision tree looks like.

The last time we looked at these trees it was splitting on values of
0.5.

This time we have multiple different split values.

Here, if your lab3 mark was less than 83.5 the tree predicts your
`quiz2` grade to be `Not A+`.

Before when we had binary data, features could only really be split once
but now you’ll notice that some features come up multiple times in the
tree with a different split value.

For example, `lab4` is split on a value of 83.5 and if we go further
down the branches we have another split for lab4 at 96.5.

---

``` python
X_subset = X[["lab4", "quiz1"]]
X_subset.head()
```

```out
   lab4  quiz1
0    91     92
1    83     91
2    80     80
3    91     89
4    92     85
```

Notes:

For the next example let’s consider a subset of the data with only two
features.

This is because it’s easier to visualize the splitting in 2 dimensions.

Let’s subset the data to only include `lab4` and `quiz1`.

---

## Decision boundaries

``` python
depth = 1
model = DecisionTreeClassifier(max_depth=depth)
model.fit(X_subset, y);
```

<center>

<img src="/module2/module2_08b.png"  width = "50%" alt="404 image" />

</center>

Notes:

What do we do with learned models?

We build our model but here you may notice that we are setting an
argument called `max_depth`.

We will cover this in more detail in the next section but for now, just
know that setting this constricts our model.

Setting this to 1 constricts the model to a depth of 1 which is a
decision stump.

Another way to think about them is to ask: what sort of test examples
will the model classify as positive, and what sort will it classify as
negative?

Here we can look at this ***decision stump*** which will show us where
the first feature (`lab4`) makes a divide between an `A+` and `Not A+`.

---

<center>

<img src="/module2/module2_08b.png"  width = "20%" alt="404 image" />

</center>

<img src="/module2/module2_08/unnamed-chunk-11-1.png" width="60%" style="display: block; margin: auto;" />

Notes:

We can assume a geometric view of the data. (More on this soon)

Here the red region corresponds to the `not A+` class and the blue
region corresponds to the `A+` class.

There is a line separating the red region and the blue region which is
called the **decision boundary** of the model.

In our current model, this decision boundary is created by asking one
question.

---

### Another example of decision boundaries

``` python
df = pd.read_csv('data/canada_usa_cities.csv')
df.head()
```

```out
   longitude  latitude country
0  -130.0437   55.9773     USA
1  -134.4197   58.3019     USA
2  -123.0780   48.9854     USA
3  -122.7436   48.9881     USA
4  -122.2691   48.9951     USA
```

Notes:

Here is another example of a decision boundary which can help explain
the concept more visually.

We have the latitude and longitude locations of different cities.

We want to predict if they are Canadian or American cities using these
features.

---

``` python
chart1 = alt.Chart(df).mark_circle(size=20, opacity=0.6).encode(
    alt.X('longitude:Q', scale=alt.Scale(domain=[-140, -40]), axis=alt.Axis(grid=False)),
    alt.Y('latitude:Q', scale=alt.Scale(domain=[20, 60]), axis=alt.Axis(grid=False)),
    alt.Color('country:N', scale=alt.Scale(domain=['Canada', 'USA'],
                                           range=['red', 'blue']))
)
chart1
```
<img src="/module2/chart1.png" alt="A caption" width="50%" />

Notes:

Now we’re plotting our latitude and longitude and you can see all of the
red dots are Canadian cities and all the blue dots are American cities.

---

## Real boundary between Canada and USA

<center>

<img src="/module2/canada-us-border.jpg" width="70%">

</center>

**Attribution:**
<a href="https://sovereignlimits.com/blog/u-s-canada-border-history-disputes" target="_blank">sovereignlimits.com</a>

Notes:

We can compare this with the actual border between Canada and the U. S.

---

# Let’s apply what we learned\!

Notes: <br>
