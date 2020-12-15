from collections import deque

num = int(input())
pumps = deque()

for _ in range(num):
    info = [int(x) for x in input().split()]
    pumps.append(info)

for i in range(num):
    is_valid = True
    fuel = 0

    for _ in range(num):
        current = pumps.popleft()
        fuel += current[0] - current[1]
        if fuel < 0:
            is_valid = False
        pumps.append(current)

    if is_valid:
        print(i)
        break