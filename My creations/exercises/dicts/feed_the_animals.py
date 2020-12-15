info = input()

animal_food = {}
areas = {}

while True:
    if info == 'Last Info':
        break
    tokens = info.split(':')
    command = tokens[0]
    name = tokens[1]
    number = int(tokens[2])
    area = tokens[3]

    if command == 'Add':
        if name in animal_food:
            animal_food[name] += number
        else:
            animal_food.update({name: number})
            if area in areas:
                areas[area] += 1

        if area not in areas:
            areas.update({area: 1})

    elif command == 'Feed':
        if name in animal_food:
            animal_food[name] -= number
            if animal_food[name] <= 0:
                animal_food.pop(name)
                print(f'{name} was successfully fed')
                areas[area] -= 1
                if areas[area] <= 0:
                    del areas[area]

    info = input()

print('Animals:')
a = sorted(animal_food.items(), key=lambda x: (-x[1], x[0]))
for (key, value) in a:
    print(f'{key} -> {value}g')

print('Areas with hungry animals:')
for key in sorted(areas, reverse=True):
    print("{} : {}".format(key, areas[key]))
# print("\n".join("{} : {}".format(k, v) for k, v in areas.items()))
