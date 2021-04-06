def test():
    # Here we can either check objects created in the solution code, or the
    # string value of the solution, available as __solution__. A helper for
    # printing formatted messages is available as __msg__. See the testTemplate
    # in the meta.json for details.
    # If an assertion fails, the message will be displayed

    assert not (
        mass_density_plot is None or
        mass_boxplot is None or
        penguin_heatmap is None or 
        culmen_facet_plot is None
    ), "Make sure correct plots are still assigned to mass_density_plot, mass_boxplot, penguin_heatmap, and culmen_facet_plot in your solution"
    assert not combined_plot is None, "Your answer for combined_plot does not exist. Have you assigned the plot to the correct variable name?"
    
    assert type(combined_plot) == alt.VConcatChart, "combined_plot does not appear to be an Altair VConcatChart object. Hint: note that mass_density_plot is at the top of the row. Try experimenting with & and | operators with appropriate parentheses to reproduce the same plot."
    assert len(combined_plot.vconcat) == 3, "Make sure combined_plot has 3 rows."

    # top row plot
    plot1 = combined_plot.vconcat.pop(0); plot1.data = combined_plot.data
    assert plot1 == mass_density_plot, "Top row of combined_plot should be mass_density_plot."

    # second row plot
    plot2 = combined_plot.vconcat.pop(0); plot2.data = combined_plot.data
    assert plot2 == mass_boxplot | penguin_heatmap, "Second row of combined_plot should contain mass_boxplot and penguin_heatmap. Make sure they are also in the correct order."

    # third row plot
    plot3 = combined_plot.vconcat.pop(0); plot3.data = combined_plot.data
    assert plot3 == culmen_facet_plot, "Last row of combined_plot should be culmen_facet_plot."
    
    __msg__.good("You're correct, well done!")
