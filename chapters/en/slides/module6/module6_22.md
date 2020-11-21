---
type: slides
---

# Text data

Notes: <br>

---

<center>

<img src="/module6/num_xy.png"  width = "100%" alt="404 image" />

</center>

Notes:

Machine Learning algorithms we have seen so far prefer numeric and
fixed-length input that looks like this.

But what if we are only given data in the form of raw text and
associated labels?

How can we represent such data into a fixed number of features?

---

<center>

<img src="/module6/cat_xy.png"  width = "100%" alt="404 image" />

</center>

Notes:

Would you be able to apply the algorithms we have seen so far on the
data that looks like this?

In categorical features or ordinal features, we have a fixed number of
categories.

In text features such as above, each feature value (i.e., each text
message) is going to be different.

How do we encode these features?

---

## Bag of words (BOW) representation

<center>

<img src="/module6/bag-of-words.png"  width = "100%" alt="404 image" />

</center>

<a href="https://web.stanford.edu/~jurafsky/slp3/4.pdf" target="_blank">Attribution:
Daniel Jurafsky & James H. Martin</a>

Notes:

One way is to use a simple bag of words (BOW) representation which
involves two components. - The vocabulary (all unique words in all
documents) - A value indicating either the presence or absence or the
count of each word in the document.

---

### Extracting BOW features using *scikit-learn*

``` python
X = [
    "URGENT!! As a valued network customer you have been selected to receive a £900 prize reward!",
    "Lol you are always so convincing.",
    "Nah I don't think he goes to usf, he lives around here though",
    "URGENT! You have won a 1 week FREE membership in our £100000 prize Jackpot!",
    "Had your mobile 11 months or more? U R entitled to Update to the latest colour mobiles with camera for Free! Call The Mobile Update Co FREE on 08002986030",
    "As per your request 'Melle Melle (Oru Minnaminunginte Nurungu Vettam)' has been set as your callertune for all Callers. Press *9 to copy your friends Callertune"]
    
y = ["spam", "non spam", "non spam", "spam", "spam", "non spam"]
```

Notes:

Let’s say we have 1 feature in our `X` dataframe consisting of the
following text messages.

In our target column, we have the classification of each message as
either `spam` or `non spam`.

---

``` python
from sklearn.feature_extraction.text import CountVectorizer
```

``` python
vec = CountVectorizer()
X_counts = vec.fit_transform(X);
bow_df = pd.DataFrame(X_counts.toarray(), columns=sorted(vec.vocabulary_), index=X)
bow_df
```

```out
                                                    08002986030  100000  11  900  all  always  are  around  as  been  call  callers  callertune  camera  co  colour  convincing  copy  customer  don  entitled  for  free  friends  goes  ...  oru  our  per  press  prize  receive  request  reward  selected  set  so  the  think  though  to  update  \
URGENT!! As a valued network customer you have ...            0       0   0    1    0       0    0       0   1     1     0        0           0       0   0       0           0     0         1    0         0    0     0        0     0  ...    0    0    0      0      1        1        0       1         1    0   0    0      0       0   1       0   
Lol you are always so convincing.                             0       0   0    0    0       1    1       0   0     0     0        0           0       0   0       0           1     0         0    0         0    0     0        0     0  ...    0    0    0      0      0        0        0       0         0    0   1    0      0       0   0       0   
Nah I don't think he goes to usf, he lives arou...            0       0   0    0    0       0    0       1   0     0     0        0           0       0   0       0           0     0         0    1         0    0     0        0     1  ...    0    0    0      0      0        0        0       0         0    0   0    0      1       1   1       0   
URGENT! You have won a 1 week FREE membership i...            0       1   0    0    0       0    0       0   0     0     0        0           0       0   0       0           0     0         0    0         0    0     1        0     0  ...    0    1    0      0      1        0        0       0         0    0   0    0      0       0   0       0   
Had your mobile 11 months or more? U R entitled...            1       0   1    0    0       0    0       0   0     0     1        0           0       1   1       1           0     0         0    0         1    1     2        0     0  ...    0    0    0      0      0        0        0       0         0    0   0    2      0       0   2       2   
As per your request 'Melle Melle (Oru Minnaminu...            0       0   0    0    1       0    0       0   2     1     0        1           2       0   0       0           0     1         0    0         0    1     0        1     0  ...    1    0    1      1      0        0        1       0         0    1   0    0      0       0   1       0   

                                                    urgent  usf  valued  vettam  week  with  won  you  your  
URGENT!! As a valued network customer you have ...       1    0       1       0     0     0    0    1     0  
Lol you are always so convincing.                        0    0       0       0     0     0    0    1     0  
Nah I don't think he goes to usf, he lives arou...       0    1       0       0     0     0    0    0     0  
URGENT! You have won a 1 week FREE membership i...       1    0       0       0     1     0    1    1     0  
Had your mobile 11 months or more? U R entitled...       0    0       0       0     0     1    0    0     1  
As per your request 'Melle Melle (Oru Minnaminu...       0    0       0       1     0     0    0    0     3  

[6 rows x 72 columns]
```

