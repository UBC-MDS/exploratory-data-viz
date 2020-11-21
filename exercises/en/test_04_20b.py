def test():
    # Here we can either check objects created in the solution code, or the
    # string value of the solution, available as __solution__. A helper for
    # printing formatted messages is available as __msg__. See the testTemplate
    # in the meta.json for details.

    # If an assertion fails, the message will be displayed
    assert 'KNeighborsClassifier' in __solution__, "Make sure you are using the KNeighborsClassifier() function with n_neighbors = 11."
    assert "n_neighbors=11" in __solution__, "Make sure you are setting n_neighbors to 11."
    assert 'model.fit' in __solution__, "Make sure you are fitting the model on the training data."
    assert round(test_score,4) == 0.9627, "Your test score is incorrect. Are you fitting and scoring the model properly?"
    __msg__.good("Nice work, well done!")
