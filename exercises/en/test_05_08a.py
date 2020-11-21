def test():
    # Here we can either check objects created in the solution code, or the
    # string value of the solution, available as __solution__. A helper for
    # printing formatted messages is available as __msg__. See the testTemplate
    # in the meta.json for details.

    # If an assertion fails, the message will be displayed
    assert 'X_train.info()' in __solution__, "Make sure you are using the .info() function to explore the data."
    assert 'any(axis=1)' in __solution__, "Make sure you are using any(axis=1) when computing the number of missing values."
    assert num_nan == 56, "The number of missing values is incorrect. Are you using the .isnull() function?"
    __msg__.good("Nice work, well done!")