Notes:

We import a tool call `CountVectorizer()`.

`CountVectorizer` converts a collection of text documents to a matrix of
word counts.  
\- Each row represents a “document” (e.g., a text message in our
example). - Each column represents a word in the vocabulary in the
training data. - Each cell represents how often the word occurs in the
document.

In the NLP community, a text data set is referred to as a **corpus**
(plural: corpora).

---

## The output type…

``` python
X_counts
```

```out
<6x72 sparse matrix of type '<class 'numpy.int64'>'
 with 85 stored elements in Compressed Sparse Row format>
```

``` python
print("The total number of elements: ", np.prod(X_counts.shape))
```

```out
The total number of elements:  432
```

``` python
print("The number of non-zero elements: ", X_counts.nnz)
```

```out
The number of non-zero elements:  85
```

``` python
print( "Proportion of non-zero elements:", (X_counts.nnz / np.prod(X_counts.shape).round(4)))
```

```out
Proportion of non-zero elements: 0.19675925925925927
```

``` python
print("The value at cell 3,", vec.vocabulary_["jackpot"], "is:", X_counts[3, vec.vocabulary_["jackpot"]]
)
```

```out
The value at cell 3, 31 is: 1
```

Notes:

What is a sparse matrix?

A **sparse matrix** is a multidimensional array mostly contain with zero
elements.

  - Most words do not appear in a given document.
  - We get massive computational savings if we only store the nonzero
    elements.
  - There is a bit of overhead because we also need to store the
    locations:
      - e.g. “location (3,31): 1”.
  - However, if the fraction of nonzero is small, this is a huge win.

---

### *OneHotEncoder* and sparse features

``` python
ohe = OneHotEncoder(sparse=False, dtype=int, drop="if_binary") # <-- see here
ohe.fit(X_train[["sex"]])
ohe_df = pd.DataFrame(data=ohe.transform(X_train[["sex"]]), columns=ohe.get_feature_names(["sex"]), index=X_train.index)
ohe_df
```

``` out
OneHotEncoder(drop='if_binary', dtype=<class 'int'>, sparse=False)
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

In the last slide deck, you may have noticed that we set an argument
named `sparse=False` when we were binarizing our data.

By default, `OneHotEncoder` also creates sparse features.

We were setting `sparse=False` to get a regular `numpy` array.

If there are a huge number of categories, it may be beneficial to keep
them sparse.

For a smaller number of categories, it doesn’t matter much.

---

### Important hyperparameters of `CountVectorizer`

  - `binary`:
      - Whether to use absence/presence feature values or counts.
  - `max_features`:
      - Only considers top `max_features` ordered by frequency in the
        corpus.
  - `max_df`:
      - When building the vocabulary ignore terms that have a document
        frequency strictly higher than the given threshold.
  - `min_df`:
      - When building the vocabulary ignore terms that have a document
        frequency strictly lower than the given threshold.
  - `ngram_range`:
      - Consider word sequences in the given range.

Notes:

There are many useful and important hyperparameters of
`CountVectorizer`.

---

``` python
vec_all = CountVectorizer()
X_counts = vec_all.fit_transform(X)
pd.DataFrame(data = X_counts.sum(axis=0).tolist()[0], 
             index = vec_all.get_feature_names(), columns=['counts']).sort_values('counts', ascending=False).head(20)
