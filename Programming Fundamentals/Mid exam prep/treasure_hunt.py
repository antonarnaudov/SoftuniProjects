treasure_chest = input().split('|')

while True:
    tokens = input().split(' ')
    command = tokens[0]
    if command == 'Yohoho!':
        break

    if command == 'Loot':
        for item in tokens[1::]:
            if item not in treasure_chest:
                treasure_chest.insert(0, item)

    elif command == 'Drop':
        index = int(tokens[1])
        if 0 <= index < len(treasure_chest):
            treasure_chest.append(treasure_chest.pop(index))

    elif command == 'Steal':
        count_stolen = int(tokens[1])
        stolen_items = []
        if count_stolen > len(treasure_chest):
            for _ in range(count_stolen):
                stolen_items = treasure_chest[-count_stolen::]
                for i in range(count_stolen):
                    treasure_chest.pop()
        else:
            stolen_items = treasure_chest.copy()
            treasure_chest.clear()
        print(', '.join(stolen_items))

if treasure_chest:
    average_sum = 0
    for item in treasure_chest:
        average_sum += len(item)
    print(f'Average treasure gain: {average_sum/len(treasure_chest):.2f} pirate credits.')
else:
    print('Failed treasure hunt.')
