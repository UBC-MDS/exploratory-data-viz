def test():
    # Here we can either check objects created in the solution code, or the
    # string value of the solution, available as __solution__. A helper for
    # printing formatted messages is available as __msg__. See the testTemplate
    # in the meta.json for details.
    # If an assertion fails, the message will be displayed

    assert not text is None, "Your answer for text does not exist. Have you assigned the added text to the correct variable name?"
    assert type(text) == alt.Chart, "text does not appear to be an Altair Chart object. Have you assigned the Altair Chart object for added text to the correct variable?"
    assert text.mark != alt.utils.schemapi.Undefined and (
        text.mark.align == 'center' and
        text.mark.dx == 10 and
        text.mark.type == 'text'
    ), "Make sure you are using mark_text and specify `center` alignment and location at dx=10."
    assert text.encoding.x != alt.utils.schemapi.Undefined and (
        text.encoding.x.field in {'count()', 'count():quantitative', 'count():Q'} or
        text.encoding.x.shorthand in {'count()', 'count():quantitative', 'count():Q'}
    ), "Make sure you are using 'count()' as the x-axis encoding for the added text."
    assert text.encoding.y != alt.utils.schemapi.Undefined and (
        text.encoding.y.field in {'species', 'species:nominal', 'species:N'} or
        text.encoding.y.shorthand in {'species', 'species:nominal', 'species:N'}
    ), "Make sure you are using 'species' as the y-axis encoding for the added text."
    assert text.encoding.text != alt.utils.schemapi.Undefined and (
        text.encoding.text.field in {'count()', 'count():quantitative', 'count():Q'} or
        text.encoding.text.shorthand in {'count()', 'count():quantitative', 'count():Q'}
    ), "Make sure you are using 'count()' as the text encoding for the added text."

    assert not penguin_title is None, "Your answer for penguin_title does not exist. Have you assigned the title and subtitle formatting to the correct variable name?"
    assert type(penguin_title) == alt.TitleParams, "penguin_title does not appear to be an Altair TitleParams object. Have you assigned the Altair TitleParams object for title and subtitle formatting to the correct variable?"
    assert penguin_title.fontSize == 18, "Can you set fontSize of 18 for penguin_title?"
    assert penguin_title.subtitleColor == 'firebrick', "Can you set subtitleColor to 'firebrick' for penguin_title?"
    assert type(penguin_title.text) == str and len(penguin_title.text) >= 5, "Make sure you specify a descriptive title for penguin_title. Hint: title text for penguin_title can be specified using text argument, which is also the first argument."
    assert not penguin_title.text.islower(), "Make sure the title for penguin_title is capitalized."
    assert type(penguin_title.subtitle) == str and len(penguin_title.subtitle) >= 5, "Make sure you specify a descriptive subtitle for penguin_title."
    assert not penguin_title.subtitle.islower(), "Make sure the subtitle for penguin_title is capitalized."

    assert not formatted_plot is None, "Your answer for formatted_plot does not exist. Have you assigned the final formatted plot to the correct variable name?"
    assert type(formatted_plot) == alt.LayerChart, "formatted_plot does not appear to be an Altair LayerChart object. Have you assigned the LayerChart object for formatted plot to the correct variable?"
    assert (
        formatted_plot.config != alt.utils.schemapi.Undefined and 
        formatted_plot.config.view != alt.utils.schemapi.Undefined and
        formatted_plot.config.view.strokeWidth == 0
    ), "Make sure to remove the grey box outline from the figure. Hint: setting the strokeWidth argument to 0 in the .configure_view() method hides the outline."
    __msg__.good("You're correct, well done!")
