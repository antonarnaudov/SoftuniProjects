from math import floor
lemons_kg = float(input())
sugar_kg = float(input())
water_liter = float(input())

# juice_quantity = 0
# lemonade_quantity_sum = 0
# cups_sold = 0
# money_income = 0
one_cup_price = 1.20
kg_to_ml_lemon_juice = 980

juice_quantity = lemons_kg * kg_to_ml_lemon_juice
lemonade_quantity_sum = juice_quantity + water_liter * 1000 + (0.3 * sugar_kg)
cups_sold = floor(lemonade_quantity_sum / 150)
money_income = cups_sold * one_cup_price

print(f'All cups sold: {cups_sold}')
print(f'Money earned: {money_income:.2f}')