def rearrange(arr, n):

    arr.sort()

    #To store the modiflied array
    tempArr = [0] * (n+1)

    #Adding numbers from sorted array to new array accordingly
    arrIndex = 0

    #Traverse frombegin and end simultaneously
    i = 0
    j = n - 1

    while (i <= n // 2 or j > n // 2):

        tempArr[arrIndex] = arr[i]
        arrIndex += 1

        tempArr[arrIndex] = arr[j]
        arrIndex += 1

        i += 1
        j -= 1

    for i in range(0, n):
        arr[i] = tempArr[i]


arr = [5, 8, 1, 4, 2, 9, 3, 7, 6]
n = len(arr)
rearrange(arr, n)

for i in range(0, n):
    print(arr[i], end=" ")





