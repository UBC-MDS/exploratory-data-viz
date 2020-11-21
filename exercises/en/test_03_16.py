def test():
    # Here we can either check objects created in the solution code, or the
    # string value of the solution, available as __solution__. A helper for
    # printing formatted messages is available as __msg__. See the testTemplate
    # in the meta.json for details.

    # If an assertion fails, the message will be displayed
    assert "return_train_score" in __solution__, "Make sure you are retaining the training score using the 'return_train_score' function."
    assert 'cross_validate' in __solution__, "Make sure you are doing cross validation using the 'cross_validate' function."
    assert 'cv=10' in __solution__, "Make sure you are doing 10-fold cross validation."
    assert '.mean()' in __solution__, "Make sure you are taking the mean of each column?"
    assert round(mean_scores.values[2],2) - 0.89 < 0.00001, "The mean test score is incorrect. Are you fitting the model correctly?"
    assert round(mean_scores.values[3],2) - 1.0 < 0.00001, "The mean training score is incorrect. Are you fitting the model correctly?"
    __msg__.good("Nice work, well done!")
