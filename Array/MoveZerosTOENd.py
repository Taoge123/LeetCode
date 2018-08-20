
def moveZeros(arr, n):

    count = 0

    #Traverse the array. If element encountered is non-zero, then replace the element at index 'count'
    for i in range(n):
        if arr[i] != 0:

            arr[count] = arr[i]
            count += 1

    #Now all non-zero elements have been shifted to front and 'count' is set as
    #index of first 0
    while count < n:
        arr[count] = 0
        count += 1


arr = [1, 9, 8, 4, 0, 0, 2, 7, 0, 6, 0, 9]
n = len(arr)
moveZeros(arr, n)
print("Array after pushing all zeros to end of array:")
print(arr)
