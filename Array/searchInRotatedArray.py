def pivotBinarySearch(arr, n, key):

    pivot = findPivot(arr, 0, n-1)

    #If we didn't find a pivot, then array is not rotated
    if pivot == -1:
        return binarySearch(arr, 0, n-1, key)

    #If we found a pivot, then first compare with pivot
    # and then search in 2 subarrays around pivot
    if arr[pivot] == key:
        return pivot

    if arr[0] <= key:
        return binarySearch(arr, 0, pivot-1, key)
    return binarySearch(arr, pivot+1, n-1, key)


def findPivot(arr, low, high):

    #Base cases
    if high < low:
        return -1

    if high == low:
        return low

    mid = int((low + high) / 2)

    if mid < high and arr[mid] > arr[mid + 1]:
        return mid

    if mid > low and arr[mid] < arr[mid - 1]:
        return (mid - 1)

    if arr[low] >= arr[mid]:
        return findPivot(arr, low, mid-1)
    return findPivot(arr, mid+1, high)

def binarySearch(arr, low, high, key):

    if high < low:
        return -1

    mid = int((low + high) / 2)

    if key == arr[mid]:
        return mid

    if key > arr[mid]:
        return binarySearch(arr, (mid+1), high, key)
    return binarySearch(arr, low, (mid-1), key)


arr1 = [5, 6, 7, 8, 9, 10, 1, 2, 3]
n = len(arr1)
key = 3
print("Index of the element is : ", pivotBinarySearch(arr1, n, key))




