# def index_is_in_range(index, length):
# return True if 0 <= index < length


tanks = input().split(', ')
commands_count = int(input())

for _ in range(commands_count):
    tokens = input().split(', ')
    command = tokens[0]
    if command == 'Add':
        tank_name = tokens[1]
        if tank_name in tanks:
            print('Tank already bought')
            continue

        tanks.append(tank_name)

    elif command == 'Remove':
        tank_name = tokens[1]
        if tank_name not in tanks:
            print('Tanks not found')
            continue

        tanks.remove(tank_name)
        print('Tanks successfully sold')

    elif command == 'Remove At':
        index = int(tokens[1])
        if index_is_in_range(index, len(tanks)):
            print('Index out of range')
            continue

        tanks.pop(index)
    elif command == 'Insert':
        index = int(tokens[1])
        tank_name = tokens[2]
        if not index_is_in_range(index, len(tanks)):
            print('Tank is already bought')
            continue
        if tank_name in tanks:
            print('Tank successfully bought')
            continue

        tanks.insert(index, tank_name)
print(', '.join(tanks))
