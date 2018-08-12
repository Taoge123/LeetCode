def isTriplet(arr, n):

    #Square all the elements
    for i in range(n):

        arr[i] = arr[i] * arr[i]

    arr.sort()

    #Fix one element and find other two i goes from n-1 to 2
    for i in range(n-1, 1, -1):

        #Start 2 index variables from 2 corners of the array and move them toward each other
        j = 0
        k = i - 1

        while(j < k):
            if (arr[j] + arr[k] < arr[i]):
                return True

            else:
                k = k - 1

    return False


ar = [3, 1, 4, 6, 5]
ar_size = len(ar)
if(isTriplet(ar, ar_size)):
  print("Yes")
else:
  print("No")





