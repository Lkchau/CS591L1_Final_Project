import ast, sys, tokenize
from os import path
from checkTailRecursion import hasTailRecursiveFunction
from instrumentation import instrument
from writeFile import writeToResult
from commentFinder import comments
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
        userPath = currPath + '\\userCode\\'
        currPath = currPath +'\\test\\'
        
        assert len(sys.argv) == 2, "Invalid amount of arguments!"
        assert path.exists(path.join(currPath, sys.argv[1])) or path.exists(path.join(currPath, sys.argv[1] + ".py" )) or path.exists(path.join(userPath, sys.argv[1])) or path.exists(path.join(userPath, sys.argv[1] + ".py")), sys.argv[1] + " does not exist!"
        if path.exists(path.join(currPath,sys.argv[1] + ".py")):
            filename = path.join(currPath,sys.argv[1] + ".py")
            resFile = sys.argv[1]
            filePath = "test"
        elif path.exists(path.join(currPath, sys.argv[1])):
            filename = path.join(currPath,sys.argv[1])
            resFile = sys.argv[1][:-3]
            filePath = "test"
        elif path.exists(path.join(userPath, sys.argv[1])):
            filename = path.join(userPath, sys.argv[1])
            resFile = sys.argv[1][:-3]
            filePath = "user"
        else:
            filename = path.join(userPath, sys.argv[1] + ".py")
            resFile = sys.argv[1]
            filePath = "user"
        
        comment = input("Please type 'comment' without the quotes if you would like to only transform tail-recursive functions with comments\n")
        print()
        # Open and read the file as code!

        with open(filename, 'r') as code_file:
            # copy = code_file
            code = code_file.read().strip()
            # Create the ast
            tree = ast.parse(code)
            tailEndRecursion, lineno = hasTailRecursiveFunction(tree)
            commentLines, commentMap = comments(filename, lineno)
            # print(ast.dump(tree))
            print("Original: \n" + code + "\n")
            # print("Has tail rec: " + str(hasTailRecursiveFunction(tree)))

            assert(tailEndRecursion is not None), "No Tail-End Recursion exists in " + sys.argv[1]
            if(comment == ""):
                instrumentedCode = instrument(tree, tailEndRecursion, False)
            
            else:
                instrumentedCode = instrument(tree, tailEndRecursion, True, commentMap)

            print("\n===== \nInstrumented: \n" + str(instrumentedCode))
            writeToResult(instrumentedCode, resFile, filePath)

            print("-----")
    except AssertionError as e:
        print(e)
        print("-----")

