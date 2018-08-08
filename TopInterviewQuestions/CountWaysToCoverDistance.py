def printCountRec(dist):

    if dist < 0:
        return 0

    if dist == 0:
        return 1

    return (printCountRec(dist - 1) +
            printCountRec(dist - 2) +
            printCountRec(dist - 3))


dist = 4
print(printCountRec(dist))

'----------------------------------'
def printCountDP(dist):
    count = [0] * (dist + 1)

    count[0] = 1
    count[1] = 1
    count[2] = 2

    for i in range(3, dist + 1):
        count[i] = (count[i-1] + count[i-2] + count[i-3])

    return count[dist]

dist = 4;
print( printCountDP(dist))