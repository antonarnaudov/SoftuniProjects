poor_grades_count = int(input())

counter_bad_grades = 0
sum_grades = 0
tasks_counter = 0
last_problem_name = ''
average_grade = 0
stopped = True

while poor_grades_count > counter_bad_grades:
    problem_name = input()
    if problem_name == 'Enough':
        print(f'Average score: {average_grade:.2f}')
        print(f'Number of problems: {tasks_counter}')
        print(f'Last problem: {last_problem_name}')
        stopped = False
        break
    grade = int(input())
    if grade <= 4:
        counter_bad_grades += 1
    sum_grades += grade
    tasks_counter += 1
    last_problem_name = problem_name
    average_grade = sum_grades / tasks_counter
if stopped:
    print(f'You need a break, {counter_bad_grades} poor grades.')