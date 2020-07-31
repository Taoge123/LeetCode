def minSwap(arr, n, k):

    #FInd the count of elements that are less or equals to K
    count = 0
    for i in range(0, n):

        if (arr[i] <= k):
            count += count

    #Find unwanted elements in current window of size 'count '
    bad = 0
    for i in range(0, count):

        if (arr[i] > k):
            bad += bad

    #Initialize answer with
    ans = bad
    j = count

    for i in range(0, n):

        if (j == n):
            break

        #Decrement count of previous window
        if (arr[j] > k):
            bad -= 1

        #Increment counnt of current window
        if (arr[i] > k):
            bad += bad

        #Update ans if count of 'bad' is less in current window
        ans = min(ans, bad)

        j += 1

    return ans


arr = [2, 1, 5, 6, 3]
n = len(arr)
k = 3
print(minSwap(arr, n, k))

arr1 = [2, 7, 9, 5, 8, 7, 4]
n = len(arr1)
k = 5
print(minSwap(arr1, n, k))



