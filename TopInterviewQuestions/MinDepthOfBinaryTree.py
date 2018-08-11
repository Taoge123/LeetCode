class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def minDepth(root):

    if root is None:
        return 0

    if root.left is None and root.right is None:
        return 1

    #If left is None then we recur for the right
    if root.left is None:
        return minDepth(root.right) + 1

    #If right is None then we recur for the left
    if root.right is None:
        return minDepth(root.left) + 1

    return min(minDepth(root.left), minDepth(root.right)) + 1

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
print(minDepth(root))



