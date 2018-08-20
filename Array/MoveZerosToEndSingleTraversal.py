def moveZeros(arr, n):

    #Also similar to partition in quick sort
    count = 0

    for i in range(0, n):

        if (arr[i] != 0):

            arr[count], arr[i] = arr[i], arr[count]
            count += 1

def printArray(arr, n):

    for i in range(0, n):
        print(arr[i], end=" ")


def printArray(arr, n):
    for i in range(0, n):
        print(arr[i], end=" ")


# Driver program to test above
arr = [0, 1, 9, 8, 4, 0, 0, 2,
       7, 0, 6, 0, 9]
n = len(arr)

print("Original array:", end=" ")
printArray(arr, n)

moveZeros(arr, n)

print("\nModified array: ", end=" ")
printArray(arr, n)