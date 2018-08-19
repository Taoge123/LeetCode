def countRotations(arr, n):

    #Find the min index
    min = arr[0]

    for i in range(0, n):

        if (min > arr[i]):

            min = arr[i]
            min_index = i

    return min_index


def countRotations2(arr, low, high):

    #This condition is needed to handle the case when array is not rotated
    if (high < low):
        return 0

    #If there is only one element left
    if (high == low):
        return low

    #Find mid
    mid = low + (high - low) / 2
    mid = int(mid)

    #Check is element (mid + 1) is min element [3, 4, 5, 1, 2]
    if (mid < high and arr[mid+1] < arr[mid]):
        return (mid + 1)

    #Check if mid itself is min element
    if (mid > low and arr[mid] < arr[mid - 1]):
        return mid

    #Decide whether we need to go to left half or right half
    if (arr[high] > arr[mid]):
        return countRotations2(arr, low, mid - 1)
    return countRotations2(arr, mid+1, high)


arr = [15, 18, 2, 3, 6, 12]
n = len(arr)
print(countRotations2(arr, 0, n-1))

