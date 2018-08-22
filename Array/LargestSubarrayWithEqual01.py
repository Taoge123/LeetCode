def findSubArray(arr, n):

    sum = 0
    maxSize = -1

    #Pick a starting point as i
    for i in range(0, n-1):

        sum = -1 if (arr[i] == 0) else 1

        #Consider all subarray starting from i
        for j in range(i+1, n):

            if arr[j] == 0:
                sum -= 1
            else:
                sum += 1

            if (sum == 0 and maxSize < j - i + 1):

                maxSize = j - i + 1
                startIndex = i

    if (maxSize == -1):
        print("No such array")
    else:
        print(startIndex, "to", startIndex + maxSize - 1)

    return maxSize

arr = [1, 0, 0, 1, 0, 1, 1]
size = len(arr)
findSubArray(arr, size)




