def printArr(arr, n):
    for i in range(n):
        print(arr[i], " ", end="")
    print()


def generateUtil(A, B, C, i, j, m, n, len, flag):
    if (flag):  # Include valid element from A

        # Print output if there is at
        # least one 'B' in output array 'C'
        if (len):
            printArr(C, len + 1)

        # Recur for all elements of
        # A after current index
        for k in range(i, m):

            if (not len):

                ''' this block works for the
                    very first call to include
                    the first element in the output array '''
                C[len] = A[k]

                # don't increment lem
                # as B is included yet
                generateUtil(A, B, C, k + 1, j, m, n, len, not flag)

            else:

                # include valid element from A and recur
                if (A[k] > C[len]):
                    C[len + 1] = A[k]
                    generateUtil(A, B, C, k + 1, j, m, n, len + 1, not flag)


    else:

        # Include valid element from B and recur
        for l in range(j, n):

            if (B[l] > C[len]):
                C[len + 1] = B[l]
                generateUtil(A, B, C, i, l + 1, m, n, len + 1, not flag)


# Wrapper function
def generate(A, B, m, n):
    C = []  # output array
    for i in range(m + n + 1):
        C.append(0)
    generateUtil(A, B, C, 0, 0, m, n, 0, True)


# Driver program

A = [10, 15, 25]
B = [5, 20, 30]
n = len(A)
m = len(B)

generate(A, B, n, m)