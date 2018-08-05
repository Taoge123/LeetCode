from collections import defaultdict

class Graph:

    def __init__(self, vertices):
        self.V = vertices
        self.gragh = defaultdict(list)

    def DFSUtil(self, v, visited):

        visited[v] = True

        for i in self.gragh[v]:
            if visited[i] == False:
                self.DFSUtil(i, visited)

    def addEdge(self, v, w):
        self.gragh[v].append(w)

    def findMother(self):

        #visited is for DFS
        visited = [False] * (self.V)
        motherVertex = 0

        for i in range(self.V):
            if visited[i] == False:
                self.DFSUtil(i, visited)
                motherVertex = i

        #We simply check is every vertex is reachable by v
        visited = [False] * (self.V)

        self.DFSUtil(motherVertex, visited)

        if any(i == False for i in visited):
            return -1

        else:
            return motherVertex

g = Graph(7)
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 3)
g.addEdge(4, 1)
g.addEdge(6, 4)
g.addEdge(5, 6)
g.addEdge(5, 2)
g.addEdge(6, 0)
print ("A mother vertex is " + str(g.findMother()))







