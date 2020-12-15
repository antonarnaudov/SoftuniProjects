employee_one = int(input())
employee_two = int(input())
employee_three = int(input())
people_count = int(input())

all_employees = employee_one + employee_two + employee_three # this many per hour

people_answered = 0
hours_needed =0
while people_answered < people_count:

    hours_needed += 1
    if hours_needed % 4 == 0:
        people_answered += 0
    else:
        people_answered += all_employees

print('Time needed: {}h.'.format(hours_needed))