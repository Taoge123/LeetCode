from collections import defaultdict

class Graph:

    def __init__(self, vertices):
        self.V = vertices
        self.graph = defaultdict(list)
        self.Time = 0
        self.count = 0

    def addEdge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)

    def BCCUtil(self, u, parent, low, disc, st):

        #Count of chilkdren in current node
        children = 0

        #Initialize discovery time and low value
        disc[u] = self.Time
        low[u] = self.Time
        self.Time += 1

        #Recur for all the vertices adjacent to this vertex
        for v in self.graph[u]:

            #If v is not visited yet, then make it a child of u
            #in DFS tree and recur for it
            if disc[v] == -1:
                parent[v] = u
                children += 1

                #Store edges in stack
                st.append(u, v)
                self.BCCUtil(v, parent, low, disc, st)

                #Check if the subtree rooted with v has a connection to one of the ancestors of u
                #Case 1, base on SCC paper
                low[u] = min(low[u], low[v])

                #If u is an articulation point, then pop
                #All edges from stack till (u, v)
                if parent[u] == -1 and children > 1 or parent[u] != -1 and low[v] >= disc[u]:

                    self.count += 1
                    w = - 1
                    while w != (u, v):

                        w = st.pop()
                        print(w)
                    print(" ")


            elif v != parent[u] and low[u] > disc[v]:

                low[u] = min(low[u], disc[v])
                st.append((u, v))

    def BCC(self):

        disc = [-1] * (self.V)
        low = [-1] * (self.V)
        parent = [-1] * (self.V)
        st = []

        for i in range(self.V):
            if disc[i] == -1:
                self.BCCUtil(i, parent, low, disc, st)

            #If stac is not empty, pop all edsges from stacks
            if st:
                self.count = self.count + 1

                while st:
                    w = st.pop()
                    print(w)

                print(" ")

g = Graph(12)
g.addEdge(0, 1)
g.addEdge(1, 2)
g.addEdge(1, 3)
g.addEdge(2, 3)
g.addEdge(2, 4)
g.addEdge(3, 4)
g.addEdge(1, 5)
g.addEdge(0, 6)
g.addEdge(5, 6)
g.addEdge(5, 7)
g.addEdge(5, 8)
g.addEdge(7, 8)
g.addEdge(8, 9)
g.addEdge(10, 11)

g.BCC()
print("Above are %d biconnected components in graph" % (g.count));







