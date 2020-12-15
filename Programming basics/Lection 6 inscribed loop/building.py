floors = int(input())
premises = int(input())
last_floor = floors
for f in range(floors, 0, -1):
    for p in range(premises):
        if f == last_floor:
            if p == premises - 1:
                print(f'L{f}{p}')
            else:
                print(f'L{f}{p} ', end='')
        elif f % 2 == 0:
            if p == premises - 1:
                print(f'O{f}{p}')
            else:
                print(f'O{f}{p} ', end='')
        else:
            if p == premises - 1:
                print(f'A{f}{p}')
            else:
                print(f'A{f}{p} ', end='')
