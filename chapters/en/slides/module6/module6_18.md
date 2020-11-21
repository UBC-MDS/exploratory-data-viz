---
type: slides
---

# Handling categorical features: binary, ordinal and more

Notes: <br>

---

## Returning to ordinal encoding

``` python
adult = pd.read_csv('data/adult.csv')
adult = adult.replace("?", np.NaN)
train_df, test_df = train_test_split(adult, test_size=0.2, random_state=42)
X_train = train_df.drop(columns=['income'])
y_train = train_df['income']

X_test = test_df.drop(columns=['income'])
y_test = test_df['income']

numeric_features = [
    "age",
    "fnlwgt",
    "education.num",
    "capital.gain",
    "capital.loss",
    "hours.per.week"
]

categorical_features = [
    "workclass",
    "education",
    "marital.status",
    "occupation",
    "relationship",
    "race",
    "sex",
    "native.country"
]
```

``` python
train_df[categorical_features].head()
```

```out
       workclass     education      marital.status      occupation   relationship   race     sex native.country
5514     Private       HS-grad       Never-married    Craft-repair  Not-in-family  White    Male  United-States
19777    Private       HS-grad       Never-married   Other-service  Not-in-family  White  Female  United-States
10781    Private     Bachelors            Divorced    Adm-clerical      Unmarried  White  Female  United-States
32240  State-gov  Some-college  Married-civ-spouse    Adm-clerical           Wife  White  Female  United-States
9876   Local-gov     Bachelors  Married-civ-spouse  Prof-specialty        Husband  White    Male  United-States
```

``` python
train_df["education"].unique()
```

```out
array(['HS-grad', 'Bachelors', 'Some-college', '11th', '5th-6th', 'Assoc-voc', 'Masters', '9th', 'Doctorate', 'Prof-school', '7th-8th', '10th', '12th', '1st-4th', 'Assoc-acdm', 'Preschool'], dtype=object)
```

Notes:

Taking where we left off with our adult census data, it’s a good idea to
take a look at the categorical features we specified in more detail.

Some of the categorical features are truly categorical, meaning that
there is no ordinality among values.

But what about the `education` column? - Here there is actually an order
in the values and it might help to encode this column using
`OrdinalEncoder` - Example: Masters \> 10th

---

``` python
train_df["education"].unique()
```

```out
array(['HS-grad', 'Bachelors', 'Some-college', '11th', '5th-6th', 'Assoc-voc', 'Masters', '9th', 'Doctorate', 'Prof-school', '7th-8th', '10th', '12th', '1st-4th', 'Assoc-acdm', 'Preschool'], dtype=object)
```

``` python
oe = OrdinalEncoder(dtype=int)
oe.fit(X_train[["education"]]);
ed_transformed = oe.transform(X_train[["education"]])
ed_transformed = pd.DataFrame(data=ed_transformed, columns=["education_enc"], index=X_train.index)
ed_transformed.head()
```

```out
       education_enc
5514              11
19777             11
10781              9
32240             15
9876               9
```

``` python
ed_transformed['education_enc'].unique()
```

```out
array([11,  9, 15,  1,  4,  8, 12,  6, 10, 14,  5,  0,  2,  3,  7, 13])
```

Notes: Let’s use `OrdinalEncoder` and see what happens.

We fit and then transform the `education` column.

We now see that we have given each education category a value.

---

``` python
oe.categories_[-1]
```

```out
array(['10th', '11th', '12th', '1st-4th', '5th-6th', '7th-8th', '9th', 'Assoc-acdm', 'Assoc-voc', 'Bachelors', 'Doctorate', 'HS-grad', 'Masters', 'Preschool', 'Prof-school', 'Some-college'], dtype=object)
```

``` python
pd.DataFrame(data=np.arange(len(oe.categories_[0])), columns=["transformed"], index=oe.categories_[0]).head(10)
```

```out
            transformed
10th                  0
11th                  1
12th                  2
1st-4th               3
5th-6th               4
7th-8th               5
9th                   6
Assoc-acdm            7
Assoc-voc             8
Bachelors             9
```

Notes:

But which integer value corresponds to each education category?

`OrdinalEncoder` has encoded the categories by alphabetically sorting
them and then assigning integers to them in that order.

Is this what we want?

---

``` python
train_df["education"].unique()
```

```out
array(['HS-grad', 'Bachelors', 'Some-college', '11th', '5th-6th', 'Assoc-voc', 'Masters', '9th', 'Doctorate', 'Prof-school', '7th-8th', '10th', '12th', '1st-4th', 'Assoc-acdm', 'Preschool'], dtype=object)
```

``` python
education_levels = ['Preschool', '1st-4th', '5th-6th', '7th-8th', 
                    '9th', '10th', '11th', '12th', 'HS-grad',
                    'Prof-school', 'Assoc-voc', 'Assoc-acdm', 
                    'Some-college', 'Bachelors', 'Masters', 'Doctorate']
```

``` python
assert set(education_levels) == set(train_df["education"].unique())
```

