class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def leftLeavesSumRec(root, isLeft, summ):
    if root is None:
        return

    #Check whether this node is a leaf node and is left
    if root.left is None and root.right is None and isLeft == True:

        summ[0] += root.data

    leftLeavesSumRec(root.left, 1, summ)
    leftLeavesSumRec(root.right, 0, summ)

def leftLeavesSum(root):

    summ = [0]
    leftLeavesSumRec(root, 0, summ)

    return summ[0]

root = Node(20)
root.left = Node(9)
root.right = Node(49)
root.right.left = Node(23)
root.right.right = Node(52)
root.right.right.left = Node(50)
root.left.left = Node(5)
root.left.right = Node(12)
root.left.right.right = Node(12)
print ("Sum of left leaves is")
print(leftLeavesSum(root))


