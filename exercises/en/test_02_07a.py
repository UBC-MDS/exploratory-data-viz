def test():
    # Here we can either check objects created in the solution code, or the
    # string value of the solution, available as __solution__. A helper for
    # printing formatted messages is available as __msg__. See the testTemplate
    # in the meta.json for details.
    # If an assertion fails, the message will be displayed

    assert not fuel_efficiency is None, "Your answer does not exist. Have you passed in the correct variable?"
    assert type(fuel_efficiency) == type(alt.Chart()), "Your answer is not an Altair Chart object. Check to make sure that you have assigned an alt.Chart object to fuel_efficiency."
    assert fuel_efficiency.data.equals(data.cars()), "Make sure you are using cars() dataset from vega_datasets."
    assert fuel_efficiency.mark == 'area', "Make sure you are using the area mark type."
    assert (fuel_efficiency.encoding.x.field in {'Year', 'Year:temporal', 'Year:T'} or 
            fuel_efficiency.encoding.x.shorthand in {'Year', 'Year:temporal', 'Year:T'}), "Make sure you are using 'Year' as the x-axis encoding."
    assert (fuel_efficiency.encoding.y.field in {'Miles_per_Gallon', 'Miles_per_Gallon:quantitative', 'Miles_per_Gallon:Q'} or 
            "Miles_per_Gallon" in fuel_efficiency.encoding.y.shorthand), "Make sure you are using mean of the 'Miles_per_Gallon' as the y-axis encoding."
    assert ((fuel_efficiency.encoding.y.field in {'Miles_per_Gallon', 'Miles_per_Gallon:quantitative', 'Miles_per_Gallon:Q'} and fuel_efficiency.encoding.y.aggregate == 'mean') or
            fuel_efficiency.encoding.y.shorthand in {'mean(Miles_per_Gallon)', 'mean(Miles_per_Gallon):quantitative', 'mean(Miles_per_Gallon):Q'}), "You're very close. Make sure that you are using the mean aggregate for the y-axis encoding."
    assert type(fuel_efficiency.title) == str and len(fuel_efficiency.title) >= 5, "Make sure you specify a descriptive title for the fuel_efficiency plot."
    __msg__.good("You're correct, well done!")
