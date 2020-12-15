budget = float(input())
season = input()

destination = ''
place = ''
expenses = 0


if budget <= 100:
    destination = 'Bulgaria'
    if season == 'summer':
        expenses = budget * 0.30
    if season == 'winter':
        expenses = budget * 0.70
elif budget <= 1000:
    destination = 'Balkans'
    if season == 'summer':
        expenses = budget * 0.40
    if season == 'winter':
        expenses = budget * 0.80
else:
    destination = 'Europe'
    expenses = budget * 0.90

#and destination == 'Bulgaria' or destination == 'Balkans':


if destination == 'Europe':
    place = 'Hotel'
elif season == 'summer':
    if destination == 'Bulgaria' or destination == 'Balkans':
        place = 'Camp'
elif season == 'winter':
    if destination == 'Bulgaria' or destination == 'Balkans':
        place = 'Hotel'


print(f'Somewhere in {destination}')
print(f'{place} - {expenses:.2f}')