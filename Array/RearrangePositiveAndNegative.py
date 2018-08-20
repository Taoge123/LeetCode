def rearrange(arr, n):

    """similar to partition in quick sort"""
    #[-1, 2, -3, 4, 5, 6, -7, 8, 9]
    i = -1
    for j in range(n):

        if (arr[j] < 0):

            i += 1

            arr[i], arr[j] = arr[j], arr[i]

    #Now all the pos are at end and neg are at beginning
    pos, neg = i+1, 0

    #Increment the neg index by 2 and pos by 1 ans swap every alternnate nnegative number with positive number
    while (pos < n and neg < pos and arr[neg] < 0):

        arr[neg], arr[pos] = arr[pos], arr[neg]

        pos += 1
        neg += 2


def printArray(arr, n):

    for i in range(n):
        print(arr[i])


arr = [-1, 2, -3, 4, 5, 6, -7, 8, 9]
n = len(arr)
rearrange(arr, n)
printArray(arr, n)



