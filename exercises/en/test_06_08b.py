def test():
    # Here we can either check objects created in the solution code, or the
    # string value of the solution, available as __solution__. A helper for
    # printing formatted messages is available as __msg__. See the testTemplate
    # in the meta.json for details.
    # If an assertion fails, the message will be displayed

    assert not world_df is None, "Your answer for world_df does not exist. Have you loaded the TopoJSON data to the correct variable name?"
    assert "topo_feature" in __solution__, "The loaded data should be in TopoJSON format. In order to read TopoJSON file correctly, you need to use the alt.topo_feature() function."
    assert (
        "quantitative" in __solution__ or 
        "pop_density:Q" in __solution__
    ), "Make sure you use pop_density column from gapminder_df for the color encoding. Hint: since pop_density column does not exist in world_df, Altair can't infer its data type and you need to specify that it is quantitative data."
    assert type(world_df) == alt.UrlData, "world_df does not appear to be an Altair UrlData object. Have you assigned the Altair UrlData object for the TopoJSON data to the correct variable?"
    assert world_df.url == data.world_110m.url, "Make sure you are loading the data from correct url."
    assert (world_df.format != alt.utils.schemapi.Undefined and 
            world_df.format.type == 'topojson'
    ), "The loaded data should be in TopoJSON format. In order to read TopoJSON file correctly, you need to use the alt.topo_feature() function."
    assert world_df.format.feature == "countries", "Make sure to specify 'countries' feature when loading the TopoJSON file using alt.topo_feature()."

    assert not pop_dense_plot is None, "Your answer for pop_dense_plot does not exist. Have you assigned the plot to the correct variable name?"
    assert type(pop_dense_plot) == alt.Chart, "pop_dense_plot does not appear to be an Altair Chart object. Have you assigned the Altair Chart object for the plot to the correct variable?"
    assert pop_dense_plot.mark == 'geoshape', "Make sure you are using mark_geoshape for pop_dense_plot."

    assert pop_dense_plot.encoding.color != alt.utils.schemapi.Undefined and (
        pop_dense_plot.encoding.color.shorthand in {'pop_density:quantitative', 'pop_density:Q'} or
        (pop_dense_plot.encoding.color.shorthand == 'pop_density' and pop_dense_plot.encoding.color.type == 'quantitative') or
        pop_dense_plot.encoding.color.field in {'pop_density:quantitative', 'pop_density:Q'} or
        (pop_dense_plot.encoding.color.field == 'pop_density' and pop_dense_plot.encoding.color.type == 'quantitative')
    ), "Make sure you use pop_density column from gapminder_df for the color encoding. Hint: since pop_density column does not exist in world_df, Altair can't infer its data type and you need to specify that it is quantitative data."

    assert pop_dense_plot.encoding.color.scale != alt.utils.schemapi.Undefined and (
        pop_dense_plot.encoding.color.scale.scheme != alt.utils.schemapi.Undefined
    ), "Make sure to specify a colour scheme."
    assert pop_dense_plot.encoding.color.scale.domainMid == 81, "Make sure you set the domainMid of the color scale as the global median (81)."

    assert type(pop_dense_plot.transform) == list and (
        len(pop_dense_plot.transform) == 1 and
        pop_dense_plot.transform[0]['from'] != alt.utils.schemapi.Undefined and
        pop_dense_plot.transform[0]['from'].fields == ['pop_density'] and
        pop_dense_plot.transform[0]['from'].key
    ), "Make sure you use .transform_lookup() to lookup the column 'pop_density' from the gapminder_df data using 'id' as the connecting column. Hint: 'pop_density' should be inside a list."

    assert pop_dense_plot.projection != alt.utils.schemapi.Undefined and (
        pop_dense_plot.projection.scale == 80
    ), "Make sure you use 'equalEarth' projection. Hint: you can use .project() method with type argument to specify projection type."    

    __msg__.good("You're correct, well done!")
