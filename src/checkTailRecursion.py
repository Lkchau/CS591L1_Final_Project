import ast
def hasTailRecursiveFunction(tree):
    tailRecursiveFunctions = []
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
                            print("Tail-end Recursive Function at line " + str(node.lineno) + " (" + str(retFuncName)+")")
                            tailRecursiveFunctions.append(retFuncName)
    return tailRecursiveFunctions