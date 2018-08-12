def min(x, y):
    return x if (x<y) else y

def max(x, y):
    return x if (x>y) else y

def findLength(arr, n):

    max_len = 1
    for i in range(n-1):

        #Initialize min and max for all subarray with i
        mn = arr[i]
        mx = arr[i]

        #Consider all subarrays starting with i and ending with j
        for j in range(i+1, n):

            #Update min and max in this subarray if needed
            mn = min(mn, arr[j])
            mx = max(mx, arr[j])

            #If current subarray has all contiguous elements
            if ((mx - mn) == j - i):
                max_len = max(max_len, mx - mn + 1)

    return max_len

arr = [1, 56, 58, 57, 90, 92, 94, 93, 91, 45]
n = len(arr)
print("Length of the longest contiguous subarray is ", findLength(arr, n))