income = float(input())
middle_grade = float(input())
minimal_payment = float(input())

scholarship = 0
if income < minimal_payment and middle_grade > 4.50:
    scholarship = minimal_payment * 0.65
elif middle_grade <= 5.50:
    scholarship = middle_grade * 25
