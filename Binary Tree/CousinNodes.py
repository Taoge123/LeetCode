class Node:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def isSibling(root, a, b):

    #Base case
    if root is None:
        return 0

    return ((root.left == a and root.right == b) or
            (root.left == b and root.right == a) or
            isSibling(root.left, a, b) or
            isSibling(root.right, a, b))

#Recursicely to find level of Node 'ptr' in a binary tree
def level(root, ptr, lev):

    if root is None:
        return 0
    if root == ptr:
        return lev

    #Return leve if node is present in left subtree
    left = level(root.left, ptr, lev+1)
    if left != 0:
        return left

    #Else search in right subtree
    return level(root.right, ptr, lev+1)

#Return 1 if a and b are cousins, otherwise 0
def isCousin(root, a, b):

    if ((level(root, a, 1) == level(root, b, 1)) and not (isSibling(root, a, b))):
        return 1
    else:
        return 0

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.left.right.right = Node(15)
root.right.left = Node(6)
root.right.right = Node(7)
root.right.left.right = Node(8)

node1 = root.left.right
node2 = root.right.right

print ("Yes") if isCousin(root, node1, node2) == 1 else print("No")







