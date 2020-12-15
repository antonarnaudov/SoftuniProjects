nums = int(input())
grades = {}

for _ in range(nums):
    tokens = input().split()
    name = tokens[0]
    grade = float(tokens[1])
    if name not in grades:
        grades[name] = [grade]
    else:
        grades[name].append(grade)

for names, grade in grades.items():
    number = 0
    for gr in grade:
        number += gr
    average = number / len(grade)

    print(f"{names} -> {' '.join(f'{g:.2f}' for g in grade)} (avg: {average:.2f})")

# " ".join(f'{a:.2f}' for a in x)
