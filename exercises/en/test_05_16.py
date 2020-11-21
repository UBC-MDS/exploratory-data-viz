def test():
    # Here we can either check objects created in the solution code, or the
    # string value of the solution, available as __solution__. A helper for
    # printing formatted messages is available as __msg__. See the testTemplate
    # in the meta.json for details.
    import pandas as pd

    # If an assertion fails, the message will be displayed
    assert 'SimpleImputer(strategy="median")' in __solution__, "Make sure you are including a simple imputer with strategy median in your pipeline."
    assert 'StandardScaler()' in __solution__, "Make sure you are using a StandardScaler() in your pipeline."
    assert "KNeighborsClassifier()" in __solution__,  "Make sure you are using a KNeighborsClassifier() in your pipeline."
    assert "cross_validate" in __solution__, "Make sure you are calling the cross validate function on your pipeline."
    assert "return_train_score" in __solution__, "Make sure you are returning the cross validation scores"
    assert [round(x,3) for x in mean_scores] == [0.005, 0.003, 0.882, 0.915], "Your mean scores are incorect. Are you returning the mean of the cross validation scores?"
    __msg__.good("Nice work, well done!")
