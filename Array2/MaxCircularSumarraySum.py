def kadane(a):

    n = len(a)
    max_so_far = 0
    max_ending_here = 0

    for i in range(0, n):
        max_ending_here = max_ending_here + a[i]

        if (max_ending_here < 0):
            max_ending_here = 0

        if (max_so_far < max_ending_here):
            max_so_far = max_ending_here

    return max_so_far


def maxCircularSum(a):
    n = len(a)

    #Case 1 is get the max sum using standard kadane algo
    max_kadane = kadane(a)

    #Case 2 is to find the max sum that includes corner # elements
    max_wrap = 0

    for i in range(0, n):
        max_wrap += a[i]
        a[i] = -a[i]

    #Max sum with corner elements will be
    #array - sum - (-max subarray sum of inverted array)
    max_wrap = max_wrap + kadane(a)

    #The max circular sum will be max of 2 sums
    if max_wrap > max_kadane:
        return max_wrap
    else:
        return max_kadane

a = [11, 10, -20, 5, -3, -5, 8, -13, 10]
print("Maximum circular sum is", maxCircularSum(a))