Notes:

Instead, let’s order them manually.

We can use the set datatype that we learned in Programming in Python for
Data Science to make sure that each has been accounted for.

---

``` python
oe = OrdinalEncoder(categories=[education_levels], dtype=int)
oe.fit(X_train[["education"]]);
ed_transformed = oe.transform(X_train[["education"]])
ed_transformed = pd.DataFrame(data=ed_transformed, columns=["education_enc"], index=X_train.index)
oe.categories_
```

```out
[array(['Preschool', '1st-4th', '5th-6th', '7th-8th', '9th', '10th', '11th', '12th', 'HS-grad', 'Prof-school', 'Assoc-voc', 'Assoc-acdm', 'Some-college', 'Bachelors', 'Masters', 'Doctorate'], dtype=object)]
```

``` python
pd.DataFrame(data=np.arange(len(oe.categories_[0])), columns=["transformed"], index=oe.categories_[0]).head(10)
```

```out
             transformed
Preschool              0
1st-4th                1
5th-6th                2
7th-8th                3
9th                    4
10th                   5
11th                   6
12th                   7
HS-grad                8
Prof-school            9
```

Notes:

Ah\! That looks better.

---

``` python
numeric_features = ['age', 'fnlwgt', 'capital.gain', 
                    'capital.loss', 'hours.per.week']
categorical_features = ['workclass', 'marital.status', 'occupation', 
                        'relationship', 'race', 'sex', 'native.country']
ordinal_features = ['education']
target_column = 'income'
```

Notes:

So now when we are sorting our columns into their respective feature
types, we need to separate

---

``` python
numeric_transformer = make_pipeline(SimpleImputer(strategy="median"), StandardScaler())

categorical_transformer = make_pipeline(
    SimpleImputer(strategy="constant", fill_value="missing"),
    OneHotEncoder(handle_unknown="ignore")
)

ordinal_transformer = make_pipeline(
    SimpleImputer(strategy="constant", fill_value="missing"),
    OrdinalEncoder(categories=[education_levels], dtype=int,)
)

preprocessor = make_column_transformer(
        (numeric_transformer, numeric_features),
        (categorical_transformer, categorical_features),
        (ordinal_transformer, ordinal_features)
)
pipe = make_pipeline(preprocessor, SVC())
```

Notes:

This means that we need to make a separate pipeline for our ordinal
columns. We then specify this transformation in or
`make_column_transformer()` function.

---

``` python
scores = cross_validate(pipe, X_train, y_train, return_train_score=True)
pd.DataFrame(scores).mean()
```

```out
fit_time       8.157877
score_time     1.390675
test_score     0.851927
train_score    0.853348
dtype: float64
```

Notes:

This then produces new scores.

---

## Binary Features

``` python
X_train.head()
```

```out
       age  workclass  fnlwgt     education  education.num      marital.status      occupation   relationship   race     sex  capital.gain  capital.loss  hours.per.week native.country
5514    26    Private  256263       HS-grad              9       Never-married    Craft-repair  Not-in-family  White    Male             0             0              25  United-States
19777   24    Private  170277       HS-grad              9       Never-married   Other-service  Not-in-family  White  Female             0             0              35  United-States
10781   36    Private   75826     Bachelors             13            Divorced    Adm-clerical      Unmarried  White  Female             0             0              40  United-States
32240   22  State-gov   24395  Some-college             10  Married-civ-spouse    Adm-clerical           Wife  White  Female             0             0              20  United-States
9876    31  Local-gov  356689     Bachelors             13  Married-civ-spouse  Prof-specialty        Husband  White    Male             0             0              40  United-States
```

``` python
X_train['sex'].unique()
```

```out
array(['Male', 'Female'], dtype=object)
```

Notes:

Let’s take another look at our columns.

If we look at the values for `sex`, they were collected in a binary way.

Note that this representation reflects how the data were collected and
is not meant to imply that, for example, gender is binary.

---

``` python
ohe = OneHotEncoder(sparse=False, dtype=int)
ohe.fit(X_train[["sex"]])
```

```out
OneHotEncoder(dtype=<class 'int'>, sparse=False)
```

``` python
ohe_df = pd.DataFrame(data=ohe.transform(X_train[["sex"]]), columns=ohe.get_feature_names(["sex"]), index=X_train.index)
ohe_df
```

```out
       sex_Female  sex_Male
5514            0         1
19777           1         0
10781           1         0
32240           1         0
9876            0         1
...           ...       ...
29802           0         1
5390            0         1
860             0         1
15795           0         1
23654           0         1

[26048 rows x 2 columns]
```

Notes:

When we do one-hot encoding on this feature, we get 2 separate columns
which aren’t particularly necessary.

---

``` python
ohe = OneHotEncoder(sparse=False, dtype=int, drop="if_binary") # <-- see here
ohe.fit(X_train[["sex"]])
```

```out
OneHotEncoder(drop='if_binary', dtype=<class 'int'>, sparse=False)
```

