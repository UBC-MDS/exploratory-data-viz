def test():
    # Here we can either check objects created in the solution code, or the
    # string value of the solution, available as __solution__. A helper for
    # printing formatted messages is available as __msg__. See the testTemplate
    # in the meta.json for details.
    # If an assertion fails, the message will be displayed

    assert not pokemon_circleplot is None, "Your answer does not exist. Have you passed in the correct variable?"
    assert type(pokemon_circleplot) == type(alt.Chart()), "Your answer is not an Altair Chart object. Check to make sure that you have assigned an alt.Chart object to pokemon_circleplot."
    assert pokemon_circleplot.mark == 'circle', "Make sure you are using the 'mark_circle' to generate a circleplot."

    assert (
        pokemon_circleplot.encoding.x.shorthand in {'gen:ordinal', 'gen:O'} or 
        pokemon_circleplot.encoding.x.field in {'gen:ordinal', 'gen:O'}
    ), "Make sure you are using 'gen' as the x-axis encoding and specify that it is an ordinal (`O`) value."
    assert type(pokemon_circleplot.encoding.x.title) == str and not pokemon_circleplot.encoding.x.title.islower(), "Make sure you give a descriptive legend title with appropriate capitalization for the x-axis encoding. Hint: use title argument."
    
    assert (
        pokemon_circleplot.encoding.y.shorthand in {'type', 'type:nominal', 'type:N'} or 
        pokemon_circleplot.encoding.y.field in {'type', 'type:nominal', 'type:N'}
    ), "Make sure you are using 'type' as the y-axis encoding."
    assert type(pokemon_circleplot.encoding.y.title) == str and not pokemon_circleplot.encoding.y.title.islower(), "Make sure you give a descriptive legend title with appropriate capitalization for the y-axis encoding. Hint: use title argument."
    
    assert pokemon_circleplot.encoding.color != alt.utils.schemapi.Undefined and (
        pokemon_circleplot.encoding.color.field in {'count()', 'count():quantitative', 'count():Q'} or 
        pokemon_circleplot.encoding.color.shorthand in {'count()', 'count():quantitative', 'count():Q'}
    ), "Make sure you are using 'count()' as the color encoding."
    assert type(pokemon_circleplot.encoding.color.title) == str and not pokemon_circleplot.encoding.color.title.islower(), "Make sure you give a descriptive legend title with appropriate capitalization for the color encoding. Hint: use title argument."

    assert pokemon_circleplot.encoding.size != alt.utils.schemapi.Undefined and (
        pokemon_circleplot.encoding.size.field in {'count()', 'count():quantitative', 'count():Q'} or 
        pokemon_circleplot.encoding.size.shorthand in {'count()', 'count():quantitative', 'count():Q'}
    ), "Make sure you are using 'count()' as the size encoding."
    assert type(pokemon_circleplot.encoding.size.title) == str and not pokemon_circleplot.encoding.size.title.islower(), "Make sure you give a descriptive legend title with appropriate capitalization for the size encoding. Hint: use title argument."
        
    assert type(pokemon_circleplot.title) == str and len(pokemon_circleplot.title) >= 5, "Make sure you specify a descriptive title for the pokemon_circleplot plot."
    assert not pokemon_circleplot.title.islower(), "Make sure the plot title is capitalized."
    __msg__.good("You're correct, well done!")