---
type: slides
---

# Data Splitting

Notes: <br>

---

## Recap

### Training score versus generalization score

Given a model, in Machine Learning (ML), people usually talk about two
kinds of scores (accuracies):

1.  Score on the training data

<br>

2.  Score on the entire distribution of data

Notes:

At the end of module 2, we discussed two kinds of scores (accuracies) in
a model:

1.  Score on the training data

2.  Score on the entire distribution of data

But we do not have access to the entire distribution which is where our
interests lie so what do we do?

---

## We can approximate generalization accuracy by splitting our data\!

<br> <br>

<center>

<img src="/module3/splitted.png"  width = "100%" alt="404 image" />

</center>

Notes:

What we do is we keep a randomly selected portion of our data aside we
call that the testing data.

We do our fitting on the training data and then we can assess the model
on this testing data which we’re using to be representative of the whole
distribution of the data.

---

## Simple train and test split

<br> <br>

<center>

<img src="/module3/train-test-split.png"  width = "100%" alt="404 image" />

</center>

Notes:

The data needs to be shuffled before splitting since our data could be
in a specific order and if we took the last part as our test set we
wouldn’t have a random sample of our data.

So first we shuffle and then split the rows of the data into 2 sections.

Here the training portion in green and the test portion in red.

The lock and key icon on the test set symbolizes that we don’t want to
touch it until the end.

---

<center>

<img src="/module3/split_funct.png"  width = "80%" alt="404 image" />

</center>

<a href="https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.train_test_split.html" target="_blank">*Attribution*</a>

Notes:

We can do this very easily with the `train_test_split` function Scikit
Learn.

This function allows us to split the data like we just discussed and it
also does the shuffling for us.

There are two ways of using it: Pass in a dataframe and then it does the
split Pass in `X` and `y` and it will then split these both separately.

It uses useful arguments such as:

  - `test_size`
  - `train_size`
  - `random_state`

---

``` python
cities_df = pd.read_csv("data/canada_usa_cities.csv")
cities_df
```

```out
     longitude  latitude country
0    -130.0437   55.9773     USA
1    -134.4197   58.3019     USA
2    -123.0780   48.9854     USA
3    -122.7436   48.9881     USA
4    -122.2691   48.9951     USA
..         ...       ...     ...
204   -72.7218   45.3990  Canada
205   -66.6458   45.9664  Canada
206   -79.2506   42.9931  Canada
207   -72.9406   45.6275  Canada
208   -79.4608   46.3092  Canada

[209 rows x 3 columns]
```

Notes: Let’s test it out in action with the Canadian and United States
cities data that we saw in module 2.

---

``` python
X = cities_df.drop(columns=["country"])
X
```

```out
     longitude  latitude
0    -130.0437   55.9773
1    -134.4197   58.3019
2    -123.0780   48.9854
3    -122.7436   48.9881
4    -122.2691   48.9951
..         ...       ...
204   -72.7218   45.3990
205   -66.6458   45.9664
206   -79.2506   42.9931
207   -72.9406   45.6275
208   -79.4608   46.3092

[209 rows x 2 columns]
```

Notes:

We’re gonna separate our `X` and `y`.

The `X` in this case is `longitude` and `latitude`.

---

``` python
y = cities_df["country"]
y
```

```out
0         USA
1         USA
2         USA
3         USA
4         USA
        ...  
204    Canada
205    Canada
206    Canada
207    Canada
208    Canada
Name: country, Length: 209, dtype: object
```

Notes:

And the `y` is the country that we’re going to try to predict for each
city.

---

``` python
from sklearn.model_selection import train_test_split

# Split the dataset
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=123)
```

``` python
X_train.head(3)
```

```out
     longitude  latitude
160   -76.4813   44.2307
127   -81.2496   42.9837
169   -66.0580   45.2788
```

Notes:

First we import `train_test_split` from `sklearn.model_selection`.

And then we are going to pass in the `X` and the `y` to give us the 4
separate objects that we name:

  - `X_train`
  - `X_test`
  - `y_train`
  - `y_test`

This gives us a look at what `X_train` looks like as we can see that
it’s been shuffled because the index is out of order and it contains
our 2 columns `longitude` and `latitude`.

---

``` python
X_test.head(3)
```

```out
     longitude  latitude
172   -64.8001   46.0980
175   -82.4066   42.9746
181  -111.3885   56.7292
```

``` python
y_train.head(3)
```

