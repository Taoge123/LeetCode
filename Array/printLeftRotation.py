def leftRotation(arr, n, k):

    mod = k % n

    for i in range(n):

        print(str(arr[(mod + i) % n]))

    print()
    return


arr = [1, 3, 5, 7, 9]
n = len(arr)
k = 2
leftRotation(arr, n, k)

k = 3
leftRotation(arr, n, k)

k = 4
leftRotation(arr, n, k)





