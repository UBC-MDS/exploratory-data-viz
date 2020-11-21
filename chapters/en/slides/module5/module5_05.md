---
type: slides
---

# Preprocessing with imputation

Notes: <br>

---

## Case study: California housing prices

``` python
housing_df = pd.read_csv("data/housing.csv")
train_df, test_df = train_test_split(housing_df, test_size=0.1, random_state=123)

train_df.head()
```

```out
       longitude  latitude  housing_median_age  total_rooms  total_bedrooms  population  households  median_income  median_house_value ocean_proximity
6051     -117.75     34.04                22.0       2948.0           636.0      2600.0       602.0         3.1250            113600.0          INLAND
20113    -119.57     37.94                17.0        346.0           130.0        51.0        20.0         3.4861            137500.0          INLAND
14289    -117.13     32.74                46.0       3355.0           768.0      1457.0       708.0         2.6604            170100.0      NEAR OCEAN
13665    -117.31     34.02                18.0       1634.0           274.0       899.0       285.0         5.2139            129300.0          INLAND
14471    -117.23     32.88                18.0       5566.0          1465.0      6303.0      1458.0         1.8580            205000.0      NEAR OCEAN
```

We are using the data that can be
<a href="https://www.kaggle.com/harrywang/housing" target="_blank">downloaded
here</a>.

This dataset is a modified version of the California Housing dataset
available from:
<a href="https://www.dcc.fc.up.pt/~ltorgo/Regression/cal_housing.html" target="_blank">Luís
Torgo’s University of Porto website</a>.

Notes:

For the next few slide decks, we are going to be using a dataset
exploring the prices of homes in California to demonstrate feature
transformation techniques.

The task is to predict median house values in California districts,
given several features from these districts.

Before we do anything, we load in the data and split it into our train
and test splits.

We can see in our training data that we have various districts and
information such as where it is, `median_house_age`, `total_bedrooms`
etc. Our target columns in the column labeled `median_house_value`.

Something we need to be aware of is that some column values are
mean/median while others are totals or not completely clear.

---

``` python
train_df = train_df.assign(rooms_per_household = train_df["total_rooms"]/train_df["households"],
                           bedrooms_per_household = train_df["total_bedrooms"]/train_df["households"],
                           population_per_household = train_df["population"]/train_df["households"])
                        
test_df = test_df.assign(rooms_per_household = test_df["total_rooms"]/test_df["households"],
                         bedrooms_per_household = test_df["total_bedrooms"]/test_df["households"],
                         population_per_household = test_df["population"]/test_df["households"])
                         
train_df = train_df.drop(columns=['total_rooms', 'total_bedrooms', 'population'])  
test_df = test_df.drop(columns=['total_rooms', 'total_bedrooms', 'population']) 

train_df.head()
```

```out
       longitude  latitude  housing_median_age  households  median_income  median_house_value ocean_proximity  rooms_per_household  bedrooms_per_household  population_per_household
6051     -117.75     34.04                22.0       602.0         3.1250            113600.0          INLAND             4.897010                1.056478                  4.318937
20113    -119.57     37.94                17.0        20.0         3.4861            137500.0          INLAND            17.300000                6.500000                  2.550000
14289    -117.13     32.74                46.0       708.0         2.6604            170100.0      NEAR OCEAN             4.738701                1.084746                  2.057910
13665    -117.31     34.02                18.0       285.0         5.2139            129300.0          INLAND             5.733333                0.961404                  3.154386
14471    -117.23     32.88                18.0      1458.0         1.8580            205000.0      NEAR OCEAN             3.817558                1.004801                  4.323045
```

Notes:

Before we use this data we need to do some **feature engineering**.

That means we are going to transform our data into features that may be
more meaningful for our prediction.

Since we have inconsistent columns, we are going to engineer the new
features `rooms_per_household`, `bedrooms_per_household`, and
`population_per_household` and remove the columns `total_rooms`,
`total_bedrooms`, and `population`.

---

## Exploratory Data Analysis (EDA)

``` python
train_df.info()
```

