budget = float(input())
floor_price = float(input())
eggs_price = floor_price * 0.75
milk_litter_price = floor_price * 1.25
milk_price = milk_litter_price / 4

colored_eggs_price = 0
colored_eggs_count = 0
cozunac_count = 0

cozunac_price = eggs_price + milk_price + floor_price

while budget >= cozunac_price:
    cozunac_count += 1
    colored_eggs_count += 3

    if cozunac_count % 3 == 0:
        colored_eggs_count -= cozunac_count - 2

    budget -= cozunac_price
print(f'You made {cozunac_count} cozonacs! Now you '
      f'have {colored_eggs_count} eggs and {budget:.2f}BGN left.')