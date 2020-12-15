words = input().split('|')

while True:
    tokens = input().split(' ')
    command = tokens[0]
    if command == 'Done':
        break

    if command == 'Move':
        command = tokens[1]
        index = int(tokens[2])
        if command == 'Left':
            if 0 < index < len(words):
                words.insert(index - 1, words.pop(index))
        if command == 'Right':
            length = len(words) - 1
            if 0 <= index < length:
                words.insert(index + 1, words.pop(index))

    elif command == 'Check':
        command = tokens[1]
        if command == 'Even':
            counter = 0
            for word in words:
                if counter % 2 == 0:
                    print(word, end=' ')
                counter += 1
        elif command == 'Odd':
            counter = 0
            for word in words:
                if counter % 2 != 0:
                    print(word, end=' ')
                counter += 1

print(f'\nYou crafted {"".join(words)}!')
