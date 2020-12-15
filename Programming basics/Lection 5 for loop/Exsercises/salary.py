open_tabs_count = int(input())
salary = int(input())

salary_lost = False

for i in range(open_tabs_count):
    open_tab = input()
    if open_tab == 'Facebook':
        salary -= 150
    if open_tab == 'Instagram':
        salary -= 100
    if open_tab == 'Reddit':
        salary -= 50

    if salary <= 0:
        salary = 0
        salary_lost = True
        print('You have lost your salary.')
        break

if not salary_lost:
    print(salary)