def modify(arr, n):

    if n <= 1:
        return
    # [2, 3, 4, 5, 6]
    #To store current value of arr[0] and update it
    prev = arr[0]
    arr[0] = arr[0] * arr[1]

    for i in range(1, n-1):

        #Store the current value of of next iteration
        curr = arr[i]

        #Update current value using previous value
        arr[i] = prev * arr[i+1]

        #Update the previous value
        prev = curr

    arr[n-1] = prev * arr[n-1]


arr = [2, 3, 4, 5, 6]
n = len(arr)
modify(arr, n)
for i in range (0, n):
    print(arr[i],end=" ")



