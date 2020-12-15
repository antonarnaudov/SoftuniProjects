(rows_count, cols_count) = [int(x) for x in input().split()]

matrix = []

for _ in range(rows_count):
    lines = [x for x in input().split()]
    matrix.append(lines)

counter = 0
for rows_idx in range(rows_count - 1):
    for cols_idx in range(cols_count - 1):
        if matrix[rows_idx][cols_idx] == matrix[rows_idx][cols_idx + 1] == \
                matrix[rows_idx + 1][cols_idx] == matrix[rows_idx + 1][cols_idx + 1]:

            # print(matrix[rows_idx][cols_idx], matrix[rows_idx][cols_idx + 1], matrix[rows_idx + 1][cols_idx],
            #       matrix[rows_idx + 1][cols_idx + 1])

            counter += 1

print(counter)
