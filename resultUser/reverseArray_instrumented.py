def reverseArrayH(Arr, left, right):
    while True:
        if left >= right:
            return Arr
        Arr[left], Arr[right] = Arr[right], Arr[left]
        [Arr, left, right] = [Arr, left + 1, right - 1]


def reverseArray(Arr):
    return reverseArrayH(Arr, 0, len(Arr) - 1)


arr1 = [5, 3, 6, 2, 7, 9]
print('Reversed array:', reverseArray(arr1))
