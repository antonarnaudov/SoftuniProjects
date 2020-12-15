def result(numbers):
    print(f'The minimum number is {min(numbers)}')
    print(f'The maximum number is {max(numbers)}')
    print(f'The sum number is: {sum(numbers)}')


result([int(i) for i in input().split()])
