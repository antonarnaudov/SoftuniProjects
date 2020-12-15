games_sold = int(input())

hearth_counter = 0
fornite_counter = 0
overwatch_counter = 0
others_counter = 0

for games in range(games_sold):
    game_name = input()
    if game_name == 'Hearthstone':
        hearth_counter += 1
    elif game_name == 'Fornite':
        fornite_counter += 1
    elif game_name == 'Overwatch':
        overwatch_counter += 1
    else:
        others_counter += 1

hearth_percent = (hearth_counter / games_sold) * 100
print(f"Hearthstone - {hearth_percent:.2f}%")

fornite_percent = (fornite_counter / games_sold) * 100
print(f"Fornite - {fornite_percent:.2f}%")

overwatch_percent = (overwatch_counter / games_sold) * 100
print(f"Overwatch - {overwatch_percent:.2f}%")

others_percent = (others_counter / games_sold) * 100
print(f"Others - {others_percent:.2f}%")