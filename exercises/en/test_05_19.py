def test():
    # Here we can either check objects created in the solution code, or the
    # string value of the solution, available as __solution__. A helper for
    # printing formatted messages is available as __msg__. See the testTemplate
    # in the meta.json for details.
    # If an assertion fails, the message will be displayed

    assert not temp_plot is None, "Your answer for temp_plot does not exist. Have you assigned the plot to the correct variable name?"
    assert type(temp_plot) == alt.Chart, "temp_plot does not appear to be an Altair Chart object. Have you assigned the Altair Chart object for the plot to the correct variable?"
    assert temp_plot.mark != alt.utils.schemapi.Undefined and (
        temp_plot.mark.size == 50 and
        temp_plot.mark.type == 'circle'
    ), "Make sure you are using mark_circle and set size to 50."

    assert (
        temp_plot.encoding.x.field in {'date', 'date:temporal', 'date:T'} or
        temp_plot.encoding.x.shorthand in {'date', 'date:temporal', 'date:T'}
    ), "Make sure you are using 'date' as the x-axis encoding."
    assert type(temp_plot.encoding.x.title) == str and not temp_plot.encoding.x.title.islower(), "Make sure you give a descriptive axis title with appropriate capitalization for the x-axis encoding."

    assert (
        temp_plot.encoding.y.field in {'total_rain_mm', 'total_rain_mm:quantitative', 'total_rain_mm:Q'} or
        temp_plot.encoding.y.shorthand in {'total_rain_mm', 'total_rain_mm:quantitative', 'total_rain_mm:Q'}
    ), "Make sure you are using 'total_rain_mm' as the y-axis encoding."
    assert type(temp_plot.encoding.y.title) == str and not temp_plot.encoding.y.title.islower(), "Make sure you give a descriptive axis title with appropriate capitalization for the y-axis encoding."
    assert (
        "mm" in temp_plot.encoding.y.title
    ), "Make sure to include the unit for the y-axis title (Hint: 'total_rain_mm' is measured in 'mm'."

    assert temp_plot.encoding.color != alt.utils.schemapi.Undefined and (
        temp_plot.encoding.color.field in {'mean_temp', 'mean_temp:quantitative', 'mean_temp:Q'} or
        temp_plot.encoding.color.shorthand in {'mean_temp', 'mean_temp:quantitative', 'mean_temp:Q'}
    ), "Make sure you are using 'mean_temp' as the color encoding."
    assert type(temp_plot.encoding.color.title) == str and not temp_plot.encoding.color.title.islower(), "Make sure you give a descriptive legend title with appropriate capitalization for the color encoding."
    assert temp_plot.encoding.color.scale != alt.utils.schemapi.Undefined and (
        temp_plot.encoding.color.scale.scheme != alt.utils.schemapi.Undefined and
        temp_plot.encoding.color.scale.domainMid != alt.utils.schemapi.Undefined
    ), "Are you selecting an appropriate colour scheme and specifying mid-point value for color encoding? Hint: set scheme argument and domainMid argument in alt.Scale() for color encoding"
    
    assert type(temp_plot.title) == str and len(temp_plot.title) >= 5, "Make sure you specify a descriptive title for temp_plot."
    assert not temp_plot.title.islower(), "Make sure the plot title is capitalized."
    __msg__.good("You're correct, well done!")
