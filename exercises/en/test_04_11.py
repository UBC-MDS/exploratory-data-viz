def test():
    # Here we can either check objects created in the solution code, or the
    # string value of the solution, available as __solution__. A helper for
    # printing formatted messages is available as __msg__. See the testTemplate
    # in the meta.json for details.
    # If an assertion fails, the message will be displayed

    assert not numeric_cols is None, "Your answer for numeric_cols does not exist. Have you assigned the list of labels for numeric columns to the correct variable name?"
    assert type(numeric_cols) == list, "numeric_cols does not appear to be of type list. Can you store all the labels of the numeric columns into a list called numeric_cols?"
    assert set(numeric_cols) == set(['culmen_length_mm', 'culmen_depth_mm', 'flipper_length_mm', 'body_mass_g']), "Make sure you only include the numeric columns in numeric_cols. Hint: there are 4 numeric columns in the dataframe."
    assert numeric_cols == ['culmen_length_mm', 'culmen_depth_mm', 'flipper_length_mm', 'body_mass_g'], "You're close. Please make sure that the numeric columns are ordered in the same order they appear in the dataframe."

    assert not numeric_histograms is None, "Your answer for numeric_histograms does not exist. Have you assigned the chart object to the correct variable name?"
    assert type(numeric_histograms) == alt.vegalite.v4.api.RepeatChart, "Your answer is not an Altair RepeatChart object. Check to make sure that you have assigned an alt.Chart object to numeric_histograms and that you are repeating by columns in numeric_cols."
    assert numeric_histograms.columns == 2, "Make sure you have 2 columns in your RepeatChart. Hint: use columns argument."
    assert numeric_histograms.spec.mark == 'bar', "Make sure you are using the 'mark_bar' to generate histograms."

    assert numeric_histograms.spec.encoding.x.shorthand == alt.RepeatRef(repeat = 'repeat'), "Make sure you specify that the chart set-up is repeated for different columns as the x-axis encoding. Hint: use alt.repeat()"
    assert numeric_histograms.spec.encoding.x.bin != alt.utils.schemapi.Undefined, "Make sure you are specifying the bin argument for the x-axis encoding for the histogram."
    assert numeric_histograms.spec.encoding.x.bin.maxbins != alt.utils.schemapi.Undefined, "Make sure you specify the maxbins argument for binning the x-axis encoding to something reasonable (like 30 or 40)."
    assert numeric_histograms.spec.encoding.x.type == "quantitative", "Make sure you let Altair know that alt.repeat() is a quantitative type, since it's not a column in the dataframe."

    assert (
        numeric_histograms.spec.encoding.y.field in {'count()', 'count():quantitative', 'count():Q'} or
        numeric_histograms.spec.encoding.y.shorthand in {'count()', 'count():quantitative', 'count():Q'}
    ), "Make sure you are using 'count()' as the y-axis encoding."

    assert numeric_histograms.spec.height == 150, "Make sure your plot has a height of 150."
    assert numeric_histograms.spec.width == 150, "Make sure your plot has a width of 150."
    __msg__.good("You're correct, well done!")
