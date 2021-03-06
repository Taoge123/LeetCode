class Node:
    def __init__(self, d):
        self.data = d
        self.left = None
        self.right = None
 
# function to convert sorted array to a
# balanced BST
# input : sorted array of integers
# output: root node of balanced BST
def sortedArrayToBST(arr):
     
    if not arr:
        return None
 
    # find middle
    mid = int((len(arr)) / 2)

    root = Node(arr[mid])

    root.left = sortedArrayToBST(arr[:mid])
    root.right = sortedArrayToBST(arr[mid+1:])
    return root

def preOrder(node):
    if not node:
        return
     
    print(node.data)
    preOrder(node.left)
    preOrder(node.right) 

 
arr = [1, 2, 3, 4, 5, 6, 7]
root = sortedArrayToBST(arr)
print("PreOrder Traversal of constructed BST ")
preOrder(root)