```out
160    Canada
127    Canada
169    Canada
Name: country, dtype: object
```

``` python
y_test.head(3)
```

```out
172    Canada
175    Canada
181    Canada
Name: country, dtype: object
```

Notes:

We can look at the other object as well.

Here we have `X_test`, `y_train`, `y_test`, and as expected, the `y`
objects contain the countries.

The function keeps the original index and we can see that the index is
not in order anymore due to the shuffling.

But the first 3 tests examples 172.175.181 in the `X` objects map to the
same test example in the `y` object which makes sense since they
correspond to each other.

---

``` python
shape_dict = {"Data portion": ["X", "y", "X_train", "y_train", "X_test", "y_test"],
    "Shape": [X.shape, y.shape,
              X_train.shape, y_train.shape,
              X_test.shape, y_test.shape]}

shape_df = pd.DataFrame(shape_dict)
shape_df
```

```out
  Data portion     Shape
0            X  (209, 2)
1            y    (209,)
2      X_train  (167, 2)
3      y_train    (167,)
4       X_test   (42, 2)
5       y_test     (42,)
```

Notes:

Let’s take a look at the shape of each of these dataframes now.

The code is less important here and instead let’s focus our attention on
the output.

`X` started as being 209 rows and 2 columns (`longitude` and
`latitude`).

`y` started as the same 209 rows but being only one dimensional.

After the splitting, 167 of the examples went to the training set and 42
of the examples went to the test set.

The `X` only 2 have 2 columns and the `y` is 1 dimensional.

---

``` python
train_df, test_df = train_test_split(cities_df, test_size = 0.2, random_state = 123)

X_train, y_train = train_df.drop(columns=["country"]), train_df["country"]

X_test, y_test = test_df.drop(columns=["country"]), test_df["country"]

train_df.head()
```

```out
     longitude  latitude country
160   -76.4813   44.2307  Canada
127   -81.2496   42.9837  Canada
169   -66.0580   45.2788  Canada
188   -73.2533   45.3057  Canada
187   -67.9245   47.1652  Canada
```

Notes:

Sometimes we want to split first into the training and testing datasets
and then we can split these 2 objects after into the feature and target
objects.

The earlier to split the data the better and this is a great way to
split as well.

We can do this by splitting our `cities_df` dataframe into a train and
test dataframe as objects `train_df`, `test_df`, and then separate the
features from the target after the fact.

Sometimes we may want to keep the target in the train split for EDA or
for visualization.

---

``` python
chart_cities = alt.Chart(train_df).mark_circle(size=20, opacity=0.6).encode(
    alt.X('longitude:Q', scale=alt.Scale(domain=[-140, -40])),
    alt.Y('latitude:Q', scale=alt.Scale(domain=[20, 60])),
    alt.Color('country:N', scale=alt.Scale(domain=['Canada', 'USA'],
                                           range=['red', 'blue'])))
chart_cities
```
<img src="/module3/chart_cities.png" alt="A caption" width="60%" />

Notes:

This plot shows the `train_df` object.

This is another reason why splitting with the target and features
together can be useful as it can visually show what’s going on and
potentially provide some insights into our analysis.

---

``` python
model = DecisionTreeClassifier()
model.fit(X_train, y_train);
```

Notes:

We can build our model here by constructing a decision tree classifier
and fitting it.

---

<center>

<img src="/module3/module3_01_small.png"  width = "78%" alt="404 image" />

</center>

Notes:

The model corresponds to the following tree.

---

<br> <br> <br>

<center>

<img src="/module3/boundary_tree.png"  width = "100%" alt="404 image" />

</center>

Notes:

For example, we see here, if the `latitude` is less than 42.9. and say
it’s the `latitude` is also less than 42.096, the model predicts `USA`
etc.

Here we have the decision tree on the left and a picture of it on the
right that corresponds to the decision boundaries.

The first split corresponds to the `latitude` column using a threshold
of 42.9.

if `latitude` is greater than 42.9, then the model will be predicting
above the horizontal line that lines upright with 42.9 on the y-axis
which is the `latitude` axis.

And if the statement is true and `latitude` is less than 42.9. The
prediction corresponds to the bottom half of this plot.

We see here that the bottom half is splitting again but both sides are
being predicted as `USA` making the entire bottom half of the plot red,
corresponding to `USA` predictions.

It doesn’t completely make sense to split and then predict the same
thing on both sides but the reason why this occurs as it could be useful
if we decide to have a deeper tree.

