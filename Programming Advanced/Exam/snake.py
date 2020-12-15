def snake_pos_is_valid(pos):
    return 0 <= pos[0] < n and 0 <= pos[1] < n


def burrow():
    pass


def get_burrow(matrix, n):
    burrows = []
    for r in range(n):
        for c in range(n):
            if matrix[r][c] == 'B':
                burrows.append((r, c))
    return burrows[0], burrows[1]


def change_pos_trough_burrow(matrix, n, burrow_one, burrow_two, current_pos):
    if current_pos == burrow_one:
        matrix[burrow_one[0]][burrow_one[1]] = '.'
        return (burrow_two[0], burrow_two[1])
    elif (current_pos) == (burrow_two):
        matrix[burrow_two[0]][burrow_two[1]] = '.'
        return (burrow_one[0], burrow_one[1])


n = int(input())
matrix = []

for _ in range(n):
    matrix.append([x for x in list(input())])
snake_pos = [0, 0]
max_food = 0
for row in range(n):
    for col in range(n):
        if matrix[row][col] == 'S':
            snake_pos = [row, col]
        if matrix[row][col] == '*'
            max_food += 1

# food = *
# when snake moves it leaves a trail .
# empty pos = -
# lair = B

directions = {
    "up": (-1, 0),
    "right": (0, 1),
    "down": (1, 0),
    "left": (0, -1)
}
food = 0

while food < 10:
    move = input()

    snake_pos += directions[move]

    if not snake_pos_is_valid(snake_pos):
        print(f'Game over!')
        matrix[snake_pos[0]][snake_pos[1]] = '.'
        break

    if snake_pos == '':