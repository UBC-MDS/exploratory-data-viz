def test():
    # Here we can either check objects created in the solution code, or the
    # string value of the solution, available as __solution__. A helper for
    # printing formatted messages is available as __msg__. See the testTemplate
    # in the meta.json for details.

    # If an assertion fails, the message will be displayed
    assert 'DecisionTreeClassifier' in __solution__, "Make sure you are specifying a 'DecisionTreeClassifier'."
    assert model.get_params()['random_state'] == 1, "Make sure you are settting the model's 'random_state' to 1."
    assert 'model.fit' in __solution__, "Make sure you are using the '.fit()' function to fit 'X' and 'y'."
    assert 'model.predict(X)' in __solution__, "Make sure you are using the model to predict on 'X'."
    assert list(predicted).count('Canada') == 6, "Your predicted values are incorrect. Are you fitting the model properly?"
    assert list(predicted).count('Both') == 8, "Your predicted values are incorrect. Are you fitting the model properly?"
    assert list(predicted).count('America') == 11, "Your predicted values are incorrect. Are you fitting the model properly?"
    __msg__.good("Nice work, well done!")