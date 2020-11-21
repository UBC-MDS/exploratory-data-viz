def test():
    # Here we can either check objects created in the solution code, or the
    # string value of the solution, available as __solution__. A helper for
    # printing formatted messages is available as __msg__. See the testTemplate
    # in the meta.json for details.

    # If an assertion fails, the message will be displayed
    assert 'train_test_split' in __solution__, "Make sure you are creating splitting the dataset using the 'train_test_split()' function."
    assert 'random_state=7', "Make sure you are settting the random state to 7 when splittting the data."
    assert 'test_size=0.2' in __solution__, "Make sure you are doing a 20-80 split."
    assert 'DecisionTreeClassifier' in __solution__, "Make sure you are specifying a 'DecisionTreeClassifier'."
    assert 'model.fit' in __solution__, "Make sure you are using the '.fit()' function to fit 'X' and 'y'."
    assert 'model.score' in __solution__, "Make sure you are scoring on both the training and the test set."
    assert train_score - 0.95 < 0.00001, "The training score is incorrect. Are you fitting the model properly?"
    assert test_score - 0.4 < 0.00001, "The test score is incorrect. Are you fitting the model properly?"
    __msg__.good("Nice work, well done!")