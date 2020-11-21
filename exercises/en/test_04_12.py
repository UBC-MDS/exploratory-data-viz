def test():
    # Here we can either check objects created in the solution code, or the
    # string value of the solution, available as __solution__. A helper for
    # printing formatted messages is available as __msg__. See the testTemplate
    # in the meta.json for details.

    # If an assertion fails, the message will be displayed
    assert 'NearestNeighbors' in __solution__, "Make sure you are using the NearestNeighbors() function with n_neighbors = 1."
    assert 'nn.fit(X_train)' in __solution__, "Make sure you are fitting the model on the training data."
    assert 'NearestNeighbors' in __solution__, "Make sure you are using the NearestNeighbors argument."
    assert snoodle_name == 'Servine', "The value for the nearest neighbour is incorrect. Are you setting up the model correctly?"
    assert round(snoodles_neighbour[0][0][0]) == 23.0, "The nearest neighbor distance is incorrect. Are you fitting the model properly?"
    __msg__.good("Nice work, well done!")