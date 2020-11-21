---
type: slides
---

# One-hot encoding

Notes: <br>

---

## From before …

``` python
encoding_view
```

```out
      language  language_enc
0      English             0
1   Vietnamese             5
2      English             0
3     Mandarin             3
4      English             0
5      English             0
6     Mandarin             3
7      English             0
8   Vietnamese             5
9     Mandarin             3
10      French             1
11     Spanish             4
12    Mandarin             3
13       Hindi             2
```

Notes:

In the last section, we saw that we can transform our categorical data
into numeric data using `OrdinalEncoder`. Seems pretty standard and easy
enough but we asked you a question in the last slide deck if we should
always use this method.

The answer is no. Can you see why?

---

## What wrong with this?

``` python
oe.categories_
```

```out
[array(['English', 'French', 'Hindi', 'Mandarin', 'Spanish', 'Vietnamese'], dtype=object)]
```

``` python
encoding_view.drop_duplicates()
```

```out
      language  language_enc
0      English             0
1   Vietnamese             5
3     Mandarin             3
10      French             1
11     Spanish             4
13       Hindi             2
```

Notes:

What’s the problem with this approach?

If you look at the original values and compare them to the new
transformed ones what do you notice?

We have imposed ordinality on the categorical data.

For example, imagine when you are calculating distances. Is it fair to
say that French and Hindi are closer to one another than French and
Spanish?

In general, label encoding is useful if there is ordinality in your data
and capturing it is important for your problem, e.g., `[cold, warm,
hot]`.

---

## One-hot encoding (OHE)

Ordinal encoding:

``` python
encoding_view[['language_enc']].head()
```

```out
   language_enc
0             0
1             5
2             0
3             3
4             0
```

One-hot encoding:

``` python
one_hot_df.head()
```

```out
   language_English  language_French  language_Hindi  language_Mandarin  language_Spanish  language_Vietnamese
0               1.0              0.0             0.0                0.0               0.0                  0.0
1               0.0              0.0             0.0                0.0               0.0                  1.0
2               1.0              0.0             0.0                0.0               0.0                  0.0
3               0.0              0.0             0.0                1.0               0.0                  0.0
4               1.0              0.0             0.0                0.0               0.0                  0.0
```

Notes:

So what do we do when our values are not truly ordinal categories?

We can do something called **One hot encoding**\!

Rather than assign integer labels to our data, we use it to create new
binary columns to represent our categories.

Before we would transform one original column into one transformed
column but in this case, we will transform one column into several
transformed columns, one per category.

One-hot encoding creates new binary columns to represent our categories.

If we have 𝑐 categories in our column, we create 𝑐 new binary columns to
represent those categories. - Example: Imagine a language column which
has the information on whether you

  - We can use sklearn’s
    <a href="https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.OneHotEncoder.html" target="_blank">`OneHotEncoder`</a>

---

## How to one-hot encode

``` python
X_toy
```

```out
      language
0      English
1   Vietnamese
2      English
3     Mandarin
4      English
5      English
6     Mandarin
7      English
8   Vietnamese
9     Mandarin
10      French
11     Spanish
12    Mandarin
13       Hindi
```

Let’s take our `X_toy` and one-hot encode it.

---

``` python
from sklearn.preprocessing import OneHotEncoder

ohe = OneHotEncoder(sparse=False, dtype='int')
ohe.fit(X_toy);
X_toy_ohe = ohe.transform(X_toy)

X_toy_ohe
```

```out
array([[1, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 1],
       [1, 0, 0, 0, 0, 0],
       [0, 0, 0, 1, 0, 0],
       [1, 0, 0, 0, 0, 0],
       [1, 0, 0, 0, 0, 0],
       [0, 0, 0, 1, 0, 0],
       [1, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 1],
       [0, 0, 0, 1, 0, 0],
       [0, 1, 0, 0, 0, 0],
       [0, 0, 0, 0, 1, 0],
       [0, 0, 0, 1, 0, 0],
       [0, 0, 1, 0, 0, 0]])
```

Notes:

We import the `OneHotEncoder` transformer from `sklearn` and then build
our transformer.

