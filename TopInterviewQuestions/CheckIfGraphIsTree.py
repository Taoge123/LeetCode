from collections import defaultdict

class Graph:

    def __init__(self, vertices):
        self.V = vertices
        self.graph = defaultdict(list)

    def addEdge(self, v, u):
        self.graph[u].append(v)
        self.graph[v].append(u)

    def isCyclicUtil(self, v, visited, parent):

        #Mark the current node as visited
        visited[v] = True

        for i in self.graph[v]:
            # If an adjacent is not visited, then recur for that adjacent
            if visited[i] == False:
                if self.isCyclicUtil(i, visited, v) == True:
                    return True

            #If an adjacent is visited and not parent of current vertex, then there is a cycle
            elif i != parent:
                return True

        return False

    def isTree(self):

        visited = [False] * self.V

        """The call to isCyclicUtil serves multiple purposes
        It returns true if graph reachable from vertex 0 is cyclic. It also marks
        all vertices reachable from 0
        """
        if self.isCyclicUtil(0, visited, -1) == True:
            return False

        """If we find a vertex which is not reachable from 0 -- not marked by isCyclicUtil()
        Then we return False"""
        for i in range(self.V):
            if visited[i] == False:
                return False

        return True


g1 = Graph(5)
g1.addEdge(1, 0)
g1.addEdge(0, 2)
g1.addEdge(0, 3)
g1.addEdge(3, 4)
print("Graph is a Tree" if g1.isTree() == True else "Graph is a not a Tree")

g2 = Graph(5)
g2.addEdge(1, 0)
g2.addEdge(0, 2)
g2.addEdge(2, 1)
g2.addEdge(0, 3)
g2.addEdge(3, 4)



