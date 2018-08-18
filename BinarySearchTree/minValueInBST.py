class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def insert(root, data):

    if root is None:
        return Node(data)

    else:

        if data < root.data:
            root.left = insert(root.left, data)
        else:
            root.right = insert(root.right, data)

        return root

def minValue(node):

    current = node

    while(current.left):
        current = current.left

    return current.data


root = None
root = insert(root, 4)
insert(root, 2)
insert(root, 1)
insert(root, 3)
insert(root, 6)
insert(root, 5)

print("\nMinimum value in BST is %d" % (minValue(root)))






