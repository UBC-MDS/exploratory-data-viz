def test():
    # Here we can either check objects created in the solution code, or the
    # string value of the solution, available as __solution__. A helper for
    # printing formatted messages is available as __msg__. See the testTemplate
    # in the meta.json for details.
    # If an assertion fails, the message will be displayed
    
    assert slider.input == 'range', 'Make sure you are creating slider range binding.'
    assert slider.name == 'Body mass (g)', "Make sure you are providing the correct name to the slider range object."
    assert slider.max == 6300.0, "Make sure you are taking the max of the body_mass_g column in the slider range object."
    assert slider_scatter.encoding.opacity.condition.test == '(datum.body_mass_g < selector001.body_mass_g)', "Make sure you are setting the opacity threshold correctly for a click."
    assert slider_scatter.encoding.opacity.value == 0.05, "Make sure you are setting the opacity value to 0.05 when there is no click."
    assert 'add_selection(select_rating)' in __solution__, "Make sure you are passing the slider range object to the add_selection() function."
    __msg__.good("You're correct, well done!")
