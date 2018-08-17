class Node:

    def __init__(self, data):

        self.data = data
        self.left = None
        self.right = None

def printLevelOrder(root):
    h = height(root)
    for i in range(1, h+1):
        printGivenOrder(root, i)


def height(root):

    if root is None:
        return 0
    else:
        return height(root.left) + height(root.right) + 1

def printGivenOrder(root, level):

    if root is None:
        return

    if level == 1:
        print(root.data)
        print(" ")

    else:

        printGivenOrder(root.left, level - 1)
        printGivenOrder(root.right, level - 1)

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

print("Level order traversal of binary tree is -")
printLevelOrder(root)
printGivenOrder(root, 3)

# height = height(root)
# print(height)
#
