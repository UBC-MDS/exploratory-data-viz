def test():
    # Here we can either check objects created in the solution code, or the
    # string value of the solution, available as __solution__. A helper for
    # printing formatted messages is available as __msg__. See the testTemplate
    # in the meta.json for details.
    # If an assertion fails, the message will be displayed

    # Since we haven't started assigning charts to variable names yet,
    # this might be the better way to test for the first exercise.
    # Maybe even for later exercises.
    assert not penguin_hist is None, "Your answer does not exist. Have you passed in the correct variable?"
    assert type(penguin_hist) == type(alt.Chart()), "Your answer is not an Altair Chart object. Check to make sure that you have assigned an alt.Chart object to penguin_hist."
    assert penguin_hist.data.equals(penguins_df) and penguin_hist.data.shape == (344, 7), "Make sure you are using the penguins dataset."
    assert penguin_hist.mark == 'bar', "Make sure you are using the bar mark type."
    assert (penguin_hist.encoding.x.shorthand in {'flipper_length_mm', 'flipper_length_mm:quantitative', 'flipper_length_mm:Q'} or 
            penguin_hist.encoding.x.field in {'flipper_length_mm', 'flipper_length_mm:quantitative', 'flipper_length_mm:Q'}), "Make sure you are using 'flipper_length_mm' as the x-axis encoding."
    assert penguin_hist.encoding.x.bin != alt.utils.schemapi.Undefined, "Make sure you are specifying the bin argument for the x-axis encoding for the histogram."
    assert (penguin_hist.encoding.y.field in {'count()', 'count():quantitative', 'count():Q'} or 
            penguin_hist.encoding.y.shorthand in {'count()', 'count():quantitative', 'count():Q'}), "Make sure you are using 'count()' as the y-axis encoding."
    assert type(penguin_hist.title) == str and len(penguin_hist.title) >= 5, "Make sure you specify a descriptive title for the penguin_hist plot."
    assert penguin_hist.height == 150, "Make sure you specify the plot height of 150."
    assert penguin_hist.width == 300, "Make sure you specify the plot width of 300." 
    __msg__.good("You're correct, well done!")
