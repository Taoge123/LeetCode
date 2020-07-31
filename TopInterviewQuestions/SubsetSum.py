def isSubsetSUm(set, n, sum):

    if (sum == 0):
        return True

    if (n == 0 and sum != 0):
        return False

    #IF the last element is greater than sum, then ignore it
    if (set[n - 1] > sum):
        return isSubsetSUm(set, n - 1, sum)

    """Else chec is sum can be obtained by the below 2 cases
    1. include the last element
    2. exclude the last element 
    """
    return isSubsetSUm(set, n-1, sum) or isSubsetSUm(set, n-1, sum - set[n-1])


set = [3, 34, 4, 12, 5, 2]
sum = 9

n = len(set)

if (isSubsetSUm(set, n, sum) == True):
    print("Found a subset with given sum")

else:
    print("No subset with given sum")



def isSubsetSumDP(set, n, sum):

    subset = [[0] * (n+1)] * (sum+1)
    print(subset)

    for i in range(n):
        subset[i][0] = True

    for j in range(sum-1):
        subset[0][j] = False

    for i in range(n):
        for j in range(sum):

            if (j < set[i-1]):
                subset[i][j] = subset[i-1][j]

            if (j >= set[i-1]):
                subset[i][j] = subset[i-1][j] or subset[i-1][j-set[i-1]]

    return subset[n][sum]

set = [3, 34, 4, 12, 5, 2]
sum = 9

n = len(set)

if (isSubsetSumDP(set, n, sum) == True):
    print("Found a subset with given sum")

else:
    print("No subset with given sum")


