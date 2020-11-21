def test():
    # Here we can either check objects created in the solution code, or the
    # string value of the solution, available as __solution__. A helper for
    # printing formatted messages is available as __msg__. See the testTemplate
    # in the meta.json for details.

    # If an assertion fails, the message will be displayed
    assert 'X' in __solution__, "Make sure you are using 'X' as a variable"
    assert 'y' in __solution__, "Make sure you are using 'y' as a variable"
    assert X.shape == (25, 8), "The dimensions of X is incorrect. Are you selcting the correct columns?"
    assert y.shape == (25,), "The dimensions of y is incorrect. Are you selcting the correct columns?"
    assert 'availability' not in X.columns, "Make sure the target is not in X dataframe"
    assert sorted(list(X.columns))[0:4] == ['caramel', 'chocolate', 'coconut', 'cookie_wafer_rice'], "The X dataframe includes the incorrect columns. Make sure you are selecting the correct columns"
    __msg__.good("Nice work, well done!")
 
