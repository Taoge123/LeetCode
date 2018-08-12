def zigZag(arr, n):

    flag = True

    for i in range(n-1):

        if flag is True:

            #If we have a situation like A > B > C, then we got A > B < C
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]

        else:

            #If we have a situation like A < B < C, then we got A < C > B
            if arr[i] < arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]

        flag = bool(1-flag)

    print(arr)

arr = [4, 3, 7, 8, 6, 2, 1]
n = len(arr)
zigZag(arr, n)




