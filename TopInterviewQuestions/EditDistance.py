def editDistance(str1, str2, m, n):

    if m == 0:
        return n

    if n == 0:
        return m

    if str1[m-1] == str2[n-1]:
        return editDistance(str1, str2, m-1, n-1)

    return 1 + min(editDistance(str1, str2, m, n-1),
                   editDistance(str1, str2, m-1, n),
                   editDistance(str1, str2, m-1, n-1))


str1 = "sunday"
str2 = "saturday"
print(editDistance(str1, str2, len(str1), len(str2)))


def editDistanceDP(str1, str2, m, n):
    dp = [[0 for x in range(n+1)] for x in range(m+1)]

    #Fill d[][] in bottom up manner
    for i in range(m+1):
        for j in range(n+1):

            #IF first thing is empty, only option is to insert all characters of second string
            if i == 0:
                dp[i][j] = j

            #If second strign is empty, onlu option is to remove all characters of second string
            elif j == 0:
                dp[i][j] = i

            #IF last character matches, ignore last character and recur for the remaininf string
            elif str1[i-1] == str2[j-1]:
                dp[i][j] = dp[i-1][j-1]

            #If last characters are same, consider all possibilities and find minimum
            else:
                dp[i][j] = 1 + min(dp[i][j-1],
                                   dp[i-1][j],
                                   dp[i-1][j-1])

    return dp[m][n]


str1 = "sunday"
str2 = "saturday"

print(editDistanceDP(str1, str2, len(str1), len(str2)))


