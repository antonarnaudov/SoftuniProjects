from math import ceil
people_count = int(input())
tax = float(input())
seat_price = float(input())
umbrella_price = float(input())

tax_sum = people_count * tax
percent_of_seats = ceil(people_count * 0.75)
price_per_seats = percent_of_seats * seat_price
umbrella_count = ceil(people_count * 0.50)
umbrella_price_sum = umbrella_count * umbrella_price
final_price = tax_sum + price_per_seats + umbrella_price_sum
print(f'{final_price:.2f} lv.')