class Node:

    def __init__(self, data):

        self.data = data
        self.left = None
        self.right = None

def getMaxWidth(root):
    maxWidth = 0

    h = height(root)

    #Get width of each level and compare the width with max width
    for i in range(1, h+1):
        width = getWidth(root, i)

        if width > maxWidth:
            maxWidth = width
    return maxWidth


def getWidth(root, level):

    if root is None:
        return 0

    if level == 1:
        return 1

    else:
        return (getWidth(root.left, level - 1) + getWidth(root.right, level - 1))


def height(root):

    if root is None:
        return 0

    else:
        return max(height(root.left), height(root.right)) + 1


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.right = Node(8)
root.right.right.left = Node(6)
root.right.right.right = Node(7)

"""
Constructed bunary tree is:
       1
      / \
     2   3
    / \      \
   4   5   8 
          / \
         6   7
"""

print("Maximum width is %d" % (getMaxWidth(root)))
