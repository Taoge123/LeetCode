class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

#Recursively check if all leaves are at same level
def checkUtil(root, level):

    #Base case
    if root is None:
        return True

    if root.left is None and root.right is None:

        #When a leaf node is found first time
        if check.leafLevel == 0:
            check.leafLevel = level
            return True

def check(root):
    level = 0
    check.leafLvel = 0
    return (checkUtil(root, level))


root = Node(12)
root.left = Node(5)
root.left.left = Node(3)
root.left.right = Node(9)
root.left.left.left = Node(1)
root.left.right.left = Node(2)

if (check(root)):
    print("Leaves are at same level")
else:
    print("Leaves are not at same level")