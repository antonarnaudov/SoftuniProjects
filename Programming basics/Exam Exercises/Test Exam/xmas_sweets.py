baklava_price = float(input())
muffin_price = float(input())
shtolen_kg = float(input())
candy_kg = float(input())
bisquits_kg = int(input())

shtolen_price = baklava_price + baklava_price * 0.6
candy_price = muffin_price + muffin_price * 0.8
busquits_price = 7.50
shtolen_sum = shtolen_kg * shtolen_price
candy_sum = candy_kg * candy_price
bisquits_sum = bisquits_kg * busquits_price
all_sum = shtolen_sum + candy_sum + bisquits_sum
print(f'{all_sum:.2f}')