class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def treeSum(root):
    if root is None:
        return 0

    return root.data + treeSum(root.left) + treeSum(root.right)



root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.right = Node(6)

print(treeSum(root))