```out
<class 'pandas.core.frame.DataFrame'>
Int64Index: 18576 entries, 6051 to 19966
Data columns (total 10 columns):
 #   Column                    Non-Null Count  Dtype  
---  ------                    --------------  -----  
 0   longitude                 18576 non-null  float64
 1   latitude                  18576 non-null  float64
 2   housing_median_age        18576 non-null  float64
 3   households                18576 non-null  float64
 4   median_income             18576 non-null  float64
 5   median_house_value        18576 non-null  float64
 6   ocean_proximity           18576 non-null  object 
 7   rooms_per_household       18576 non-null  float64
 8   bedrooms_per_household    18391 non-null  float64
 9   population_per_household  18576 non-null  float64
dtypes: float64(9), object(1)
memory usage: 1.6+ MB
```

Notes:

After using `.info()` we can we all the different column dtypes and also
all the number of null values.

We see that we have all columns with dtype `float64` except for
`ocean_proximity` which appears categorical.

---

``` python
train_df.describe()
```

```out
          longitude      latitude  housing_median_age    households  median_income  median_house_value  rooms_per_household  bedrooms_per_household  population_per_household
count  18576.000000  18576.000000        18576.000000  18576.000000   18576.000000        18576.000000         18576.000000            18391.000000              18576.000000
mean    -119.565888     35.627966           28.622255    500.061100       3.862552       206292.067991             5.426067                1.097516                  3.052349
std        1.999622      2.134658           12.588307    383.044313       1.892491       115083.856175             2.512319                0.486266                 10.020873
min     -124.350000     32.540000            1.000000      1.000000       0.499900        14999.000000             0.846154                0.333333                  0.692308
25%     -121.790000     33.930000           18.000000    280.000000       2.560225       119400.000000             4.439360                1.005888                  2.430323
50%     -118.490000     34.250000           29.000000    410.000000       3.527500       179300.000000             5.226415                1.048860                  2.818868
75%     -118.010000     37.710000           37.000000    606.000000       4.736900       263600.000000             6.051620                1.099723                  3.283921
max     -114.310000     41.950000           52.000000   6082.000000      15.000100       500001.000000           141.909091               34.066667               1243.333333
```

``` python
train_df["bedrooms_per_household"].isnull().sum()
```

```out
185
```

Notes:

It looks like the training data is missing 185 values for
`bedrooms_per_household`.

---

### What happens?

``` python
X_train = train_df.drop(columns=["median_house_value", "ocean_proximity"])
y_train = train_df["median_house_value"]

X_test = test_df.drop(columns=["median_house_value", "ocean_proximity"])
y_test = test_df["median_house_value"]
```

``` python
knn = KNeighborsRegressor()
knn.fit(X_train, y_train)
```

``` out
ValueError: Input contains NaN, infinity or a value too large for dtype('float64').
```

Notes:

First, we are going to drop the categorical variable `ocean_proximity`.

Right now, we only know how to build models with numerical data. We will
come back to the categorical variables in module 6.

We create our `X` and `y` objects and attempt to run a model.

Does it work?

\-No.

We can see that the classifier is not able to deal with missing values
(NaNs).

What are the possible ways to deal with the problem?

---

## Dropping

``` python
train_df["bedrooms_per_household"].isnull().sum()
```

```out
185
```

``` python
X_train.shape
```

```out
(18576, 8)
```

``` python
X_train_no_nan = X_train.dropna()
y_train_no_nan = y_train.dropna()
```

``` python
X_train_no_nan.shape
```

```out
(18391, 8)
```

Notes:

What can we do?

We could drop the rows but we’d need to do the same in our test set.

That also doesn’t help us if we get a missing value in deployment. What
do we do then?

Furthermore, what if the missing values don’t occur at random and we’re
systematically dropping certain data? Perhaps a certain type of house
contributes to more missing values.

This is not a great solution, especially if there’s a lot of missing
values.

---

## Dropping a column

``` python
X_train.shape
```

```out
(18576, 8)
```

``` python
X_train_no_col = X_train.dropna(axis=1)
```

``` python
X_train_no_col.shape
```

```out
(18576, 7)
```

Notes:

One can also drop all columns with missing values.

This generally throws away a lot of information, because we lose a whole
column just for 185 missing values out of a total of 18567.

That means we are throwing away 99% of the column’s data because we are
missing 1%.

But dropping a column if it’s 99.9% missing values, for example, makes
more sense.

---

## Imputation

**Imputation**: Imputation means inventing values for the missing data.

``` python
from sklearn.impute import SimpleImputer
```

We can impute missing values in:

  - **Categorical columns**: with the most frequent value.
  - **Numeric columns**: with the mean or median of the column or a
    constant of our choosing.

