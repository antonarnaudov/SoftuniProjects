product = input()
count = int(input())

coffee_price = 1.50
water_price = 1.00
coke_price = 1.40
snacks_price = 2.00


def calculate(drink, quantity):
    result = 0
    if drink == 'coffee':
        result = coffee_price * quantity
    elif drink == 'water':
        result = water_price * quantity
    elif drink == 'coke':
        result = coke_price * quantity
    elif drink == 'snacks':
        result = snacks_price * quantity
    return result


print(f'{calculate(product, count):.2f}')
