CHARS = 26

class Graph:
    def __init__(self, V):
        self.V = V
        self.adj = [[] for x in range(V)]
        self.inp = [0] * V

    def addEdge(self, u, v):
        self.adj[u].append(v)
        self.inp[v] += 1

    def isSC(self):
        visited = [False] * self.V

        #Find the first vertex with non zero degree
        n = 0
        for n in range(self.V):
            if len(self.adj[n]) > 0:
                break

        #Do DFS traversal starting from first non zero degree vertex
        self.DFSUtil(n, visited)

        #IF DFS doesnt visited all vertices, then return False
        for i in range(self.V):
            if len(self.adj[i]) > 0 and visited[i] == False:
                return False

        #Create a reversed graph
        gr = self.getTranspose()

        #Mark all the vertices as not visited for the second DFS
        for i in range(self.V):
            visited[i] = False

        #Do DFS for reversed graph starting from first vertex
        #Starting vertex must be same starting point of first DFS
        gr.DFSUtil(n, visited)

        for i in range(self.V):
            if len(self.adj[i]) > 0 and visited[i] == False:
                return False

        return True

    #This function will return true if the directed graph has an Eulerian cycle,
    # otherwise returns false
    def isEulerianCycle(self):

        #Check if all non-zero degree vertices are connected
        if self.isSC() == False:
            return False

        #Check if in degree and out degree of every vertex is same
        for i in range(self.V):
            if len(self.adj[i]) != self.inp[i]:
                return False

        return True

    #A recursive function to do DFS starting from v
    def DFSUtil(self, v, visited):

        visited[v] = True

        for i in range(len(self.adj[v])):
            if not visited[self.adj[v][i]]:
                self.DFSUtil(self.adj[v][i], visited)

    #Funnction that returns reverse (or transpose) of this graph
    #This function is needed in isSC()
    def getTranspose(self):
        g = Graph(self.V)

        for v in range(self.V):

            #Recur for all the vertices adjacent to this vertex
            for i in range(len(self.adj[v])):

                g.adj[self.adj[v][i]].append(v)

        return g

    #This function takes an of strings and returns true if the given
    #array of strings can be chained to form cycle
def canBeChained(arr, n):

    #Create a graph with 'alpha' edges
    g = Graph(CHARS)

    #Create an edge from first character to last character of every string
    for i in range(n):

        s = arr[i]
        g.addEdge(ord(s[0]) - ord('a'), ord(s[len(s) - 1]) - ord('a'))

    return g.isEulerianCycle()


arr1 = ["for", "geek", "rig", "kaf"]
n1 = len(arr1)
if canBeChained(arr1, n1):
    print("Can be chained")
else:
    print("Cant be chained")

arr2 = ["aab", "abb"]
n2 = len(arr2)
if canBeChained(arr2, n2):
    print("Can be chained")
else:
    print("Can't be chained")






