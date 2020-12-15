info_list = input().split('#')
water = int(input())

effort = 0
total_fire = 0

print('Cells:')
for i in info_list:
    info = i.split(' = ')
    fire_type = info[0]
    amount = int(info[1])

    if fire_type == 'High':
        if 81 <= amount <= 125:
            if water >= amount:
                print(f' - {amount}')
                water -= amount
                total_fire += amount
                effort += amount * 0.25
    if fire_type == 'Medium':
        if 51 <= amount <= 80:
            if water >= amount:
                print(f' - {amount}')
                water -= amount
                total_fire += amount
                effort += amount * 0.25
    if fire_type == 'Low':
        if 1 <= amount <= 50:
            if water >= amount:
                print(f' - {amount}')
                water -= amount
                total_fire += amount
                effort += amount * 0.25

print(f'Effort: {effort:.2f}')
print(f'Total Fire: {total_fire}')

