from collections import deque

q = deque()

q.append(1)
q.append(2)
q.append(3)

while q:
    print(q.popleft())  # or q.pop(0)

# DONT DO THIS!
q.appendleft(1)
q.appendleft(2)
q.appendleft(3)

while q:
    print(q.pop())  # reversed

print()
print('ROTATE')

q = deque([1, 2, 3, 4, 5, 6])
print(q
      )
q.rotate(2)
print(q)

q.rotate(-2)
print(q)

q.rotate(-2)
print(q)
