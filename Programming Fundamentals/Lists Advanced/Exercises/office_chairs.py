counter = int(input())
free = 0
game_on = True
for i in range(1, counter + 1):
    needed = 0
    info = input().split(' ')
    chairs = len(info[0])
    taken = int(info[1])
    if chairs - taken >= 0:
        free += chairs - taken
    else:
        game_on = False
        needed = abs(taken - chairs)
        print(f'{needed} more chairs needed in room {i}')

if game_on:
    print(f'Game On, {free} free chairs left')
