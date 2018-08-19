def maxSum(arr):

    arrSum = 0

    currVal = 0

    n = len(arr)

    for i in range(0, n):
        arrSum = arrSum + arr[i]
        currVal = currVal + (i * arr[i])

    print(currVal)
    #initialize result
    maxVal = currVal

    #Try all rotations one by one and find the max rotation sum
    for j in range(1, n):
        currVal = currVal + arrSum - n * arr[n-j]
        if currVal > maxVal:
            maxVal = currVal

    return maxVal


arr = [10, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print("Max sum is: ", maxSum(arr))

# https://www.geeksforgeeks.org/find-maximum-value-of-sum-iarri-with-only-rotations-on-given-array-allowed/
