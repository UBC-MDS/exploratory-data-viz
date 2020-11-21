def test():
    # Here we can either check objects created in the solution code, or the
    # string value of the solution, available as __solution__. A helper for
    # printing formatted messages is available as __msg__. See the testTemplate
    # in the meta.json for details.

    # If an assertion fails, the message will be displayed
    assert "train_test_split" in __solution__, "Make sure you are calling the 'train_test_split()' function to partition the data"
    assert "test_size=0.2" in __solution__, "Make sure you are doing an 80-20 split on the data."
    assert "random_state=33" in __solution__, "Make sure you are setting the random state properly"
    assert 'DecisionTreeClassifier' in __solution__, "Make sure you are specifying a 'DecisionTreeClassifier'."
    assert "max_depth=depth" in __solution__, "Make sure you are specifying the depth in each iteration."
    assert "return_train_score" in __solution__, "Make sure you are retaining the training score using the 'return_train_score' function."
    assert 'cv=10' in __solution__, "Make sure you are doing 10-fold cross validation."
    assert 'mark_line()' in __solution__, "Make sure you are plotting a line graph."
    assert "alt.Chart(results_df)" in __solution__, "Make sure you plotting the results dataframe."
    assert "alt.Y" in __solution__, "Make sure you are plotting the score on the y-axis."
    __msg__.good("Nice work, well done!")
