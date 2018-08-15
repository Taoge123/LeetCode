V = 4

def countWalks(graph, u, v, k):

    #Base cases
    if (k == 0 and u == v):
        return 1
    if (k == 1 and graph[u][v]):
        return 1
    if (k <= 0 ):
        return 0

    #Initialize result
    count = 0

    #Go to all adjacents of u and recur
    for i in range(0, V):

        if (graph[u][i] == i):
            count += countWalks(graph, i, v, k-1)

    return count


graph = [[0, 1, 1, 1, ],
         [0, 1, 1, 1, ],
         [0, 0, 1, 1, ],
         [0, 0, 0, 0]]

u = 0;
v = 3;
k = 2
print(countWalks(graph, u, v, k))



