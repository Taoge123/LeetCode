class Node:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def inOrderSuccessor(root, n):

    #If the right subtree is not NULL, then succ lies in right subtree
    if n.right:
        return minValue(n.right)

    #If the right subtree is NULL, then succ is ont of the ancestors
    p = n.parent
    while p:
        if n != p.right:
            break
        n = p
        p = p.right
    return p


def minValue(root):

    current = root

    while current.left:
        current = current.left

    return current

def insert(node, data):

    if node is None:
        return Node(data)

    else:

        if data < node.data:

            temp = insert(node.left, data)
            node.left = temp
            temp.parent = node

        else:

            temp = insert(node.right, data)
            node.right = temp
            temp.parent = node

        return node


root = None

# Creating the tree given in the above diagram
root = insert(root, 20)
root = insert(root, 8);
root = insert(root, 22);
root = insert(root, 4);
root = insert(root, 12);
root = insert(root, 10);
root = insert(root, 14);
temp = root.left.right.right

succ = inOrderSuccessor(root, temp)
if succ is not None:
    print("\nInorder Successor of %d is %d " % (temp.data, succ.data))
else:
    print("\nInorder Successor doesn't exist")



