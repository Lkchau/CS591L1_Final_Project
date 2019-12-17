from os import path
def writeToResult(code, funcName):
    fileName = funcName + "_instrumented.py"
    resultPath = path.abspath(__file__ +'\..\..\\result\\')
    filePath = path.join(resultPath, fileName)
    resultPath = open(filePath, "w+")
    resultPath.write(code)
    resultPath.close()

    print("Executable code has been written to: " + str(fileName) + " in \n" + str(filePath))
    print("Please go to the result directory and run the new " + str(fileName) + " code!")