student_name = input("Input student's name:")
subj_count = int(input("Enter subject's count:"))
subj_counter = 0
grades_sum = 0

print(f'Student {student_name}:')

while subj_count > subj_counter:
    current_subj = input("Input subject's name:")
    current_grade = float(input("Input subject's grade:"))
    if 5.50 <= current_grade <= 6:
        print(f'At subject {current_subj}')
        print(f'Has grade Perfect: {current_grade:.2f}')
        grades_sum += current_grade
        subj_counter += 1
    elif 4.50 <= current_grade < 5.50:
        print(f'At subject {current_subj}')
        print(f'Has grade Very good: {current_grade:.2f}')
        grades_sum += current_grade
        subj_counter += 1
    elif 3.50 <= current_grade < 4.50:
        print(f'At subject {current_subj}')
        print(f'Has grade Good: {current_grade:.2f}')
        grades_sum += current_grade
        subj_counter += 1
    elif 3 <= current_grade < 3.50:
        print(f'At subject {current_subj}')
        print(f'Has grade Average: {current_grade:.2f}')
        grades_sum += current_grade
        subj_counter += 1
    elif 2 <= current_grade < 3:
        print(f'At subject {current_subj}')
        print(f'Has grade Low: {current_grade:.2f}')
        grades_sum += current_grade
        subj_counter += 1
    else:
        print('Wrong grade')

average_grade = grades_sum / subj_count

if 5.50 <= average_grade <= 6:
    print(f'Student {student_name} has average grade of Perfect: {average_grade:.2f}')
elif 4.50 <= average_grade <= 5.50:
    print(f'Student {student_name} has average grade of Very good: {average_grade:.2f}')
elif 3.50 <= average_grade < 4.50:
    print(f'Student {student_name} has average grade of Good: {average_grade:.2f}')
elif 3 <= average_grade < 3.50:
    print(f'Student {student_name} has average grade of Average: {average_grade:.2f}')
elif 2 <= average_grade < 3:
    print(f'Student {student_name} has average grade of Low: {average_grade:.2f}')
