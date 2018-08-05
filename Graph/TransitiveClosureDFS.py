from collections import defaultdict

class Graph:

    def __init__(self, vertices):

        self.V = vertices
        self.graph = defaultdict(list)
        self.tc = [[0 for j in range(self.V)] for i in range(self.V)]

    def addEdge(self, u, v):
        self.graph[u].append(v)

    def DFSUtil(self, s, v):

        #Mark reachable node as true
        self.tc[s][v] = 1

        #Find all the vertices reachable through v
        for i in self.graph[v]:
            if self.tc[s][i] == 0:
                self.DFSUtil(s, i)


    def transitiveClosure(self):
        #Call the recursive helper function to print DFS traversal starting form all veritves one by one
        for i in range(self.V):
            self.DFSUtil(i, i)

        print(self.tc)


g = Graph(4)
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 2)
g.addEdge(2, 0)
g.addEdge(2, 3)
g.addEdge(3, 3)


g.transitiveClosure();
print("Transitive closure matrix is")




