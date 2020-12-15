decoration_budget = int(input())

sum_name = 0
money_left = 0
not_enough_money = False

item_name = input()
while item_name != 'Stop':
    for letters in item_name:
        sum_name += ord(letters)
    if decoration_budget > sum_name:
        decoration_budget = decoration_budget - sum_name
        print('Item successfully purchased!')
        sum_name = 0
    if decoration_budget < sum_name:
        not_enough_money = True
        break
    item_name = input()
if not_enough_money:
    print('Not enough money!')
else:
    print(f'Money left: {decoration_budget}')
