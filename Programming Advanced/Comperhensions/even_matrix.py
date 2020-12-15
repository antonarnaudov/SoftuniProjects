n = int(input())
matrix = []

for _ in range(n):
    matrix.append([int(x) for x in input().split(', ') if int(x) % 2 == 0])

# r = 0
# for row in matrix:
#     for col in row:
#         if col % 2 != 0:
#             matrix[r].remove(col)
#     r += 1

print(matrix)
