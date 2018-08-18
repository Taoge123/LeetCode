class Node:

    def __init__(self, data):

        self.data = data
        self.left = None
        self.right = None

def storeInorder(root, inorder):

    #Base case
    if root is None:
        return

    #First store the inorder traversal of a tree
    storeInorder(root.left, inorder)

    inorder.append(root.data)

    storeInorder(root.right, inorder)


def countNodes(root):

    if root is None:
        return 0

    return countNodes(root.left) + countNodes(root.right) + 1

def arrayToBST(arr, root):

    #Base case
    if root is None:
        return

    #First update the left subtree
    arrayToBST(arr, root.left)

    #Now update the root data delete the value from array
    root.data = arr[0]
    arr.pop(0)

    #Finally update the right subtree
    arrayToBST(arr, root.right)

def binaryTreeToBST(root):

    #Base case
    if root is None:
        return

    #Count the number of nodes in Binary tree so that we know the size of temp array
    n = countNodes(root)

    #Create the temp array and store the inorder traversal of the tree
    arr = []
    storeInorder(root, arr)

    #Sort the array
    arr.sort()

    #Copy array elements back to binary tree
    arrayToBST(arr, root)

def printInorder(root):

    if root is None:
        return

    printInorder(root.left)
    print(root.data)
    printInorder(root.right)


root = Node(10)
root.left = Node(30)
root.right = Node(15)
root.left.left = Node(20)
root.right.right = Node(5)

# Convert binary tree to BST
binaryTreeToBST(root)

print("Following is the inorder traversal of the converted BST")
printInorder(root)



