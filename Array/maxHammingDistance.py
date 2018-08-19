def maxHamming(arr, n):

    brr = [0] * (2 * n + 1)

    for i in range(n):
        brr[i] = arr[i]

    for i in range(n):
        brr[n+i] = arr[i]

    #Hamming distance with 0 rotation is 0
    maxHam = 0

    #WE try other rotations one by one and compute Hamming distance
    #of efvery rotation
    for i in range(1, n):
        currHam = 0
        k = 0

        for j in range(i, i+n):
            if brr[j] != arr[k]:
                currHam += 1
                k += 1
                # print(brr)

        if currHam == n:
            return n

        maxHam = max(maxHam, currHam)

    return maxHam

arr = [2, 4, 6, 8]
n = len(arr)
print(maxHamming(arr, n))




