with open('text.txt', 'r') as file:
    lines = [line for line in file.readlines()]

    for line in range(len(lines)):
        words = 0
        punctuation = 0

        for letter in lines[line]:
            if letter.isalpha():
                words += 1
            elif letter != ' ' and letter != '\n':
                punctuation += 1

        print(f'Line {line + 1}: {lines[line]} ({words})({punctuation})')
