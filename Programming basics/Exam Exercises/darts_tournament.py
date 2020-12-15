points_start = int(input())
points_counter = points_start
moves_counter = 0
lost = False
bullseye = False
while points_counter != 0:
    target_section = input()
    if target_section == 'bullseye':
        moves_counter += 1
        bullseye = True
        break
    number_section = int(input())
    if target_section == 'number section':
        points_counter = points_counter - number_section
        moves_counter += 1
    elif target_section == 'double ring':
        number_section = number_section * 2
        points_counter = points_counter - number_section
        moves_counter += 1
    elif target_section == 'triple ring':
        number_section = number_section * 3
        points_counter = points_counter - number_section
        moves_counter += 1
    if points_counter < 0:
        lost = True
        break
if points_counter == 0:
    print(f"Congratulations! You won the game in {moves_counter} moves!")
if bullseye:
    print(f"Congratulations! You won the game with a bullseye in {moves_counter} moves!")
if lost:
    print(f"Sorry, you lost. Score difference: {abs(points_counter)}.")