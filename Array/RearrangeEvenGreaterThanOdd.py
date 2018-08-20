def rearrange(a, n):

    a.sort()

    ans = [0] * n
    p = 0
    q = n - 1

    for i in range(n):

        #Assign even indexes with max elements
        if (i + 1) % 2 == 0:
            ans[i] = a[q]
            q -= 1

        #Assign odd indexes with remaining elements
        else:

            ans[i] = a[p]
            p += 1


    for i in range(n):
        print(ans[i], end=" ")


A = [ 1, 3, 2, 2, 5 ]
n = len(A)
rearrange(A, n)




