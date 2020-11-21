---
type: slides
---

# What is Supervised Machine Learning?

Notes: <br>

---

## Prevalence of Machine Learning (ML)

<center>

<img src='/module1/examples.png'  width = "75%" alt="404 image" />

</center>

Notes:

You may not know it, but machine learning (ML) is all around you.

Some examples include:

  - Voice assistance
  - Google news
  - Recommender systems
  - Face recognition
  - Auto completion
  - Stock market predictions
  - Character recognition
  - Self-driving cars
  - Cancer diagnosis
  - Drug discovery

The best AlphaGo player in the world is not human anymore.

AlphaGo, a machine learning-based system from Google, is the world’s
best player at the moment.

---

## What is Machine Learning?

  - A field of study that gives computers the ability to learn without
    being explicitly programmed.\* <br> – Arthur Samuel (1959)

<center>

<img src="/module1/traditional-programming-vs-ML.png" height="800" width="800">

</center>

Notes:

What exactly is machine learning? There is no clear consensus on the
definition of machine learning. But here is a popular definition by
Artur Samuel who was one of the pioneers of machine learning and
artificial intelligence.

Arthur Samuel said that machine learning is *“A field of study that
gives computers the ability to learn without being explicitly
programmed.”*

Machine learning is a different way to think about problem-solving.
Usually, when we write a program we’re thinking logically and
mathematically. Here is how a traditional program looks like. We are
given input and an algorithm and we produce an output.

Instead, in the machine learning paradigm, we’re given data and some
output and our machine learning algorithm returns a program. we can use
this program to predict the output for some unseen input.

In this paradigm, we’re making observations about an uncertain world and
thinking about it statistically.

---

## Some concrete examples of supervised learning

<br> <br>

## Example 1: Predict whether a patient has a liver disease or not

*In all the the upcoming examples, Don’t worry about the code. Just
focus on the input and output in each example.*

Notes:

Before we start let’s look at some concrete examples of supervised
machine learning.

Our first example is predicting whether a patient has a liver disease or
not.

For now, ignore the code and only focus on input and output.

---

``` python
train_df, test_df = train_test_split(df, test_size=4, random_state=16)
train_df.head()
```

```out
     Age  Total_Bilirubin  Direct_Bilirubin  Alkaline_Phosphotase  Alamine_Aminotransferase  Aspartate_Aminotransferase  Total_Protiens  Albumin  Albumin_and_Globulin_Ratio      Target
13    74              1.1               0.4                   214                        22                          30             8.1      4.1                         1.0     Disease
236   22              0.8               0.2                   300                        57                          40             7.9      3.8                         0.9  No Disease
335   13              0.7               0.1                   182                        24                          19             8.9      4.9                         1.2     Disease
234   40              0.9               0.2                   285                        32                          27             7.7      3.5                         0.8     Disease
159   50              1.2               0.4                   282                        36                          32             7.2      3.9                         1.1     Disease
```

Notes:

Usually, for supervised machine learning, we are provided data in a
tabular form.

We have columns full of data and a special “target” column which is what
we are trying to predict.

We pass this to a machine learning algorithm.

---

``` python
from xgboost import XGBClassifier
X_train = train_df.drop(columns=['Target'])
y_train = train_df['Target']
X_test = test_df.drop(columns=['Target'])
model = XGBClassifier()
model.fit(X_train, y_train)
```

Notes:

Next, we build a model and train our model using the labels we already
have.

Ignore this output here.

It’s just explaining what’s going on in the model which we will explain
soon.

---

``` python
pred_df = pd.DataFrame(
    {"Predicted label": model.predict(X_test).tolist()}
)
df_concat = pd.concat([X_test.reset_index(drop=True), pred_df], axis=1)
df_concat
```

```out
   Age  Total_Bilirubin  Direct_Bilirubin  Alkaline_Phosphotase  Alamine_Aminotransferase  Aspartate_Aminotransferase  Total_Protiens  Albumin  Albumin_and_Globulin_Ratio Predicted label
0   61              0.7               0.2                   145                        53                          41             5.8      2.7                        0.87         Disease
1   42             11.1               6.1                   214                        60                         186             6.9      2.8                        2.80         Disease
2   22              0.8               0.2                   198                        20                          26             6.8      3.9                        1.30      No Disease
3   72              1.7               0.8                   200                        28                          37             6.2      3.0                        0.93         Disease
```

Notes:

Then, given new unseen input, we can apply our learned model to predict
the target for the input.

