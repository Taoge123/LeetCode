from heapq import *
from random import shuffle
data = range(10)

shuffle(data)
heap = []

for i in data:
    heappush(heap, i)

print(heap)

heappush(heap, 0.5)
print(heap)

heap = [5, 8, 0, 3, 6, 7, 9, 1, 4, 2]
heapify(heap)
print(heap)


heapreplace(heap, 0.5)
