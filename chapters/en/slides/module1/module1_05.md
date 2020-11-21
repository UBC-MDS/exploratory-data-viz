---
type: slides
---

# Classification vs Regression

Notes:

There are two main kinds of supervised learning problems based on what
they are trying to predict; ***Classification*** and ***Regression***.

---

## Classification vs. Regression

  - **Classification problem**: predicting among two or more categories,
    also known as classes
      - *Example1*: Predict whether a patient has a liver disease or not
      - *Example2*: Predict whether the letter grade of a student
        (A,B,C,D or F)
  - **Regression problem**: predicting a continuous (in other words, a
    number) value
      - Example1: Predict housing prices
      - Example2: Predict a student’s score in this course’s quiz2

Notes:

In **Classification** problems we predict target value among two or more
known categories.

For example:

  - Whether a patient has a liver disease or not (2 possible target
    values)
  - The letter grade of a student: A, B, C, D or F. ( There are 5
    categories)

**Regression** predicts a continuous (typically, floating-point) value.

For example: - Housing prices - The scores of students in this course’s
quiz2.

---

<center>

<img src="/module1/classification-vs-regression.png" height="1500" width="1500">

</center>

Notes:

Here are examples of classification and regression problems.

As we said before in a classification problem the target has discrete
categories. In this example, our target has only two possible values; A+
or not A+. Our goal is to predict if a student will get a value of A+ or
not A+.

In Regression problems, we are predicting each student’s grade, so the
target here which is quiz2 contains the actual students’ score.

---

``` python
classification_df = pd.read_csv("data/quiz2-grade-toy-classification.csv")
classification_df.head()
```

```out
   ml_experience  class_attendance  lab1  lab2  lab3  lab4  quiz1   quiz2
0              1                 1    92    93    84    91     92      A+
1              1                 0    94    90    80    83     91  not A+
2              0                 0    78    85    83    80     80  not A+
3              0                 1    91    94    92    91     89      A+
4              0                 1    77    83    90    92     85      A+
```

Notes:

We have created two toy datasets for classification and regression and
this is our toy dataset for classification.

We can see in the first example, the target here is `quiz2` and contains
only 2 possible values; A+ or not A+.

---

``` python
regression_df = pd.read_csv("data/quiz2-grade-toy-regression.csv")
regression_df.head()
```

```out
   ml_experience  class_attendance  lab1  lab2  lab3  lab4  quiz1  quiz2
0              1                 1    92    93    84    91     92     90
1              1                 0    94    90    80    83     91     84
2              0                 0    78    85    83    80     80     82
3              0                 1    91    94    92    91     89     92
4              0                 1    77    83    90    92     85     90
```

Notes:

On the other hand, in the regression problem, the target column (
‘quiz2`) contains the actual scores so we have continuous values in
our`quiz2\` column.

---

# Let’s apply what we learned\!

Notes: <br>
