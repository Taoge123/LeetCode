import random

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:

    def __init__(self):
        self.head = None

    def printRandom(self):

        if self.head is None:
            return

        random.seed()

        result = self.head.data

        #Iterate from (k+1)th element to nth element
        current = self.head
        n = 2

        while (current is not None):

            #change result with prob = 1/n
            if (random.randrange(n) == 0):

                result = current.data

            #Move to next mode
            current = current.next
            n += 1

        print("Randomly selected key is %d" % (result))

    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    # Utility function to print the linked LinkedList
    def printList(self):
        temp = self.head
        while (temp):
            print(temp.data)
            temp = temp.next


# Driver program to test above function
llist = LinkedList()
llist.push(5)
llist.push(20)
llist.push(4)
llist.push(3)
llist.push(30)
llist.printRandom()



