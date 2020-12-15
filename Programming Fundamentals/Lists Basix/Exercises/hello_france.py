info_list = input().split('|')
budget = int(input())

money_needed = 150
money_earned = 0
profit = 0
prices = 0
# non exceedable price list
max_price_dict = {
    'Clothes': 50.00,
    'Shoes': 35.00,
    'Accessories': 20.50,
}
# HOW TO USE
# price_dict['Clothes'] * amount
new_price_list = []

for i in info_list:
    info = i.split('->')
    product = info[0]
    price = float(info[1])

    if product == 'Clothes':
        if price <= max_price_dict['Clothes']:
            if budget >= price:
                budget -= price
                prices += price
                money_earned += price + price * 0.4
                new_price_list.append(f'{price + price * 0.4:.2f}')

    elif product == 'Shoes':
        if price <= max_price_dict['Shoes']:
            if budget >= price:
                budget -= price
                prices += price
                money_earned += price + price * 0.4
                new_price_list.append(f'{price + price * 0.4:.2f}')

    elif product == 'Accessories':
        if price <= max_price_dict['Accessories']:
            if budget >= price:
                budget -= price
                prices += price
                money_earned += price + price * 0.4
                new_price_list.append(f'{price + price * 0.4:.2f}')

profit = abs(prices - money_earned)
money_earned += budget

print(*new_price_list, sep=" ")
# print(' '.join(new_price_list))
print(f'Profit: {profit:.2f}')
if money_earned >= money_needed:
    print('Hello, France!')
else:
    print('Time to go.')