On the other hand, if we have `latitude` greater than 42.9, this
corresponds to the upper half of the plot. The second split on this is
on the `longitude` feature.

This is the vertical line here. Now anything less than -130.017 on the
x-axis is predicted as `USA` and anything greater is predicted as
`Canada`.

---

<center>

<img src="/module3/module3_01a.png"  width = "75%" alt="404 image" />

</center>

Notes:

So here is the deeper tree.

Now the second split on the left side makes sense because it gets split
again on `latitude` and we see that there is a `Canada` class and a
`USA` class.

This tree is too large to go into detail but feel free to take a moment
to look at it.

---

``` python
print("Train score: " + str(round(model.score(X_train, y_train), 2)))
```

```out
Train score: 1.0
```

``` python
print("Test score: " + str(round(model.score(X_test, y_test), 2)))
```

```out
Test score: 0.74
```

Notes:

For this tree, the training score is giving us a score of 1.0 and the
test score is only 0.71.

On the training data, our model predicts well but how will it do on data
it hasn’t seen yet?

We simulate this by using our test set and here we see that our model
does not do quite as well as 100% in this case.

---

<img src="/module3/module3_01/unnamed-chunk-19-1.png" width="105%" />

Notes:

And so here’s a picture of that deeper decision tree and its decision
boundaries.

On the left and the right, we have the same boundaries But different
data being shown.

What’s important to see here is that the model is getting 100 percent
accuracy on the training data so every time we have a red training
sample, the coloring there’s also read meaning we correctly predicted
it.

Every time we have a blue training sample meaning a Canadian city the
background coloring there is also blue meaning we predicted it
correctly.

In order to get 100 percent accuracy, the model ends up being extremely
specific.

We can see this long blue horizontal section which the model is
predicting contains Canadian cities.

We know that’s not true and quite silly since there is no small thin
section of Canada slicing the US in half.

That the model got over complicated on the training data and this
doesn’t generalize to the test data well.

In the plot on the right, we can see some red triangles in the blue area
and that is the model making mistakes which explains the 71% accuracy.

We see that although the model does well on the training data, it does
not do well on unseen data.

---

### *test\_size* and *train\_size* arguments

``` python
train_df, test_df = train_test_split(cities_df, test_size = 0.2, random_state = 123)
```

``` python
shape_dict2 = {"Data portion": ["cities_df", "train_df", "test_df"],
    "Shape": [cities_df.shape, train_df.shape,
              test_df.shape]}

shape_df2 = pd.DataFrame(shape_dict2)
shape_df2
```

```out
  Data portion     Shape
0    cities_df  (209, 3)
1     train_df  (167, 3)
2      test_df   (42, 3)
```

Notes:

Let’s take a look at the arguments in the `.train_test_split()`
function.

When we specify how we want to split the data, we can specify either
`test_size` or `train_size`.

See the documentation
<a href="https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.train_test_split.html" target="_blank">here</a>.

There is no hard and fast rule on the split sizes should we use and it
depends upon how much data is available to us

Some common splits are 90/10, 80/20, 70/30 (training/test).

In the above example, we used an 80/20 split.

The trade-off is that the more training data we have the more
information we have to train our model on, but also the more test data
we have, the better we can assess our model afterward, hence it is a
difficult choice to make.

---

### *random\_state* argument

``` python
train_df_rs5, test_df_rs5 = train_test_split(cities_df, test_size = 0.2, random_state = 5)
```

``` python
train_df_rs7, test_df_rs7 = train_test_split(cities_df, test_size = 0.2, random_state = 7)
```

``` python
train_df_rs5.head(3)
```

```out
    longitude  latitude country
39   -96.7969   32.7763     USA
55   -97.5171   35.4730     USA
40  -121.8906   37.3362     USA
```

``` python
train_df_rs7.head(3)
```

```out
     longitude  latitude country
128  -118.7148   50.4165  Canada
195  -122.7454   53.9129  Canada
99    -72.0968   45.0072  Canada
```

Notes:

The other argument we will focus on is the `random_state` argument.

The data is shuffled before splitting which is a crucial step.

The `random_state` argument controls this shuffling.

Without this argument set, each time we split our data, it will be split
in a different way.

We set this to add a component of reproducibility to our code and if we
set it with a `random_state` when we run our code again it will produce
the same result.

In the example above we used `random_state=5` and `random_state=7` and
we can see that they contain different observations.

---

# Let’s apply what we learned\!

Notes: <br>
