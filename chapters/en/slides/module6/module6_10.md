---
type: slides
---

# *ColumnTransformer*

Notes: <br>

---

## Problem: We have different transformations for different columns

Before we fit our model, we want to apply different transformations on
different columns.

  - Numeric columns:
      - imputation
      - scaling
  - Categorical columns:
      - imputation  
      - one-hot encoding

Notes:

We can’t use a pipeline since not all the transformations are occurring
on every feature.

We could do so without but then we would be violating the Golden Rule of
Machine learning when we did cross-validation.

So we need a new tool and it’s called `ColumnTransformer`\!

---

## *ColumnTransformer*

<br> <br>

<center>

<img src="/module6/column-transformer.png"  width = "90%" alt="404 image" />

</center>

<a href="https://amueller.github.io/COMS4995-s20/slides/aml-04-preprocessing/#37" target="_blank">Adapted
from here. </a>

Notes:

sklearn’s
<a href="https://scikit-learn.org/stable/modules/generated/sklearn.compose.ColumnTransformer.html" target="_blank">`ColumnTransformer`</a>
makes this more manageable.

A big advantage here is that we build all our transformations together
into one object, and that way we’re sure we do the same operations to
all splits of the data.

Otherwise, we might, for example, do the OHE on both train and test but
forget to scale the test data.

---

``` python
from sklearn.compose import ColumnTransformer
```

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

Notes:

We import `ColumnTransformer` from the `sklearn` library.

And we will have to look at our data.

---

``` python
X_train.dtypes
```

```out
longitude                   float64
latitude                    float64
housing_median_age          float64
households                  float64
median_income               float64
ocean_proximity              object
rooms_per_household         float64
bedrooms_per_household      float64
population_per_household    float64
dtype: object
```

``` python
numeric_features = [ "longitude",
                     "latitude",
                     "housing_median_age",
                     "households",
                     "median_income",
                     "rooms_per_household",
                     "bedrooms_per_household",
                     "population_per_household"]
                     
categorical_features = ["ocean_proximity"]
```

Notes:

We must first identify the categorical and numeric columns.

---

``` python
numeric_transformer = Pipeline(
    steps=[("imputer", SimpleImputer(strategy="median")), 
           ("scaler", StandardScaler())]
)

categorical_transformer = Pipeline(
    steps=[("imputer", SimpleImputer(strategy="constant", fill_value="missing")),
           ("onehot", OneHotEncoder(handle_unknown="ignore"))]
)
```

Notes:

Next, we build a pipeline for our dataset.

This means we need to make at least 2 preprocessing pipelines; one for
the categorical and one for the numeric features\!

(If we needed to use the ordinal encoder for binary data or ordinal
features then we would need a third.)

---

``` python
col_transformer = ColumnTransformer(
    transformers=[
        ("numeric", numeric_transformer, numeric_features),
        ("categotical", categorical_transformer, categorical_features)
    ], 
    remainder='passthrough'    
)
```

Notes:

We then call the numeric and categorical features with their respective
transformers in `ColumnTransformer()`.

The `ColumnTransformer` syntax is somewhat similar to that of `Pipeline`
in that you pass in a list of tuples.

But This time, each tuple has 3 values instead of 2: (name of the step,
transformer object, list of columns)

A big advantage here is that we build all our transformations together
into one object, and that way we’re sure we do the same operations to
all splits of the data.

Otherwise, we might, for example, do the OHE on both train and test but
forget to scale the test data.

`remainder="passthrough"`:

  - The `ColumnTransformer` will automatically remove columns that are
    not being transformed.  
  - We can use `remainder="passthrough"` of `ColumnTransformer` to keep
    the other columns intact.

---

``` python
col_transformer.fit(X_train)
```

```out
ColumnTransformer(remainder='passthrough',
                  transformers=[('numeric',
                                 Pipeline(steps=[('imputer',
                                                  SimpleImputer(strategy='median')),
                                                 ('scaler', StandardScaler())]),
                                 ['longitude', 'latitude', 'housing_median_age',
                                  'households', 'median_income',
                                  'rooms_per_household',
                                  'bedrooms_per_household',
                                  'population_per_household']),
                                ('categotical',
                                 Pipeline(steps=[('imputer',
                                                  SimpleImputer(fill_value='missing',
                                                                strategy='constant')),
                                                 ('onehot',
                                                  OneHotEncoder(handle_unknown='ignore'))]),
                                 ['ocean_proximity'])])
```

``` python
X_train_pp = col_transformer.transform(X_train)
```

Notes:

When we `fit` with the `col_transformer`, it calls `fit` on ***all***
the transformers.

And when we transform with the preprocessor, it calls `transform` on
***all*** the transformers.

---

``` python
onehot_cols = col_transformer.named_transformers_["categotical"].named_steps["onehot"].get_feature_names(categorical_features)
onehot_cols
```

