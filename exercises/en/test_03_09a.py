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
    assert "island" in str(mass_density_plot.transform), "Make sure you are grouping by 'island'."
    assert "body_mass_g" in str(mass_density_plot.transform), "Make sure you are computing the density values using the 'body_mass_g' column."
    assert "density" in str(mass_density_plot.transform), "Make sure you are giving a name of 'densitys' to the KDE estimates"
    assert "steps: 100" in str(mass_density_plot.transform), "Make sure you are using  steps=100 when computing the KDE."
    assert mass_density_plot.encoding.color.shorthand == 'island', "Make sure you are coloring by island."
    assert mass_density_plot.encoding.x.shorthand == 'body_mass_g', "Make sure you are plotting 'body_mass_g' on the X-axis."
    assert mass_density_plot.encoding.y.shorthand == 'density:Q', "Make sure you are plotting 'density' as quantititave on the X-axis."
    assert not mass_density_plot.title is None, "Make sure you are providing a title for your plot."
    assert not mass_density_plot.title.islower(), "Make sure the plot title is capitalized."
    __msg__.good("You're correct, well done!")
