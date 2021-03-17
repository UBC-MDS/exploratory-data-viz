def test():
    # Here we can either check objects created in the solution code, or the
    # string value of the solution, available as __solution__. A helper for
    # printing formatted messages is available as __msg__. See the testTemplate
    # in the meta.json for details.
    # If an assertion fails, the message will be displayed

    assert not penguin_heatmap is None, "Your answer does not exist. Have you passed in the correct variable?"
    assert type(penguin_heatmap) == type(alt.Chart()), "Your answer is not an Altair Chart object. Check to make sure that you have assigned an alt.Chart object to penguin_heatmap."
    assert penguin_heatmap.mark == 'rect', "Make sure you are using the 'mark_rect' to generate a heatmap."
    
    assert (
        penguin_heatmap.encoding.x.shorthand in {'flipper_length_mm', 'flipper_length_mm:quantitative', 'flipper_length_mm:Q'} or 
        penguin_heatmap.encoding.x.field in {'flipper_length_mm', 'flipper_length_mm:quantitative', 'flipper_length_mm:Q'}
    ), "Make sure you are using 'flipper_length_mm' as the x-axis encoding."
    assert penguin_heatmap.encoding.x.bin != alt.utils.schemapi.Undefined, "Make sure you are specifying the bin argument for the x-axis encoding for the heatmap."
    assert penguin_heatmap.encoding.x.bin.maxbins == 30, "Have you set the maxbins argument for the x-axis encoding to 30?"
    assert type(penguin_heatmap.encoding.x.title) == str and not penguin_heatmap.encoding.x.title.islower(), "Make sure you give a descriptive legend title with appropriate capitalization for the x-axis encoding. Hint: use title argument."
    
    assert (
        penguin_heatmap.encoding.y.shorthand in {'body_mass_g', 'body_mass_g:quantitative', 'body_mass_g:Q'} or 
        penguin_heatmap.encoding.y.field in {'body_mass_g', 'body_mass_g:quantitative', 'body_mass_g:Q'}
    ), "Make sure you are using 'body_mass_g' as the y-axis encoding."
    assert penguin_heatmap.encoding.y.bin != alt.utils.schemapi.Undefined, "Make sure you are specifying the bin argument for the y-axis encoding for the heatmap."
    assert penguin_heatmap.encoding.y.bin.maxbins == 30, "Have you set the maxbins argument for the y-axis encoding to 30?"
    assert type(penguin_heatmap.encoding.y.title) == str and not penguin_heatmap.encoding.y.title.islower(), "Make sure you give a descriptive legend title with appropriate capitalization for the y-axis encoding. Hint: use title argument."
    
    assert penguin_heatmap.encoding.color != alt.utils.schemapi.Undefined and (
        penguin_heatmap.encoding.color.field in {'count()', 'count():quantitative', 'count():Q'} or 
        penguin_heatmap.encoding.color.shorthand in {'count()', 'count():quantitative', 'count():Q'}
    ), "Make sure you are using 'count()' as the color encoding."
    assert type(penguin_heatmap.encoding.color.title) == str and not penguin_heatmap.encoding.color.title.islower(), "Make sure you give a descriptive legend title with appropriate capitalization for the color encoding. Hint: use title argument."
    
    assert type(penguin_heatmap.title) == str and len(penguin_heatmap.title) >= 5, "Make sure you give a descriptive title for the penguin_heatmap plot."
    assert not penguin_heatmap.title.islower(), "Make sure the plot title is capitalized."
    assert penguin_heatmap.height == 200, "Make sure your plot has a height of 200."
    assert penguin_heatmap.width == 250, "Make sure your plot has a width of 250."
    __msg__.good("You're correct, well done!")
