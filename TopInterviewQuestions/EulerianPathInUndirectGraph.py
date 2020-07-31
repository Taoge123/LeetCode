def findpath(graph):
    n = len(graph)
    numOfAdj =list()

    #Find out number of edges each vertex has
    for i in range(n):
        numOfAdj.append(sum(graph[i]))

    #Find out how many vertex has odd number edges
    startpoint = 0
    numOfOdd = 0
    for i in range(n-1, -1, -1):
        if (numOfAdj[i] % 2 == 1):
            numOfOdd += 1
            startpoint = i

    #If number of vertex with odd number of edges
    ## is greater than two return 'no solutiom'
    if (numOfOdd > 2):
        print("No solution")
        return

    """If there is a path find the path 
    Initialize empty stack and path take the starting current"""
    stack = list()
    path = list()
    cur = startpoint

    #Loop will run until there is element in the stack or current edge has some neighbor
    while(stack != [] or sum(graph[cur]) != 0):

        #If current node has any neighbor add it to path and pop stack
        if (sum(graph[cur]) == 0):
            path.append(cur + 1)
            cur = stack.pop(-1)

        #If the current vertex has at least one neighbor add the current vertex to stack,
        #Remove the edge betwen them and set the current to its neighbor
        else:
            




