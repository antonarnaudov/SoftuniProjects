targets = list(map(int, input().split('|')))

# result = (start_index +length) / len(targets)

line = input().split('@')
while line[0] != 'Game over':
    command = line[0]

    if command == 'Shoot Left':
        start_index = int(line[1])
        length = int(line[2])
        # algoritum
        result = len(targets) - ((start_index + length) % len(targets))
        if 0 <= start_index < len(targets):
            targets[result] -= 5

    if command == 'Shoot Right':
        start_index = int(line[1])
        length = int(line[2])
        # algoritum
        result = ((start_index + length) % len(targets))
        if 0 <= start_index < len(targets):
            targets[result] -= 5

    if command == 'Reverse':
        targets.reverse()
