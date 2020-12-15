friends_list = input().split(', ')

while True:
    tokens = input().split(' ')
    command = tokens[0]
    if command == 'Report':
        break

    elif command == 'Blacklist':
        name = tokens[1]
        if name in friends_list:
            counter = 0
            for i in friends_list:
                if i == name:
                    friends_list[counter] = 'Blacklisted'
                    print(f'{name} was blacklisted.')
                    break
                else:
                    counter += 1
        else:
            print(f'{name} was not found.')

    elif command == 'Error':
        index = int(tokens[1])
        if 0 <= index < len(friends_list):
            if friends_list[index] != 'Blacklisted' and friends_list[index] != 'Lost':
                name = friends_list[index]
                friends_list[index] = 'Lost'
                print(f'{name} was lost due to an error.')

    elif command == 'Change':
        index = int(tokens[1])
        new_name = tokens[2]
        if 0 <= index < len(friends_list):
            name = friends_list[index]
            friends_list[index] = new_name
            print(f'{name} changed his username to {new_name}.')

blacklisted = 0
lost = 0
for i in friends_list:
    if i == 'Blacklisted':
        blacklisted += 1
    elif i == 'Lost':
        lost += 1
print(f'Blacklisted names: {blacklisted} ')
print(f'Lost names: {lost} ')
print(' '.join(friends_list))

