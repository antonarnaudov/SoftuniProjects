from math import floor
player_name = input()
games_played = int(input())

# 'volleyball'0.07 | 'tennis'0.05 | 'badminton'0.02
volleyball_points = 0
tennis_points = 0
badminton_points = 0

volley_games = 0
tennis_games = 0
badminton_games = 0

volleyball_sum = 0
tennis_sum = 0
badminton_sum = 0

average_volleyball_points = 0
average_tennis_points = 0
average_badminton_points = 0

points_sum = 0

for games in range(games_played):
    current_game = input()
    points_count = int(input())
    if current_game == 'volleyball':
        volleyball_points = points_count + 0.07 * points_count
        volleyball_sum += volleyball_points
        volley_games += 1

    if current_game == 'tennis':
        tennis_points = points_count + 0.05 * points_count
        tennis_sum += tennis_points
        tennis_games += 1

    if current_game == 'badminton':
        badminton_points = points_count + 0.02 * points_count
        badminton_sum += badminton_points
        badminton_games += 1

average_volleyball_points = floor(volleyball_sum / volley_games)
average_tennis_points = floor(tennis_sum / tennis_games)
average_badminton_points = floor(badminton_sum / badminton_games)

points_sum = floor(volleyball_sum + tennis_sum + badminton_sum)

if average_volleyball_points >= 75 and average_badminton_points >= 75 and average_tennis_points >= 75:
    print(f"Congratulations, {player_name}! You won the cruise games with {points_sum} points.")
else:
    print(f"Sorry, {player_name}, you lost. Your points are only {points_sum}.")