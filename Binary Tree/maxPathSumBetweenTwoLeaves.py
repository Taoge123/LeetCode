INT_MIN = -2**32

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def maxPathSumUtil(root, res):

    if root is None:
        return 0

    if root.left is None and root.right is None:
        return root.data

    #FInd the max sum in left subtree and right subtree
    leftSum = maxPathSumUtil(root.left, res)
    rightSum = maxPathSumUtil(root.right, res)

    if root.left is not None and root.right is not None:

        #Update result if needed
        res[0] = max(res[0], leftSum + rightSum + root.data)

        return max(leftSum, rightSum) + root.data

    if root.left is None:
        return rightSum + root.data
    else:
        return leftSum + root.data

def maxPathSum(root):
    res = [INT_MIN]
    maxPathSumUtil(root, res)
    return res[0]


root = Node(-15)
root.left = Node(5)
root.right = Node(6)
root.left.left = Node(-8)
root.left.right = Node(1)
root.left.left.left = Node(2)
root.left.left.right = Node(6)
root.right.left = Node(3)
root.right.right = Node(9)
root.right.right.right = Node(0)
root.right.right.right.left = Node(4)
root.right.right.right.right = Node(-1)
root.right.right.right.right.left = Node(10)

print("Max pathSum of the given binary tree is", maxPathSum(root))




