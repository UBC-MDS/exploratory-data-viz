---
type: slides
---

# The fundamental tradeoff and the golden rule

Notes: <br>

---

## Reminder:

  - **score\_train**: is our training score (or mean train score from
    cross-validation).

<br>

  - **score\_valid** is our validation score (or mean validation score
    from cross-validation).

<br>

  - **score\_test** is our test score.

Notes:

Before going further, let’s just remind ourselves of the different
possible scores.

The training score, the validation score and the test score.

---

## The “fundamental tradeoff” of supervised learning

<br> <br> <br>

### As model complexity ↑, Score\_train ↑ and Score\_train − Score\_valid tend to ↑.

Notes:

We are going to talk about the fundamental tradeoff of supervised
learning. We’ve already danced around this topic which involves the
concepts of overfitting and underfitting.

If our model is very simple, like `DummyClassifier()`, or a Decision
tree with a `max_depth` of 1 then we won’t really learn any “specific
patterns” of the training set, we will only learn some general trend.

This is **underfitting**.

If our model is very complex, like a
`DecisionTreeClassifier(max_depth=None)`, then we will learn unreliable
patterns that get every single training example correct, but there will
be a huge gap between training error and validation error.

This is **overfitting**.

The trade-off is there is a tension between these two concepts. When we
underfit less, we overfit more.

As we increase model complexity, our training score increases (overfit
more, underfit less) **but** the trade-off is that the gap between the
training data and the test data will also increase.

The question is how will the validation score react?

---

## How to pick a model that would generalize better?

``` python
df = pd.read_csv("data/canada_usa_cities.csv")
X = df.drop(columns=["country"])
y = df["country"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=123)
```

Notes:

How do we approach this?

Let’s go back to our cities data as an example.

---

``` python
results_dict = {"depth": list(), "mean_train_score": list(), "mean_cv_score": list()}

for depth in range(1,20):
    model = DecisionTreeClassifier(max_depth=depth)
    scores = cross_validate(model, X_train, y_train, cv=10, return_train_score=True)
    results_dict["depth"].append(depth)
    results_dict["mean_cv_score"].append(scores["test_score"].mean())
    results_dict["mean_train_score"].append(scores["train_score"].mean())

results_df = pd.DataFrame(results_dict)
```

Notes:

First, let’s fit a decision tree classifier for different max\_depth
values ranging from 1 to 19.

We are going to run `cross_validate()` and set `return_train_score=True`
so we can observe both the train and validation scores.

---

``` python
results_df
```

```out
    depth  mean_train_score  mean_cv_score
0       1          0.834349       0.809926
1       2          0.844989       0.804044
2       3          0.862967       0.804412
3       4          0.906865       0.840074
4       5          0.918848       0.845956
..    ...               ...            ...
14     15          1.000000       0.809191
15     16          1.000000       0.809191
16     17          1.000000       0.809191
17     18          1.000000       0.809191
18     19          1.000000       0.809191

[19 rows x 3 columns]
```

Notes:

The results show our train and validation scores for each `max_depth`
value.

---

``` python
source = results_df.melt(id_vars=['depth'] , 
                              value_vars=['mean_train_score', 'mean_cv_score'], 
                              var_name='plot', value_name='score')
```

``` python
chart1 = alt.Chart(source).mark_line().encode(
    alt.X('depth:Q', axis=alt.Axis(title="Tree Depth")),
    alt.Y('score:Q'),
    alt.Color('plot:N', scale=alt.Scale(domain=['mean_train_score', 'mean_cv_score'],
                                           range=['teal', 'gold'])))
chart1
```
<img src="/module3/chart1.png" alt="A caption" width="55%" />

Notes:

This plot shows that as we increase our depth (increase our complexity)
our training data increases.

We can also see that as we increase our depth, we overfit more, and the
gap between the train score and validation score also increases.

We can see that there is a spot where the gap is the smallest while
still producing a decent validation score. Somewhat of a “sweet spot” if
you will. In the plot, this would be around `max_depth` is 5.

In summary, at the beginning when our model is simple and underfitting,
increasing our model complexity is a good idea since that will cause us
to underfit less and overfit, not that much more. But as we continue to
increase our complexity, the trade-off is more evident and overfitting
occurs more without increasing the validation score so much.

