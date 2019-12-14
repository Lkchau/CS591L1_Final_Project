import ast, sys, inspect
from os import path

# Main function should read an input file in the same directory and find function defs
if __name__ == "__main__":
    try:
        print("-----")
        # Assert that they will call python main <filename> or python main <filename>.py
        assert len(sys.argv) == 2, "Invalid amount of arguments!"
        assert path.exists(sys.argv[1]) or path.exists(sys.argv[1] + ".py" ), sys.argv[1] + " does not exist!"
        if path.exists(sys.argv[1] + ".py"):
            filename = sys.argv[1] + ".py"
        else:
            filename = sys.argv[1]
        
        # Open and read the file as code!
        with open(filename, 'r') as code_file:
            code = code_file.read()
            # Create the ast
            tree = ast.parse(code)
        
            # Call our function to find the functions.
            
            print("-----")
    except AssertionError as e:
        print(e.args[0])
        print("-----")

