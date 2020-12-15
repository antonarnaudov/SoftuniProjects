(rows, columns) = [int(x) for x in input().split(', ')]
matrix = []
for _ in range(rows):
    row = [int(x) for x in input().split(', ')]
    matrix.append(row)

summary = 0
for row in matrix:
    summary += sum(row)

print(summary)
print(matrix)

summary2 = sum(sum(row) for row in matrix)
print(summary2)