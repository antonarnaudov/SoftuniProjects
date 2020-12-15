number = int(input())
dictionary = {}
counter = {}
for _ in range(number):
    name = input()
    grade = float(input())
    if name not in dictionary:
        dictionary[name] = grade
        counter[name] = 1
    else:
        dictionary[name] += grade
        counter[name] += 1

for key in dictionary.keys():
    dictionary[key] /= counter[key]

dictionary = dict(sorted(dictionary.items(), key=lambda x: -x[1]))

# average_grades = {k: sum(v) / len(v) for k, v in students.items() if sum(v) / len(v) >= 4.5}

for x, y in dictionary.items():
    if y >= 4.50:
        print(f'{x} -> {y:.2f}')
