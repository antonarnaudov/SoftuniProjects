width_cake = int(input())
length_cake = int(input())
cake_size = width_cake * length_cake
pieces_counter = 0
pieces_left = 0
while cake_size > pieces_counter:
    pieces_taken = input()
    if pieces_taken == 'STOP':
        pieces_left = abs(cake_size - pieces_counter)
        print(f'{pieces_left} pieces are left.')
        break
    pieces_taken = int(pieces_taken)
    pieces_counter += pieces_taken
if pieces_counter >= cake_size:
    pieces_left = abs(cake_size - pieces_counter)
    print(f'No more cake left! You need {pieces_left} pieces more.')
