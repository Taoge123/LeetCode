def nextGreatest(arr):

    size = len(arr)

    # [16, 17, 4, 3, 5, 2]
    max_from_right = arr[size - 1]
    #The next greatest element for the right most element is always -1
    arr[size - 1] = -1

    #Replace all other elements with the next greatest
    for i in range(size - 2, -1, -1):

        #Store the current element with the next greatest
        temp = arr[i]

        #Replace current element with the next greatest
        arr[i] = max_from_right

        #Update the greatest element, if needed
        if max_from_right < temp:
            max_from_right = temp



def printArray(arr):

    for i in range(0, len(arr)):
        print(arr[i])


arr = [16, 17, 4, 3, 5, 2]
nextGreatest(arr)
print("Modified array is")
printArray(arr)





