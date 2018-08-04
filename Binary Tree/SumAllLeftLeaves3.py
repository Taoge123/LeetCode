class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def sumOfLeftLeaves(root):

    if (root is None):
        return

    stack = []
    stack.append(root)

    sum = 0

    while stack:
        currentNode = stack.pop()
        if currentNode.left is not None:
            stack.append(currentNode.left)

            #Check if currentNode's left child is a leaf node
            if currentNode.left.left is None and currentNode.left.right is None:

                #If currentNode is a leaf, add its data to the sum
                sum = sum + currentNode.left.data

        if currentNode.right is not None:
            stack.append(currentNode.right)
    return sum

root = Node(20)
root.left = Node(9)
root.right = Node(49)
root.right.left = Node(23)
root.right.right = Node(52)
root.right.right.left = Node(50)
root.left.left = Node(5)
root.left.right = Node(12)
root.left.right.right = Node(12)
print ("Sum of left leaves is")
print(sumOfLeftLeaves(root))


