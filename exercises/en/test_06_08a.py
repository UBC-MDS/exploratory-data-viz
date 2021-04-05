def test():
    # Here we can either check objects created in the solution code, or the
    # string value of the solution, available as __solution__. A helper for
    # printing formatted messages is available as __msg__. See the testTemplate
    # in the meta.json for details.
    # If an assertion fails, the message will be displayed

    assert not world_df is None, "Your answer for world_df does not exist. Have you loaded the TopoJSON data to the correct variable name?"
    assert "topo_feature" in __solution__, "The loaded data should be in TopoJSON format. In order to read TopoJSON file correctly, you need to use the alt.topo_feature() function."
    assert type(world_df) == alt.UrlData, "world_df does not appear to be an Altair UrlData object. Have you assigned the Altair UrlData object for the TopoJSON data to the correct variable?"
    assert world_df.url == data.world_110m.url, "Make sure you are loading the data from correct url."
    assert (world_df.format !=  alt.utils.schemapi.Undefined and 
            world_df.format.type == 'topojson'
    ), "The loaded data should be in TopoJSON format. In order to read TopoJSON file correctly, you need to use the alt.topo_feature() function."
    assert world_df.format.feature == "countries", "Make sure to specify 'countries' feature when loading the TopoJSON file using alt.topo_feature()."

    assert not world_plot is None, "Your answer for world_plot does not exist. Have you assigned the plot to the correct variable name?"
    assert type(world_plot) == alt.Chart, "world_plot does not appear to be an Altair Chart object. Have you assigned the Altair Chart object for the plot to the correct variable?"
    assert world_plot.mark == 'geoshape', "Make sure you are using mark_geoshape for world_plot."

    assert world_plot.projection != alt.utils.schemapi.Undefined and (
        world_plot.projection.type == 'equalEarth'
    ), "Make sure you use 'equalEarth' projection. Hint: you can use .project() method with type argument to specify projection type."

    __msg__.good("You're correct, well done!")
