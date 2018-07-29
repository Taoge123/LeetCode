class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def inorder(self, root):
        stack = []
        list = []
        while root or stack:
            if root:
                stack.append(root)
                root = root.left
            else:
                root = stack.pop()
                list.append(root.val)
                root = root.right

        print(list)
        return list



s = Solution()

root = TreeNode(1)
root.left = TreeNode(4)
root.right = TreeNode(2)
root.right.right = TreeNode(3)



s.inorder(root)
