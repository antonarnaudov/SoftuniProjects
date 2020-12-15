from collections import deque

rows, cols = [int(x) for x in input().split()]
text = deque(input())
matrix = []

for r in range(rows):
    matrix.append([])
    for c in range(cols):
        matrix[r].append('')

for r in range(rows):
    for c in range(cols):
        for t in text:
            matrix[r][c] = t
            text.append(text.popleft())
            break

    if r == 0 or r % 2 == 0:
        print(''.join(matrix[r]))
        continue

    matrix[r].reverse()
    print(''.join(matrix[r]))
