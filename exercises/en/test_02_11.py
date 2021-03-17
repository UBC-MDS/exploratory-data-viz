def test():
    # Here we can either check objects created in the solution code, or the
    # string value of the solution, available as __solution__. A helper for
    # printing formatted messages is available as __msg__. See the testTemplate
    # in the meta.json for details.
    # If an assertion fails, the message will be displayed

    # Since we haven't started assigning charts to variable names yet,
    # this might be the better way to test for the first exercise.
    # Maybe even for later exercises.
    assert not penguin_bar is None, "Your answer does not exist. Have you passed in the correct variable?"
    assert type(penguin_bar) == type(alt.Chart()), "Your answer is not an Altair Chart object. Check to make sure that you have assigned an alt.Chart object to penguin_bar."
    assert penguin_bar.data.equals(penguins) and penguin_bar.data.shape == (344, 7), "Make sure you are using the penguins dataset."
    assert penguin_bar.mark == 'bar', "Make sure you are using the bar mark type."
    assert (penguin_bar.encoding.x.shorthand in {'count()', 'count():quantitative', 'count():Q'} or 
            penguin_bar.encoding.x.field in {'count()', 'count():quantitative', 'count():Q'}), "Make sure you are using 'count()' as the x-axis encoding."
    assert (penguin_bar.encoding.y.field in {'species', 'species:nominal', 'species:N'} or 
            penguin_bar.encoding.y.shorthand in {'species', 'species:nominal', 'species:N'}), "Make sure you are using 'species' as the y-axis encoding."
    assert penguin_bar.encoding.y.sort != alt.utils.schemapi.Undefined, "Make sure you specify the sort argument for the y-axis encoding."
    assert type(penguin_bar.title) == str and len(penguin_bar.title) >= 5, "Make sure you specify a descriptive title for the penguin_bar plot."
    assert penguin_bar.height == 150, "Make sure you specify the plot height of 150."
    assert penguin_bar.width == 300, "Make sure you specify the plot width of 300." 
    __msg__.good("You're correct, well done!")
