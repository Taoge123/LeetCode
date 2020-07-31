global N
N = 4

def minCostRec(cost, s, d):

    if s == d or s+1 == d:
        return cost[s][d]

    min = cost[s][d]

    for i in range(s+1, d):
        c = minCostRec(cost, s, i) + minCostRec(cost, i, d)

        if c < min:
            min = c

    return min

def minCost(cost):

    return minCostRec(cost, 0, N-1)

cost = [ [0, 15, 80, 90],
         [float("inf"), 0, 40, 50],
         [float("inf"), float("inf"), 0, 70],
         [float("inf"), float("inf"), float("inf"), 0]
        ]
print("The Minimum cost to reach station %d is %d" % (N, minCost(cost)))


INF = 2147483647
N = 4

def minCost2(cost):

    dist = [0 for i in range(N)]
    for i in range(N):
        dist[i] = INF
    dist[0] = 0

    #Go through every station and check is using it as an intermediate station gives better path
    for i in range(N):
        for j in range(i+1, N):

            if (dist[j] > dist[i] + cost[i][j]):
                dist[j] = dist[i] + cost[i][j]

    return dist[N-1]


cost = [[0, 15, 80, 90],
        [INF, 0, 40, 50],
        [INF, INF, 0, 70],
        [INF, INF, INF, 0]]

print("The Minimum cost to reach station ", N, " is ", minCost2(cost))




