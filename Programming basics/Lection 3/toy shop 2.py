holiday_price = float(input())

puzzels_count = int(input())
dolls_count = int(input())
bears_count = int(input())
minions_count = int(input())
trucks_count = int(input())

cash = puzzels_count * 2.60 + dolls_count * 3 + bears_count * 4.10 + minions_count * 8.20 + trucks_count * 2
toys_count = puzzels_count+dolls_count+bears_count+minions_count+trucks_count

if toys_count >= 50:
    cash = cash - (cash*0.25)

cash = cash - (cash*0.10)

result = abs(cash - holiday_price)

if cash >= holiday_price:
    print(f'Yes! {result:.2f} lv left.')
else:
    print(f'Not enough money! {result:.2f} lv needed.')
