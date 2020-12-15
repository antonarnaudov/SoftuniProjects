shopping_list = input().split('!')

while True:
    token = input().split(' ')
    command = token[0]
    if command == 'Go':
        command = token[1]
        if command == 'Shopping!':
            break

    elif command == 'Urgent':
        item = token[1]
        if item not in shopping_list:
            shopping_list.insert(0, item)

    elif command == 'Unnecessary':
        item = token[1]
        counter = 0
        if item in shopping_list:
            for i in shopping_list:
                if i == item:
                    shopping_list.pop(counter)
                else:
                    counter += 1

    elif command == 'Correct':
        old_item = token[1]
        new_item = token[2]
        if old_item in shopping_list:
            counter = 0
            for i in shopping_list:
                if i == old_item:
                    shopping_list[counter] = new_item
                else:
                    counter += 1

    elif command == 'Rearrange':
        item = token[1]
        if item in shopping_list:
            counter = 0
            if item in shopping_list:
                for i in shopping_list:
                    if i == item:
                        shopping_list.append(shopping_list.pop(counter))
                    else:
                        counter += 1

print(', '.join(shopping_list))
