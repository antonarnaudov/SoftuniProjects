def sum_primary_diagonal(size_matrix, matrix_prim):
    primary_diagonal_sum = 0
    for row in range(size_matrix):
        col = row
        primary_diagonal_sum += matrix_prim[row][col]

    return primary_diagonal_sum


def sum_secondary_diagonal(size_matrix, matrix_sec):
    secondary_diagonal_sum = 0
    for row in range(size_matrix):
        col = size_matrix - row - 1
        secondary_diagonal_sum += matrix_sec[row][col]

    return secondary_diagonal_sum


n = int(input())
matrix = []

for _ in range(n):
    line = [int(x) for x in input().split()]
    matrix.append(line)

difference = abs(sum_primary_diagonal(n, matrix) - sum_secondary_diagonal(n, matrix))
print(difference)
