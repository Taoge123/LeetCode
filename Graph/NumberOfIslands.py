class Graph:

    def __init__(self, row, col, graph):
        self.ROW = row
        self.COL = col
        self.graph = graph

    def isSafe(self, i, j, visited):

        return (i>=0 and i < self.ROW and
                j >=0 and j < self.COL and
                not visited[i][j] and self.graph[i][j])

    def DFS(self, i, j, visited):

        rowNumber = [-1, -1, -1, 0, 0, 1, 1, 1]
        colNumber = [-1, 0, 1, -1, 1, -1, 0, 1]

        visited[i][j] = True


        #Recursively for all connected neighbors
        for k in range(8):
            if self.isSafe(i + rowNumber[k], j + colNumber[k], visited):
                self.DFS(i + rowNumber[k], j + colNumber[k], visited)


    def countIslands(self):

        visited = [[False for j in range(self.COL)] for i in range(self.ROW)]

        #Initialize count as 0 and traverse through all cells of given matrix
        count = 0

        for i in range(self.ROW):
            for j in range(self.COL):

                if visited[i][j] == False and self.graph[i][j] == 1:

                    self.DFS(i, j, visited)

                    count += 1

        return count


graph = [[1, 1, 0, 0, 0],
        [0, 1, 0, 0, 1],
        [1, 0, 0, 1, 1],
        [0, 0, 0, 0, 0],
        [1, 0, 1, 0, 1]]

row = len(graph)
col = len(graph[0])

g = Graph(row, col, graph)

print("Number of islands is:")
print(g.countIslands())





