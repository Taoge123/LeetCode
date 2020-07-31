class Graph:

    def __init__(self, row, col, g):
        self.ROW = row
        self.COL = col
        self.graph = g

    def isSafe(self, i, j, visited):

        return (i>=0 and i<self.ROW and
                j>=0 and j<self.COL and
                not visited[i][j] and self.graph[i][j])

    def DFS(self, i, j, visited):

        #These arrays are used to get row and column numbers of 8 neighbors
        rowNum = [-1, -1, -1,  0, 0,  1, 1, 1];
        colNum = [-1,  0,  1, -1, 1, -1, 0, 1];

        visited[i][j] = True

        for k in range(8):
            if self.isSafe(i + rowNum[k], j + colNum[k], visited):
                self.DFS(i + rowNum[k], j + colNum[k], visited)

    def countIslands(self):

        visited = [[False for j in range(self.COL)] for i in range(self.ROW)]

        #Initialize count as 0 and traverse through the all cells of given matrix
        count = 0
        for i in range(self.ROW):
            for j in range(self.COL):

                 #IF a cell with value 1 is not visited yet, then new island found
                 if visited[i][j] == False and self.graph[i][j] == 1:


                    #Visited all cells in this island and incrememnt island count
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

g = graph(row, col, graph)

print("Number of islands is:")
print(g.countIslands())