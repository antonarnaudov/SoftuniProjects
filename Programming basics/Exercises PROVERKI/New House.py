flower_type = input()
flower_count = int(input())
budget = int(input())

roses_price = 5
dahlias_price = 3.80
tulips_price = 2.80
narcissus_price = 3
gladiouls_price = 2.50

final_price = 0

if flower_type == 'Roses':
    final_price = flower_count * roses_price
elif flower_type == 'Dahlias':
    final_price = flower_count * dahlias_price
elif flower_type == 'Tulips':
    final_price = flower_count * tulips_price
elif flower_type == 'Narcissus':
    final_price = flower_count * narcissus_price
elif flower_type == 'Gladiolus':
    final_price = flower_count * gladiouls_price


if flower_count > 80 and flower_type == 'Roses':
    final_price = final_price - final_price * 0.1
elif flower_count > 90 and flower_type == 'Dahlias':
    final_price = final_price - final_price * 0.15
elif flower_count > 80 and flower_type == 'Tulips':
    final_price = final_price - final_price * 0.15
elif flower_count < 120 and flower_type == 'Narcissus':
    final_price = final_price * 1.15
elif flower_count < 80 and flower_type == 'Gladiolus':
    final_price = final_price *1.12

if budget < final_price:
    print(f'Not enough money, you need {abs(budget - final_price):.2f} leva more.')
elif budget >= final_price:
    print(f'Hey, you have a great garden with {flower_count} {flower_type} and {abs(budget - final_price):.2f} leva left.')