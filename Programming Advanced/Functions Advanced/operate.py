def operate(operator, *args):
    if operator == '+' or operator == '-':
        result = 0
    else:
        result = 1

    for n in args:
        result = eval(f'{result}{operator}{n}')
    return result


print(operate("+", 1, 2, 3))
print(operate("*", 3, 4))
