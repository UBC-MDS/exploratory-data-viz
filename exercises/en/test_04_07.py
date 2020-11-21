def test():
    # Here we can either check objects created in the solution code, or the
    # string value of the solution, available as __solution__. A helper for
    # printing formatted messages is available as __msg__. See the testTemplate
    # in the meta.json for details.

    # If an assertion fails, the message will be displayed
    assert list(sub_pk) == [13, 14, 15, 15, 15, 0, 0], "Values in sub_pk are incorrect. Are you subtracting correctly?"
    assert list(sq_sub_pk) == [169, 196, 225, 225, 225, 0, 0], "Values in sq_sub_pk are incorrect. Are you squaring each value correctly?"
    assert sss_pk == 1040, "The value for sss_pk is incorrect. Are you taking the sum?"
    assert 'sqrt' in __solution__, "Make sure you are using the sqrt function"
    assert round(pk_distance,2) == 32.25, "The value for sss_pk is incorrect. Are you taking the square root"
    __msg__.good("Nice work, well done!")