from collections import defaultdict

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = defaultdict(list)
        self.Time = 0

    def addEdge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)

    def bridgeUtil(self, u, visited, parent, low, disc):

        #Count of children in current node
        children = 0
        visited[u] = True

        #Initialize discoverty time and low value
        disc[u] = self.Time
        low[u] = self.Time
        self.Time += 1

        #Recur for all the vertices adjacent to this vertices
        for v in self.graph[u]:

            #IF v is not visited yet, then make it a child of u inDFS tree and recur for it
            if visited[v] == False:
                parent[v] = u
                children += 1
                self.bridgeUtil(v, visited, parent, low, disc)

                #Check if the subtree rooted with v has a connectionmto one of the ancestors of u
                low[u] = min(low[u], low[v])

                if low[v] > disc[u]:
                    print("%d%d" % (u, v))

            elif v != parent[u]:
                low[u] = min(low[u], disc[v])


    def bridge(self):

        visited = [False] * (self.V)
        disc = [float("inf")] * (self.V)
        low = [float("inf")] * (self.V)
        parent = [-1] * (self.V)

        for i in range(self.V):
            if visited[i] == False:
                self.bridgeUtil(i, visited, parent, low, disc)


g1 = Graph(5)
g1.addEdge(1, 0)
g1.addEdge(0, 2)
g1.addEdge(2, 1)
g1.addEdge(0, 3)
g1.addEdge(3, 4)

print("Bridges in first graph ")
g1.bridge()

g2 = Graph(4)
g2.addEdge(0, 1)
g2.addEdge(1, 2)
g2.addEdge(2, 3)
print("\nBridges in second graph ")
g2.bridge()

g3 = Graph(7)
g3.addEdge(0, 1)
g3.addEdge(1, 2)
g3.addEdge(2, 0)
g3.addEdge(1, 3)
g3.addEdge(1, 4)
g3.addEdge(1, 6)
g3.addEdge(3, 5)
g3.addEdge(4, 5)
print("\nBridges in third graph ")
g3.bridge()










