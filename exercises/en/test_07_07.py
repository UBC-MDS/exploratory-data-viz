def test():
    # Here we can either check objects created in the solution code, or the
    # string value of the solution, available as __solution__. A helper for
    # printing formatted messages is available as __msg__. See the testTemplate
    # in the meta.json for details.
    # If an assertion fails, the message will be displayed
    
    assert click.selection.type == 'multi', "Make sure you are creating a multiple selection tool."
    assert click.selection.bind == 'legend', "Make sure you are creating a multiple selection tool that binds to the legend."
    assert click.selection.fields[0] == 'island', "Make sure we are selecting observations from the island column."
    assert click_legend.encoding.y.sort == 'x', "Make sure you are sorting the Y-axis by the x values."
    assert click_legend.encoding.color.shorthand == 'island', "Make sure you are coloring the plot using the island column."
    assert click_legend.encoding.opacity.condition.selection, "Make sure you are passing the click variable to the opacity encoding."
    assert click_legend.encoding.opacity.condition.value == 0.9, "Make sure you are setting the opacity value for a click to 0.9."
    assert click_legend.encoding.opacity.value == 0.2, "Make sure you are setting the opacity value to 0.2 when there is no click."
    assert 'add_selection(click)' in __solution__, "Make sure you are passing the selection tool object to the add_selection() function."
    __msg__.good("You're correct, well done!")
