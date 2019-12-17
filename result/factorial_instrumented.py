def factorial(n, a=1):
    while True:
        if n == 0:
            return a
        [n, a] = [n - 1, n * a]


def alteredFactorial(n, a=1):
    while True:
        if n == 0:
            return a
        n, a = n - 1, n * a


def factorial2(n):
    if n == 0:
        return 1
    else:
        return n * factorial2(n - 1)


def factorialIter(n):
    val = 1
    for i in range(n, 0, -1):
        if i == 0:
            return val
        val = val * i
    return val


print('tail-end factorial test: ' + str(factorial(5)))
print('Alt tail-end factorial test: ' + str(alteredFactorial(5)))
print('Recursive factorial test: ' + str(factorial2(5)))
print('Iterative factorial test: ' + str(factorialIter(5)))
