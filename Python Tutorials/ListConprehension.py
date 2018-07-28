a = [1, 2, 3, 4, 5, 6, 7, 8]
x = [i for i in range(10) if i % 2 == 0]
print(x)


y = [i for i in a if i % 2 == 0]
print(y)

z = [i for i in a if i  > 5]
print(z)



a = frozenset([1,23,234,324,23])
print(a)


from collections import deque
q = deque(range(50))
q.append(1)
q.appendleft(99999)

q.pop()
q.rotate(30)

print(q)