In this case, we can imagine that a new patient arrives and we want to
predict if the patient has a disease or not.

Given the patient’s information, our model predicts if the patient has
the disease or not.

---

<br> <br> <br>

## Example 2: Predict the label of a given image

Notes:

Our second example is predicting the label of a given image.

---

## Predict labels with associated probability scores for unseen images

``` python
images = glob.glob("test_images/*.*")
for image in images:
    img = Image.open(image)
    img.load()
    plt.imshow(img)
    plt.show()
    df = classify_image(img)
    print(df.to_string(index=False))
```

<img src="/module1/module1_01/unnamed-chunk-6-1.png" width="300" />

``` out
  Class  Probability
      ox     0.869893
  oxcart     0.065034
  sorrel     0.028593
 gazelle     0.010053
```

Notes:

Here we use a machine learning model trained on millions of images and
their labels.

We are applying our model to predict the labels of unseen images.

In this particular case, our unseen image is that of an ox.

When we apply our trained model on this image, it gives us some
predictions and their associated probability scores.

So in this particular case, the model predicted that the image was that
of an ox with a confidence of 0.869.

---

``` python
images = glob.glob("test_images/*.*")
for image in images:
    img = Image.open(image)
    img.load()
    plt.imshow(img)
    plt.show()
    df = classify_image(img)
    print(df.to_string(index=False))
```

<img src="/module1/module1_01/unnamed-chunk-6-2.png" width="300" />

``` out
            Class  Probability
            llama     0.123625
               ox     0.076333
           kelpie     0.071548
 ibex, Capra ibex     0.060569
```

Notes:

Our second unseen image contains some donkeys.

In this case, when we apply our mode to the image, The model predicts
that it contains a llama. That being said, the probability score here is
only 0.123.

---

<br> <br> <br>

## Example 3: Predict sentiment expressed in a movie review (pos/neg)

*Attribution: The dataset `imdb_master.csv` was obtained from
<a href="https://www.kaggle.com/uttam94/imdb-mastercsv" target="_blank">Kaggle</a>*

Notes:

Our third example is about predicting sentiment expressed in movie
reviews.

---

``` python
train_df.head()
```

``` out
                                                review label         file
43020  Just caught it at the Toronto International Fi...   pos   3719_9.txt
49131  The movie itself made me want to go and call s...   pos  9219_10.txt
23701  I came across this movie on DVD purely by chan...   pos   8832_9.txt
4182   Having seen Carlo Lizzani's documentary on Luc...   neg   2514_4.txt
38521  I loved this film. I first saw it when I was 2...   pos  1091_10.txt
```

Notes: First we wrangle our data so that we can train our model.

This data contains the review in a column named `review` and a `label`
column which contains values of either `pos` or `neg` for positive or
negative.

---

``` python
X_train, y_train = train_df['review'], train_df['label']
X_test, y_test = test_df['review'], test_df['label']

clf = Pipeline(
    [
        ("vect", CountVectorizer(max_features=5000)),
        ("clf", LogisticRegression(max_iter=5000)),
    ]
)
clf.fit(X_train, y_train)
```

```out
Pipeline(steps=[('vect', CountVectorizer(max_features=5000)),
                ('clf', LogisticRegression(max_iter=5000))])
```

Notes: Next, we build our model and train on our existing data.

Again, don’t worry about the code here.

---

``` python
pred_dict = {
    "reviews": X_test[0:4],
    "true_sentiment": y_test[0:4],
    "sentiment_predictions": clf.predict(X_test[0:4]),
}
pred_df = pd.DataFrame(pred_dict)
pred_df.head()
```

```out
                                                 reviews true_sentiment sentiment_predictions
34622  I love horror movies that brings out a real am...            neg                   pos
1163   It seems that some viewers assume that the onl...            neg                   neg
7637   I have seen this film 3 times. Mostly because ...            neg                   neg
7045   For weeks I had been looking forward to seeing...            neg                   neg
```

Notes:

Once we have the model, we can use this to predict the sentiment
expressed in new movie reviews.

---

<br> <br> <br>

## Example 4: Predict housing prices

*Attribution: The dataset `kc_house_data.csv` was obtained from
<a href="https://www.kaggle.com/harlfoxem/housesalesprediction" target="_blank">Kaggle</a>.*

Notes:

Example 4 is about predicting housing prices.

---

``` python
df = pd.read_csv("data/kc_house_data.csv")
df = df.drop(columns=["id", "date"])
train_df, test_df = train_test_split(df, test_size=0.2, random_state=4)
train_df.head()
```

