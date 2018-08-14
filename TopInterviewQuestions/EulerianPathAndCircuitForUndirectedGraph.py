from collections import defaultdict

class Graph:

    def __init__(self, vertices):
        self.V = vertices
        self.graph = defaultdict(list)

    def addEdge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)

    def DFSUtil(self, v, visited):

        visited[v] = True

        for i in self.graph[v]:
            if visited[i] == False:
                self.DFSUtil(i, visited)

    def isConnected(self):

        visited = [False] * (self.V)

        #Find a vertex with non zero degree
        for i in range(self.V):
            if len(self.graph[i]) > 1:
                break

        #if there are no edges in the graph
        if i == self.V - 1:
            return True

        #Start DFS traversal from a vertex with non - zero
        self.DFSUtil(i, visited)

        #Check if all non zero degree vertices
        for i in range(self.V):
            if visited[i] == False and len(self.graph[i]) > 0:
                return False

        return True

    def isEulerian(self):

        if self.isConnected() == False:
            return 0

        else:

            odd = 0
            for i in range(self.V):
                if len(self.graph[i]) % 2 != 0:
                    odd += 1

                if odd == 0:
                    return 2

                elif odd == 2:
                    return 1

                elif odd > 2:
                    return 0

    def test(self):

        res = self.isEulerian()
        if res == 0:
            print("not Eulerian")

        elif res == 1:
            print("graph has Eular path")

        else:
            print("graph has a Eular cycle")


g1 = Graph(5);
g1.addEdge(1, 0)
g1.addEdge(0, 2)
g1.addEdge(2, 1)
g1.addEdge(0, 3)
g1.addEdge(3, 4)
g1.test()

g2 = Graph(5)
g2.addEdge(1, 0)
g2.addEdge(0, 2)
g2.addEdge(2, 1)
g2.addEdge(0, 3)
g2.addEdge(3, 4)
g2.addEdge(4, 0)
g2.test();

g3 = Graph(5)
g3.addEdge(1, 0)
g3.addEdge(0, 2)
g3.addEdge(2, 1)
g3.addEdge(0, 3)
g3.addEdge(3, 4)
g3.addEdge(1, 3)
g3.test()

# Let us create a graph with 3 vertices
# connected in the form of cycle
g4 = Graph(3)
g4.addEdge(0, 1)
g4.addEdge(1, 2)
g4.addEdge(2, 0)
g4.test()

# Let us create a graph with all veritces
# with zero degree
g5 = Graph(3)
g5.test()