```

```out
         counts
to            5
your          4
you           3
free          3
as            3
...         ...
prize         2
receive       1
or            1
oru           1
our           1

[20 rows x 1 columns]
```

Notes:

Let’s look at all features, i.e., words along with their frequencies.

---

``` python
vec8 = CountVectorizer(max_features=8)
X_counts = vec8.fit_transform(X)
pd.DataFrame(data = X_counts.sum(axis=0).tolist()[0], 
             index = vec8.get_feature_names(), columns=['counts']).sort_values('counts', ascending=False)
```

```out
        counts
to           5
your         4
as           3
free         3
you          3
the          2
update       2
urgent       2
```

Notes:

We can control the size of X (the number of features) using
`max_features`.

---

``` python
bow_df = pd.DataFrame(X_counts.toarray(), columns=sorted(vec8.vocabulary_), index=X)
bow_df
```

```out
                                                    as  free  the  to  update  urgent  you  your
URGENT!! As a valued network customer you have ...   1     0    0   1       0       1    1     0
Lol you are always so convincing.                    0     0    0   0       0       0    1     0
Nah I don't think he goes to usf, he lives arou...   0     0    0   1       0       0    0     0
URGENT! You have won a 1 week FREE membership i...   0     1    0   0       0       1    1     0
Had your mobile 11 months or more? U R entitled...   0     2    2   2       2       0    0     1
As per your request 'Melle Melle (Oru Minnaminu...   2     0    0   1       0       0    0     3
```

Notes:

---

``` python
vec8_binary = CountVectorizer(binary=True, max_features=8)
X_counts_binary = vec8_binary.fit_transform(X)
pd.DataFrame(data = X_counts_binary.sum(axis=0).tolist()[0], 
             index = vec8.get_feature_names(), columns=['counts']).sort_values('counts', ascending=False)
```

```out
        counts
urgent       4
you          3
as           2
free         2
the          2
to           2
update       2
your         2
```

``` python
bow_df_binary = pd.DataFrame(X_counts_binary.toarray(), columns=sorted(vec8_binary.vocabulary_), index=X)
bow_df_binary
```

```out
                                                    as  been  free  have  prize  to  you  your
URGENT!! As a valued network customer you have ...   1     1     0     1      1   1    1     0
Lol you are always so convincing.                    0     0     0     0      0   0    1     0
Nah I don't think he goes to usf, he lives arou...   0     0     0     0      0   1    0     0
URGENT! You have won a 1 week FREE membership i...   0     0     1     1      1   0    1     0
Had your mobile 11 months or more? U R entitled...   0     0     1     0      0   1    0     1
As per your request 'Melle Melle (Oru Minnaminu...   1     1     0     0      0   1    0     1
```

Notes:

---

``` python
bow_df
```

```out
                                                    as  free  the  to  update  urgent  you  your
URGENT!! As a valued network customer you have ...   1     0    0   1       0       1    1     0
Lol you are always so convincing.                    0     0    0   0       0       0    1     0
Nah I don't think he goes to usf, he lives arou...   0     0    0   1       0       0    0     0
URGENT! You have won a 1 week FREE membership i...   0     1    0   0       0       1    1     0
Had your mobile 11 months or more? U R entitled...   0     2    2   2       2       0    0     1
As per your request 'Melle Melle (Oru Minnaminu...   2     0    0   1       0       0    0     3
```

``` python
bow_df_binary
```

```out
                                                    as  been  free  have  prize  to  you  your
