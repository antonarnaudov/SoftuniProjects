a = [int(x) for x in input().split(', ')]
rows = a[0]
columns = a[1]

matrix = []
for _ in range(rows):
    row = [int(x) for x in input().split(', ')]
    matrix.append(row)


def get_submatrix_sum(matrix_in, r, c):
    return matrix_in[r][c] + matrix_in[r][c + 1] + \
           matrix_in[r + 1][c] + matrix_in[r + 1][c + 1]


def print_sum_matrix(matrix_in, row_in, col_in):
    for r in range(row_in, row_in + 2):
        for c in range(col_in, col_in + 2):
            print(matrix_in[r][c], end=" ")
        print()


best_position = (0, 0)
best_value = get_submatrix_sum(matrix, 0, 0)

for row in range(len(matrix) - 1):
    for col in range(len(matrix[row]) - 1):
        current_value = get_submatrix_sum(matrix, row, col)
        if best_value < current_value:
            best_value = current_value
            best_position = (row, col)

(best_row, best_col) = best_position
print_sum_matrix(matrix, best_row, best_col)
print(best_value)

# print(best_position)
