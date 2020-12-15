paintings_numbers = input().split(' ')

while True:
    token = input().split(' ')
    command = token[0]
    if command == 'END':
        break

    if command == 'Change':
        number = token[1]
        new_number = token[2]
        index = 0
        if number in paintings_numbers:
            for i in paintings_numbers:
                if i == number:
                    paintings_numbers[index] = new_number
                    break
                else:
                    index += 1
    elif command == 'Hide':
        number = token[1]
        if number in paintings_numbers:
            paintings_numbers.remove(number)
    elif command == 'Switch':
        number = token[1]
        number_two = token[2]
        if number in paintings_numbers and number_two in paintings_numbers:
            index = 0
            index_two = 0
            for i in paintings_numbers:
                if i == number:
                    break
                else:
                    index += 1
            for i in paintings_numbers:
                if i == number_two:
                    break
                else:
                    index_two += 1
            if index < index_two:
                paintings_numbers[index], paintings_numbers[index_two] = paintings_numbers[index_two], \
                                                                         paintings_numbers[index]
            elif index > index_two:
                paintings_numbers[index_two], paintings_numbers[index] = paintings_numbers[index], paintings_numbers[
                    index_two]
    elif command == 'Insert':
        place = int(token[1]) + 1
        number = token[2]
        length = len(paintings_numbers) - 1
        if 0 < place <= length:
            paintings_numbers.insert(place, number)
    elif command == 'Reverse':
        paintings_numbers.reverse()

print(' '.join(paintings_numbers))
