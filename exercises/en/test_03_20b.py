def test():
    # Here we can either check objects created in the solution code, or the
    # string value of the solution, available as __solution__. A helper for
    # printing formatted messages is available as __msg__. See the testTemplate
    # in the meta.json for details.

    # If an assertion fails, the message will be displayed
    assert 'DecisionTreeClassifier' in __solution__, "Make sure you are specifying a 'DecisionTreeClassifier'."
    assert "max_depth=4" in __solution__, "Make sure you are using the correct depth value determined in the previous question."
    assert 'model.fit' in __solution__, "Make sure you are using the '.fit()' function to fit 'X_train' and 'y_train'."
    assert 'round' in __solution__, "Make sure you are rounding the test score to 4 decimal places."
    assert test_score - 0.9032 < 0.00001, "The mean test score is incorrect. Are you fitting the model and specifying the correct depth?"
    __msg__.good("Nice work, well done!")