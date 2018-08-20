def segregateElement(arr, n):

    temp = [0 for _ in range(n)]
    # [1, -1, -3, -2, 7, 5, 11, 6]
    #Traversal array and store element in temp array
    #j is tracking the negagtive, whenever i is positive, assign back to j
    j = 0

    for i in range(n):
        if (arr[i] >= 0):

            temp[j] = arr[i]
            j += 1

    #If array contains all positive or all negative
    if (j == n or j == 0):
        return

    #Store element in temp array
    for i in range(n):
        if (arr[i] < 0):
            temp[j] = arr[i]
            j += 1

    #Copy contents of temp back to arr
    for k in range(n):
        arr[k] = temp[k]


arr = [1, -1, -3, -2, 7, 5, 11, 6]
n = len(arr)

segregateElement(arr, n);

for i in range(n):
    print(arr[i])



