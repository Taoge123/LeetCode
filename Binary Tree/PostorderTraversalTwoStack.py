
class Node:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def postOrderIterative(root):
    if root is None:
        return

    stack1 = []
    stack2 = []

    stack1.append(root)

    while (stack1):

        node = stack1.pop()
        stack2.append(node)

        if node.left:
            stack1.append(node.left)
        if node.right:
            stack1.append(node.right)

    while (stack2):
        node = stack2.pop()
        print(node.data)


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)
postOrderIterative(root)