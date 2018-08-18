class Node:

    # Constructor to create a new node
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def buildTree(inOrder, preOrder, inStrt, inEnd):
    if (inStrt > inEnd):
        return None

    # PicK current node from Preorder
    node = Node(preOrder[buildTree.preIndex])
    buildTree.preIndex += 1

    # If this node has no children then return
    if inStrt == inEnd:
        return node

    # Else find the index of this node in Inorder traversal
    inIndex = search(inOrder, inStrt, inEnd, node.data)

    # Using index in Inorder Traversal, construct left
    # and right subtrees
    node.left = buildTree(inOrder, preOrder, inStrt, inIndex - 1)
    node.right = buildTree(inOrder, preOrder, inIndex + 1, inEnd)

    return node


# UTILITY FUNCTIONS
# Function to find index of vaue in arr[start...end]
# The function assumes that value is rpesent in inOrder[]

def search(arr, start, end, value):
    for i in range(start, end + 1):
        if arr[i] == value:
            return i


def printInorder(node):
    if node is None:
        return

    printInorder(node.left)

    print(node.data)

    printInorder(node.right)


inOrder = ['D', 'B', 'E', 'A', 'F', 'C']
preOrder = ['A', 'B', 'D', 'E', 'C', 'F']

# Static variable preIndex
buildTree.preIndex = 0
root = buildTree(inOrder, preOrder, 0, len(inOrder) - 1)

print("Inorder traversal of the constructed tree is")
printInorder(root)