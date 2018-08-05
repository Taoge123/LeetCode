class Node:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def getLevelDiff(root):

    #Base case
    if root is None:
        return 0

    return (root.data - getLevelDiff(root.left) - getLevelDiff(root.right))

root = Node(5)
root.left = Node(2)
root.right = Node(6)
root.left.left = Node(1)
root.left.right = Node(4)
root.left.right.left = Node(3)
root.right.right = Node(8)
root.right.right.right = Node(9)
root.right.right.left = Node(7)

print ("%d is the required difference" %(getLevelDiff(root)))



