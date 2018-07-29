# Definition for a binary tree node.


# iterativePreorder(node)
#   parentStack = empty stack
#   while (not parentStack.isEmpty() or node ≠ null)
#     if (node ≠ null)
#       visit(node)
#       if (node.right ≠ null) parentStack.push(node.right)
#       node = node.left
#     else
#       node = parentStack.pop()



class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """

        stack = []
        List = []
        while root or stack:
            if root:
                List.append(root.val)
                stack.append(root)
                root = root.left
            else:
                root = stack.pop()
                root = root.right

        print(List)
        return List



s = Solution()

root = TreeNode(1)
root.right = TreeNode(2)
root.right.right = TreeNode(3)



s.preorderTraversal(root)














