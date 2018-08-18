class Node:
    def __init__(self, data):

        self.data = data
        self.left = None
        self.right = None

def inorder(root):
    if root is not None:
        inorder(root.left)
        print(root.data)
        inorder(root.right)

def insert(node, data):

    #If the tree is empty, then return a new node
    if node is None:
        return Node(data)

    if data < node.data:
        node.left = insert(node.left, data)

    else:
        node.right = insert(node.right, data)

    return node


def minValueNode(node):

    current = node

    while (current.left is not None):
        current = current.left

    return current

def deleteNode(root, data):

    #Base case
    if root is None:
        return root

    if data < root.data:
        root.left = deleteNode(root.left, data)

    elif data > root.data:
        root.right = deleteNode(root.right, data)

    else:

        if root.left is None:
            temp = root.right
            # root = None
            return temp

        elif root.right is None:
            temp = root.left
            # root = None
            return temp

        #Node with 2 children: get the inorder successor (smallest in the right subtree)
        temp = minValueNode(root.right)

        #copy th einorder successor content to this node
        root.data = temp.data

        #Delete the inorder successor
        root.right = deleteNode(root.right, temp.data)

    return root


root = None
root = insert(root, 50)
root = insert(root, 30)
root = insert(root, 20)
root = insert(root, 40)
root = insert(root, 70)
root = insert(root, 60)
root = insert(root, 80)

print("Inorder traversal of the given tree")
inorder(root)

print("\nDelete 20")
root = deleteNode(root, 20)
print("Inorder traversal of the modified tree")
inorder(root)

print("\nDelete 30")
root = deleteNode(root, 30)
print("Inorder traversal of the modified tree")
inorder(root)

print("\nDelete 50")
root = deleteNode(root, 50)
print("Inorder traversal of the modified tree")
inorder(root)









