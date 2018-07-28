class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data


    def insert(self, data):
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)

            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data



    def printTree(self):
        if self.left:
            self.left.printTree()
        print(self.data)
        if self.right:
            self.right.printTree()


root = Node(10)
root.left = Node(213)
root.right = Node(21332)
root.insert(7)
root.insert(7878)
root.printTree()
