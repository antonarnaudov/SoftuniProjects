def diagonal_prim(matrix, size):
    prim = []
    prim_sum = 0
    for i in range(size):
        prim.append(str(matrix[i][i]))
        prim_sum += matrix[i][i]
    print(f"First diagonal: {', '.join(prim)}. Sum: {prim_sum}")


def diagonal_sec(matrix, size):
    sec = []
    sec_sum = 0
    for i in range(size):
        sec.append(str(matrix[i][size - i - 1]))
        sec_sum += matrix[i][size - i - 1]
    print(f"Second diagonal: {', '.join(sec)}. Sum: {sec_sum}")


matrix = []
n = int(input())
for _ in range(n):
    matrix.append([int(x) for x in input().split(', ')])

diagonal_prim(matrix, n)
diagonal_sec(matrix, n)