We fit and transform the data and exactly as before, our output from the
`transform` function is a NumPy array.

---

``` python
pd.DataFrame(
    data=X_toy_ohe,
    columns=enc.get_feature_names(['language']),
    index=X_toy.index,
)
```

```out
    language_English  language_French  language_Hindi  language_Mandarin  language_Spanish  language_Vietnamese
0                  1                0               0                  0                 0                    0
1                  0                0               0                  0                 0                    1
2                  1                0               0                  0                 0                    0
3                  0                0               0                  1                 0                    0
4                  1                0               0                  0                 0                    0
5                  1                0               0                  0                 0                    0
6                  0                0               0                  1                 0                    0
7                  1                0               0                  0                 0                    0
8                  0                0               0                  0                 0                    1
9                  0                0               0                  1                 0                    0
10                 0                1               0                  0                 0                    0
11                 0                0               0                  0                 1                    0
12                 0                0               0                  1                 0                    0
13                 0                0               1                  0                 0                    0
```

Notes:

We can convert it to a Pandas dataframe and see that instead of 1
column, we have 6\!

---

``` python
X_train.head()
```

```out
       longitude  latitude  housing_median_age  households  median_income ocean_proximity  rooms_per_household  bedrooms_per_household  population_per_household
6051     -117.75     34.04                22.0       602.0         3.1250          INLAND             4.897010                1.056478                  4.318937
20113    -119.57     37.94                17.0        20.0         3.4861          INLAND            17.300000                6.500000                  2.550000
14289    -117.13     32.74                46.0       708.0         2.6604      NEAR OCEAN             4.738701                1.084746                  2.057910
13665    -117.31     34.02                18.0       285.0         5.2139          INLAND             5.733333                0.961404                  3.154386
14471    -117.23     32.88                18.0      1458.0         1.8580      NEAR OCEAN             3.817558                1.004801                  4.323045
```

``` python
X_train['ocean_proximity'].unique()
```

```out
array(['INLAND', 'NEAR OCEAN', '<1H OCEAN', 'NEAR BAY', 'ISLAND'], dtype=object)
```

Notes:

Ok, so what should we use on our California housing data?

`ocean_proximity` seems like an ordinal feature, however, looking at the
possible categories seems a little less clear.

How would you order these?

Should `NEAR OCEAN` be higher in value than `NEAR BAY`?

In unsure times, maybe one-hot encoding is the better option.

---

## One hot encoding the California housing data

``` python
ohe = OneHotEncoder(sparse=False, dtype="int")
ohe.fit(X_train[["ocean_proximity"]])
```

```out
OneHotEncoder(dtype='int', sparse=False)
```

``` python
X_imp_ohe_train = ohe.transform(X_train[["ocean_proximity"]])

X_imp_ohe_train
```

```out
array([[0, 1, 0, 0, 0],
       [0, 1, 0, 0, 0],
       [0, 0, 0, 0, 1],
       ...,
       [1, 0, 0, 0, 0],
       [0, 0, 0, 1, 0],
       [0, 1, 0, 0, 0]])
```

Notes:

Ok great we’ve transformed our data, however, Just like before, the
transformer outputs a NumPy array.

---

``` python
transformed_ohe = pd.DataFrame(
    data=X_imp_ohe_train,
    columns=ohe.get_feature_names(['ocean_proximity']),
    index=X_train.index,
)

transformed_ohe.head()
```

```out
       ocean_proximity_<1H OCEAN  ocean_proximity_INLAND  ocean_proximity_ISLAND  ocean_proximity_NEAR BAY  ocean_proximity_NEAR OCEAN
6051                           0                       1                       0                         0                           0
20113                          0                       1                       0                         0                           0
14289                          0                       0                       0                         0                           1
13665                          0                       1                       0                         0                           0
14471                          0                       0                       0                         0                           1
```

Notes:

We can transform it into a dataframe to see the values more clearly.

### But ….Now What?

How do we put this together with other columns in the data before
fitting the model?

We want to apply different transformations to different columns.

We will explain that in the next section.

---

# Let’s apply what we learned\!

Notes: <br>
