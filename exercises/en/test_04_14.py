def test():
    # Here we can either check objects created in the solution code, or the
    # string value of the solution, available as __solution__. A helper for
    # printing formatted messages is available as __msg__. See the testTemplate
    # in the meta.json for details.
    # If an assertion fails, the message will be displayed

    assert not cat_cols is None, "Your answer for cat_cols does not exist. Have you assigned the list of labels for categorical columns to the correct variable name?"
    assert type(cat_cols) == list, "cat_cols does not appear to be of type list. Can you store all the labels of the categorical columns into a list called cat_cols?"
    assert set(cat_cols) == set(['species', 'island', 'sex']), "Make sure you only include the categorical columns in cat_cols. Hint: there are 3 categorical columns in the dataframe."
    assert cat_cols == ['species', 'island', 'sex'], "You're close. Please make sure that the categorical columns are ordered in the same order they appear in the dataframe."

    assert not categorical_plots is None, "Your answer for categorical_plots does not exist. Have you assigned the chart object to the correct variable name?"
    assert type(categorical_plots) == alt.vegalite.v4.api.RepeatChart, "Your answer is not an Altair RepeatChart object. Check to make sure that you have assigned an alt.Chart object to categorical_plots and that you are repeating by columns in cat_cols."
    assert categorical_plots.spec.mark == 'circle', "Make sure you are using the 'mark_circle' to generate the plots."

    assert (
        ([categorical_plots.spec.encoding.x.shorthand, 
          categorical_plots.spec.encoding.y.shorthand] == 
         [alt.RepeatRef(repeat = 'row'), 
          alt.RepeatRef(repeat = 'column')]) or 
        ([categorical_plots.spec.encoding.x.shorthand,
          categorical_plots.spec.encoding.y.shorthand] == 
         [alt.RepeatRef(repeat = 'column'),
          alt.RepeatRef(repeat = 'row')])
    ), "Make sure you specify that the chart set-up is repeated for different rows & columns as the x-axis and y-axis encodings. Hint: use alt.repeat() with row and column arguments."
    
    assert categorical_plots.spec.encoding.x.type == "nominal", "Make sure you let Altair know that alt.repeat() on the x-axis encoding is a nominal type. Altair can't infer the type since alt.repeat() is not a column in the dataframe."
    assert categorical_plots.spec.encoding.y.type == "nominal", "Make sure you let Altair know that alt.repeat() on the y-axis encoding is a nominal type. Altair can't infer the type since alt.repeat() is not a column in the dataframe."

    assert categorical_plots.spec.encoding.color != alt.utils.schemapi.Undefined and (
        categorical_plots.spec.encoding.color.field in {'count()', 'count():quantitative', 'count():Q'} or
        categorical_plots.spec.encoding.color.shorthand in {'count()', 'count():quantitative', 'count():Q'}
    ), "Make sure you are using 'count()' as the color encoding."
    assert categorical_plots.spec.encoding.color.title is None, "Make sure you specify that no title should be assigned for color encoding. Hint: use None"

    assert categorical_plots.spec.encoding.size != alt.utils.schemapi.Undefined and (
        categorical_plots.spec.encoding.size.field in {'count()', 'count():quantitative', 'count():Q'} or
        categorical_plots.spec.encoding.size.shorthand in {'count()', 'count():quantitative', 'count():Q'}
    ), "Make sure you are using 'count()' as the size encoding."
    assert categorical_plots.spec.encoding.size.title is None, "Make sure you specify that no title should be assigned for size encoding. Hint: use None"

    assert categorical_plots.resolve != alt.utils.schemapi.Undefined and categorical_plots.resolve.scale != alt.utils.schemapi.Undefined and (
        categorical_plots.resolve.scale.color == "independent" and
        categorical_plots.resolve.scale.size == "independent"
    ), "Make sure to give the size and colour channels independent scales. Hint: use resolve_scale"
    __msg__.good("You're correct, well done!")
