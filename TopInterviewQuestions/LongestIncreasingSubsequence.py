
global maximum


def listUtil(arr, n):
    # to allow the access of global variable
    global maximum

    # Base Case
    if n == 1:
        return 1

    # maxEndingHere is the length of LIS ending with arr[n-1]
    maxEndingHere = 1

    """Recursively get all LIS ending with arr[0], arr[1]..arr[n-2]
       IF arr[n-1] is maller than arr[n-1], and max ending with
       arr[n-1] needs to be updated, then update it"""
    for i in range(1, n):
        res = listUtil(arr, i)
        if arr[i - 1] < arr[n - 1] and res + 1 > maxEndingHere:
            maxEndingHere = res + 1

    # Compare maxEndingHere with overall maximum. And
    # update the overall maximum if needed
    maximum = max(maximum, maxEndingHere)

    return maxEndingHere


def lis(arr):
    # to allow the access of global variable
    global maximum

    # lenght of arr
    n = len(arr)

    # maximum variable holds the result
    maximum = 1

    # The function _lis() stores its result in maximum
    listUtil(arr, n)

    return maximum


arr = [10, 22, 9, 33, 21, 50, 41, 60]
n = len(arr)
print("Length of lis is ", lis(arr))




def lisDP(arr):

    n = len(arr)
    lis = [1] * n

    for i in range(1, n):
        for j in range(0, n):
            if arr[i] > arr[j] and lis[i] < lis[j] + 1:
                lis[i] = lis[j] + 1

    maximum = 0

    for i in range(n):
        maximum = max(maximum, lis(i))

    return maximum


arr = [10, 22, 9, 33, 21, 50, 41, 60]
print ("Length of lis is", lis(arr))