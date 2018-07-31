class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def printLevelOrderLineByLine(root):

    queue = [root]


    while queue:
        levelNodes = len(queue)

        while levelNodes:

            node = queue.pop(0)
            print(" " + str(node.data))

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

            levelNodes -= 1


        print('   ---   ')





root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.left.left.left = Node(7)
root.left.left.right = Node(8)
root.left.left.left.right = Node(8)

print( "Level Order Traversal of binary tree is -")
printLevelOrderLineByLine(root)
