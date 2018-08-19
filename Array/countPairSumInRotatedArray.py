def pairInSortedRotated(arr, n, x):

    #Find the pivot element
    for i in range(n):
        if arr[i] > arr[i+1]:
            break

    left = (i + 1) % n
    right = i

    count = 0

    #Find sum of pair formed by arr[low] and arr[right], and update left, right
    #and count accordingly
    while (left != right):

        #IF we find a pair with sum x, then increment count, move left
        #and right to next element
        if arr[left] + arr[right] == x:
            count += 1

            #This condition is required to be checked, otherwise l and r
            #will cross each other and loop will never terminate
            if left == (right - 1 + n) % n:
                return count

            left = (left + 1) % n
            right = (right - 1 + n) % n

        #If current pair sum is less, move to the higher sum side
        elif arr[left] + arr[right] < x:
            left = (left + 1) % n

        else:
            right = (n + right - 1) % n

    return count


arr = [11, 15, 6, 7, 9, 10]
s = 16

print(pairInSortedRotated(arr, 6, s))







