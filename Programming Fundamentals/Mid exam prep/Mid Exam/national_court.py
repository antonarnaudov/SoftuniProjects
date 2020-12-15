employee_one = int(input())  # efficiency
employee_two = int(input())
employee_three = int(input())
people_count = int(input())

# employee_count = 3
efficiency_sum = employee_one + employee_two + employee_three
people = people_count
hours = 0
while True:
    if people > efficiency_sum:
        people -= efficiency_sum
        hours += 1
        if hours % 4 == 0:
            hours += 1
    else:
        hours += 1
        if hours % 4 == 0:
            hours += 1
        break
print(f'Time needed: {hours}h.')
