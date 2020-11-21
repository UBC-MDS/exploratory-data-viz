def test():
    # Here we can either check objects created in the solution code, or the
    # string value of the solution, available as __solution__. A helper for
    # printing formatted messages is available as __msg__. See the testTemplate
    # in the meta.json for details.

    # If an assertion fails, the message will be displayed
    assert 'KNeighborsClassifier' in __solution__, "Make sure you are using the KNeighborsClassifier() function with n_neighbors = 5."
    assert 'model.fit' in __solution__, "Make sure you are fitting the model on the training data."
    assert round(train_score,4) == 0.9828, "Your training score is incorrect. Are you fitting and scoring the model properly?"
    assert round(test_score,4) == 0.9441, "Your test score is incorrect. Are you fitting and scoring the model properly?"
    __msg__.good("Nice work, well done!")
