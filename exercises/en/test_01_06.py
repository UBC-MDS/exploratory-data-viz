def test():
    # Here we can either check objects created in the solution code, or the
    # string value of the solution, available as __solution__. A helper for
    # printing formatted messages is available as __msg__. See the testTemplate
    # in the meta.json for details.
    # If an assertion fails, the message will be displayed

    # Since we haven't started assigning charts to variable names yet,
    # this might be the better way to test for the first exercise.
    # Maybe even for later exercises.
    assert 'alt.Chart(cars)' in __solution__, "Make sure you're passing the correct data object for plotting."
    assert 'mark_point' in __solution__, "Make sure you're using the correct type of mark"
    assert 'x="Weight_in_lbs"' in __solution__, "Did you encode the x channel correctly?"
    assert 'y="Horsepower"' in __solution__, "Did you encode the y channel correctly?"
    assert 'color="Origin"' in __solution__, "Did you encode the color channel correctly?"
    __msg__.good("You're correct, well done!")
