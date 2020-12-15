jury = int(input())
presentation_name = input()
grades_counter = 0
final_grade = 0
current_grade_counter = 0
all_grades_counter = 0

while presentation_name != 'Finish':
    while jury > grades_counter:
        current_grade = float(input())
        current_grade_counter += current_grade
        grades_counter += 1

        all_grades_counter += 1
        final_grade += current_grade
    current_grade_counter = current_grade_counter / grades_counter
    print(f'{presentation_name} - {current_grade_counter:.2f}.')
    current_grade_counter = 0
    grades_counter = 0
    presentation_name = input()

final_grade = final_grade / all_grades_counter
print(f"Student's final assessment is {final_grade:.2f}.")