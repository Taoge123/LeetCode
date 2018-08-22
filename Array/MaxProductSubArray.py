def maxSubarrayProduct(arr):

    n = len(arr)

    #max_positive product ending at here
    max_ending_here = 1

    #min positive product ending at here
    min_ending_here = 1

    max_so_far = 1

    #Traverse the array
    for i in range(0, n):

        #If this element is positive, update the max_ending_here
        if arr[i] > 0:
            max_ending_here = max_ending_here * arr[i]
            min_ending_here = min(min_ending_here * arr[i], 1)

        elif arr[i] == 0:
            max_ending_here = 1
            min_ending_here = 1

        #If element is negative.
        else:
            temp = max_ending_here
            max_ending_here = max(min_ending_here * arr[i], 1)
            min_ending_here = temp * arr[i]

        if (max_so_far < max_ending_here):

            max_so_far = max_ending_here

    return max_so_far



arr = [1, -2, -3, 0, 7, -8, -2]
print ("Maximum product subarray is",maxSubarrayProduct(arr))






