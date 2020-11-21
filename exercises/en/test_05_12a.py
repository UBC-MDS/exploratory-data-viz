def test():
    # Here we can either check objects created in the solution code, or the
    # string value of the solution, available as __solution__. A helper for
    # printing formatted messages is available as __msg__. See the testTemplate
    # in the meta.json for details.

    # If an assertion fails, the message will be displayed
    assert ' StandardScaler()' in __solution__, "Make sure you are using the  StandardScaler()() function."
    assert "ss_scaler.transform" in __solution__,  "Make sure you are transforming the test data using the scaler model."
    assert "KNeighborsClassifier()" in __solution__, "Make sure you are buiding a KNeighborsClassifier()."
    assert ss_score == 0.902, "Your training score is incorrect. Are you fitting and scoring the model on the training data? Are you rounding to 3 decimal places?"
    __msg__.good("Nice work, well done!")