Notes:

`SimpleImputer()` is a **transformer** in `sklearn` which can deal with
this problem.

We are going to concentrate on numeric columns in this section and
address categorical preprocessing in Module 6.

---

``` python
X_train.sort_values('bedrooms_per_household').tail(10)
```

```out
       longitude  latitude  housing_median_age  households  median_income  rooms_per_household  bedrooms_per_household  population_per_household
18786    -122.42     40.44                16.0       181.0         2.1875             5.491713                     NaN                  2.734807
17923    -121.97     37.35                30.0       386.0         4.6328             5.064767                     NaN                  2.588083
16880    -122.39     37.59                32.0       715.0         6.1323             6.289510                     NaN                  2.581818
4309     -118.32     34.09                44.0       726.0         1.6760             3.672176                     NaN                  3.163912
538      -122.28     37.78                29.0      1273.0         2.5762             4.048704                     NaN                  2.938727
4591     -118.28     34.06                42.0      1179.0         1.2254             2.096692                     NaN                  3.218830
19485    -120.98     37.66                10.0       255.0         0.9336             3.662745                     NaN                  1.572549
6962     -118.05     33.99                38.0       357.0         3.7328             4.535014                     NaN                  2.481793
14970    -117.01     32.74                31.0       677.0         2.6973             5.129985                     NaN                  3.098966
7763     -118.10     33.91                36.0       130.0         3.6389             5.584615                     NaN                  3.769231
```

Notes:

First, let’s sort the values by `bedrooms_per_household` and we’ll see
that the `NaN` values will fall to the end.

Here we see that the index `7763` has a `NaN` value for
`bedrooms_per_household`.

---

``` python
imputer = SimpleImputer(strategy="median")
imputer.fit(X_train);
X_train_imp = imputer.transform(X_train)
X_test_imp = imputer.transform(X_test)
```

``` python
X_train_imp
```

```out
array([[-117.75      ,   34.04      ,   22.        , ...,    4.89700997,    1.05647841,    4.31893688],
       [-119.57      ,   37.94      ,   17.        , ...,   17.3       ,    6.5       ,    2.55      ],
       [-117.13      ,   32.74      ,   46.        , ...,    4.73870056,    1.08474576,    2.0579096 ],
       ...,
       [-121.76      ,   37.33      ,    5.        , ...,    5.95839311,    1.03156385,    3.49354376],
       [-122.44      ,   37.78      ,   44.        , ...,    4.7392638 ,    1.02453988,    1.7208589 ],
       [-119.08      ,   36.21      ,   20.        , ...,    5.49137931,    1.11781609,    3.56609195]])
```

Notes:

Simple import will work by replacing all the `NaN` values in some way,
in this case, the column median.

Let’s input our data and instead of dropping the examples, let’s use the
`fit` and `transform` steps that we saw earlier.

We fit on the training data and transform it on the train and test
splits.

We do not need to fit on our target column.

Note that `imputer.transform()` returns a NumPy array and not a
dataframe.

---

``` python
X_train_imp_df = pd.DataFrame(X_train_imp, columns = X_train.columns, index = X_train.index)
X_train_imp_df.loc[[7763]]
```

```out
      longitude  latitude  housing_median_age  households  median_income  rooms_per_household  bedrooms_per_household  population_per_household
7763     -118.1     33.91                36.0       130.0         3.6389             5.584615                 1.04886                  3.769231
```

``` python
X_train.loc[[7763]]
```

```out
      longitude  latitude  housing_median_age  households  median_income  rooms_per_household  bedrooms_per_household  population_per_household
7763     -118.1     33.91                36.0       130.0         3.6389             5.584615                     NaN                  3.769231
```

Notes:

We are going to convert the output from the transformer into a dataframe
so it’s easier to look at.

Let’s check whether the `NaN` values have been replaced or not.

Now we can see our example 7763 no longer has any `NaN` values for the
`bedrooms_per_household` now.

---

``` python
knn = KNeighborsRegressor();
knn.fit(X_train_imp, y_train)
```

```out
KNeighborsRegressor()
```

``` python
knn.score(X_train_imp, y_train)
```

```out
0.5609808539232339
```

Notes:

Can we train on the data with the new data `X_train_imp`?

Yes\!

---

# Let’s apply what we learned\!

Notes: <br>
