import sys
class Graph():
    def __init__(self, vertivces):
        self.V = vertivces
        self.graph = [[0 for column in range(vertivces) for row in range(vertivces)]]

    #A utility function to find the vertex with minimum
    def minDistance(self, dist, sptSet):

        min = sys.maxsize
        # search not nearest vertex not in the shortest path tree
        for v in range(self.V):
            if dist[v] < min and sptSet[v] == False:
                min = dist[v]
                min_index = v
        return min_index


    #Function that implements Dijstra's single source shortest path
    def dijkstra(self, src):

        dist = [sys.maxsize] * self.V
        dist[src] = 0
        sptSet = [False] * self.V
        for count in range(self.V):

            #Pick the min dist vertex from the set of vertices not yet processed
            u = self.minDistance(dist, sptSet)

            #Put the min distance vertex in the shortest path tree
            sptSet[u] = True

            #Update dist value of the adjacent vertices of picked vertex
            for v in range(self.V):
                if self.graph[u][v] > 0 and sptSet[v] == False and dist[v] > dist[u] + self.graph[u][v]:
                    dist[v] = dist[u] + self.graph[u][v]
                    # print(dist[u])

        self.printSolution(dist)

    def printSolution(self, dist):
        print("Vertex distance from Source")
        for node in range(self.V):
            print(str(node) +  "    to       " +  str(dist[node]))




#main function
g = Graph(9)
g.graph = [[0, 4, 0, 0, 0, 0, 0, 8, 0],
           [4, 0, 8, 0, 0, 0, 0, 11, 0],
           [0, 8, 0, 7, 0, 4, 0, 0, 2],
           [0, 0, 7, 0, 9, 14,  0, 0, 0],
           [0, 0, 0, 9, 0, 10, 0, 0, 0],
           [0, 0, 4, 14, 10, 0, 2, 0, 0],
           [0, 0, 0, 0, 0, 2, 0, 1, 6],
           [8, 11, 0, 0, 0, 0, 1, 0, 7],
           [0, 0, 2, 0, 0, 0, 6, 7, 0]
          ];

g.dijkstra(0)




