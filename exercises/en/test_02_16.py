def test():
    # Here we can either check objects created in the solution code, or the
    # string value of the solution, available as __solution__. A helper for
    # printing formatted messages is available as __msg__. See the testTemplate
    # in the meta.json for details.
    # If an assertion fails, the message will be displayed

    # Since we haven't started assigning charts to variable names yet,
    # this might be the better way to test for the first exercise.
    # Maybe even for later exercises.
    assert not penguin_facet is None, "Your answer does not exist. Have you passed in the correct variable?"
    assert type(penguin_facet) == alt.vegalite.v4.api.FacetChart, "Your answer is not an Altair FacetChart object. Check to make sure that you have assigned an alt.Chart object to penguin_facet and that you are facetting by 'species' for the columns and by 'island' for the rows."
    assert penguin_facet.data.equals(penguins) and penguin_facet.data.shape == (344, 7), "Make sure you are using the penguins dataset."
    assert penguin_facet.facet.column in {'species', 'species:nominal', 'species:N'}, "Make sure you are facetting by 'species' for the columns."
    assert penguin_facet.facet.row in {'island', 'island:nominal', 'island:N'}, "Make sure you are facetting by 'island' for the rows."
    assert penguin_facet.spec.mark == 'bar', "Make sure you are using the bar mark type."
    assert (penguin_facet.spec.encoding.x.shorthand in {'body_mass_g', 'body_mass_g:quantitative', 'body_mass_g;Q'} or 
            penguin_facet.spec.encoding.x.field in {'body_mass_g', 'body_mass_g:quantitative', 'body_mass_g;Q'}), "Make sure you are using 'body_mass_g' as the x-axis encoding."
    assert penguin_facet.spec.encoding.x.bin != alt.utils.schemapi.Undefined, "Make sure you are specifying the bin argument for the x-axis encoding for the histogram."
    assert (penguin_facet.spec.encoding.y.field in {'count()', 'count():quantitative', 'count:Q'} or 
            penguin_facet.spec.encoding.y.shorthand in {'count()', 'count():quantitative', 'count:Q'}), "Make sure you are using 'count()' as the y-axis encoding."
    assert type(penguin_facet.spec.title) == str and len(penguin_facet.spec.title) >= 5, "Make sure you specify a descriptive title for the penguin_bar plot."
    assert penguin_facet.spec.height == 100, "Make sure you specify the plot height of 100."
    assert penguin_facet.spec.width == 150, "Make sure you specify the plot width of 150."
    __msg__.good("You're correct, well done!")
