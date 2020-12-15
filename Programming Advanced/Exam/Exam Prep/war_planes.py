def move(direction, distance):
    global row
    global col

    if direction == 'up':
        if row - distance >= 0 and \
                field[row - distance][col] == '.':
            field[row - distance][col] = 'p'
            field[row][col] = '.'
            row = row - distance

    elif direction == 'down':
        if row + distance < n and \
                field[row + distance][col] == '.':
            field[row + distance][col] = 'p'
            field[row][col] = '.'
            row = row + distance

    elif direction == 'left':
        if col - distance >= 0 and \
                field[row][col - distance] == '.':
            field[row][col - distance] = 'p'
            field[row][col] = '.'
            col = col - distance

    elif direction == 'right':
        if col + distance < n and \
                field[row][col + distance] == '.':
            field[row][col + distance] = 'p'
            field[row][col] = '.'
            row = row + distance


def shoot(direction, distance):
    global targets_destroyed
    global row
    global col

    if direction == 'up':
        if row - distance >= 0:
            if field[row - distance][col] == 't':
                targets_destroyed += 1
            field[row - distance][col] = 'x'

    elif direction == 'down':
        if row + distance < n:
            if field[row + distance][col] == 't':
                targets_destroyed += 1
            field[row + distance][col] = 'x'

    elif direction == 'left':
        for x in field:
            print(' '.join(x))
        print(col)
        print(distance)
        if col - distance >= 0:
            if field[row][col - distance] == 't':
                targets_destroyed += 1
            field[row][col - distance] = 'x'

    elif direction == 'right':
        if col + distance < n:
            if field[row][col + distance] == 't':
                targets_destroyed += 1
            field[row][col + distance] = 'x'


n = int(input())
field = []
row = 0
col = 0
targets_count = 0
targets_destroyed = 0

# •	"." - empty field
# •	"p" - the starting position of the plane
# •	"t" - a target that the plane wants to destroy
for _ in range(n):
    field.append([x for x in input().split()])

for r in range(n):
    for c in range(n):
        if field[r][c] == 'p':
            row = r
            col = c
            break
        if field[r][c] == 't':
            targets_count += 1

# for x in field:
#     print(' '.join(x))

commands_count = int(input())
for _ in range(commands_count):
    tokens = input().split()
    (command, operator, index) = tokens[0], tokens[1], int(tokens[2])

    if command == 'move' and index < n:
        move(operator, index)

    elif command == 'shoot' and index < n:
        shoot(operator, index)

    # print('-' * 20)
    # for x in field:
    #     print(' '.join(x))

if targets_count - targets_destroyed == 0:
    print(f'Mission accomplished! All {targets_count} targets destroyed.')
else:
    print(f'Mission failed! {targets_count - targets_destroyed} targets left.')

for x in field:
    print(' '.join(x))
