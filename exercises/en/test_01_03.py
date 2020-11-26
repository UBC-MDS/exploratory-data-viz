def test():
    # Here we can either check objects created in the solution code, or the
    # string value of the solution, available as __solution__. A helper for
    # printing formatted messages is available as __msg__. See the testTemplate
    # in the meta.json for details.

    # If an assertion fails, the message will be displayed
    assert 'candybar_dim' in __solution__, "Make sure you are naming your solution 'candybar_dim'."
    assert candybar_dim == (25, 10), "Did you load your data correctly? "
    assert "shape"  in __solution__, "Are you sure you used the right functions and parameters?"
    __msg__.good("Nice work, well done!")
