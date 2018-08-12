def smallestSubArrayWithSum(arr, n, x):

    min_len = n + 1

    for start in range(0, n):

        #Initialize length of smallest
        curr_sum = arr[start]

        #If first element itself is greater
        if (curr_sum > x):
            return 1

        #Try diff ending points for current start
        for end in range(start+1, n):

            curr_sum += arr[end]

            #If sum becomes more than x and length of this subarray is smaller than current smallest length,
            #update the smallest lenngth (or result)
            if curr_sum > x and (end - start + 1) < min_len:
                min_len = (end - start + 1)

    return min_len



def smallestSubWithSum(arr, n, x):


    #Initialize the current sum and minimum length
    curr_sum = 0
    min_len = n+1

    #Initialize starting and ending indexes
    start = 0
    end = 0
    while (end < n):

        #Keep adding array elemetns while current sum is smaller than x
        while (curr_sum <= x and end < n):
            curr_sum += arr[end]
            end += 1

        #If current sum becomes greater than x
        while (curr_sum > x and start < n):

            #Update min length is needed
            if(end - start < min_len):
                min_len = end - start

            #Remove starting elements
            curr_sum -= arr[start]
            start += 1

    return min_len


arr1 = [1, 4, 45, 6, 10, 19]
x = 51
n1 = len(arr1)
res1 = smallestSubWithSum(arr1, n1, x)
print("Not possible") if (res1 == n1 + 1) else print(res1)

arr2 = [1, 10, 5, 2, 7]
n2 = len(arr2)
x = 9
res2 = smallestSubWithSum(arr2, n2, x)
print("Not possible") if (res2 == n2 + 1) else print(res2)

arr3 = [1, 11, 100, 1, 0, 200, 3, 2, 1, 250]
n3 = len(arr3)
x = 280
res3 = smallestSubWithSum(arr3, n3, x)
print("Not possible") if (res3 == n3 + 1) else print(res3)






arr1 = [1, 4, 45, 6, 10, 19]
x = 51
n1 = len(arr1)
res1 = smallestSubArrayWithSum(arr1, n1, x);
if res1 == n1 + 1:
    print("Not possible")
else:
    print(res1)

arr2 = [1, 10, 5, 2, 7]
n2 = len(arr2)
x = 9
res2 = smallestSubArrayWithSum(arr2, n2, x);
if res2 == n2 + 1:
    print("Not possible")
else:
    print(res2)

arr3 = [1, 11, 100, 1, 0, 200, 3, 2, 1, 250]
n3 = len(arr3)
x = 280
res3 = smallestSubArrayWithSum(arr3, n3, x)
if res3 == n3 + 1:
    print("Not possible")
else:
    print(res3)






