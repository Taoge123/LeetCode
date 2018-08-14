from collections import defaultdict

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = defaultdict(list)

    def addEdge(self, u, v):
        self.graph[u].append(v)

    def DFSUtil(self, v, visited):

        visited[v] = True

        for i in self.graph[v]:
            if visited[i] == False:
                self.DFSUtil(i, visited)

#Function that returns reverse (or transpose) of graph
    def getTranspose(self):

        g = Graph(self.V)

        #Recur for all the vertices adjacent to this vertex
        for i in self.graph:
            for j in self.graph[i]:
                g.addEdge(j, i)

        return g


    def isSCC(self):

        #1. Mark all the vertices as not visited
        visited = [False] * (self.V)

        #2. Do DFS traversal starting from first vertex
        self.DFSUtil(0, visited)

        #If DFS traversal doesnt visit all vertices, then return false
        if any(i == False for i in visited):
            return False

        #3. Created a reverse graph
        reversedGraph = self.getTranspose()

        #4. Mark all the vertices as not visited (For the second DFS)
        visited = [False] * (self.V)

        #5. Do DFS for reversed graph starting from first vertex
        #Starting vertec must be the same starting point of first DFS
        reversedGraph.DFSUtil(0, visited)

        #If all vertices are not visited in second DFS, then return False
        if any(i == False for i in visited):
            return False

        return True


g1 = Graph(5)
g1.addEdge(0, 1)
g1.addEdge(1, 2)
g1.addEdge(2, 3)
g1.addEdge(3, 0)
g1.addEdge(2, 4)
g1.addEdge(4, 2)
print("Yes" if g1.isSCC() else "No")

g2 = Graph(4)
g2.addEdge(0, 1)
g2.addEdge(1, 2)
g2.addEdge(2, 3)
print("Yes" if g2.isSCC() else "No")







