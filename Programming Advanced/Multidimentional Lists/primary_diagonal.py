size = int(input())
matrix = []
for _ in range(size):
    r = [int(x) for x in input().split()]
    matrix.append(r)


def sum_primary_diagonal(size_matrix, matrix_prim):
    primary_diagonal_sum = 0
    for i in range(size_matrix):
        primary_diagonal_sum += matrix_prim[i][i]

    return primary_diagonal_sum


def sum_secondary_diagonal(size_matrix, matrix_sec):
    secondary_diagonal_sum = 0
    for i in range(size_matrix):
        secondary_diagonal_sum += matrix_sec[i][size_matrix - i - 1]

    return secondary_diagonal_sum


def below_the_primary_diagonal_sum(size_matrix, matrix_bel):
    bellow_prim_sum = 0
    for row in range(size_matrix):
        for col in range(size_matrix):
            if row == col:
                break

            bellow_prim_sum += matrix_bel[row][col]
    return bellow_prim_sum


def below_the_secondary_diagonal_sum(size_matrix, matrix_bel):
    bellow_sec_sum = 0
    for row in range(size_matrix):
        for col in range(size_matrix - row - 1, size_matrix):
            if row == col:
                break

            bellow_sec_sum += matrix_bel[row][col]

    return bellow_sec_sum


print(sum_primary_diagonal(size, matrix))
print(sum_secondary_diagonal(size, matrix))
print(below_the_primary_diagonal_sum(size, matrix))
print(below_the_secondary_diagonal_sum(size, matrix))