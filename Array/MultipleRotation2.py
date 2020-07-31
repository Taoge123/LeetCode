def leftRotate(arr, n, k):

    for i in range(k, k+n):
        print(str(arr[i % n]), end=" ")


arr = [1, 3, 5, 7, 9]
n = len(arr)
k = 2
leftRotate(arr, n, k)
print()

k = 3
leftRotate(arr, n, k)
print()

k = 4
leftRotate(arr, n, k)
print()



