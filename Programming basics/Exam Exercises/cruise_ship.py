# input
cruise_type = input()
cabin_type = input()
days = int(input())

# definition of variables

holiday_price = 0
cabin_price = 0
family_members = 4
final_price = 0

# code functions
if cruise_type == 'Mediterranean':
    if cabin_type == 'standard cabin':
        cabin_price = 27.50
    elif cabin_type == 'cabin with balcony':
        cabin_price = 30.20
    elif cabin_type == 'apartment':
        cabin_price = 40.50
elif cruise_type == 'Adriatic':
    if cabin_type == 'standard cabin':
        cabin_price = 22.99
    elif cabin_type == 'cabin with balcony':
        cabin_price = 25.00
    elif cabin_type == 'apartment':
        cabin_price = 34.99
elif cruise_type == 'Aegean':
    if cabin_type == 'standard cabin':
        cabin_price = 23.00
    elif cabin_type == 'cabin with balcony':
        cabin_price = 26.60
    elif cabin_type == 'apartment':
        cabin_price = 39.80
holiday_price = cabin_price * family_members * days

if days > 7:
    holiday_price = holiday_price - holiday_price * 0.25

print(f"Annie's holiday in the {cruise_type} sea costs {holiday_price:.2f} lv.")