income_wanted = float(input())
drink_name = input()
drinks_num = int(input())

final_sum = 0
income_sum = 0
while drink_name != 'Party!':
    counter = 0
    for letters in drink_name:
        counter += 1

    final_sum = counter * drinks_num

    if final_sum % 2 != 0:
        final_sum = final_sum - final_sum * 0.25

    income_sum += final_sum
    if income_sum >= income_wanted:
        break
    drink_name = input()
    if drink_name != 'Party!':
        drinks_num = int(input())

money_needed = income_wanted - income_sum
if drink_name == 'Party!':
    print(f"We need {money_needed:.2f} leva more.")
elif income_wanted <= income_sum:
    print(f'Target acquired.')
print(f'Club income - {income_sum} leva.')