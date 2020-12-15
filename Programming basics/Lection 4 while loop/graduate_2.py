name = input()

grades_counter = 1
grades_sum = 0
exclude_counter = 0
excluded = False
while grades_counter <= 12:
    current_grade_final_mark = float(input())
    if current_grade_final_mark >= 4:
        #print(f'completed grade №:{grades_counter}')
        grades_counter += 1
        grades_sum += current_grade_final_mark
    elif current_grade_final_mark < 4:
        exclude_counter += 1
        if exclude_counter > 1:
            print(f'{name} has been excluded at {grades_counter} grade')
            excluded = True
            break
if not excluded:
    average_grade = grades_sum / 12
    print(f'{name} graduated. Average grade: {average_grade:.2f}')