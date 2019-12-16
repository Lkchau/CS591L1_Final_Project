import ast, sys, inspect
from astor import astor
from os import path
# Task 1 - Find recursive functions
# Task 2 - Find tail-end recurisive functions
# Task 3 - Figure out how to convert that to an iterative version
# Task 4 - Instrument it into the body of the tail-end recursive function
# Task 5 - Output the new code into a new file or simply edit the existing file
# Task 6 - Run to make sure that the result is as expected.

tailRecursiveFunctions = []

def hasTailRecursiveFunction(tree):
    for node in ast.walk(tree):
        if isinstance(node, ast.FunctionDef):
            # print("Found function def at line " + str(node.lineno))
            funcName = node.name
            for i in node.body:
                if isinstance(i, ast.Return):
                    retVal = i.value
                    if isinstance(retVal, ast.Call):
                        retFuncName = retVal.func.id
                        if(retFuncName == funcName):
                            print("Tail-end Recursive Function at: " + str(node.lineno))
                            tailRecursiveFunctions.append(retFuncName)
                            return True
    return False

def instrument(tree):

    statements = []
    for statement in tree.body:
        if isinstance(statement, ast.FunctionDef) and statement.name in tailRecursiveFunctions:
            statement = instrument_body(statement)
        statements.append(statement)

    tree.body = statements
    # print("tree " + str(tree))
    code = astor.to_source(tree)
    return code

def instrument_body(function_def):
    parameters = []
    statements = []
    # print(function_def.name)
    for arg in function_def.args.args:
        parameters.append(arg.arg)
    
    # statements.append(ast.parse('\nwhile True: \n \t '))
    # first = 1
    # print(function_def.body)
    while_statement = [ast.While('True',function_def.body)]
    # 'while True: \n \t'
    # for statement in function_def.body:
        
        # while_statement.body += statement
        # print(type(statement))
        # statements.append(statement)
    # print("Statement " + str(statement))
    function_def.body = while_statement
    # print("body " + str(function_def.body))
    return function_def            
            # print(statement)


# Main function should read an input file in the same directory and find function defs
if __name__ == "__main__":
    try:
        print("-----")
        # Assert that they will call python main <filename> or python main <filename>.py
        currPath = path.abspath(__file__+'\..')
        currPath = currPath +'\\test\\'
        assert len(sys.argv) == 2, "Invalid amount of arguments!"
        assert path.exists(path.join(currPath, sys.argv[1])) or path.exists(path.join(currPath, sys.argv[1] + ".py" )), sys.argv[1] + " does not exist!"
        if path.exists(path.join(currPath,sys.argv[1] + ".py")):
            filename = path.join(currPath,sys.argv[1] + ".py")
        else:
            filename = path.join(currPath,sys.argv[1])
        
        # Open and read the file as code!
        with open(filename, 'r') as code_file:
            code = code_file.read()
            # Create the ast
            tree = ast.parse(code)
            # print(ast.dump(tree))
            assert(hasTailRecursiveFunction(tree)), "No Tail-End Recursion exists in " + sys.argv[1]
            print(instrument(tree))
        
            # Call our function to find the functions.

            print("-----")
    except AssertionError as e:
        print(e.args[0])
        print("-----")

