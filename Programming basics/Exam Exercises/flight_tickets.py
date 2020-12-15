from sys import maxsize

min_stay = maxsize
current_ticket_price = 0
min_stay_ticket = 0
stay = 0

ticket_number = input()

while ticket_number != 'End':
    ticket_price = float(input())
    stay = int(input())
    lev = ticket_price * 1.96

    if stay < min_stay:
        min_stay_ticket = ticket_number
        min_stay = stay
        current_ticket_price = lev

    ticket_number = input()

hours = min_stay // 100
if hours >= 1:
    minutes = min_stay - hours * 60
else:
    minutes = min_stay % 100
if minutes > 59:
    hours += 1
    minutes = 0
print(f"Ticket found for flight {min_stay_ticket} costs {current_ticket_price:.2f} leva with {hours}h {minutes}m stay")

# n = int(s)
# hours = n // 100  # Truncating integer division
# minutes = n % 100