class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def inorder(root):

    current = root
    stack = []


    while current or stack:

        #always go to left subtree and append it to stack
        if current is not None:
            stack.append(current)
            current = current.left

        #process stacks, the first one popped out will be the left most node and take its right sub-node
        else:
            if stack:
                current = stack.pop()
                print(current.data)
                current = current.right


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

inorder(root)



