V = 4
INF = 99999

def negativeCycleFloyWarshall(graph):

    dist = [[0 for i in range(V+1)] for j in range(V+1)]

    for i in range(V):
        for j in range(V):
            dist[i][j] = graph[i][j]

    for k in range(V):
        for i in range(V):
            for j in range(V):

                if (dist[i][k] + dist[k][j] < dist[i][j]):
                    dist[i][j] = dist[i][k] + dist[k][j]


    for i in range(V):
        if (dist[i][i] < 0):
            return True

    return False



graph = [ [0, 1, INF, INF],
          [INF, 0, -1, INF],
          [INF, INF, 0, -1],
          [-1, INF, INF, 0]]

if (negativeCycleFloyWarshall(graph)):
    print("Yes")
else:
    print("No") 




