class Node:

    def __init__(self, data):

        self.data = data
        self.left = None
        self.right = None

def height(node):

    #Base case
    if node is None:
        return 0

    return max(height(node.left), height(node.right)) + 1

def diameter(node):

    if node is None:
        return 0

    lHeight = height(node.left)
    rHeight = height(node.right)

    lDiameter = diameter(node.left)
    rDiameter = diameter(node.right)

    #Return the max
    return max(lHeight + rHeight + 1, max(lDiameter, rDiameter))


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
print("Diameter of given binary tree is %d" %(diameter(root)))

