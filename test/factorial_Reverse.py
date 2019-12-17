def factorial(n, a = 1): 
    if (n == 0): 
        return a 

    return factorial(n - 1, n * a)

def reverseArrayH(Arr, left, right): 
    if left >= right: 
        return Arr
    Arr[left], Arr[right] = Arr[right], Arr[left] 
    return reverseArrayH(Arr, left+1, right-1) 

def reverseArray(Arr):
    return reverseArrayH(Arr, 0, len(Arr)-1)

arr1 = [5,3,6,2,7,9]
print("Reversed array:",reverseArray(arr1))

print("tail-end factorial test: " + str(factorial(5)))