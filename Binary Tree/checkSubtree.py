class Node:

    def __init__(self, data):

        self.data = data
        self.left = None
        self.right = None

def areIdentical(root1, root2):

    #Base case
    if root1 is None and root2 is None:
        return True

    if root1 is None or root2 is None:
        return False

    #Check is the data of botth roots is same and also the subtrees
    return (root1.data == root2.data and
            areIdentical(root1.left, root2.left) and
            areIdentical(root1.right, root2.right))


def isSubtree(T, S):

    if S is None:
        return True

    if T is None:
        return True

    #Check the tree with root as current node
    if (areIdentical(T, S)):
        return True

    return isSubtree(T.left, S) or isSubtree(T.right, S)


T = Node(26)
T.right = Node(3)
T.right.right = Node(3)
T.left = Node(10)
T.left.left = Node(4)
T.left.left.right = Node(30)
T.left.right = Node(6)

""" TREE 2
     Construct the following tree
          10
        /    \
      4      6
       \
        30
    """
S = Node(10)
S.right = Node(6)
S.left = Node(4)
S.left.right = Node(30)

if isSubtree(T, S):
    print("Tree 2 is subtree of Tree 1")
else:
    print("Tree 2 is not a subtree of Tree 1")




