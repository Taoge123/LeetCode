from collections import defaultdict

class Graph:

    def __init__(self, vertices):
        self.V = vertices
        self.graph = defaultdict(list)
        self.Time = 0

    def addEdge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)

    def removeEdge(self, u, v):
        for index, key in enumerate(self.graph[u]):
            if key == v:
                self.graph[u].pop(index)

        for index, key in enumerate(self.graph[v]):
            if key == u:
                self.graph[v].pop(index)

    def DFSCount(self, v, visited):

        count = 1
        visited[v] = True
        for i in self.graph[v]:

            if visited[i] == False:
                count = count + self.DFSCount(i, visited)

        return count

    def isValidNextEdge(self, u, v):

        #1.
        if len(self.graph[u]) == 1:
            return True

        #2.1 if there are multiple adjacents, then u-v are not a bridge
        visited = [False] * (self.V)
        count1 = self.DFSCount(u, visited)

        #2.2 Remove edge (u, v) and count the reachable from u
        self.removeEdge(u, v)
        visited = [False] * (self.V)
        count2 = self.DFSCount(u, visited)

        #2.3 Add the edge back to the graph
        self.addEdge(u, v)

        #2.4 If ocunt1 is greater, then edge (u, v) is a bridge
        return False if count1 > count2 else True

    def printEulerUtil(self, u):
        # Recur for all the vertices adjacent to this vertex
        for v in self.graph[u]:
            # If edge u-v is not removed and it's a a valid next edge
            if self.isValidNextEdge(u, v):
                print("%d-%d " % (u, v)),
                self.removeEdge(u, v)
                self.printEulerUtil(v)


    def printEulerTour(self):
        # Find a vertex with odd degree
        u = 0
        for i in range(self.V):
            if len(self.graph[i]) % 2 != 0:
                u = i
                break
        # Print tour starting from odd vertex
        print("\n")
        self.printEulerUtil(u)


# Create a graph given in the above diagram

g1 = Graph(4)
g1.addEdge(0, 1)
g1.addEdge(0, 2)
g1.addEdge(1, 2)
g1.addEdge(2, 3)
g1.printEulerTour()

g2 = Graph(3)
g2.addEdge(0, 1)
g2.addEdge(1, 2)
g2.addEdge(2, 0)
g2.printEulerTour()

g3 = Graph(5)
g3.addEdge(1, 0)
g3.addEdge(0, 2)
g3.addEdge(2, 1)
g3.addEdge(0, 3)
g3.addEdge(3, 4)
g3.addEdge(3, 2)
g3.addEdge(3, 1)
g3.addEdge(2, 4)
g3.printEulerTour()



