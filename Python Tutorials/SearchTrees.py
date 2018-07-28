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


    def findval(self, data):
        if data < self.data:
            if self.left is None:
                return str(data) + "not found"
        elif data > self.data:
            if self.right is None:
                return str(data) + "not foindsss"

        else:
            print(str(self.data) + "is found")


    def printTree(self):
        if self.left:
            self.left.printTree()
        print(self.data)
        if self.right:
            self.right.printTree()

root = Node(12)
root.insert(6)
root.insert(14)
root.insert(3)
print(root.findval(7))

print(root.findval(14))

# root.printTree()



