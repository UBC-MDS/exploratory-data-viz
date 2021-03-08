def test():
    # Here we can either check objects created in the solution code, or the
    # string value of the solution, available as __solution__. A helper for
    # printing formatted messages is available as __msg__. See the testTemplate
    # in the meta.json for details.
    # If an assertion fails, the message will be displayed

    # Since we haven't started assigning charts to variable names yet,
    # this might be the better way to test for the first exercise.
    # Maybe even for later exercises.
    assert 'alt.Chart' in __solution__, "Make sure you are calling the 'Chart' function?"
    assert 'mark_bar' in __solution__, "Make sure you are creating a bar plot using 'mark_bar'."
    assert 'bin=alt.Bin' in __solution__, "Make sure you are setting the 'maxbins' parameter."
    assert 'opacity=' in __solution__, "Make sure you are setting an appropriate opacity value"
    assert 'culmen_depth_mm' in __solution__, "Make sure you are setting the x-axis to 'culmen_depth_mm'."
    assert 'count()' in __solution__, "Make sure you are plotting the count on the y-axis."
    assert "color=" in __solution__, "Make sure you are coloring by species."
    assert culmen_layered_plot.facet.shorthand == 'sex', "Make sure you are faceting by sex."
    assert culmen_layered_plot.columns == 1, "Make sure you are using a column."
    assert culmen_layered_plot.resolve.scale.y == 'independent', "Make sure the facet scales are independent."
    __msg__.good("You're correct, well done!")
