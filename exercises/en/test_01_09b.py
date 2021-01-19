import re

def test():
    # Here we can either check objects created in the solution code, or the
    # string value of the solution, available as __solution__. A helper for
    # printing formatted messages is available as __msg__. See the testTemplate
    # in the meta.json for details.
    # If an assertion fails, the message will be displayed

    # Regex expression to capture the line plot variable name without whitespace
    capture_grp = re.search("[^\s]*(?=\s*=\s*alt.Chart\(stocks\).mark_line)", __solution__)
    assert capture_grp, "Make sure you assign the line plot to a variable name."
    # capture_grp.group() holds the variable name of line plot
    assert capture_grp.group() + ".mark_point" in __solution__, "Make sure you add a layer of another plot object, created from the line plot object with the same encodings but different mark type."

    # Making sure that the attributes for the line plot object provided in sample code remain unmodified.
    # Actual plot object is stored in globals() dict.
    line_plot_object = globals()[capture_grp.group()]
    # Following test added for a more graceful error message if line_plot_object is not of type Chart.
    assert type(line_plot_object) == type(alt.Chart()), "Something happened to your line plot. Check to make sure that it is a correct alt.Chart line plot or try renaming the line plot."
    assert line_plot_object.mark == 'line', f"Make sure you keep {capture_grp.group()} as a line plot using the correct mark type."
    assert line_plot_object.encoding.x.shorthand == 'date', "Make sure you keep 'date' as the x-axis encoding."
    assert line_plot_object.encoding.y.shorthand == 'price', "Make sure you keep 'price' as the y-axis encoding."
    assert line_plot_object.encoding.color.shorthand == 'symbol', "Make sure you keep 'symbol' as the color encoding."
    __msg__.good("You're correct, well done!")
