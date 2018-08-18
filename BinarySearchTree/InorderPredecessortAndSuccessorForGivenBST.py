class Node:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def findPreSuc(root, data):

    #Base case
    if root is None:
        return

    #If key is the root
    if root.data == data:

        #THe max value in left subtree is predecessor
        if root.left:
            temp = root.left
            while(temp.right):
                temp = temp.right
            findPreSuc.pre = temp

        #THe min value in right subtree is successor
        if root.right:
            temp = root.right
            while(temp.left):
                temp = temp.left
            findPreSuc.suc = temp

        return

    #If key is samler than root's key, go left subtree
    if root.data > data:
        findPreSuc.suc = root
        findPreSuc(root.left, data)

    else:
        findPreSuc.pre = root
        findPreSuc(root.right, data)

def insert(root, data):

    if root is None:
        return Node(data)

    if data < root.data:
        root.left = insert(root.left, data)

    else:
        root.right = insert(root.right, data)

    return root


key = 65  # Key to be searched in BST

""" Let us create following BST
              50
           /     \
          30      70
         /  \    /  \
       20   40  60   80 
"""
root = None
root = insert(root, 50)
insert(root, 30);
insert(root, 20);
insert(root, 40);
insert(root, 70);
insert(root, 60);
insert(root, 80);

# Static variables of the function findPreSuc
findPreSuc.pre = None
findPreSuc.suc = None

findPreSuc(root, key)

if findPreSuc.pre is not None:
    print("Predecessor is", findPreSuc.pre.data)

else:
    print("No Predecessor")

if findPreSuc.suc is not None:
    print("Successor is", findPreSuc.suc.data)
else:
    print("No Successor")








