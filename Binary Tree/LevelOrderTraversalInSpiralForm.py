class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def printLevelOrderInSpiral(root):

    stack1 = [root]
    stack2 = []

    while stack1 or stack2:

        while stack1:
            node = stack1.pop()
            print(node.data)

            if node.left:
                stack2.append(node.right)

            if node.right:
                stack2.append(node.left)


        while stack2:
            node = stack2.pop()
            print(node.data)

            if node.left:
                stack1.append(node.left)

            if node.right:
                stack1.append(node.right)




root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

print( "Level Order Traversal of binary tree is -")
printLevelOrderInSpiral(root)


