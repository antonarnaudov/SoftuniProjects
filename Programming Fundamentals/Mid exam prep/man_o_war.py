pirate_ship = list(map(int, input().split('>')))
warship = list(map(int, input().split('>')))
max_health = int(input())


def is_valid(index, limit):
    return 0 <= index < limit


game_over = False

line = input().split()
while line[0] != 'Retire' and game_over != True:
    command = line[0]
    if command == 'Fire':
        index = int(line[1])
        damage = int(line[2])
        if is_valid(index, len(warship)):
            warship[index] -= damage
        if warship[index] <= 0:
            print('You won! The enemy ship has sunken.')
            game_over = True
            break
    elif command == 'Defend':
        start_index = int(line[1])
        end_index = int(line[2])
        damage = int(line[3])
        both_are_valid = all([is_valid(start_index, len(pirate_ship)), is_valid(end_index, len(pirate_ship))])
        if both_are_valid:
            for i in range(start_index, end_index + 1):
                pirate_ship[i] -= damage
                if pirate_ship[i] <= 0:
                    print('You lost! The pirate ship has sunken.')
                    game_over = True

    elif command == 'Repair':
        index = int(line[1])
        hp = int(line[2])
        if is_valid(index, len(pirate_ship)):
            pirate_ship[index] += hp
            if pirate_ship[index] > max_health:
                pirate_ship[index] = max_health

    else:
        counter = 0
        for sector in pirate_ship:
            if sector < max_health * 0.2:
                counter += 1
        print(f'{counter} sections need repair.')

    line = input().split()

if not game_over:
    print(f'Pirate ship status: {sum(pirate_ship)}')
    print(f'Warship status: {sum(warship)}')
