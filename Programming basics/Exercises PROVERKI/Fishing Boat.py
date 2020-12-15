budget = int(input())
season = input()
fisherman_count = int(input())

boat_price = 0

if season == 'Spring':
    boat_price = 3000
elif season == 'Summer' or season == 'Autumn':
    boat_price = 4200
elif season == 'Winter':
    boat_price = 2600

discount = 0

if fisherman_count <= 6:
    discount = 0.1
elif fisherman_count <= 11:
    discount = 0.15
else:
    discount = 0.25

discount_value = boat_price * discount
expenses = boat_price - discount_value

if fisherman_count % 2 == 0 and season != 'Autumn':
    expenses = expenses * 0.95

if budget >= expenses:
    print(f'Yes! You have {(budget - expenses):.2f} leva left.')
else:
    print(f"Not enough money! You need {(expenses - budget):.2f} leva.")






