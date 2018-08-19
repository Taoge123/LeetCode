def pairInSortedRotated(arr, n, x):

    #Find the pivot element
    for i in range(0, n-1):
        if (arr[i] > arr[i+1]):
            break

    # low is now the index of min element
    low = (i+1) % n
    high = i

    #Keep moving either low or high until they meet
    while (low != high):

        #If we find a pair with sum x, we return True
        if (arr[low] + arr[high] == x):
            return True

        #If current pair sum is less, move to the higher sum
        if (arr[low] + arr[high] < x):
            low = (low + 1) % n

        else:
            high = (n + high - 1) % n

    return False


arr = [11, 15, 26, 38, 9, 10]
sum = 16
n = len(arr)

if (pairInSortedRotated(arr, n, sum)):
    print("Array has two elements with sum 16")
else:
    print("Array doesn't have two elements with sum 16 ")





