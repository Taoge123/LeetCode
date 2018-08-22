# Greedy algorithms

def maxSum(arr, n):

    sum = 0
    arr.sort()

    for i in range(0, int(n/2)):

        sum -= (2 * arr[i])
        sum += (2 * arr[n - i - 1])

    return sum


arr = [4, 2, 1, 8]
n = len(arr)
print (maxSum(arr, n))

