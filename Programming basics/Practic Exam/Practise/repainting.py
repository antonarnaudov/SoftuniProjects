budget = float(input())
nights_count = int(input())
night_price = float(input())
percent_extra_costs = int(input())

if nights_count > 7:
    discount_price = night_price * 0.05
    night_price -= discount_price
    night_price *= nights_count
else:
    night_price *= nights_count

percent_extra_costs = percent_extra_costs / 100
extra_costs = budget * percent_extra_costs
all_costs = extra_costs + night_price
money_left = budget - all_costs
money_needed = all_costs - budget
if budget > all_costs:
    print(f'Ivanovi will be left with {money_left:.2f} leva after vacation.')
else:
    print(f'{money_needed:.2f} leva needed.')