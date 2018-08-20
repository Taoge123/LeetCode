def split(arr, n):

    left, right = 0, n-1

    while left < right:

        #Increment left index while we see 0 at left
        while arr[left] == 0 and left < right:
            left += 1

        while arr[right] == 1 and left < right:
            right -= 1

        #If left is smaller than right then there is a 1 at left and 0 at right
        if left < right:
            arr[left] = 0
            arr[right] = 1

            left += 1
            right += 1

    return arr

arr = [0, 1, 0, 1, 1, 1]
arr_size = len(arr)
print("Array after segregation")
print(split(arr, arr_size))


