---
type: slides
---

# Make - pipelines & column transformers

Notes: <br>

---

``` python
adult = pd.read_csv('data/adult.csv')
adult = adult.replace("?", np.NaN)
adult.head()
```

```out
   age workclass  fnlwgt     education  education.num marital.status         occupation   relationship   race     sex  capital.gain  capital.loss  hours.per.week native.country income
0   90       NaN   77053       HS-grad              9        Widowed                NaN  Not-in-family  White  Female             0          4356              40  United-States  <=50K
1   82   Private  132870       HS-grad              9        Widowed    Exec-managerial  Not-in-family  White  Female             0          4356              18  United-States  <=50K
2   66       NaN  186061  Some-college             10        Widowed                NaN      Unmarried  Black  Female             0          4356              40  United-States  <=50K
3   54   Private  140359       7th-8th              4       Divorced  Machine-op-inspct      Unmarried  White  Female             0          3900              40  United-States  <=50K
4   41   Private  264663  Some-college             10      Separated     Prof-specialty      Own-child  White  Female             0          3900              40  United-States  <=50K
```

``` python
train_df, test_df = train_test_split(adult, test_size=0.2, random_state=42)
```

Notes:

Remember our Adult census data from assignment 5? Well, we are bringing
back a more complete version of it.

---

``` python
X_train = train_df.drop(columns=['income'])
y_train = train_df['income']

X_test = test_df.drop(columns=['income'])
y_test = test_df['income']
```

Notes:

Remember, we are trying to predict if a row is classified with an income
\<=50K or \>50K.

---

``` python
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

Notes:

In the last slide deck, we split our features into numeric and
categorical features which we will do again for this data.

---

``` python
numeric_transformer = Pipeline(
    steps=[("imputer", SimpleImputer(strategy="median")), 
           ("scaler", StandardScaler())]
)

categorical_transformer = Pipeline(
    steps=[
        ("imputer", SimpleImputer(strategy="constant", fill_value="missing")),
        ("onehot", OneHotEncoder())]
)

preprocessor = ColumnTransformer(
    transformers=[
        ("num", numeric_transformer, numeric_features),
        ("cat", categorical_transformer, categorical_features)]
)

pipe = Pipeline(
    steps=[
        ("preprocessor", preprocessor),
        ("clf", SVC())]
)
```

Notes:

We defined transformations on the numeric and categorical features, on a
column transformer, and on a pipeline.

This seems great but it seems quite a lot.

Well, luckily there is another method and tool that is helpful in making
our life easier.

It’s call `make_pipeline()`.

---

### *make\_pipeline* syntax

``` python
from sklearn.pipeline import make_pipeline
```

``` python
numeric_transformer = make_pipeline(SimpleImputer(strategy="median"), StandardScaler())

categorical_transformer = make_pipeline(
    SimpleImputer(strategy="constant", fill_value="missing"),
    OneHotEncoder()
)

preprocessor = ColumnTransformer(
    transformers=[
        ("num", numeric_transformer, numeric_features),
        ("cat", categorical_transformer, categorical_features)
    ]
)

pipe = make_pipeline(preprocessor, SVC())
```

Notes:

Let’s create a column transformer and a pipeline using an alternative
syntax `make_pipeline`.

This is a shorthand for the `Pipeline` constructor and does not permit,
naming the steps.

Instead, their names will be set to the lowercase of their types
automatically.

---

## *make\_column\_transformer* syntax

``` python
from sklearn.compose import make_column_transformer
```

so instead of this:

``` python
preprocessor = ColumnTransformer(
    transformers=[
        ("num", numeric_transformer, numeric_features),
        ("cat", categorical_transformer, categorical_features) ],
         remainder='passthrough' 
)
```

we can do this:

``` python
preprocessor = make_column_transformer(
    (numeric_transformer, numeric_features),
    (categorical_transformer, categorical_features),
     remainder='passthrough' )
```

Notes:

Just like `make_pipeline()`, we can make our column transformer with
`make_column_transformer()`.

This eliminates the need to designate names for the numeric and
categorical transformations.

---

So our whole thing becomes:

``` python
numeric_transformer = make_pipeline(SimpleImputer(strategy="median"),
                                    StandardScaler())


categorical_transformer = make_pipeline(
                SimpleImputer(strategy="constant", fill_value="missing"),
                OneHotEncoder(),
)
preprocessor = make_column_transformer(
               (numeric_transformer, numeric_features), 
               (categorical_transformer, categorical_features)
)
pipe = make_pipeline(preprocessor, SVC())
```

``` python
scores = cross_validate(pipe, X_train, y_train, cv=5, return_train_score=True)
```

``` out
ValueError: Found unknown categories ['Holand-Netherlands'] in column 7 during transform