```out
array(['ocean_proximity_<1H OCEAN', 'ocean_proximity_INLAND', 'ocean_proximity_ISLAND', 'ocean_proximity_NEAR BAY', 'ocean_proximity_NEAR OCEAN'], dtype=object)
```

``` python
columns = numeric_features + list(onehot_cols)
columns
```

```out
['longitude', 'latitude', 'housing_median_age', 'households', 'median_income', 'rooms_per_household', 'bedrooms_per_household', 'population_per_household', 'ocean_proximity_<1H OCEAN', 'ocean_proximity_INLAND', 'ocean_proximity_ISLAND', 'ocean_proximity_NEAR BAY', 'ocean_proximity_NEAR OCEAN']
```

Notes:

We can get the new names of the columns that were generated by the
one-hot encoding.

Combining this with the numeric feature names gives us all the column
names.

---

``` python
main_pipe = Pipeline(
    steps=[
        ("preprocessor", col_transformer), # <-- this is the ColumnTransformer!
        ("reg", KNeighborsRegressor())])
```

``` python
with_categorical_scores = cross_validate(main_pipe, X_train, y_train, return_train_score=True)
pd.DataFrame(with_categorical_scores)
```

```out
   fit_time  score_time  test_score  train_score
0  0.054538    0.324174    0.695818     0.801659
1  0.033856    0.251477    0.707483     0.799575
2  0.035995    0.303936    0.713788     0.795944
3  0.033926    0.271824    0.686938     0.801232
4  0.039747    0.257504    0.724608     0.832498
```

Notes:

Now we use a main pipeline to transform all the data and build a model.

Scaling and one hot encoding are now applied at the same time\!

We can then use `cross_validate()` and find our mean training and
validation scores\!

---

``` python
pipe = Pipeline([
        ("imputer", SimpleImputer(strategy="median")),
        ("scaler", StandardScaler()),
        ("reg", KNeighborsRegressor())])
        
pipe.fit(X_train.drop(columns=['ocean_proximity']), y_train);
```

``` python
no_categorical_scores = cross_validate(pipe, X_train.drop(columns=['ocean_proximity']), y_train, return_train_score=True)
pd.DataFrame(no_categorical_scores)
```

```out
   fit_time  score_time  test_score  train_score
0  0.023517    0.195199    0.693883     0.792395
1  0.022911    0.164879    0.685017     0.789108
2  0.024052    0.181865    0.694409     0.787796
3  0.021832    0.184389    0.677055     0.792444
4  0.020851    0.141030    0.714494     0.823421
```

Notes:

Let’s compare what we did before without ColumTransformer and without
categorical columns and observe how adding the `ocean_proximity` column
changes our results.

---

``` python
pd.DataFrame(no_categorical_scores).mean()
```

```out
fit_time       0.022633
score_time     0.173472
test_score     0.692972
train_score    0.797033
dtype: float64
```

``` python
pd.DataFrame(with_categorical_scores).mean()
```

```out
fit_time       0.039612
score_time     0.281783
test_score     0.705727
train_score    0.806182
dtype: float64
```

Notes:

We can see here that adding and one hot encoding our `ocean_proximity`
column improves our score.

This was a single column.

If we had more columns, we could improve our scores in a much more
substantial way instead of throwing the information away which is what
we have been doing\!

---

``` python
from sklearn import set_config
set_config(display='diagram')
main_pipe
```

```out
Pipeline(steps=[('preprocessor',
                 ColumnTransformer(remainder='passthrough',
                                   transformers=[('numeric',
                                                  Pipeline(steps=[('imputer',
                                                                   SimpleImputer(strategy='median')),
                                                                  ('scaler',
                                                                   StandardScaler())]),
                                                  ['longitude', 'latitude',
                                                   'housing_median_age',
                                                   'households',
                                                   'median_income',
                                                   'rooms_per_household',
                                                   'bedrooms_per_household',
                                                   'population_per_household']),
                                                 ('categotical',
                                                  Pipeline(steps=[('imputer',
                                                                   SimpleImputer(fill_value='missing',
                                                                                 strategy='constant')),
                                                                  ('onehot',
                                                                   OneHotEncoder(handle_unknown='ignore'))]),
                                                  ['ocean_proximity'])])),
                ('reg', KNeighborsRegressor())])
```

Notes:

Since there are a lot of steps happening we can use `set_config` from
sklearn and it will display a diagram of what is going on in our main
pipeline.

---

<center>

<img src="/module6/pipeline.png"  width = "90%" alt="404 image" />

</center>

Notes:

We can also look at this image which shows the more generic version of
what happens in `ColumnTransformer` and where it stands in our main
pipeline.

---

#### Do we need to preprocess categorical values in the target column?

  - Generally, there is no need for this when doing classification.
  - `sklearn` is fine with categorical labels (y-values) for
    classification problems.

Notes:

<br>

---

# Let’s apply what we learned\!

Notes: <br>
