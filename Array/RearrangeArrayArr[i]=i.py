def arrange(A, len):

    for i in range(0, len):

        if (A[i] != -1 and A[i] != i):

            x = A[i]

            #Check if desired place is not vacate
            while (A[x] != -1 and A[x] != x):

                #Store the value from desired place
                y = A[x]

                #Place the x to its correct position
                A[x] = x

                #Now y will become x, then search the place for x
                x = y

            #Place the x to its correct position
            A[x] = x

            #Check if while loop hasnt set the correct value at A[i]
            if (A[i] != i):

                A[i] = -1


A = [-1, -1, 6, 1, 9, 3, 2, -1, 4, -1]

arrange(A, len(A))

for i in range(0, len(A)):
    print(A[i], end=' ')



