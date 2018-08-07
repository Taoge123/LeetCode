class LinkedList:
    def __init__(self):
        self.head = None

    class Node:
        def __init__(self, data):
            self.data = data
            self.next = None

    def push(self, new_data):
        new_node = self.Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def merge(self, q):
        p_curr = self.head
        q_curr = q.head

        #WHile there are aviaalbel positions in p
        while p_curr != None and q_curr != None:

            """1 2 3 
               4 5 6 7 8 
               -------------- becoming 
               1 4 2 5 3 6 
               7 8
            """

            """
               p_curr  p_next
               q_curr  q_next
            
            """

            #Save next pointers, then later on we can move forward paralally
            p_next = p_curr.next
            q_next = q_curr.next

            #Make q_curr as nnext of p_curr * 1 -> 4 and 4 -> 2, then p_curr = 2 and q_curr = 5
            q_curr.next = p_curr.next
            p_curr.next = q_curr.next

            p_curr = p_next
            q_curr = q_next

        q.head = q_curr

    def printList(self):

        temp = self.head
        while temp != None:
            print(str(temp.data))
            temp = temp.next
        print('')


llist1 = LinkedList()
llist2 = LinkedList()
llist1.push(3)
llist1.push(2)
llist1.push(1)

print("First Linked List:")
llist1.printList()

llist2.push(8)
llist2.push(7)
llist2.push(6)
llist2.push(5)
llist2.push(4)

print("Second Linked List:")

llist2.printList()
llist1.merge(llist2)

print("Modified first linked list:")
llist1.printList()

print("Modified second linked list:")
llist2.printList()










