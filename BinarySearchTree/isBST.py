INT_MAX = 4294967296
INT_MIN = -4294967296


class Node:
    def __init__(self, data):

        self.data = data
        self.left = None
        self.right = None

def isBST(node):
    return (node, INT_MIN, INT_MAX)

def isBSTUtil(node, min, max):

    if node is None:
        return True

    if node.data < min or node.data > max:
        return False

    return (isBSTUtil(node.left, min, node.data - 1) and
            isBSTUtil(node.right, node.data+1, max))


root = Node(4)
root.left = Node(2)
root.right = Node(5)
root.left.left = Node(1)
root.left.right = Node(3)

if (isBST(root)):
    print("Is BST")
else:
    print("Not a BST")




