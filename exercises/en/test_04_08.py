def test():
    # Here we can either check objects created in the solution code, or the
    # string value of the solution, available as __solution__. A helper for
    # printing formatted messages is available as __msg__. See the testTemplate
    # in the meta.json for details.

    # If an assertion fails, the message will be displayed
    assert 'euclidean_distances' in __solution__, "Make sure you are using the 'euclidean_distances()' function."
    assert round(pk_distance,2) == 32.25, "The value for pk_distance is incorrect. Are you calling the 'euclidean_distances()' correctly?" 
    __msg__.good("Nice work, well done!")