class Node:

    def __init__(self, data):

        self.data = data
        self.left = None
        self.right = None

def printAncestor(root, target):

    if root == None:
        return False

    if root.data == target:
        return True

    #IF target is present in either left or right subtree of
    #of this node, then print this node
    if (printAncestor(root.left, target) or printAncestor(root.right, target)):
        print(root.data)
        return True

    return False


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.left.left.left = Node(7)

printAncestor(root, 7)




