# Definition for a binary tree node.
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
        List = []
        self.preorderTraversalUtil(root, List)


    def preorderTraversalUtil(self, root, List):
        if root is None:
            return

        List.append(root.val)
        # if root.left is None and root.right is None:
        #     List.append(root.val)

        if root.left:
            self.preorderTraversalUtil(root.left, List)

        if root.right:
            self.preorderTraversalUtil(root.right, List)

        print(List)
s = Solution()

root = TreeNode(1)
root.right = TreeNode(2)
root.right.right = TreeNode(3)



s.preorderTraversal(root)
