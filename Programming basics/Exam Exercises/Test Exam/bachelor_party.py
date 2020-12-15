guest_player_price = int(input())

income = 0
guests_count = 0
reservation_price = 0
guest_player = False

people_count = input()
while people_count != 'The restaurant is full':
    people_count = int(people_count)

    if people_count < 5:
        reservation_price = people_count * 100
        income += reservation_price
        guests_count += people_count
    elif people_count >= 5:
        reservation_price = people_count * 70
        income += reservation_price
        guests_count += people_count

    if income >= guest_player_price:
        guest_player = True

    people_count = input()

if guest_player:
    money_left = income - guest_player_price
    print(f"You have {guests_count} guests and {money_left:.0f} leva left.")
else:
    print(f"You have {guests_count} guests and {income:.0f} leva income, but no singer.")