wagons_n = int(input())
train = [0] * wagons_n

while True:
    command = input()
    if command == 'End':
        break
    tokens = command.split(' ')
    instructions = tokens[0]

    if instructions == 'add':
        people = int(tokens[1])
        train[-1] += people

    elif instructions == 'insert':
        wagon = int(tokens[1])
        people = int(tokens[2])
        train[wagon] += people

    elif instructions == 'leave':
        wagon = int(tokens[1])
        people = int(tokens[2])
        train[wagon] -= people
        if train[wagon] < 0:
            train[wagon] = 0
print(train)
