championship_part = input()
ticket_type = input()
tickets_count = int(input())
trophy_pic = input()
one_ticket_price = 0
if trophy_pic == 'Y':
    trophy_pic_price = 40
else:
    trophy_pic_price = 0

if championship_part == 'Quarter final':
    if ticket_type == 'Standard':
        one_ticket_price = 55.50
    elif ticket_type == 'Premium':
        one_ticket_price = 105.20
    elif ticket_type == 'VIP':
        one_ticket_price = 118.90

elif championship_part == 'Semi final':
    if ticket_type == 'Standard':
        one_ticket_price = 75.88
    elif ticket_type == 'Premium':
        one_ticket_price = 125.22
    elif ticket_type == 'VIP':
        one_ticket_price = 300.40

elif championship_part == 'Final':
    if ticket_type == 'Standard':
        one_ticket_price = 110.10
    elif ticket_type == 'Premium':
        one_ticket_price = 160.66
    elif ticket_type == 'VIP':
        one_ticket_price = 400

all_tickets_price = one_ticket_price * tickets_count

if all_tickets_price > 4000:
    final_price = all_tickets_price - all_tickets_price * 0.25
    trophy_pic_price = 0
    print(f'{final_price:.2f}')
elif all_tickets_price > 2500:
    final_price = (all_tickets_price - all_tickets_price * 0.10) + (trophy_pic_price * tickets_count)
    print(f'{final_price:.2f}')
else:
    final_price = all_tickets_price + (trophy_pic_price * tickets_count)
    print(f'{final_price:.2f}')
