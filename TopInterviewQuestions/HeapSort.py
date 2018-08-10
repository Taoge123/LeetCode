def heapify(arr, n, i):

    largest = i
    l = 2 * i + 1
    r = 2 * i + 2

    #See ig left child of root exists and if its greater than root
    if l < n and arr[i] < arr[l]:
        largest = l

    #also check right child and see if its greater than root
    if r < n and arr[largest] < arr[r]:
        largest = r

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]

        heapify(arr, n, largest)

def heapSort(arr):
    n = len(arr)

    for i in range(n, -1, -1):
        heapify(arr, n, i)




