class Node:
    def __init__(self, data):
        self.data = data
        self.nextval = None

class LinkedList:
    def __init__(self):
        self.head = None

    def printList(self):
        dummy = self.head

        while dummy is not None:
            print (dummy.data)
            dummy = dummy.nextval


list = LinkedList()
list.head = Node('cesd')

e2 = Node("Tue")
e3 = Node("Wed")

# Link first Node to second node
list.head.nextval = e2

# Link second Node to third node
e2.nextval = e3

list.printList()















