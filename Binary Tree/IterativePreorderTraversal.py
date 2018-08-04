class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def iterativePreorder(root):

    if root is None:
        return

    stack = []
    stack.append(root)

    while stack:
        node = stack.pop()
        print(node.data)


        if node.right:
            stack.append(node.right)

        if node.left:
            stack.append(node.left)


root = Node(10)
root.left = Node(8)
root.right = Node(2)
root.left.left = Node(3)
root.left.right = Node(5)
root.right.left = Node(2)
iterativePreorder(root)