Commonly, we look at the cross-validation score and pick the
hyperparameter with the highest cross-validation score.

---

``` python
results_df.sort_values('mean_cv_score', ascending=False).iloc[0]
```

```out
depth               5.000000
mean_train_score    0.918848
mean_cv_score       0.845956
Name: 4, dtype: float64
```

``` python
best_depth = results_df.sort_values('mean_cv_score', ascending=False).iloc[0]['depth']
best_depth
```

```out
5.0
```

``` python
model = DecisionTreeClassifier(max_depth=best_depth)
model.fit(X_train, y_train);
print("Score on test set: " + str(round(model.score(X_test, y_test), 2)))
```

```out
Score on test set: 0.81
```

Notes:

Let’s pick `max_depth=5` which is where the mean cross-validation score
is at a maximum.

Let’s now compare this error with the model’s test error.

We can take this `max_depth=5` build a new classifier and assess our
model on the test set.

---

## The Golden Rule

Even though we care the most about test score:  

<center>

<b>THE TEST DATA CANNOT INFLUENCE THE TRAINING PHASE IN ANY WAY.</b>

</center>

<br>

<center>

<img src="/module3/gavel.png" alt="A caption" width="65%" />

</center>

Notes:

Now that we’ve covered the fundamental tradeoff, we want to discuss the
\***Golden rule of Machine Learning** which is that the test data cannot
influence the training phase in any way.

It’s important to always separate our test data and not call it until
the very end.

This sounds easy enough, but there are many ways where it can be
violated (even to the best of us).

It is surprisingly hard to adhere to as we get into more sophisticated
machine learning.  
The problem is when this happens, the test data influences our training
and the test data is no longer unseen data and so the test score will be
too optimistic.

Then our model will not work well when we deploy it.

---

## Golden rule violation: Example 1

<center>

<img src="/module3/golden_rule_violation.png" alt="A caption" width="52%" />

</center>

<a href="https://www.theregister.com/2019/07/03/nature_study_earthquakes/" target="_blank">**Attribution:
The A register - Katyanna Quach**</a>

Notes:

*… He attempted to reproduce the research, and found a major flaw: there
was some overlap in the data used to both train and test the model.*

There have been several cases in the news where this occurs.

In this example, an author of a scientific paper was accused of mixing
the training and testing data by accident.

---

## Golden rule violation: Example 2

<center>

<img src="/module3/golden_rule_violation_2.png" alt="A caption" width="60%" />

</center>

<a href="https://www.technologyreview.com/2015/06/04/72951/why-and-how-baidu-cheated-an-artificial-intelligence-test/" target="_blank">**Attribution:
MIT Technology Review- Tom Simonite**</a>

Notes:

*… The Challenge rules state that you must only test your code twice a
week, because there’s an element of chance to the results. Baidu has
admitted that it used multiple email accounts to test its code roughly
200 times in just under six months – over four times what the rules
allow.*

And in other cases, people have been accused of intentionally.

---

## How can we avoid violating the golden rule?

<br> <br> <br>

<center>

<img src='/module3/train-test-split.png' alt="A caption" width="100%" />

</center>

Notes:

How can we avoid this?

The most important thing is when splitting the data, we lock it away and
keep it separate from the training data.

Before we do anything, we should split our data and not bring it back
until the end of our model building.

---

<br> <br>

### Here is the workflow we’ll generally follow.

  - **Splitting**: Before doing anything, split the data `X` and `y`
    into `X_train`, `X_test`, `y_train`, `y_test` or `train_df` and
    `test_df` using `train_test_split`.  
  - **Select the best model using cross-validation**: Use
    `cross_validate` with `return_train_score = True` so that we can get
    access to training scores in each fold. (If we want to plot train vs
    validation error plots, for instance.)
  - **Scoring on test data**: Finally score on the test data with the
    chosen hyperparameters to examine the generalization performance.

Notes:

Here we return to our workflow showing the steps of how we can build
models which always starts with splitting our data right away and only
using the test set at the very end.

---

# Let’s apply what we learned\!

Notes: <br>
