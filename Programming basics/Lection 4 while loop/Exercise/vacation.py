vacation_cost = float(input())
available_money = float(input())

spending_counter = 0
days_passed = 0
saved = True

while available_money < vacation_cost:
    #spend or save
    action_type = input()
    current_sum = float(input())
    days_passed += 1
    if action_type == 'spend':
        spending_counter += 1
        available_money -= current_sum
        if available_money < 0:
            available_money = 0
    elif action_type == 'save':
        available_money += current_sum
    if spending_counter == 5:
        print("You can't save the money.")
        print(days_passed)
        saved = False
        break

if saved:
    print(f'You saved the money for {days_passed} days.')