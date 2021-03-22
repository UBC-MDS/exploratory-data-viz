def test():
    # Here we can either check objects created in the solution code, or the
    # string value of the solution, available as __solution__. A helper for
    # printing formatted messages is available as __msg__. See the testTemplate
    # in the meta.json for details.
    # If an assertion fails, the message will be displayed

    assert not colour_plot is None, "Your answer for colour_plot does not exist. Have you assigned the plot to the correct variable name?"
    assert type(colour_plot) == alt.Chart, "colour_plot does not appear to be an Altair Chart object. Have you assigned the Altair Chart object for the plot to the correct variable?"
    assert colour_plot.mark != alt.utils.schemapi.Undefined and (
        colour_plot.mark.size == 10 and
        colour_plot.mark.type == 'point'
    ), "Make sure you are using mark_point and set size to 10."

    assert colour_plot.encoding.x.scale != alt.utils.schemapi.Undefined and (
        colour_plot.encoding.x.scale.domain != alt.utils.schemapi.Undefined
    ), "Are you selecting an appropriate domain for x-axis? Hint: set domain argument in alt.Scale()"
    assert type(colour_plot.encoding.x.title) == str and not colour_plot.encoding.x.title.islower(), "Make sure you give a descriptive axis title with appropriate capitalization for the x-axis encoding."
    assert (
        "mm" in colour_plot.encoding.x.title
    ), "Make sure to include the unit for the x-axis title (Hint: 'flipper_length_mm' is measured in 'mm'."

    assert colour_plot.encoding.y.scale != alt.utils.schemapi.Undefined and (
        colour_plot.encoding.y.scale.domain != alt.utils.schemapi.Undefined
    ), "Are you selecting an appropriate domain for y-axis? Hint: set domain argument in alt.Scale()"
    assert type(colour_plot.encoding.y.title) == str and not colour_plot.encoding.y.title.islower(), "Make sure you give a descriptive axis title with appropriate capitalization for the y-axis encoding."
    assert (
        "g" in colour_plot.encoding.y.title
    ), "Make sure to include the unit for the y-axis title (Hint: 'body_mass_g' is measured in 'g'."

    assert colour_plot.encoding.color != alt.utils.schemapi.Undefined and (
        colour_plot.encoding.color.field in {'species', 'species:nominal', 'species:N'} or
        colour_plot.encoding.color.shorthand in {'species', 'species:nominal', 'species:N'}
    ), "Make sure you are using 'species' as the color encoding."
    assert type(colour_plot.encoding.color.title) == str and not colour_plot.encoding.color.title.islower(), "Make sure you give a descriptive legend title with appropriate capitalization for the color encoding."
    assert colour_plot.encoding.color.scale != alt.utils.schemapi.Undefined and (
        colour_plot.encoding.color.scale.scheme != alt.utils.schemapi.Undefined
    ), "Are you selecting an appropriate colour scheme for color encoding? Hint: set scheme argument in alt.Scale() for color encoding"
    
    assert colour_plot.encoding.shape != alt.utils.schemapi.Undefined and (
        colour_plot.encoding.shape.field in {'species', 'species:nominal', 'species:N'} or
        colour_plot.encoding.shape.shorthand in {'species', 'species:nominal', 'species:N'}
    ), "Make sure you are using 'species' as the shape encoding."
    
    assert type(colour_plot.title) == str and len(colour_plot.title) >= 5, "Make sure you specify a descriptive title for colour_plot."
    assert not colour_plot.title.islower(), "Make sure the plot title is capitalized."
    __msg__.good("You're correct, well done!")
