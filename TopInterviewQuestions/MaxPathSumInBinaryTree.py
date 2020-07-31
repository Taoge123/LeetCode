class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def findMaxUtil(root):

    if root is None:
        return 0

    #l and r store max path sum going through left and right child of root respectively
    l = findMaxUtil(root.left)
    r = findMaxUtil(root.right)

    #Max path for parent call of root. THis path must inclide at most onne child of root
    max_single = max(max(l, r) + root.data, root.data)

    #Max top represents the sum when the node under consideration is the root of the maxSum path and
    #no ancestor of root are there in max sum path
    max_top = max(max_single, l+r+root.data)

    #static variable to store the changes and store the max result
    findMaxUtil.res = max(findMaxUtil.res, max_top)

    return max_single


def findMaxSum(root):

    findMaxUtil.res = float("-inf")

    findMaxUtil(root)
    return findMaxUtil.res

root = Node(10)
root.left = Node(2)
root.right   = Node(10);
root.left.left  = Node(20);
root.left.right = Node(1);
root.right.right = Node(-25);
root.right.right.left   = Node(3);
root.right.right.right  = Node(4);
print("Max path sum is " ,findMaxSum(root))






