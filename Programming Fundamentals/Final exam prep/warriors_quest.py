text = input()

while True:
    command = input()
    if command == 'For Azeroth':
        break
    elif command == 'GladiatorStance':
        text = text.upper()
        print(text)
        continue
    elif command == "DefensiveStance":
        text = text.lower()
        print(text)
        continue

    tokens = command.split()
    if tokens[0] == 'Dispel':
        index = int(tokens[1])
        letter = tokens[2]

        if 0 <= index < len(text):
            text = list(text)
            text[index] = letter
            text = ''.join(text)
            print('Success!')
        else:
            print('Dispel too weak.')

    elif tokens[1] == 'Change':
        substring = tokens[2]
        second_substring = tokens[3]
        text = text.replace(substring, second_substring)
        print(text)
    elif tokens[1] == 'Remove':
        subtracting = tokens[2]
        text = text.replace(subtracting, '')
        print(text)
    else:
        print("Command doesn't exist!")
