class Node:

    def __init__(self, data):

        self.data = data
        self.left = None
        self.right = None

def getMaxWidth(root):

    #Base case
    if root is None:
        return 0

    queue = []
    maxWidth = 0

    queue.insert(0, root)

    while queue:

        #Get the size of queue when the level order traversal for one level finishes
        count = len(queue)

        #Update the maximum node count value
        maxWidth = max(count, maxWidth)

        while (count > 0):
            count = count - 1
            temp = queue[-1]
            queue.pop(0)

            if temp.left:
                queue.append(temp.left)

            if temp.right:
                queue.append(temp.right)

    return maxWidth


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.right = Node(8)
root.right.right.left = Node(6)
root.right.right.right = Node(7)

"""
Constructed bunary tree is:
       1
      / \
     2   3
    / \      \
   4   5   8
          / \
         6   7
"""

print("Maximum width is %d" % (getMaxWidth(root)))



