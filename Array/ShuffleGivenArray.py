import random

def randomize(arr, n):

    #To start from the last element and swap one by one
    for i in range(n-1, 0, -1):

        #Pick a random index from 0 to i
        j = random.randint(0, i)

        #Swap arr[i] with the element at random index
        arr[i], arr[j] = arr[j], arr[i]

    return arr

arr = [1, 2, 3, 4, 5, 6, 7, 8]
n = len(arr)
print(randomize(arr, n))




