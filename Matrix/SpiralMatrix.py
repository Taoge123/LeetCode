def spiralPrint(m, n, a):

    """
    row = starting row index
    m = ending row index
    col = starting column index
    n = ending column index
    i = iterator
    """
    row = 0
    col = 0


    """
        
       col  n
    row . . . 
        . . .
     m  . . .
    
    """

    while (col < m and col < n):

        #Print the first row from the remaining row
        for i in range(col,n):
            print(a[row][i], end=" ")

        row += 1

        #Print the last column from the remaining columns
        for i in range(row, m):
            print(a[i][n-1], end=" ")

        n -= 1

        #Print the last row from the remaining rows
        if (row < m):

            for i in range(n-1, (col-1), -1):
                print(a[m-1][i], end=" ")

            m -= 1

        #Print the first column from the remaining columns
        if (col < n):
            for i in range(m-1, row-1, -1):
                print(a[i][col], end=" ")

            col += 1


a = [[1, 2, 3, 4, 5, 6],
     [7, 8, 9, 10, 11, 12],
     [13, 14, 15, 16, 17, 18]]

R = 3
C = 6
spiralPrint(R, C, a)







