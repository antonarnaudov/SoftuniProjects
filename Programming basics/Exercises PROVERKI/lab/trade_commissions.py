city = input()
sells_area = float(input())

commissions = 0

if city == 'Sofia':
    if 0 <= sells_area <= 500:
        commissions = sells_area * 0.05
    elif 500 <= sells_area <= 1000:
        commissions = sells_area * 0.07
    elif 1000 <= sells_area <= 10000:
        commissions = sells_area * 0.08
    elif sells_area > 10000:
        commissions = sells_area * 0.12
    else:
        print('error')
elif city == 'Varna':
    if 0 <= sells_area <= 500:
        commissions = sells_area * 0.045
    elif 500 <= sells_area <= 1000:
        commissions = sells_area * 0.075
    elif 1000 <= sells_area <= 10000:
        commissions = sells_area * 0.10
    elif sells_area > 10000:
        commissions = sells_area * 0.13
    else:
        print('error')
elif city == 'Plovdiv':
    if 0 <= sells_area <= 500:
        commissions = sells_area * 0.055
    elif 500 <= sells_area <= 1000:
        commissions = sells_area * 0.08
    elif 1000 <= sells_area <= 10000:
        commissions = sells_area * 0.12
    elif sells_area > 10000:
        commissions = sells_area * 0.145
    else:
        print('error')
else:
    print('error')
if commissions != 0:
    print(f'{commissions:.2f}')