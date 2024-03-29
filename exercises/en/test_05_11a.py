def test():
    # Here we can either check objects created in the solution code, or the
    # string value of the solution, available as __solution__. A helper for
    # printing formatted messages is available as __msg__. See the testTemplate
    # in the meta.json for details.
    # If an assertion fails, the message will be displayed

    assert not income_plot is None, "Your answer for income_plot does not exist. Have you assigned the plot to the correct variable name?"
    assert type(income_plot) == alt.Chart, "income_plot does not appear to be an Altair Chart object. Have you assigned the Altair Chart object for the plot to the correct variable?"
    assert income_plot.mark != alt.utils.schemapi.Undefined and (
        income_plot.mark.opacity == 0.5 and
        income_plot.mark.size == 10 and
        income_plot.mark.type == 'circle'
    ), "Make sure you are using mark_circle and set opacity to 0.5 and size to 10."

    assert income_plot.encoding.x.axis != alt.utils.schemapi.Undefined and (
        income_plot.encoding.x.axis.format in {'s', '~s'}
    ), "Make sure you are specifying that the axis values for x-axis encoding have SI units. Hint: set format argument to 's' in alt.Axis()"
    assert type(income_plot.encoding.x.title) == str and not income_plot.encoding.x.title.islower(), "Make sure you give a descriptive axis title with appropriate capitalization for the x-axis encoding."
    assert (
        "₱" in income_plot.encoding.x.title or
        "PHP" in income_plot.encoding.x.title
    ), "Make sure to include the unit for the x-axis title (Hint: 'tot_income' is measured in 'PHP' currency."

    assert income_plot.encoding.y.axis != alt.utils.schemapi.Undefined and (
        income_plot.encoding.y.axis.format in {'s', '~s'}
    ), "Make sure you are specifying that the axis values for y-axis encoding have SI units. Hint: set format argument to 's' in alt.Axis()"
    assert type(income_plot.encoding.y.title) == str and not income_plot.encoding.y.title.islower(), "Make sure you give a descriptive axis title with appropriate capitalization for the y-axis encoding."
    assert (
        "₱" in income_plot.encoding.y.title or
        "PHP" in income_plot.encoding.y.title
    ), "Make sure to include the unit for the y-axis title (Hint: 'education_expenditure' is measured in 'PHP' currency."

    assert type(income_plot.title) == str and len(income_plot.title) >= 5, "Make sure you specify a descriptive title for income_plot."
    assert not income_plot.title.islower(), "Make sure the plot title is capitalized."
    __msg__.good("You're correct, well done!")
