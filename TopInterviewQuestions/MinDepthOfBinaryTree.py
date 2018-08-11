class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def minDepth(root):

    if root is None:
        return 0

    if root.left is None and root.right is None:
        return 1

    #If left is None then we recur for the right
    if root.left is None:
        return minDepth(root.right) + 1

    #If right is None then we recur for the left
    if root.right is None:
        return minDepth(root.left) + 1

    return min(minDepth(root.left), minDepth(root.right)) + 1

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
print(minDepth(root))



#Method 2 by using BFS
def minDepth(root):

    if root is None:
        return 0

    q = []

    #Enqueue root and initialize depth as 1
    q.append({'node' : root, 'depth' : 1})

    while (len(q) > 0):
        queueItem = q.pop(0)

        #Get details of the removed item
        node = queueItem['node']
        depth = queueItem['depth']

        #If this is the first leaf node seen so far then return its depth as answer
        if node.left is None and node.right is None:
            return depth

        #IF left subtree is not None, add it to queue
        if node.left is not None:
            q.append({'node' : node.left, 'depth' : depth+1})

        if node.right is not None:
            q.append({'node' : node.right, 'depth' : depth + 1})


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
print(" -- ")
print(minDepth(root))




