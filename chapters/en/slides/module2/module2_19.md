---
type: slides
---

# Generalization

Notes: <br>

---

### Visualizing model complexity using decision boundaries

``` python
classification_df = pd.read_csv("data/quiz2-grade-toy-classification.csv")
classification_df
```

```out
    ml_experience  class_attendance  lab1  lab2  lab3  lab4  quiz1   quiz2
0               1                 1    92    93    84    91     92      A+
1               1                 0    94    90    80    83     91  not A+
2               0                 0    78    85    83    80     80  not A+
3               0                 1    91    94    92    91     89      A+
4               0                 1    77    83    90    92     85      A+
..            ...               ...   ...   ...   ...   ...    ...     ...
16              0                 0    75    91    93    86     85      A+
17              1                 0    86    89    65    86     87  not A+
18              1                 1    91    93    90    88     82  not A+
19              0                 1    77    94    87    81     89  not A+
20              1                 1    96    92    92    96     87      A+

[21 rows x 8 columns]
```

Notes:

In the last slide deck, we learned about decision boundaries.

We saw that we could visualize the splitting of decision trees using
these boundaries.

Let’s use our familiar quiz2 data classification dataset back again to
build on our decision boundary knowledge.

---

``` python
X = classification_df.drop(columns=["quiz2"])
y = classification_df["quiz2"]
```

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

Let’s start off and get our `X` and `Y` objects.

In this case, in order to visualize our decision boundaries, we are just
going to look at 2 columns so that we can visualize in 2 dimensions.

If we subset our data and look at the 2 features from data named `lab4`
and `quiz1` we can see the values the decision tree is splitting on in a
graph.

---

``` python
depth = 1
model = DecisionTreeClassifier(max_depth=depth)
model.fit(X_subset, y);
model.score(X_subset, y)
```

```out
0.7142857142857143
```

<center>

<img src="/module2/module2_18a.png"  width = "30%" alt="404 image" />

</center>

Notes:

Let’s build our model now.

We’re going to build a decision tree classifier and set the `max_depth`
hyperparameter to 1 to create a decision stop.

In this decision tree there is only 1 split.

When we score it on data that it’s already seen we get an accuracy of
71.4%.

---

<center>

<img src="/module2/module2_18a.png"  width = "25%" alt="404 image" />

</center>

<img src="/module2/module2_19/unnamed-chunk-7-1.png" width="50%" style="display: block; margin: auto;" />

Notes:

Plotting the values of `lab4` and `quiz1`, we see the red region
corresponds to the “not A+” class and the blue region corresponds to the
“A+” class.

The decision boundary separating the red region and the blue region is
at the model split where `lab4=84.5`.

---

``` python
depth = 2
model = DecisionTreeClassifier(max_depth=depth)
model.fit(X_subset, y);
model.score(X_subset, y)
```

```out
0.8095238095238095
```

<center>

<img src="/module2/module2_18b.png"  width = "30%" alt="404 image" />

</center>

Notes:

Let’s see what happens to our decision boundaries when we change for a
maximum tree depth of 2.

In the following model, the decision boundaries are created by asking
two questions and we can see 2 splits now.

Our score here has increased from 71.4% to 81%.

---

<center>

<img src="/module2/module2_18b.png"  width = "25%" alt="404 image" />

</center>

<img src="/module2/module2_19/unnamed-chunk-10-1.png" width="50%" style="display: block; margin: auto;" />

Notes:

When we graph it, we can now see 2 boundaries. One where `quiz1` equals
83.5 and another where `lab4` equals 84.5.

---

``` python
depth = 4
model = DecisionTreeClassifier(max_depth=depth)
model.fit(X_subset, y);
model.score(X_subset, y)
```

```out
0.9523809523809523
```

<center>

<img src="/module2/module2_18c.png"  width = "40%" alt="404 image" />

</center>

Notes:

Now let’s continue on making a new model with a hyperparameter
`max_depth` equal to 4.

Our score now has shot up to 95% and we have multiple splits now.

Six splits can be seen with 3 on the `quiz1` feature and the other 3 on
the `lab4` feature.

---

``` python
model.score(X_subset, y)
```

```out
0.9523809523809523
```

<img src="/module2/module2_19/unnamed-chunk-14-1.png" width="50%" style="display: block; margin: auto;" />

Notes:

Here we can see our boundaries are getting more complex.

We can see our 6 decision boundaries, 3 on our x-axis `lab4` and 3 on
our y-axis `quiz1`.

---

``` python
depth = 10
model = DecisionTreeClassifier(max_depth=depth)
model.fit(X_subset, y);
model.score(X_subset, y)
```

```out
1.0
```

<center>

<img src="/module2/module2_18d.png"  width = "36%" alt="404 image" />

</center>

Notes:

Now, what happens when we have a `max_depth` of 10?

Things are getting much more complicated now.

Our model now has a score of 100%.

---

``` python
model.score(X_subset, y)
```

```out
1.0
```

<img src="/module2/module2_19/unnamed-chunk-18-1.png" width="65%" style="display: block; margin: auto;" />

Notes:

The model is now more specific and sensitive to the training data.

Do you think that’s going to be helpful for us?

---

## Fundamental goal of machine learning

<center>

<img src="/module2/generalization-train.png" width = "42%" alt="404 image" />

</center>

Notes:

In machine learning the fundamental goal is **to generalize beyond what
we see in the training examples**.

We are only given a sample of the data and do not have the full
distribution.

Using the training data, we want to come up with a reasonable model that
will perform well on some unseen examples.

At the end of the day, we want to deploy models that make reasonable
predictions on unseen data

Example: Imagine that a learner sees the following images as training
data and corresponding labels.

She is trying to predict the labels of the image on the right after
learning from the images from the training dataset on the left.

She’s given 2 cats and 2 dogs in the training data.

---

### Generalizing to unseen data

<center>

<img src="/module2/generalization-predict.png" width = "100%" alt="404 image" />

</center>

Notes:

Now the learner is presented with new images.

Would you expect her to be able to correctly identify each image?

She likely will be able to identify the first three but what about the
4th one? It’s unlikely.

The point here is that we want this learning to be able to generalize
beyond what it sees here and be able to predict and predict labels for
the new examples.

These new examples should be representative of the training data.

---

## Training score versus Generalization score

Given a model in machine learning, people usually talk about two kinds
of accuracies (scores):

1.  Accuracy on the training data

2.  Accuracy on the entire distribution of data

Notes:

We saw with depth 10 we could get perfect accuracy of 1 but what makes
ML hard is that we only have access to a sample and not the full data
distribution.

For example, in our toy quiz 2 classification problem we only had 21
examples and 7 features so there could be many more possible examples.

We were expected to make a reasonable model that made reasonable
predictions with only 21 examples from several possible options.

The question is when we get an accuracy of 1, on limited data, can we
really trust the training accuracy?

Would you deploy this model and expect it to perform reasonably on
unseen examples? Probably not.

This is why in machine learning people usually talk about 2 types of
scores.

Scores on the training data and score on the entire distribution.

We are really interested in the score on the entire distribution because
at the end of the day we want our model to perform well on unseen
examples.

But the problem is that we do not have access to the distribution and
only the limited training data that is given to us.

So, what do we do?

We will cover this, in the next module.

---

# Let’s apply what we learned\!

Notes: <br>
