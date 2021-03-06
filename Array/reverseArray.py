def reverse(A, start, end):

    while start < end:

        A[start], A[end] = A[end], A[start]

        start += 1
        end -= 1


def reverseRecursively(A, start, end):

    if start >= end:
        return

    #Base case
    A[start], A[end] = A[end], A[start]

    reverseRecursively(A, start + 1, end - 1)

A = [1, 2, 3, 4, 5, 6]
print(A)
reverseRecursively(A, 0, 5)
print("Reversed list is")
print(A)




