import re

def test():
    # Here we can either check objects created in the solution code, or the
    # string value of the solution, available as __solution__. A helper for
    # printing formatted messages is available as __msg__. See the testTemplate
    # in the meta.json for details.
    # If an assertion fails, the message will be displayed

    # Regex expression to capture the line plot variable name without whitespace
    capture_grp = re.search("[^\s]*(?=\s*=\s*alt.Chart\(stocks\).mark_line)", __solution__)
    assert capture_grp, "Make sure you assign the line plot to a variable name."
    # capture_grp.group() holds the variable name of line plot 
    assert capture_grp.group() + ".mark_point(" in __solution__, "Make sure you add a layer of another plot object, created from the line plot object with the same encodings but different mark type."
    __msg__.good("You're correct, well done!")
