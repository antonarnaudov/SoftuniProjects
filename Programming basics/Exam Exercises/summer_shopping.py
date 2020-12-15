budget = int(input())
towel_price = float(input())
discount = int(input())

discount = discount / 100
umbrella_price = 2/3 * towel_price
flip_flops_price = 0.75 * umbrella_price
bag_price = 1/3 * (towel_price + flip_flops_price)
price_sum = towel_price + umbrella_price + flip_flops_price + bag_price

discounted_price = price_sum * discount

Final_price = price_sum - discounted_price
if budget >= Final_price:
    print(f"Annie's sum is {Final_price:.2f} lv. She has {budget - Final_price:.2f} lv. left.")
if Final_price > budget:
    print(f"Annie's sum is {Final_price:.2f} lv. She needs {Final_price - budget:.2f} lv. more.")