```out
          price  bedrooms  bathrooms  sqft_living  sqft_lot  floors  waterfront  view  condition  grade  sqft_above  sqft_basement  yr_built  yr_renovated  zipcode      lat     long  sqft_living15  sqft_lot15
8583   509000.0         2       1.50         1930      3521     2.0           0     0          3      8        1930              0      1989             0    98007  47.6092 -122.146           1840        3576
19257  675000.0         5       2.75         2570     12906     2.0           0     0          3      8        2570              0      1987             0    98075  47.5814 -122.050           2580       12927
1295   420000.0         3       1.00         1150      5120     1.0           0     0          4      6         800            350      1946             0    98116  47.5588 -122.392           1220        5120
15670  680000.0         8       2.75         2530      4800     2.0           0     0          4      7        1390           1140      1901             0    98112  47.6241 -122.305           1540        4800
3913   357823.0         3       1.50         1240      9196     1.0           0     0          3      8        1240              0      1968             0    98072  47.7562 -122.094           1690       10800
```

Notes:

In this particular case, our data contains attributes associated with
properties

For example, our attributes consist of the number of bedrooms, the
number of bathrooms, etc.

Our special column which we call our “target column” is the price for
the corresponding property.

Note that this price column here contains continuous values and not
discrete values as we saw in our previous examples.

---

``` python

X_train = train_df.drop(columns=["price"])
X_train.head()
```

```out
       bedrooms  bathrooms  sqft_living  sqft_lot  floors  waterfront  view  condition  grade  sqft_above  sqft_basement  yr_built  yr_renovated  zipcode      lat     long  sqft_living15  sqft_lot15
8583          2       1.50         1930      3521     2.0           0     0          3      8        1930              0      1989             0    98007  47.6092 -122.146           1840        3576
19257         5       2.75         2570     12906     2.0           0     0          3      8        2570              0      1987             0    98075  47.5814 -122.050           2580       12927
1295          3       1.00         1150      5120     1.0           0     0          4      6         800            350      1946             0    98116  47.5588 -122.392           1220        5120
15670         8       2.75         2530      4800     2.0           0     0          4      7        1390           1140      1901             0    98112  47.6241 -122.305           1540        4800
3913          3       1.50         1240      9196     1.0           0     0          3      8        1240              0      1968             0    98072  47.7562 -122.094           1690       10800
```

``` python
y_train = train_df["price"]
y_train.head()
```

```out
8583     509000.0
19257    675000.0
1295     420000.0
15670    680000.0
3913     357823.0
Name: price, dtype: float64
```

``` python
X_test = test_df.drop(columns=["price"])
y_test = train_df["price"]
```

Notes:

It’s important that we separate our data from the target column (The `y`
variables).

---

``` python
from xgboost import XGBRegressor

model = XGBRegressor()
model.fit(X_train, y_train)
```

Notes:

Again we use this data to train our machine learning model.

---

``` python
pred_df = pd.DataFrame(
    {"Predicted price": model.predict(X_test[0:4]).tolist(), "Actual price": y_test[0:4].tolist()}
)
df_concat = pd.concat([X_test[0:4].reset_index(drop=True), pred_df], axis=1)
df_concat.head()
```

```out
   bedrooms  bathrooms  sqft_living  sqft_lot  floors  waterfront  view  condition  grade  sqft_above  sqft_basement  yr_built  yr_renovated  zipcode      lat     long  sqft_living15  sqft_lot15  Predicted price  Actual price
0         4       2.25         2130      8078     1.0           0     0          4      7        1380            750      1977             0    98055  47.4482 -122.209           2300        8112      333981.6250      509000.0
1         3       2.50         2210      7620     2.0           0     0          3      8        2210              0      1994             0    98052  47.6938 -122.130           1920        7440      615222.4375      675000.0
2         4       1.50         1800      9576     1.0           0     0          4      7        1800              0      1977             0    98045  47.4664 -121.747           1370        9576      329770.0625      420000.0
3         3       2.50         1580      1321     2.0           0     2          3      8        1080            500      2014             0    98107  47.6688 -122.402           1530        1357      565091.6250      680000.0
```

Notes:

And once we have our trained model, we apply it to predict the price
associated with new home properties.

When we pass new properties into the model we get a predicted price for
those properties.

And note again that our predicted prices here are continuous numbers and
not discrete values

---

# Let’s apply what we learned\!

Notes: <br>