Detailed traceback: 
  File "<string>", line 1, in <module>
  File "/usr/local/lib/python3.8/site-packages/sklearn/utils/validation.py", line 72, in inner_f
    return f(**kwargs)
  File "/usr/local/lib/python3.8/site-packages/sklearn/model_selection/_validation.py", line 242, in cross_validate
    scores = parallel(
  File "/usr/local/lib/python3.8/site-packages/joblib/parallel.py", line 1032, in __call__
    while self.dispatch_one_batch(iterator):
  File "/usr/local/lib/python3.8/site-packages/joblib/parallel.py", line 847, in dispatch_one_batch
```

Notes:

What’s going on here??

---

``` out
ValueError: Found unknown categories ['Holand-Netherlands'] in column 7 during transform

Detailed traceback: 
  File "<string>", line 1, in <module>
  File "/usr/local/lib/python3.8/site-packages/sklearn/utils/validation.py", line 72, in inner_f
    return f(**kwargs)
  File "/usr/local/lib/python3.8/site-packages/sklearn/model_selection/_validation.py", line 242, in cross_validate
    scores = parallel(
  File "/usr/local/lib/python3.8/site-packages/joblib/parallel.py", line 1032, in __call__
    while self.dispatch_one_batch(iterator):
  File "/usr/local/lib/python3.8/site-packages/joblib/parallel.py", line 847, in dispatch_one_batch
```

``` python
X_train["native.country"].value_counts().tail(5)
```

```out
Trinadad&Tobago       12
Hungary               11
Scotland              10
Honduras               7
Holand-Netherlands     1
Name: native.country, dtype: int64
```

Notes:

Let’s look at the error message:

`Found unknown categories ['Holand-Netherlands'] in column 6 during
transform`.

There is only one instance of Holand-Netherlands.

During cross-validation, this is getting put into the validation split.

By default, `OneHotEncoder` throws an error because you might want to
know about this.

---

## How do we fix it?

``` python
numeric_transformer = make_pipeline(SimpleImputer(strategy="median"), StandardScaler())

categorical_transformer = make_pipeline(
    SimpleImputer(strategy="constant", fill_value="missing"),
    OneHotEncoder(handle_unknown="ignore"),
)

preprocessor = make_column_transformer(
    (numeric_transformer, numeric_features), 
    (categorical_transformer, categorical_features)
)

pipe = make_pipeline(preprocessor, SVC())
```

``` python
scores = cross_validate(pipe, X_train, y_train, cv=5, return_train_score=True)
pd.DataFrame(scores).mean()
```

```out
fit_time       11.432835
score_time      1.676877
test_score      0.855421
train_score     0.867792
dtype: float64
```

Notes:

Simplest fix: Pass `handle_unknown="ignore"` argument to
`OneHotEncoder`.  
\- It creates a row with all zeros.

Do you want this behaviour though?

In that case, “Holland” or “Mars” or “Hogwarts” would all be treated the
same.

Are you expecting to get many unknown categories? Do you want to be able
to distinguish between them?

With this approach, all unknown categories will be represented with all
zeros.

---

### Cases where it’s OK to break the golden rule

  - If it’s some fixed number of categories.

<!-- end list -->

``` python
all_countries = adult["native.country"].unique()
all_countries
```

```out
array(['United-States', nan, 'Mexico', 'Greece', 'Vietnam', 'China', 'Taiwan', 'India', 'Philippines', 'Trinadad&Tobago', 'Canada', 'South', 'Holand-Netherlands', 'Puerto-Rico', 'Poland', 'Iran', 'England', 'Germany', 'Italy', 'Japan', 'Hong', 'Honduras', 'Cuba', 'Ireland', 'Cambodia', 'Peru', 'Nicaragua', 'Dominican-Republic', 'Haiti', 'El-Salvador', 'Hungary', 'Columbia', 'Guatemala',
       'Jamaica', 'Ecuador', 'France', 'Yugoslavia', 'Scotland', 'Portugal', 'Laos', 'Thailand', 'Outlying-US(Guam-USVI-etc)'], dtype=object)
```

``` python
ohe_cat = OneHotEncoder(categories=all_countries)
```

Notes:

Are there any cases where it’s OK to break the golden rule?

  - If it’s some fixed number of categories.

For example, if the categories are provinces/territories of Canada, we
know the possible values and we can just specify them.

If we know the categories, this might be a reasonable time to “violate
the Golden Rule” (look at the test set) and just hard-code all the
categories.

This syntax allows you to pre-define the categories.

---

# Let’s apply what we learned\!

Notes: <br>
