cards = input().split()

team_a = [1] * 11
team_b = [1] * 11

for card in cards:
    tokens = card.split("-")
    team = tokens[0]
    player = int(tokens[1])

    if team == 'A':
        team_a[player - 1] = 0
    else:
        team_b[player - 1] = 0

team_a_count = sum(team_a)
team_b_count = sum(team_b)
if team_a_count >= 7 and team_b_count >= 7:
    print(f'Team A - {team_a_count}; Team B - {team_b_count}')
else:
    print(f'Team A - {team_a_count}; Team B - {team_b_count}')
    print('Game was terminated')
