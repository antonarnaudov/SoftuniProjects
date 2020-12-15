frogs = input().split(' ')

while True:
    token = input().split(' ')
    length = len(frogs) - 1
    command = token[0]
    if command == 'Join':
        name = token[1]
        frogs.append(name)

    elif command == 'Jump':
        name = token[1]
        index = int(token[2])
        if length >= index:
            if index >= 0:
                frogs.insert(index, name)

    elif command == 'Dive':
        index = int(token[1])
        if length >= index:
            if index >= 0:
                frogs.pop(index)

    elif command == 'First':
        count = int(token[1])
        if length <= count:

            print(' '.join(frogs))
        else:
            print(' '.join(frogs[0:count]))

    elif command == 'Last':
        count = int(token[1])
        if length <= count:
            print(' '.join(frogs))
        else:
            print(' '.join(frogs[-count:]))

    elif command == 'Print':
        operator = token[1]
        if operator == 'Normal':
            print(f"Frogs: {' '.join(frogs)}")
            break
        if operator == 'Reversed':
            print(f"Frogs: {' '.join(reversed(frogs))}")
            break
