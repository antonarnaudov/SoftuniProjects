budget = float(input())
statists_count = int(input())
clothes_price = float(input())

dekor = budget * 0.10

if statists_count > 150:
    clothes_price = clothes_price * 0.90

cloathes_budget = statists_count * clothes_price
expenses = dekor + cloathes_budget
money_left = abs(budget - expenses)

if expenses > budget:
    print('Not enough money!')
    print(f'Wingard needs {money_left:.2f} leva more.')
elif expenses <= budget:
    print('Action!')
    print(f"Wingard starts filming with {money_left:.2f} leva left.")