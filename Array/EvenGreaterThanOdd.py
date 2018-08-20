def rearrange(arr, n):

    for i in range(n-1):

        if (i % 2 == 0 and arr[i] > arr[i + 1]):


            arr[i], arr[i+1] = arr[i+1], arr[i]


        if (i % 2 != 0 and arr[i] < arr[i+1]):

            arr[i], arr[i + 1] = arr[i + 1], arr[i]


def printArray(arr, size):

    for i in range(size):
        print(arr[i], " ", end=' ')
    print()


arr = [6, 4, 2, 1, 8, 3]
n = len(arr)

print("Before rearranging: ")
printArray(arr, n)

rearrange(arr, n)

print("After rearranging:")
printArray(arr, n);



