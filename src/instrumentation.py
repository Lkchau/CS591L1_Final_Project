from astor import astor
import ast
def instrument(tree, tailEndRecursion):

    statements = []
    for statement in tree.body:
        # print(statement)
        if isinstance(statement, ast.FunctionDef) and statement.name in tailEndRecursion:
            statement = instrument_body(statement)
            # print(statement)
        statements.append(statement)
    
    tree.body = statements
    # print("tree " + str(tree.body[3].body))
    code = astor.to_source(tree)
    return code

def instrument_body(function_def):
    parameters = []
    statements = []
    # print(function_def.name)
    for arg in function_def.args.args:
        parameters.append(arg.arg)
    
    whileBody = []
    # print(function_def.body)
    for obj in function_def.body:
        statement = [obj]
        if isinstance(obj, ast.Return):
            objVal = obj.value
            if isinstance(objVal, ast.Call):
                assignStatement = [ast.Assign([ast.List([ast.Name(id = function_def.args.args[i].arg) for i in range(len(function_def.args.args))])],ast.List(objVal.args)) ]
                print(assignStatement)
                statement = assignStatement
                whileBody += statement
        if statement == [obj]:
            whileBody += statement
    # whileBody += [ast.Continue(), ast.Break()]
    # function_def.body = whileBody

    while_statement = [ast.While(test = ast.NameConstant(value=True), body = whileBody, orelse = [])]
    # print(while_statement[0].body)
    # while_statement += whileBody

    function_def.body = while_statement
    # print("body " + str(function_def.body))
    return function_def