def test():
    # Here we can either check objects created in the solution code, or the
    # string value of the solution, available as __solution__. A helper for
    # printing formatted messages is available as __msg__. See the testTemplate
    # in the meta.json for details.

    # If an assertion fails, the message will be displayed
    assert "DummyClassifier" in __solution__, "Make sure you are intiating a dummy classifier."
    assert "most_frequent" in __solution__, "Make sure you are using the 'most_frequent' strategy."
    assert "model.fit"  in __solution__, "Are you sure you used the right functions and parameters?"
    assert "model.predict"  in __solution__, "Are you sure you used the right functions and parameters?"
    assert accuracy == 0.36, "The accuracy value is incorrect. Are you using the 'model.score() function?"
    __msg__.good("Well done! You successfully trained the data and predicted labels using a machine learning model!")
 