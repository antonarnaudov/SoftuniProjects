contract_duration = input()
contract_type = input()
dessert = input()
months_count = int(input())

months_payment = 0

dessert_added = False
if dessert == 'yes':
    dessert_added = True

if contract_duration == 'one':
    if contract_type == 'Small':
        months_payment = 9.98
    elif contract_type == 'Middle':
        months_payment = 18.99
    elif contract_type == 'Large':
        months_payment = 25.98
    elif contract_type == 'ExtraLarge':
        months_payment = 35.99
elif contract_duration == 'two':
    if contract_type == 'Small':
        months_payment = 8.58
    elif contract_type == 'Middle':
        months_payment = 17.09
    elif contract_type == 'Large':
        months_payment = 23.59
    elif contract_type == 'ExtraLarge':
        months_payment = 31.79

if dessert_added:
    if months_payment <= 10:
        months_payment += 5.50
    elif months_payment <= 30:
        months_payment += 4.35
    elif months_payment > 30:
        months_payment += 3.85
all_sum = months_payment
if contract_duration == 'two':
    all_sum = all_sum - all_sum * 0.0375
all_sum = all_sum * months_count
print(f'{all_sum:.2f} lv.')