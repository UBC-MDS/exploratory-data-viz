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
            # iframe_start = "<iframe srcdoc='"
            # iframe_end = "' width=100% height=400px></iframe>"

            # json_start = '
            # <html>
            # <head>
            #   <script src="https://cdn.jsdelivr.net/npm/vega@5"></script>
            #   <script src="https://cdn.jsdelivr.net/npm/vega-lite@4.8.1"></script>
            #   <script src="https://cdn.jsdelivr.net/npm/vega-embed@6"></script>
            # </head>
            # <body>
            #   <div id="vis"></div>
            #   <script type="text/javascript">
            #     var spec ='
            # json_end = ';
            #     var opt = {"renderer": "canvas", "actions": false};
            #     vegaEmbed("#vis", spec, opt);
            #   </script>
            # </body>
            # </html>'
            # # cat(paste(iframe_start, json_start, json_end, iframe_end))
            # module_dir <- paste(unlist(strsplit(options$fig.path, '_'))[1:2], collapse = '_')
            module_dir <- unlist(strsplit(options$fig.path, '_'))[1]
            chapter_dir <- unlist(strsplit(options$fig.path, '_'))[2]

            parent_dir <- file.path('..', '..', '..', '..', 'static', module_dir, 'charts', chapter_dir)
            if (!dir.exists(parent_dir)) {
                dir.create(parent_dir, recursive = T)
            }
            file_name <- paste(file.path(parent_dir, options$label), '.png', sep='')

            # cat(paste('<iframe src="', file_name, '" width=100% height=400px style=border-width:0;></iframe>', sep=''))
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
                # c(default_source_hook(x, options), vegawidget::vw_to_svg(exec_with_return(paste(xx, '.to_json()'))))}
                # c(default_source_hook(x, options), paste(iframe_start, json_start, exec_with_return(paste(xx, '.to_json()')), json_end, iframe_end))}
                exec_with_return(paste(xx, '.save("', file_name, '")', sep=''))
                c(default_source_hook(x, options), paste('<iframe src="', file_name, '" width=100% height=400px style=border-width:0;></iframe>', sep=''))}

            else {
                # c(default_source_hook(x, options), vegawidget::vw_to_svg(exec_with_return(paste(x, '.to_json()'))))}}
                # c(default_source_hook(x, options), paste(iframe_start, json_start, exec_with_return(paste(x, '.to_json()')), json_end, iframe_end))}}
                exec_with_return(paste(x, '.save("', file_name, '")', sep=''))
                c(default_source_hook(x, options), paste('<iframe src="', file_name, '" width=100% height=400px style=border-width:0;></iframe>', sep=''))}}
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
