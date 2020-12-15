minutes_input = input().split(' ')

while True:
    token = input().split(' ')
    command = token[0]

    if command == 'End':
        break

    length = len(minutes_input) - 1
    if command == 'Complete':
        index = int(token[1])
        if length >= index:
            if index >= 0:
                minutes_input[index] = '0'

    elif command == 'Change':
        index = int(token[1])
        change = token[2]
        if length >= index:
            if index >= 0:
                minutes_input[index] = change
    elif command == 'Drop':
        index = int(token[1])
        if length >= index:
            if index >= 0:
                minutes_input[index] = '-1'

    if command == 'Count':
        operator = token[1]

        if operator == 'Completed':
            completed = [i for i in minutes_input if int(i) == 0]
            print(len(completed))
        elif operator == 'Incomplete':
            incomplete = [i for i in minutes_input if int(i) > 0]
            print(len(incomplete))
        elif operator == 'Dropped':
            dropped = [i for i in minutes_input if int(i) < 0]
            print(len(dropped))

incomplete = [i for i in minutes_input if int(i) > 0]
print(' '.join(incomplete), end='')
