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
    source = function(code_chunk, options) {
        # Using element-wise `&&` to avoid raising warning for multi-line R code chunks.
        # Python chunks are always one line.
        # The strings to look for are just heuristics for altair syntax or
        # variable names I used.
        # It would maybe be better to have a chunk options (could be T by default)
        if ((options$engine == "python" && grepl("alt.Chart(", code_chunk, fixed = T))
            || (options$engine == "python" && grepl("chart.", code_chunk, fixed = T))
            || (options$engine == "python" && grepl("choropleth", code_chunk, fixed = T))
            || (options$engine == "python" && grepl("points", code_chunk, fixed = T))
            || (options$engine == "python" && grepl("mark_", code_chunk, fixed = T))) {
            # We can use the chunk option `fig.path` to find the name of the
            # directory for the executed scripts, which contains the module and
            # chapter names.
            module_name <- unlist(strsplit(options$fig.path, '_'))[1]
            chapter_name <- unlist(strsplit(options$fig.path, '_'))[2]
            # Create directory for storing the charts if it does not already exist
            chart_dir <- file.path('..', '..', '..', '..', 'static', module_name, 'charts', chapter_name)
            if (!dir.exists(chart_dir)) {
                dir.create(chart_dir, recursive = T)
            }
            # The label of the chunk is set automaticlly by default which makes
            # it suitable for defining the file name of each chunk's chart.
            file_name <- paste(file.path(chart_dir, options$label), '.html', sep='')

            # This first if section handles layered plots where a parenthesis
            # needs to be added to the last element of the string so that
            # `to_X()` can be called on the entire plot instead of just the
            # last layer.
            vector_string <- unlist(strsplit(code_chunk, '\n'))
            last_command <- tail(vector_string, 1)
            if (grepl('\\+|\\&|\\|', last_command)) {
                new_last <- paste0('(', last_command, ')')
                vector_string[length(vector_string)] <- new_last
                code_chunk_to_execute <- paste(vector_string, collapse='\n')
            }

            else {
                code_chunk_to_execute <- code_chunk
            }

            # We technically don't need execute with return when saving a file
            # to disk (just execute is enough), but if we ever want to switch
            # back to inserting the charts as svg/html strings directly in the
            # md-document then this is needed.
            exec_with_return(paste(code_chunk_to_execute, '.save("', file_name, '")', sep=''))
            # The output to the md document is the iframe string referencing
            # the plot file we just saved.
            c(default_source_hook(code_chunk, options),
              paste('<iframe src="', file_name, '" width=100% height=420px style=border:none;></iframe>', sep=''))
        }
        else {
            default_source_hook(code_chunk, options)}
    }
)

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
    output = function(code_chunk, options) {
        if (options$engine == "python" && grepl("alt\\..*Chart\\(", code_chunk)) {
            # Swallow the output so that "alt.Chart(...)" is not printed
        }
        else {
            default_output_hook(code_chunk, options)}})
