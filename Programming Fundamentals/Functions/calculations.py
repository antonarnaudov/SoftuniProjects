input_operator = input()
input_a = int(input())
input_b = int(input())


def solve(operator, a, b):
    if operator == 'multiply':
        return a * b
    elif operator == 'divide':
        return int(a / b)
    elif operator == 'add':
        return a + b
    elif operator == 'subtract':
        return a - b


print(solve(input_operator, input_a, input_b))
