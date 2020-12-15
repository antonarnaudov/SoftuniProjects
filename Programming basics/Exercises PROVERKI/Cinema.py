projection_type = input()
rows = int(input())
columns = int(input())

income = 0
cinema_capacity = rows * columns
prem = 12.00
norm = 7.50
disc = 5.00

if projection_type == "Premiere":
    income = cinema_capacity * prem
elif projection_type == "Normal":
    income = cinema_capacity * norm
elif projection_type == "Discount":
    income = cinema_capacity * disc

print(f'{income:.2f}')
