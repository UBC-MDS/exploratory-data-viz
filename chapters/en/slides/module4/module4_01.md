---
type: slides
---

# Terminology with analogy-based models

Notes: <br>

---

## Analogy-based models

<br> <br>

<img src='/module4/knn-motivation.png' width="100%">
<a href="https://vipl.ict.ac.cn/en/database.php" target="_blank">Attribution</a>

Notes:

Suppose we are given the following training examples with corresponding
labels and are asked to label a given test example.

An intuitive way to classify the test example is by finding the most
“similar” example(s) from the training set and using that label for
the test example.

In the previous module, we saw that in supervised machine learning, we
are given some training data.

We are given `X` and `y`. We learn a mapping function from this training
data than given a new unseen example, we predict the target of this new
example using our learn-mapping function.

In the case of decision trees, we did this by asking a series of
questions on some features and some thresholds on future values.

Another intuitive way to do this is by using the notion of analogy.

For example, suppose we are given many images and their labels.

So, our `X` in is a set of pictures and our `y` is a set of names
associated with those pictures.

Then we are given a new unseen test example, a picture in this
particular case.

We want to find out the label for this new test picture.

An intuitive way to do this is by finding the most similar picture in
our training set and using the label of the most similar picture as the
label of this new test example.

That’s the basic idea behind analogy based algorithms.

---

## Analogy-based algorithms in practice

  - <a href="https://www.hertasecurity.com/en" target="_blank">Herta’s
    High-tech Facial Recognition</a>

<center>

<img src="/module4/face_rec.png"  width = "20%" alt="404 image" />

</center>

  - Recommendation systems

<center>

<img src="/module4/book_rec.png"  width = "90%" alt="404 image" />

</center>

Notes:

Here, I am showing two examples of analogy based algorithms in practice.

We can see this idea being used in facial recognition systems and
recommendation systems.

For example, we can imagine having a bunch of faces on our watchlist and
a new face comes up.

We want to check whether that new face is in our watchlist or not.

Another example is recommendation systems. In recommendation systems, we
usually want to find out similar users or similar items.

We are not going to look into these applications in this particular
course but it’s worth mentioning these applications because
analogy-based algorithms are used the most in these contexts.

---

### Geometric view of tabular data and dimensions

<center>

<img src="/module4/3d-table.png"  width = "100%" alt="404 image" />

</center>

Notes: In analogy based algorithms, our goal is to come up with a way to
find similarity between examples. For this, we need some terminology.

In analogy based algorithms, it’s useful to think of data as points in a
high dimensional space.

So, given `X`, each feature in it is a dimension and each example is a
point in the dimensional space.

In this example, we have three features; speed attack and defense. Each
example is a point in this three-dimensional space.

---

``` python
cities_df = pd.read_csv("data/canada_usa_cities.csv")
train_df, test_df = train_test_split(cities_df, test_size=0.2, random_state=123)
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

Now let’s go back to our Canada and USA cities data.

How many dimensions (features) are there in this cities data?

If you said 2, then you are off to a good start.

The two features are `longitude` and `latitude`.

Each example would be a point in two-dimensional space.

---

``` python
cities_plot = alt.Chart(train_df).mark_circle(size=20, opacity=0.6).encode(
    alt.X('longitude:Q', scale=alt.Scale(domain=[-140, -40])),
    alt.Y('latitude:Q', scale=alt.Scale(domain=[20, 60])),
    alt.Color('country:N', scale=alt.Scale(domain=['Canada', 'USA'],
                                           range=['red', 'blue']))
)
cities_plot
```
<img src="/module4/cities_plot.png" alt="A caption" width="50%" />

Notes:

We can visualize these 2 dimensions in a 2D graph.

---

### Dimensions

``` python
grades_df = pd.read_csv("data/quiz2-grade-toy-classification.csv")
grades_df.head()
```

```out
   ml_experience  class_attendance  lab1  lab2  lab3  lab4  quiz1   quiz2
0              1                 1    92    93    84    91     92      A+
1              1                 0    94    90    80    83     91  not A+
2              0                 0    78    85    83    80     80  not A+
3              0                 1    91    94    92    91     89      A+
4              0                 1    77    83    90    92     85      A+
```

``` python
X = grades_df.drop(columns=['quiz2'])
X.shape[1]
```

```out
7
```

Notes:

Remember the quiz dataset that we’ve seen a few times?

How many dimensions (features) would this dataset have?

The number of features in the grades dataset can be checked using
`.shape`.

If we drop the target column and create `X`, `.shape` can be used to
give us the dimension of our dataset.

This time we have 7-dimensional data.

---

### Dimensions in ML problems

Dimensions:

  - Dimensions≈20: Low dimensional
  - Dimensions≈1000: Medium dimensional
  - Dimensions≈100,000: High dimensional

Notes:

We can visualize examples when dimensions are less than or equal to
three.

That said, in machine learning, we usually deal with high dimensional
problems where examples are hard to visualize.

In machine learning twenty is considered low dimensional.

One thousand as a medium dimensional.

And one hundred thousand as high dimensional.

It’s not very hard to think of problems where the dimensions are perhaps
one hundred thousand.

For instance, if we’re dealing with images, then each feature or each
dimension would be a pixel in our image.

Or think about an email spam classification system where each unique
word from all the emails that our email received is a feature.

We can imagine that the number of features would definitely be around
one hundred thousand or more\!

---

### Feature vectors

**Feature vector**: a vector composed of feature values associated with
an example.

``` python
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

An example feature vector from the cities dataset:

``` python
train_df.drop(columns=["country"]).iloc[0].round(2).to_numpy()
```

```out
array([-76.48,  44.23])
```

An example feature vector from the grading dataset:

``` python
grades_df.drop(columns=['quiz2']).iloc[0].round(2).to_numpy()
```

```out
array([ 1,  1, 92, 93, 84, 91, 92])
```

Notes:

Let’s look at feature records feature vectors now. They are composed of
feature values associated with an example.

Here is an example of the feature vector from our cities data.

In this particular case, the size of our feature vector is 2.

And we have values associated with each feature (`latitude` and
`longitude`) in this feature vector.

In the feature vector from our toy quiz2 classifications data, our
feature vector is of size 7.

---

# Let’s apply what we learned\!

Notes: <br>
