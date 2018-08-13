from collections import defaultdict

class Graph:

    def __init__(self, vertices):

        self.V = vertices
        self.graph = []

    def addEdge(self, u, v, w):
        self.graph.append([u, v, w])

    def printArr(self, dist):
        print("Vertex Distance from source")
        for i in range(self.V):
            print("%d \t\t %d" % (i, dist[i]))

    def bellmanFord(self, src):

        #1. Initialize distance from src to all other vertices
        dist = [float("inf")] * self.V
        dist[src] = 0

        #2. Relax all edges. A simple shortest path from src to any other vetex can have at most
        for i in range(self.V - 1):

            for u, v, w in self.graph:
                if dist[u] != float("inf") and dist[u] + w < dist[v]:
                    dist[v] = dist[u] + w

        #3. Check for negative-weight cycles.
        for u, v, w in self.graph:
            if dist[u] != float("inf") and dist[u] + w < dist[v]:
                print("Graph contains negative weight cycle")
                return
            print("no cycles")

        self.printArr(dist)


g = Graph(5)
g.addEdge(0, 1, -1)
g.addEdge(0, 2, 4)
g.addEdge(1, 2, 3)
g.addEdge(1, 3, 2)
g.addEdge(1, 4, 2)
g.addEdge(3, 2, 5)
g.addEdge(3, 1, 1)
g.addEdge(4, 3, -3)

g.bellmanFord(0)





