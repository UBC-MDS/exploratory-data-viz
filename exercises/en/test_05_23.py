def test():
    # Here we can either check objects created in the solution code, or the
    # string value of the solution, available as __solution__. A helper for
    # printing formatted messages is available as __msg__. See the testTemplate
    # in the meta.json for details.
    # If an assertion fails, the message will be displayed

    assert not rain_plot is None, "Your answer for rain_plot does not exist. Have you assigned the plot to the correct variable name?"
    assert type(rain_plot) == alt.Chart, "rain_plot does not appear to be an Altair Chart object. Have you assigned the Altair Chart object for the plot to the correct variable?"
    assert rain_plot.mark == 'bar', "Make sure you are using mark_bar for rain_plot."

    assert type(rain_plot.encoding.x.title) == str and not rain_plot.encoding.x.title.islower(), "Make sure you give a descriptive axis title with appropriate capitalization for the x-axis encoding."
    assert (
        "mm" in rain_plot.encoding.x.title
    ), "Make sure to include the unit for the x-axis title (Hint: 'total_rain_mm' is measured in 'mm'."

    assert (
        rain_plot.encoding.color != alt.utils.schemapi.Undefined and
        rain_plot.encoding.color.condition != alt.utils.schemapi.Undefined
    ), "Make sure you use alt.Condition in color encoding to designate a different colour to the month with the highest rainfall."
    assert(
        "datum.month" in str(rain_plot.encoding.color.condition.test) and (
            "top_month" in str(rain_plot.encoding.color.condition.test) or
            "May" in str(rain_plot.encoding.color.condition.test)
        )
    ), "Make sure you use correct condition in color encoding to designate a different colour to the month with the highest rainfall. Hint: you can compare alt.datum.month with the top_month defined above."
    assert rain_plot.encoding.color.value != rain_plot.encoding.color.condition.value, "Make sure you designate different colours to month with the highest rainfall and other months."
    
    assert type(rain_plot.title) == str and len(rain_plot.title) >= 5, "Make sure you specify a descriptive title for rain_plot."
    assert not rain_plot.title.islower(), "Make sure the plot title is capitalized."

    assert not text_plot is None, "Your answer for text_plot does not exist. Have you assigned the plot annotation object to the correct variable name?"
    assert type(text_plot) == alt.Chart, "text_plot does not appear to be an Altair Chart object. Have you assigned the Altair Chart object for the plot annotation to the correct variable?"
    assert text_plot.mark != alt.utils.schemapi.Undefined and (
        text_plot.mark.align== 'left' and
        text_plot.mark.dx== 5 and
        text_plot.mark.type == 'text'
    ), "Make sure you are using mark_text and specify `left` alignment and location at dx=4 for text_plot."
    assert (
        text_plot.encoding.text != alt.utils.schemapi.Undefined and
        text_plot.encoding.text.format == 'd' and (
            (
                text_plot.encoding.text.field in {'sum(total_rain_mm)', 'sum(total_rain_mm):quantitative', 'sum(total_rain_mm):Q'} or
                text_plot.encoding.text.shorthand in {'sum(total_rain_mm)', 'sum(total_rain_mm):quantitative', 'sum(total_rain_mm):Q'}
            ) or 
            (
                text_plot.encoding.text.aggregate == 'sum' and (
                    text_plot.encoding.text.field in {'total_rain_mm', 'total_rain_mm:quantitative', 'total_rain_mm:Q'} or
                    text_plot.encoding.text.shorthand in {'total_rain_mm', 'total_rain_mm:quantitative', 'total_rain_mm:Q'}
                )
            )
        )
    ), "Make sure you are the text encoding for text_plot displays the aggregate precipitation for each month, formatted to show integer values only." 

    assert text_plot.encoding.color != alt.utils.schemapi.Undefined and (
        text_plot.encoding.color.value == 'black'
    ), "Make sure you are setting the text color for text annotation to black. Hint: remember when setting color to a specific color, you have to use alt.value()."

    __msg__.good("You're correct, well done!")
