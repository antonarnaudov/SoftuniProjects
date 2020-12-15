elements = []


def solve(num):
    if num == 100:
        elements.append('%' * 10)
        return f'{num}% Complete!'
    else:
        rez = int(num / 10)
        rez_two = 10 - rez
        percent = '%' * rez
        dots = '.' * rez_two
        elements.append(percent + dots)
        return f"{num}% [{''.join(elements)}]"


number = int(input())
print(solve(number))

if number == 100:
    print(f"[{''.join(elements)}]")
else:
    print('Still loading...')