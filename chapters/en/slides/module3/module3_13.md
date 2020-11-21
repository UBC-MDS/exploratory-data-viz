---
type: slides
---

# Overfitting and underfitting

Notes: <br>

---

We’re going to think about 3 types of errors:

  - **score\_train**: is our training score (or mean train score from
    cross-validation).

<br>

  - **score\_valid** is our validation score (or mean validation score
    from cross-validation).

<br>

  - **score\_test** is our test score.

Notes:

We’ve talked about the different types of splits but we’ve only briefly
discussed scores and the different types of scores that we receive that
correspond to these splits. We saw in cross-validation that there were
train and validation scores and what happens if they did not align with
each other.

How do we diagnose the problem?

We’re going to think about 3 types of scores:

  - **Training score **: The score that our model gets on the same data
    that it was trained on. (seen data - training data)
  - **Validation score**: The mean validation score from
    cross-validation).
  - **Test score**: This is the score from the data that we locked away.

---

``` python
df = pd.read_csv("data/canada_usa_cities.csv")
X = df.drop(columns=["country"])
y = df["country"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=123)
```

Notes:

Let’s bring back our Canadian and United States cities’ data to help
explain the concepts of overfitting and underfitting.

---

## Overfitting

``` python
model = DecisionTreeClassifier()
scores = cross_validate(model, X_train, y_train, cv=10, return_train_score=True)
print("Train score: " + str(round(scores["train_score"].mean(), 2)))
print("Validation score: " + str(round(scores["test_score"].mean(), 2)))
```

``` out
Train score: 1.0
Validation score: 0.81
```

<img src="/module3/module3_13/unnamed-chunk-3-1.png" width="55%" />

Notes:

Using a decision tree with no specified max\_depth, can help explain the
phenomenon is called ***overfitting***.

Overfitting occurs when our model is overly specified to the particular
training data and often leads to bad results.

When our model fits the training data well and therefore the training
score is high, however, the model does not generalize to the validation
set as well and the validation error is much higher.

This is a sign of overfitting.

The train score is high but the validation score is much lower.

The gap between the train and the validation score is bigger.

This produces more severe results when the training data is minimal or
when the model’s complexity is high.

---

## Underfitting

``` python
model = DecisionTreeClassifier(max_depth=1)

scores = cross_validate(model, X_train, y_train, cv=10, return_train_score=True)
print("Train score: " + str(round(scores["train_score"].mean(), 2)))
print("Validation score: " + str(round(scores["test_score"].mean(), 2)))
```

``` out
Train score: 0.83
Validation score: 0.81
```

<img src="/module3/module3_13/unnamed-chunk-4-1.png" width="55%" />

Notes:

Underfitting is somewhat the opposite of overfitting in the sense that
it occurs when the model is not complex enough.

Using a decision tree with a max\_depth of 1, we can explain the
phenomenon.

Underfitting is when our model is too simple (`DecisionTreeClassifier`
with max\_depth=1 or `DummyClassifier`).

The model doesn’t capture the patterns in the training data and the
training score is not that high.

The model doesn’t fit the data well and hence the training score is not
high as well as the validation being very low as well.

Both train and validation scores are low and the gap between train and
validation scores is low as well.

---

<center>

<img src="/module3/over_under.png"  width = "80%" alt="404 image" />

</center>

Standard question to ask ourselves: ***Which of these scenarios am I
in?***

### How can we figure this out?

***Score\_train*** and ***Score\_valid***.

  - If they are very far apart → more likely **overfitting**.
      - Try decreasing model complexity.
  - If they are very close together → more likely **underfitting**.
      - Try increasing model complexity.

Notes:

This plot explains the complex curve attempting to hit multiple plots
versus a simple line that has a lower success of predicting the
examples.

The question to ask is which situation are we in?

Looking at the scores is a very good diagnostic to answer this question.

If the scores are very far apart then we are more likely
**overfitting**.

  - In this case, the solution would be to reduce the complexity of the
    model.

If the scores are very close together then we are more likely
**underfitting**.

  - Attempting to increase the model’s complexity could help this
    situation.

---

# Let’s apply what we learned\!

Notes: <br>