URGENT!! As a valued network customer you have ...   1     1     0     1      1   1    1     0
Lol you are always so convincing.                    0     0     0     0      0   0    1     0
Nah I don't think he goes to usf, he lives arou...   0     0     0     0      0   1    0     0
URGENT! You have won a 1 week FREE membership i...   0     0     1     1      1   0    1     0
Had your mobile 11 months or more? U R entitled...   0     0     1     0      0   1    0     1
As per your request 'Melle Melle (Oru Minnaminu...   1     1     0     0      0   1    0     1
```

Notes:

Notice that `vec8` and `vec8_binary` have different vocabularies, which
is somewhat unexpected behaviour and doesn’t match the documentation of
`scikit-learn`.

<a href="https://github.com/scikit-learn/scikit-learn/blob/master/sklearn/feature_extraction/text.py#L1206-L1225" target="_blank">In
`sklearn`’s documentation</a>
[Here](https://github.com/scikit-learn/scikit-learn/blob/master/sklearn/feature_extraction/text.py#L1206-L1225),
the code for the `binary=True` condition in `scikit-learn` shows the
binarization is done before limiting the features to `max_features`, and
so now we are actually looking at the document counts (in how many
documents it occurs) rather than term count. This is not explained
anywhere in the documentation.

---

``` python
pd.DataFrame(data = X_counts.sum(axis=0).tolist()[0], 
             index = vec8.get_feature_names(), columns=['counts']).sort_values('counts', ascending=False)
```

```out
        counts
to           5
your         4
as           3
free         3
you          3
the          2
update       2
urgent       2
```

``` python
pd.DataFrame(data = X_counts_binary.sum(axis=0).tolist()[0], 
             index = vec8.get_feature_names(), columns=['counts']).sort_values('counts', ascending=False)
```

```out
        counts
urgent       4
you          3
as           2
free         2
the          2
to           2
update       2
your         2
```

Notes:

The ties in counts between different words make it even more confusing.
I don’t think it’ll have a big impact on the results but this is good to
know\!

Remember that `scikit-learn` developers are also humans who are prone to
make mistakes. So it’s always a good habit to question whatever tools we
use now and then.

---

### Preprocessing

``` python
X
```

```out
['URGENT!! As a valued network customer you have been selected to receive a £900 prize reward!', 'Lol you are always so convincing.', "Nah I don't think he goes to usf, he lives around here though", 'URGENT! You have won a 1 week FREE membership in our £100000 prize Jackpot!', 'Had your mobile 11 months or more? U R entitled to Update to the latest colour mobiles with camera for Free! Call The Mobile Update Co FREE on 08002986030', "As per your request 'Melle Melle (Oru Minnaminunginte Nurungu Vettam)' has been set as your callertune for all Callers. Press *9 to copy your friends Callertune"]
```

``` python
vec8.get_feature_names()
```

```out
['as', 'free', 'the', 'to', 'update', 'urgent', 'you', 'your']
```

Notes:

`CountVectorizer` is carrying out some preprocessing such as because of
the default argument values. - Converting words to lowercase
(`lowercase=True`). Take a look at the word “urgent” In both cases. -
getting rid of punctuation and special characters (`token_pattern
='(?u)\\b\\w\\w+\\b'`)

---

``` python
pipe = make_pipeline(CountVectorizer(), SVC())
```

``` python
pipe.fit(X,y);
```

``` python
pipe.predict(X)
```

```out
array(['spam', 'non spam', 'non spam', 'spam', 'spam', 'non spam'], dtype='<U8')
```

``` python
pipe.score(X,y)
```

```out
1.0
```

Notes:

<br>

---

### Is this a realistic representation of text data?

Of course, this is not a great representation of language - We are
throwing out everything we know about language and losing a lot of
information. - It assumes that there is no syntax and compositional
meaning in language.

<br> <br> <br>

…But it works surprisingly well for many tasks.

Notes:

<br>

---

# Let’s apply what we learned\!

Notes: <br>
