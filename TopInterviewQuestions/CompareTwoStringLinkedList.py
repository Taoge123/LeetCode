class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def compare(list1, list2):

    while (list1 and list2 and list1.data == list2.data):
        list1 = list1.next
        list2 = list2.next

    if (list1 and list2):
        return 1 if list1.data > list2.data else -1
    if (list1 and not list2):
        return 1
    if (not list1 and list2):
        return -1

    return 0


list1 = Node('g')
list1.next = Node('e')
list1.next.next = Node('e')
list1.next.next.next = Node('k')
list1.next.next.next.next = Node('s')
list1.next.next.next.next.next = Node('b')

list2 = Node('g')
list2.next = Node('e')
list2.next.next = Node('e')
list2.next.next.next = Node('k')
list2.next.next.next.next = Node('s')
list2.next.next.next.next.next = Node('a')

print(compare(list1, list2))

