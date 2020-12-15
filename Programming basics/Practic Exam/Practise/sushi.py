from math import ceil
sushi_type = input()
kitchen_name = input()
plates_count = int(input())
delivery = input()

price = 0
not_existing = False
final_price = 0
delivery_price = 0

if kitchen_name == "Sushi Zone":
    if sushi_type == "sashimi":
        price = 4.99
    elif sushi_type == 'maki':
        price = 5.29
    elif sushi_type == "uramaki":
        price = 5.99
    elif sushi_type == "temaki":
        price = 4.29
elif kitchen_name == "Sushi Time":
    if sushi_type == "sashimi":
        price = 5.49
    elif sushi_type == 'maki':
        price = 4.69
    elif sushi_type == "uramaki":
        price = 4.49
    elif sushi_type == "temaki":
        price = 5.19
elif kitchen_name == 'Sushi Bar':
    if sushi_type == "sashimi":
        price = 5.25
    elif sushi_type == 'maki':
        price = 5.55
    elif sushi_type == "uramaki":
        price = 6.25
    elif sushi_type == "temaki":
        price = 4.75
elif kitchen_name == 'Asian Pub':
    if sushi_type == "sashimi":
        price = 4.50
    elif sushi_type == 'maki':
        price = 4.80
    elif sushi_type == "uramaki":
        price = 5.50
    elif sushi_type == "temaki":
        price = 5.50
else:
    print(f'{kitchen_name} is invalid restaurant!')
    not_existing = True

final_price = plates_count * price

if delivery == 'Y':
    delivery_price = final_price * 0.20
    final_price = ceil(final_price + delivery_price)
else:
    final_price = final_price

if not not_existing:
    print(f'Total price: {ceil(final_price)} lv.')

