---
type: slides
---

# Tabular Data and Terminology

Notes: <br>

---

## Terminology

Here is some basic terminology used in ML:

  - **examples** = rows
  - **features** = inputs
  - **targets** = outputs
  - **training** = learning = fitting

<center>

<img src="/module1/sup-ml-terminology.png" height="1000" width="1000">

</center>

Notes:

In the supervised machine learning paradigm, we have input data and an
output. We feed our input to a machine learning algorithm.

The question is how do we effectively represent this input?

Is there a specific required format for our data so that we can pass it
to machine learning algorithms. - YES\! In supervised machine learning,
we typically work with **tabular data**.

Here is a toy example of tabular data.

The task here is to predict the `quiz2` grade given all this
information.

  - Rows are ***examples***

  - Columns are ***features*** and one of the columns is typically the
    ***target***.

  - Features are relevant characteristics of the problem (usually
    suggested by experts).  

  - To a machine, column names (features) have no meaning. Only feature
    values and how they vary across examples mean something.

  - **Training** a model can also be called learning or fitting a model.

All of these will be used in the course so it’s important to get
familiar with the vocabulary now.

You will see a lot of variable terminology in machine learning and
statistics and sometimes they can be confusing. See the MDS terminology
resource
<a href="https://ubc-mds.github.io/resources_pages/terminology/" target="_blank">here</a>
to clear up any confusions.

---

### Terminology

### Example 1: Tabular data for the housing price prediction problem

``` python
df = pd.read_csv("data/kc_house_data.csv")
df = df.drop(columns=["id", "date"])
df.head(3)
```

```out
      price  bedrooms  bathrooms  sqft_living  sqft_lot  floors  waterfront  view  condition  grade  sqft_above  sqft_basement  yr_built  yr_renovated  zipcode      lat     long  sqft_living15  sqft_lot15
0  221900.0         3       1.00         1180      5650     1.0           0     0          3      7        1180              0      1955             0    98178  47.5112 -122.257           1340        5650
1  538000.0         3       2.25         2570      7242     2.0           0     0          3      7        2170            400      1951          1991    98125  47.7210 -122.319           1690        7639
2  180000.0         2       1.00          770     10000     1.0           0     0          3      6         770              0      1933             0    98028  47.7379 -122.233           2720        8062
```

``` python
df.shape
```

```out
(21613, 19)
```

Notes:

Let’s look at some examples of terminology:

Let’s go back to our housing price prediction problems. In this
particular example, there are 18 features and 21613 examples.

Our target column is the `price` column.

---

### Example 2: Tabular data for quiz2 classification problem

``` python
classification_df = pd.read_csv("data/quiz2-grade-toy-classification.csv")
classification_df.head(3)
```

```out
   ml_experience  class_attendance  lab1  lab2  lab3  lab4  quiz1   quiz2
0              1                 1    92    93    84    91     92      A+
1              1                 0    94    90    80    83     91  not A+
2              0                 0    78    85    83    80     80  not A+
```

``` python
classification_df.shape
```

```out
(21, 8)
```

Notes:

Here is another example.

This is our toy quiz2 classification data. The target here is `quiz2`.
Our task is to predict whether a student gets an A+ or not A+ in quiz2.

Since this is a toy dataset. We only have 21 examples and 7 different
features with our target column being `quiz2`.

---

``` python
X = classification_df.drop(columns=["quiz2"])
y = classification_df["quiz2"]
X.head()
```

```out
   ml_experience  class_attendance  lab1  lab2  lab3  lab4  quiz1
0              1                 1    92    93    84    91     92
1              1                 0    94    90    80    83     91
2              0                 0    78    85    83    80     80
3              0                 1    91    94    92    91     89
4              0                 1    77    83    90    92     85
```

``` python
y.head()
```

```out
0        A+
1    not A+
2    not A+
3        A+
4        A+
Name: quiz2, dtype: object
```

Notes:

In order to train a model, we need to separate our data into features
and the target.

We save our features which are columns `ml_experience` to `quiz1` in an
object named `X`.

Our target column is `quiz2` and gets saved in an object named `y`.

We will explain why we do this in the next set of slides.

---

# Let’s apply what we learned\!

Notes: <br>
