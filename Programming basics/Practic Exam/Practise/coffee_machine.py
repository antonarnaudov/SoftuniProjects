# input
drink_type = input()
sugar = input()
drinks_count = int(input())

drink_price = 0

if drink_type == 'Espresso':
    if sugar == 'Without':
        drink_price = 0.90
    elif sugar == 'Normal':
        drink_price = 1
    elif sugar == 'Extra':
        drink_price = 1.20
elif drink_type == 'Cappuccino':
    if sugar == 'Without':
        drink_price = 1
    elif sugar == 'Normal':
        drink_price = 1.20
    elif sugar == 'Extra':
        drink_price = 1.60
elif drink_type == 'Tea':
    if sugar == 'Without':
        drink_price = 0.50
    elif sugar == 'Normal':
        drink_price = 0.60
    elif sugar == 'Extra':
        drink_price = 0.70

final_price = drinks_count * drink_price

if sugar == 'Without':
    discount = final_price * 0.35
    final_price -= discount

if drink_type == 'Espresso':
    if drinks_count > 5:
        discount = final_price * 0.25
        final_price -= discount

if final_price > 15:
    discount = final_price * 0.20
    final_price -= discount

print(f'You bought {drinks_count} cups of {drink_type} for {final_price:.2f} lv.')