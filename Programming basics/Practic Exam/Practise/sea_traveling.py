food_money = float(input())
items_money = float(input())
hotel_money = float(input())

fuel_price = 1.85
fuel_money = 420 / 100 * 7

fuel_money_needed = fuel_money * fuel_price

staying_price = 3 * food_money + 3 * items_money

first_day = hotel_money * 0.9
second_day = hotel_money * 0.85
third_day = hotel_money * 0.8

all_sum = fuel_money_needed + staying_price + first_day + second_day + third_day
print(f'Money needed: {all_sum:.2f}')
