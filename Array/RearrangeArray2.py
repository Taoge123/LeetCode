def rerrange(A, len):
    sets = {*()}

    for i in range(len):
        sets.add(A[i])

    for i in range(len):

        if i in sets:

            A[i] = i

        else:

            A[i] = -1

    return A

A = [ -1, -1, 6, 1, 9, 3, 2, -1, 4, -1 ]

rerrange(A, len(A))

print(A)






