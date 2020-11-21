def test():
    # Here we can either check objects created in the solution code, or the
    # string value of the solution, available as __solution__. A helper for
    # printing formatted messages is available as __msg__. See the testTemplate
    # in the meta.json for details.

    # If an assertion fails, the message will be displayed
    assert 'DecisionTreeClassifier' in __solution__, "Make sure you are specifying a 'DecisionTreeClassifier'."
    assert hyper_tree.get_params()['random_state'] == 1, "Make sure you are setting the model's 'random_state' to 1."
    assert hyper_tree.get_params()['max_depth'] == 8, "Make sure you are setting the model's 'max_depth' to 8."
    assert hyper_tree.get_params()['min_samples_split'] == 4, "Make sure you are setting the model's 'min_samples_split' to 4."
    assert 'hyper_tree.fit' in __solution__, "Make sure you are using the '.fit()' function to fit 'X' and 'y'."
    assert 'hyper_tree.score' in __solution__, "Make sure you are using the '.score()' function to score the model's performance."
    assert round(tree_score,2) == 0.76, "The model's score is incorrect. Are you fitting the model with the correct parameters?"
    __msg__.good("Nice work, well done!")