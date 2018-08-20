def rearrange(arr, n):

    #Create an auxiliary array of some size
    temp = [0] * n

    #Store result in temp[]
    for i in range(0, n):
        temp[arr[i]] = i

    #Copy temp back to arr[]
    for i in range(0, n):
        arr[i] = temp[i]


def printArray(arr, n):
    for i in range(0, n):
        print(arr[i], end=" ")


arr = [1, 3, 0, 2]
n = len(arr)
print("Given array is", end=" ")
printArray(arr, n)

rearrange(arr, n)
print("\nModified array is", end=" ")
printArray(arr, n)
