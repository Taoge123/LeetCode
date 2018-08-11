INI_MIN = -2 * 32

def canRepresentBST(pre):

    stack = []

    root = INI_MIN

    for value in pre:

        #If we find a equal to pre[i] according to the given algo
        #If we find a node who is on the right side and similar than root, return False
        #Thern return False
        if value < root:
            return False

        while (stack and stack[-1] < value):
            root = stack.pop()

        stack.append(value)

    return True

pre1 = [40 , 30 , 35 , 80 , 100]
print("true" if canRepresentBST(pre1) == True else "false")
pre2 = [40 , 30 , 35 , 20 ,  80 , 100]
print("true" if canRepresentBST(pre2) == True else "false")






