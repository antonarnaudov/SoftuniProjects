def validator(swap, r1, c1, r2, c2):
    if swap != 'swap' or int(r1) > rows_count or int(c1) > cols_count \
            or int(r2) > rows_count or int(c2) > cols_count:
        return False

    return True


(rows_count, cols_count) = [int(x) for x in input().split()]

matrix = []
for _ in range(rows_count):
    lane = [x for x in input().split()]
    matrix.append(lane)

# i[0] = swap
# i[1] = row1 | i[2] = col1
# i[3] = row2 | i[4] = col2

while True:
    com = input()
    if com == 'END':
        break
    tokens = com.split()

    if len(tokens) == 5:
        command = tokens[0]
        (row1, col1) = tokens[1], tokens[2]
        (row2, col2) = tokens[3], tokens[4]

        if not validator(command, row1, col1, row2, col2):
            print("Invalid input!")
            continue

        (row1, col1, row2, col2) = int(row1), int(col1), int(row2), int(col2)
        matrix[row1][col1], matrix[row2][col2] = matrix[row2][col2], matrix[row1][col1]

        for m in matrix:
            for i in m:
                print(i, end=' ')
            print()
    else:
        print("Invalid input!")
        continue
