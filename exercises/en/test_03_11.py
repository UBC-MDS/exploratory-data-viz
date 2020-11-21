def test():
    # Here we can either check objects created in the solution code, or the
    # string value of the solution, available as __solution__. A helper for
    # printing formatted messages is available as __msg__. See the testTemplate
    # in the meta.json for details.

    # If an assertion fails, the message will be displayed
    assert 'random_state=33', "Make sure you are settting the random state to 33 when splittting the data."
    assert 'test_size=0.2' in __solution__, "Make sure you are doing a 20-80 split."
    assert 'DecisionTreeClassifier' in __solution__, "Make sure you are specifying a 'DecisionTreeClassifier'."
    assert 'cross_val_score' in __solution__, "Make sure you are doing cross validation scoring using the 'cross_val_score' function."
    assert 'cv=6' in __solution__, "Make sure you are doing 6-fold cross validation."
    assert round(sum(cv_scores)/len(cv_scores),2) == 0.96, "The average cross validation score is incorrect. Are you setting up the model properly?"
    __msg__.good("Nice work, well done!")