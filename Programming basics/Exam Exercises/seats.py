# read tickets count
# iterate through all tickets
# read ticket number value
# get ticket number length
# compare character's count
tickets_count = int(input())

for ticket in range(tickets_count):

    ticket_number = input()
    ticket_number_length = len(ticket_number)

    if ticket_number_length == 4:
        first_character = ticket_number[0]
        first_character_ascii = ord(first_character)

        if 65 <= first_character_ascii <= 90:
            print(f'Seat decoded: {ticket_number[0]}{ticket_number[1]}{ticket_number[2]}')
        else:
            print(f'Seat decoded: {ticket_number[3]}{ticket_number[1]}{ticket_number[2]}')

    elif ticket_number_length == 5 or ticket_number_length == 6:
        second_character_ascii = ord(ticket_number[1])
        print(f'Seat decoded: {ticket_number[0]}{second_character_ascii}')
