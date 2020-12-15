from math import floor
ship_width = float(input())
ship_length = float(input())
ship_height = float(input())
astronauts_height = float(input())

spaceship_volume = ship_width * ship_length * ship_height
room_volume = (astronauts_height + 0.40) * 2 * 2
free_space = floor(spaceship_volume / room_volume)

if 3 < free_space < 10:
    print(f'The spacecraft holds {free_space} astronauts.')
elif free_space < 3:
    print('The spacecraft is too small.')
elif free_space > 10:
    print("The spacecraft is too big.")