def test():
    # Here we can either check objects created in the solution code, or the
    # string value of the solution, available as __solution__. A helper for
    # printing formatted messages is available as __msg__. See the testTemplate
    # in the meta.json for details.
    # If an assertion fails, the message will be displayed
    
    assert 'alt.selection_interval' in __solution__, "Make sure you are creating a selection interval and storing it in a varialbe called 'brush'."
    assert linked_scatter.encoding.x.shorthand == 'body_mass_g', "Make sure you are plotting body_mass_g on the x-axis"
    assert not linked_scatter.encoding.x.title is None, "Make sure you are providing a title for your X-axis"
    assert not linked_scatter.encoding.x.title.islower(), "Make sure the plot X-axis title is capitalized."
    assert linked_scatter.encoding.x.title.count("_") == 0, "Make sure your X-axis title does not contain underscores"
    assert linked_scatter.encoding.y.shorthand == 'flipper_length_mm', "Make sure you are plotting flipper_length_mm on the Y-axis"
    assert not linked_scatter.encoding.y.title is None, "Make sure you are providing a title for your Y-axis"
    assert not linked_scatter.encoding.y.title.islower(), "Make sure the plot Y-axis title is capitalized."
    assert linked_scatter.encoding.y.title.count("_") == 0, "Make sure your Y-axis title does not contain underscores"
    assert linked_scatter.encoding.color.condition.selection == 'selector001', "Make sure you are using the brush you defined earlier to color the points."
    assert len(together_plots.vconcat) == 2, "Make sure you are combinng both plots"
    assert together_plots.vconcat[1].encoding.x.shorthand == 'culmen_length_mm', "Make sure you are plotting culmen_length_mm on the X-axis for the second plot."
    assert not together_plots.vconcat[1].encoding.x.title is None, "Make sure you are providing a title for your X-axis"
    assert not together_plots.vconcat[1].encoding.x.title.islower(), "Make sure the plot X-axis title is capitalized."
    assert together_plots.vconcat[1].encoding.x.title.count("_") == 0, "Make sure your X-axis title does not contain underscores"
    assert together_plots.vconcat[1].encoding.y.shorthand == 'culmen_depth_mm', "Make sure you are plotting culmen_depth_mm on the Y-axis for the second plot."
    assert not together_plots.vconcat[1].encoding.y.title is None, "Make sure you are providing a title for your Y-axis"
    assert not together_plots.vconcat[1].encoding.y.title.islower(), "Make sure the plot Y-axis title is capitalized."
    assert together_plots.vconcat[1].encoding.y.title.count("_") == 0, "Make sure your Y-axis title does not contain underscores"
    __msg__.good("You're correct, well done!")
