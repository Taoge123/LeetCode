from collections import defaultdict

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = defaultdict(list)

    def addEdge(self, u, v):
        self.graph[u].append(v)

    def printAllPathsUtil(self, u, d, visited, path):

        #Mark the current node as visited and store in path
        visited[u] = True
        path.append(u)

        #If current vertex is same as destination, then print current path[]
        if u == d:
            print(path)

        else:
            #If current vertex is not destination
            #Recur for all the vertices adjacent to this vertex
            for i in self.graph[u]:
                if visited[i] == False:
                    self.printAllPathsUtil(i, d, visited, path)

        #Remove current vertex from path[] and mark it as unvisited
        path.pop()
        visited[u] = False

    def printAllPaths(self, s, d):

        visited = [False] * (self.V)

        path = []

        self.printAllPathsUtil(s, d, visited, path)


g = Graph(4)
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(0, 3)
g.addEdge(2, 0)
g.addEdge(2, 1)
g.addEdge(1, 3)

s = 2
d = 3
print("Following are all different paths from %d to %d :" % (s, d))
g.printAllPaths(s, d)





