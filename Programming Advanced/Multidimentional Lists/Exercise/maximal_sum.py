(rows_count, cols_count) = [int(x) for x in input().split()]

matrix = []
best_sum = -9999999
best_matrix = []

for _ in range(rows_count):
    lines = [int(x) for x in input().split()]
    matrix.append(lines)

for row in range(rows_count - 2):  # matrix5 - 2 = matrix3

    for col in range(cols_count - 2):  # becomes matrix 3x3
        sub_matrix = []
        current_sum = 0
        rows_counter = 0

        for r in range(row, row + 3):
            sub_matrix.append([])

            for c in range(col, col + 3):
                sub_matrix[rows_counter].append(matrix[r][c])
                current_sum += matrix[r][c]

            rows_counter += 1

        if current_sum > best_sum:
            best_sum = current_sum
            best_matrix = sub_matrix

print(f'Sum = {best_sum}')
for row in best_matrix:
    print(' '.join([str(x) for x in row]))
