prices = {}
quantities = {}
while True:
    tokens = input()
    if tokens == 'buy':
        break
    else:
        tokens = tokens.split(" ")
        product = tokens[0]
        price = float(tokens[1])
        quantity = int(tokens[2])

    prices[product] = price

    if product not in quantities:
        quantities[product] = quantity
    else:
        quantities[product] += quantity

for keys in quantities.keys():
    result = quantities[keys] * prices[keys]
    print(f'{keys} -> {result:.2f}')
