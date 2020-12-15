luggage_width = int(input())
luggage_hight = int(input())
luggage_depth = int(input())
ticket_type = input()

luggage_size = luggage_width * luggage_hight * luggage_depth
no_tax = False
luggage_tax = 0
if luggage_size <= 50:
    no_tax = True
    luggage_tax = 0

if ticket_type == 'true' and not no_tax:
    if 50 < luggage_size <= 100:
        luggage_tax = 0
    elif 100 < luggage_size <= 200:
        luggage_tax = 10
    elif 200 < luggage_size <= 300:
        luggage_tax = 20
elif ticket_type == 'false' and not no_tax:
    if 50 < luggage_size <= 100:
        luggage_tax = 25
    elif 100 < luggage_size <= 200:
        luggage_tax = 50
    elif 200 < luggage_size <= 300:
        luggage_tax = 100

print(f'Luggage tax: {luggage_tax:.2f}')