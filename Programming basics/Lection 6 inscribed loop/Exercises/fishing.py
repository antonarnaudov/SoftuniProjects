fish_count = int(input())

fish_counter = 0
money_won = 0
money_lost = 0
sum_name = 0
quote = True

while fish_count > fish_counter:
    current_money_lost = 0
    current_money_won = 0
    sum_name = 0

    fish_name = input()
    if fish_name == 'Stop':
        quote = False
        break
    fish_kg = float(input())
    fish_counter += 1

    for letters in fish_name:
        sum_name += ord(letters)

    if fish_counter % 3 == 0:
        current_money_won = sum_name / fish_kg
        money_won += current_money_won
        # print(f'money won: {money_won:.2f}')
    else:
        current_money_lost = sum_name / fish_kg
        money_lost += current_money_lost
        # print(f'money lost: {money_lost:.2f}')

if quote:
    print('Lyubo fulfilled the quota!')
if money_won > money_lost:
    print(f"Lyubo's profit from {fish_counter} fishes is {money_won - money_lost:.2f} leva.")
else:
    print(f'Lyubo lost {money_lost:.2f} leva today.')