import ast, sys
from os import path
from checkTailRecursion import hasTailRecursiveFunction
from instrumentation import instrument
from writeFile import writeToResult
# Task 1 - Find recursive functions
# Task 2 - Find tail-end recurisive functions
# Task 3 - Figure out how to convert that to an iterative version
# Task 4 - Instrument it into the body of the tail-end recursive function
# Task 5 - Output the new code into a new file or simply edit the existing file
# Task 6 - Run to make sure that the result is as expected.

# Main function should read an input file in the same directory and find function defs
if __name__ == "__main__":
    try:
        print("-----")
        # Assert that they will call python main <filename> or python main <filename>.py
        currPath = path.abspath(__file__+'\..\..')
        print(currPath)
        currPath = currPath +'\\test\\'
        assert len(sys.argv) == 2, "Invalid amount of arguments!"
        assert path.exists(path.join(currPath, sys.argv[1])) or path.exists(path.join(currPath, sys.argv[1] + ".py" )), sys.argv[1] + " does not exist!"
        if path.exists(path.join(currPath,sys.argv[1] + ".py")):
            filename = path.join(currPath,sys.argv[1] + ".py")
            resFile = sys.argv[1]
        else:
            filename = path.join(currPath,sys.argv[1])
            resFile = sys.argv[1][:-3]
        
        # Open and read the file as code!
        with open(filename, 'r') as code_file:
            code = code_file.read().strip()
            # Create the ast
            tree = ast.parse(code)
            # print(ast.dump(tree))
            print("Original: \n" + code + "\n")
            # print("Has tail rec: " + str(hasTailRecursiveFunction(tree)))
            tailEndRecursion = hasTailRecursiveFunction(tree)
            assert(tailEndRecursion is not None), "No Tail-End Recursion exists in " + sys.argv[1]
            instrumentedCode = instrument(tree, tailEndRecursion)
            print("\n===== \nInstrumented: \n" + str(instrumentedCode))
            writeToResult(instrumentedCode, resFile)
            # Call our function to find the functions.

            print("-----")
    except AssertionError as e:
        print(e)
        print("-----")