``` python
ohe_df = pd.DataFrame(data=ohe.transform(X_train[["sex"]]), columns=ohe.get_feature_names(["sex"]), index=X_train.index)
ohe_df
```

```out
       sex_Male
5514          1
19777         0
10781         0
32240         0
9876          1
...         ...
29802         1
5390          1
860           1
15795         1
23654         1

[26048 rows x 1 columns]
```

Notes:

So, for this feature with binary values, we can use an argument called
`drop` within `OneHotEncoder` and set it to `"if_binary"`.

Now we see that after one-hot encoding we only get a single column where
the encoder has arbitrarily chosen one of the two categories based on
the sorting.

In this case, alphabetically it was \[Female, Male\] and it drops the
first one.

---

``` python
numeric_features = ['age', 'fnlwgt', 'capital.gain', 
                    'capital.loss', 'hours.per.week']
categorical_features = ['workclass', 'marital.status', 'occupation', 
                        'relationship', 'race', 'native.country']
ordinal_features = ['education']
binary_features = ['sex']
target_column = 'income'
```

Notes:

Again we must separate our binary feature from the rest.

---

``` python
numeric_transformer = make_pipeline(SimpleImputer(strategy="median"), StandardScaler())

categorical_transformer = make_pipeline(
    SimpleImputer(strategy="constant", fill_value="missing"),
    OneHotEncoder(handle_unknown="ignore")
)
ordinal_transformer = make_pipeline(
    SimpleImputer(strategy="constant", fill_value="missing"),
    OrdinalEncoder(categories=[education_levels], dtype=int,)
)
binary_transformer = make_pipeline(
    SimpleImputer(strategy="constant", fill_value="missing"),
    OneHotEncoder(drop="if_binary", dtype=int)
    )
preprocessor = make_column_transformer(
        (numeric_transformer, numeric_features),
        (categorical_transformer, categorical_features),
        (ordinal_transformer, ordinal_features),
        (binary_transformer, binary_features)
)
pipe = make_pipeline(preprocessor, SVC())
```

Notes:

And just like we said for ordinal values, when we make our pipelines, we
need to make a separate one for the binary columns and add it to our
`make_column_transformer()`.

---

``` python
scores = cross_validate(pipe, X_train, y_train, return_train_score=True)
pd.DataFrame(scores)
```

```out
   fit_time  score_time  test_score  train_score
0  8.985361    1.437713    0.850864     0.853153
1  9.101118    1.505836    0.844530     0.855792
2  9.146738    1.387174    0.859693     0.850609
3  8.699487    1.388320    0.849299     0.853832
4  8.037708    1.349813    0.854291     0.853448
```

``` python
pd.DataFrame(scores).mean()
```

```out
fit_time       8.794082
score_time     1.413771
test_score     0.851735
train_score    0.853367
dtype: float64
```

Notes:

---

## One-hot encoding with many categories

``` python
X_train["native.country"].value_counts()
```

```out
United-States                 23315
Mexico                          512
Philippines                     165
Germany                         115
Canada                           97
                              ...  
Outlying-US(Guam-USVI-etc)       12
Hungary                          11
Scotland                         10
Honduras                          7
Holand-Netherlands                1
Name: native.country, Length: 41, dtype: int64
```

Notes:

This may be too detailed, and the amount of data is very limited for
most of these countries.

Can you really learn from 11 examples?

Grouping them into bigger categories such as “South America” or “Asia”
or having an “other” category for rare cases could be a better solution.

---

### Do we actually want to use certain features for prediction?

``` python
X_train.head()
```

```out
       age  workclass  fnlwgt     education  education.num      marital.status      occupation   relationship   race     sex  capital.gain  capital.loss  hours.per.week native.country
5514    26    Private  256263       HS-grad              9       Never-married    Craft-repair  Not-in-family  White    Male             0             0              25  United-States
19777   24    Private  170277       HS-grad              9       Never-married   Other-service  Not-in-family  White  Female             0             0              35  United-States
10781   36    Private   75826     Bachelors             13            Divorced    Adm-clerical      Unmarried  White  Female             0             0              40  United-States
32240   22  State-gov   24395  Some-college             10  Married-civ-spouse    Adm-clerical           Wife  White  Female             0             0              20  United-States
9876    31  Local-gov  356689     Bachelors             13  Married-civ-spouse  Prof-specialty        Husband  White    Male             0             0              40  United-States
```

``` python
X_train["race"].unique()
```

```out
array(['White', 'Asian-Pac-Islander', 'Black', 'Amer-Indian-Eskimo', 'Other'], dtype=object)
```

Notes:

Do you want to use `race` in prediction?

Remember that the systems you build are going to be used in some
applications.

It’s extremely important to be mindful of the consequences of including
certain features in your predictive model.

Splitting `race` into 4 races and an `Other` group seems quite
insensitive and problematic to say the least.

Dropping the feature to avoid racial biases, would be a strong
suggestion.

---

# Let’s apply what we learned\!

Notes: <br>
