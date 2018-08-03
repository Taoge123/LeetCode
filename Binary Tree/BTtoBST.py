class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def storeInorder(root, inorder):

    if root is None:
        return

    #store left tree
    storeInorder(root.left, inorder)

    inorder.append(root.data)

    storeInorder(root.right, inorder)


def arrayToBST(arr, root):

    #Base case
    if root is None:
        return


    arrayToBST(arr, root.left)

    #update the root's data and delete the value from array
    root.data = arr[0]
    arr.pop(0)

    arrayToBST(arr, root.right)


def binaryTreeToBST(root):

    if root is None:
        return

    #Create the temp array and store the inorder traversal of tree
    arr = []
    storeInorder(root, arr)

    #Sort the array
    arr.sort()

    #Copy array back to BS
    arrayToBST(arr, root)


def printInorder(root):
    if root is None:
        return
    printInorder(root.left)
    print(root.data)
    printInorder(root.right)

# Driver program to test above function
root = Node(10)
root.left = Node(30)
root.right = Node(15)
root.left.left = Node(20)
root.right.right= Node(5)

# Convert binary tree to BST
binaryTreeToBST(root)
print("Following is the inorder traversal of the converted BST")
printInorder(root)





