def reverse(arr, i, j):

    while i < j:
        arr[i], arr[j] = arr[j], arr[i]

        i += 1
        j -= 1


def leftRotate(arr, d):

    n = len(arr)

    reverse(arr, 0, d - 1)
    reverse(arr, d, n-1)
    reverse(arr, 0, n-1)

def printArray(arr):

    for i in range(0, len(arr)):
        print(arr[i])


arr = [1, 2, 3, 4, 5, 6, 7]
leftRotate(arr, 2)
printArray(arr)



