# Import the function `exec_with_return`
reticulate::source_python('../../../../slide-setup.py')
# This hooks into the knitr machinery
# and appends a custom function to the standard RMarkdown source code evaluation.
# Here it is appending `to_json()` to Altair code,
# sending it to the Python function above for evaluation,
# and converting the result to SVG via vegawidget.
# The results cannot be assigned a variable for some reasons
# and the vector is needed for RMarkdown to output both the source code and the SVG result.
# The SVG introduces an unnecessary doctype string
# which can be removed by adding the following to `format_slides.R`:
# text <- gsub('&lt;!DOCTYPE svg PUBLIC .*&gt;', '', text)
default_source_hook <- knitr::knit_hooks$get('source')
knitr::knit_hooks$set(
    source = function(x, options) {
        # Using element-wise `&&` to avoid raising warning for multi-line R code chunks.
        # Python chunks are always one line.
        if (options$engine == "python" && grepl("alt.Chart(", x, fixed = T)) {
            # This section handles layered plots
            # where a parenthesis needs to be added to the last element of the string
            # so that `to_json()` can be called on the entire plot
            # instead of just the last layer.
            vector_string <- unlist(strsplit(x, '\n'))
            last_command <- tail(vector_string, 1)
            if (grepl('\\+|\\&|\\|', last_command)) {
                new_last <- paste0('(', last_command, ')')
                vector_string[length(vector_string)] <- new_last
                xx <- paste(vector_string, collapse='\n')
                c(default_source_hook(x, options), vegawidget::vw_to_svg(exec_with_return(paste(xx, '.to_json()'))))}
            else {
                c(default_source_hook(x, options), vegawidget::vw_to_svg(exec_with_return(paste(x, '.to_json()'))))}}
        else {
            default_source_hook(x, options)}})

# To get the interactive vega HTML instead of SVG when knitting,
# the source hook needs to be changed from using `vw_to_svg` to using `knit_print.vegaspec`.
# The following line also need to be uncommented to register the knit_print S3 method properly for vegaspecs:
# vctrs::s3_register("knitr::knit_print", "vegaspec")
# In addition, there is a bug in RMarkdown or vegawidget
# which requires the function `as_vegaspec` to be run once separately for plots to show up.
# R is probably not loading the CDN or other HTML resources properly otherwise.
# Since so many workarounds are required for the above,
# I came up with this simpler way of rendering the HTML,
# which can replace the second element of the output vector (the svg part):
# gsub('<!DOCTYPE html>', '', py$exec_with_return(paste(x, '.to_html()')))
# It works when knitting in RStudio,
# but we still need Ines to fix the js script bug in her framework before using it here.

# The below is needed to remove "alt.Chart(...)" when knitting inside RStudio.
# However, when using the course framework, that line already removed for some reason.
# Not sure if this discrepancy comes from a bug in the framework, RMarkdown,
# or a if it is a setting somewhere.
# alt.LayerChart shows up in both and must be removed
default_output_hook <- knitr::knit_hooks$get('output')
knitr::knit_hooks$set(
    output = function(x, options) {
        if (options$engine == "python" && grepl("alt\\..*Chart\\(", x)) {
            # Swallow the output so that "alt.Chart(...)" is not printed
        }
        else {
            default_output_hook(x, options)}})
