(columns, rows) = [int(x) for x in input().split(', ')]
matrix = []
for _ in range(columns):
    row = [int(x) for x in input().split()]
    matrix.append(row)

for r in range(rows):
    column_sum = 0
    for c in range(columns):
        column_sum += matrix[c][r]
    print(column_sum)
