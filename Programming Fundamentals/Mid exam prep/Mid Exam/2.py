def urgent_command(item, initial_list):
    if item not in initial_list:
        initial_list.insert(0, item)
    return initial_list


def unnecessary_command(item, initial_list):
    if item in initial_list:
        initial_list.remove(item)
    return initial_list


def correct_command(old, new, initial_list):
    if old in initial_list:
        old_index = initial_list.index(old)
        initial_list[old_index] = new
    return initial_list


def rearange_command(item, initial_list):
    if item in initial_list:
        initial_list.remove(item)
        initial_list.append(item)


initial_list = input().split('!')

while True:
    token = input().split(' ')
    command = token[0]
    if command == 'Go':
        sub_command = token[1]
        if sub_command == 'Shopping!':
            break
    else:
        if command == 'Urgent':
            item = token[1]
            urgent_command(item, initial_list)
        elif command == 'Unnecessary':
            item = token[1]
            unnecessary_command(item, initial_list)
        elif command == 'Correct':
            old_item = token[1]
            new_item = token[2]
            correct_command(old_item, new_item, initial_list)
        elif command == 'Rearrange':
            item = token[1]
            rearange_command(item, initial_list)

uniques = []
for i in initial_list:
    if i not in uniques:
        uniques.append(i)

print(', '.join(uniques))
