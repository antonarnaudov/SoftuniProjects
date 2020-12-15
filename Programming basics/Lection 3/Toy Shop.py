holiday_price = float(input())

puzzels_count = int(input())
dolls_count = int(input())
bears_count = int(input())
minions_count = int(input())
trucks_count = int(input())

result = puzzels_count * 2.60 + dolls_count * 3 + bears_count * 4.10 + minions_count * 8.20 + trucks_count * 2
toys_count = puzzels_count + dolls_count + bears_count + minions_count + trucks_count

if toys_count >= 50:
    result = result - (result * 0.25)

result = result - result * 0.10

diff = abs(result - holiday_price)

if result >= holiday_price:
    print(f'Yes! {diff:.2f} lv left.')
else:
    print(f'Not enough money! {diff:.2f} lv needed.')
