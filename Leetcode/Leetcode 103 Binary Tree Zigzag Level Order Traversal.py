# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root is None:
            return []

        result, current, level = [], [root], 1

        while current:

            next_level, vals = [], []

            #the loop will process all the current nodes
            for node in current:


                vals.append(node.val)

                #the next_level stored in next level later on to be reversed
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)

            if level % 2:
                result.append(vals)
            else:
                result.append(vals[::-1])

            level += 1
            current = next_level

        return result






