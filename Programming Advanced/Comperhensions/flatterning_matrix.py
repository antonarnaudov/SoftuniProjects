n = int(input())
matrix = []
for _ in range(n):
    matrix.append([int(x) for x in input().split(', ')])

# fll = [num for sublist in matrix for num in sublist]
# print(fll)

flattened = []
for sublist in matrix:
    for num in sublist:
        flattened.append(num)
print(flattened)
