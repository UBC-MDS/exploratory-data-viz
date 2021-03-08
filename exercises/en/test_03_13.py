def test():
    # Here we can either check objects created in the solution code, or the
    # string value of the solution, available as __solution__. A helper for
    # printing formatted messages is available as __msg__. See the testTemplate
    # in the meta.json for details.
    # If an assertion fails, the message will be displayed

    # Since we haven't started assigning charts to variable names yet,
    # this might be the better way to test for the first exercise.
    # Maybe even for later exercises.
   assert mass_boxplot.mark == 'boxplot', "Make sure you are using the 'mark_boxplot' to generate a boxplot."
   assert mass_boxplot.encoding.x.shorthand == 'body_mass_g', "Make sure you are plotting 'body_mass_g' on the X-axis."
   assert mass_boxplot.encoding.y.shorthand == 'species', "Make sure you are plotting 'species' on the Y-axis."
   assert not mass_boxplot.title is None, "Make sure you are providing a title for your plot."
   assert not mass_boxplot.title.islower(), "Make sure the plot title is capitalized."
   assert mass_boxplot.height == 200, "Make sure your plot has a height of 200."
   assert mass_boxplot.width == 400, "Make sure your plot has a width of 400."
   __msg__.good("You're correct, well done!")
