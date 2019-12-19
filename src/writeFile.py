from os import path
def writeToResult(code, funcName, res):
    fileName = funcName + "_instrumented.py"
    resultPath = path.abspath(__file__ +'\..\..\\result\\')
    resultUserPath = path.abspath(__file__ +'\..\..\\resultUser\\')
    filePath = path.join(resultPath, fileName)
    if(res == "user"):
        filePath = path.join(resultUserPath, fileName)
        resultPath = open(filePath, "w+")
    else:    
        resultPath = open(filePath, "w+")
    resultPath.write(code)
    resultPath.close()

    print("Executable code has been written to: " + str(fileName) + " in \n" + str(filePath))
    print("Please go to the resultUser directory and run the new " + str(fileName) + " code!")