def findThreeNumbers(arr):

    n = len(arr)
    max = n - 1
    min = 0

    #Create an array that will store index of a smaller element on left side.
    smaller = [0] * 10000
    smaller[0] = -1
    for i in range(1, n):

        if (arr[i] <= arr[min]):
            min = i
            smaller[i] = -1

        else:
            smaller[i] = min

    greater = [0] * 10000
    greater[n-1] = -1

    for i in range(n-2, -1, -1):

        if (arr[i] >= arr[max]):
            max = i
            greater[i] = -1

        else:
            greater[i] = max

    #Now find a number which has both a greater number on right side and smaller number on left side
    for i in range(0, n):
        if smaller[i] != -1 and greater[i] != -1:
            print(arr[smaller[i]], arr[i], arr[greater[i]])

            return

    print("No triplet found")
    return


arr = [12, 11, 10, 5, 6, 2, 30]
findThreeNumbers(arr)

