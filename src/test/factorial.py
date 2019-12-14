# simple tail-end recursion for calculating factorials

def factorial(n, a = 1): 
    if (n == 0): 
        return a 

    return factorial(n - 1, n * a) 

# Iterative version?

def factorialIter(n):
    val = 1
    for i in range(n, 0, -1):
        if(i == 0):
            return val
        val = val * i
    return val

# Print tests to make sure they are indeed printing the factorial
print("Recursive factorial test: " + factorial(5))
print("Iterative factorial test: " + factorialIter(5))