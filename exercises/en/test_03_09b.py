def test():
    # Here we can either check objects created in the solution code, or the
    # string value of the solution, available as __solution__. A helper for
    # printing formatted messages is available as __msg__. See the testTemplate
    # in the meta.json for details.
    # If an assertion fails, the message will be displayed

    # Since we haven't started assigning charts to variable names yet,
    # this might be the better way to test for the first exercise.
    # Maybe even for later exercises.
    assert 'alt.Chart' in __solution__, "Make sure you are calling the 'Chart' function?"
    assert 'mark_area' in __solution__, "Make sure you are creating a density plot using 'mark_area'."
    assert "groupby=" in __solution__, "Make sure you are grouping by 'island' and 'species'."
    assert "steps=100" in __solution__, "Make sure you are using  steps=100 when computing the KDE."
    assert "x=" in __solution__ or "alt.X" in __solution__, "Make sure you plotting 'body_mass_g' on the X-axis."
    assert "density:Q" in __solution__ or "density:Quantitative" in __solution__, "Make sure you are plotting 'density' as quantititave on the X-axis."
    assert "width=200" in __solution__, "Make sure you are setting the width of the plot to 200."
    assert "height=100" in __solution__, "Make sure you are setting the height of the plot to 100."
    assert "color" in __solution__ or "alt.Color" in __solution__, "Make sure you are coloring by species."
    assert mass_faceted_plot.facet.shorthand == 'species', "Make sure you are faceting by species."
    assert mass_faceted_plot.columns == 1, "Make sure you are using a column."
    __msg__.good("You're correct, well done!")
