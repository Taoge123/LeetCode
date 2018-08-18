class Node:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

#Ceil value node is the smallest data that larger than or equal to key value
def ceil(root, input):

    #Base case
    if root == None:
        return -1

    if root.data == input:
        return root.data

    #If root's data is smaller, ceil must be in right subtree
    if root.data < input:
        return ceil(root.right, input)

    #Else, either left subtree or root has the ceil value
    val = ceil(root.left, input)

    return val if val >= input else root.data


root = Node(8)

root.left = Node(4)
root.right = Node(12)

root.left.left = Node(2)
root.left.right = Node(6)

root.right.left = Node(10)
root.right.right = Node(14)

for i in range(16):
    print("%d %d" % (i, ceil(root, i)))

