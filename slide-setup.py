# Show all dataframe columns
import pandas as pd


pd.set_option('display.width', 350)
pd.set_option('display.max_columns', 50)
pd.set_option('display.max_rows', 15)

# These Python functions are from SO
# and save the day since they allow statements to be executed AND return a value.
# The built-in `exec` does not return a value,
# and `eval` does not work with statements (assignment, imports, etc).
# Reticulate only provides a thin wrapper around `eval`,
# so it is not much use here.
# The actual reticulate code for processing Python code chunks
# is more complex than these functions.
import ast
import copy


def convertExpr2Expression(Expr):
        Expr.lineno = 0
        Expr.col_offset = 0
        result = ast.Expression(Expr.value, lineno=0, col_offset=0)
        return result

def exec_with_return(code):
    code_ast = ast.parse(code)

    init_ast = copy.deepcopy(code_ast)
    init_ast.body = code_ast.body[:-1]

    last_ast = copy.deepcopy(code_ast)
    last_ast.body = code_ast.body[-1:]

    exec(compile(init_ast, "<ast>", "exec"), globals())
    if type(last_ast.body[0]) == ast.Expr:
        return eval(compile(convertExpr2Expression(last_ast.body[0]), "<ast>", "eval"),globals())
    else:
        exec(compile(last_ast, "<ast>", "exec"),globals())
