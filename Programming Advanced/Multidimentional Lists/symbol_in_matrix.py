size = int(input())
matrix = []

for _ in range(size):
    #     matrix += [input()]
    matrix += input()
symbol = input()


#
# found = False
#
# for row in range(size):
#     for col in range(size):
#         if matrix[row][col] == symbol:
#             print((row, col))
#             found = True
#
# if not found:
#     print(f'{symbol} does not occur in the matrix')

# def find_symbol(matrix, symbol):
#     n = len(matrix)
#     for row in range(n):
#         for col in range(n):
#             if matrix[row][col] == symbol:
#                 return(row, col)
#     return None

def find_symbol(words, symbol):
    for i in range(len(words)):
        word = words[i]
        if symbol == word:
            return (i, word.index(symbol))
    return None


result = find_symbol(matrix, symbol)

if result:
    (row, col) = result
    print(f"({row}, {col})")
else:
    print(f"{symbol} does not occur in the matrix")
