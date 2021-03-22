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
    assert 'mark_bar()' in __solution__, "Make sure you are creating a bar plot using 'mark_bar'."
    assert 'bin=alt.Bin' in __solution__, "Make sure you are setting the 'maxbins' parameter."
    assert culmen_stacked_plot.encoding.x.shorthand == "culmen_depth_mm", "Make sure you are setting the x-axis to 'culmen_depth_mm'."
    assert culmen_stacked_plot.encoding.y.shorthand == "count()", "Make sure you are plotting the count on the y-axis."
    assert culmen_stacked_plot.encoding.color.shorthand == "species", "Make sure you are coloring by species."
    assert not culmen_stacked_plot.title is None, "Make sure you are providing a title for your plot."
    assert not culmen_stacked_plot.title.islower(), "Make sure the plot title is capitalized."
    assert not culmen_stacked_plot.encoding.x.title is None, "Make sure you are providing a title for the X-axis."
    assert not culmen_stacked_plot.encoding.x.title.islower() , "Make sure the X-axis title is capitalized."
    __msg__.good("You're correct, well done!")
