def odd_or_even(*args):
    command = args[0]
    numbers = args[1]
    if command == 'Odd':
        odd = list(filter(lambda x: x % 2 != 0, numbers))
        print(sum(odd) * len(numbers))
    else:
        even = list(filter(lambda x: x % 2 == 0, numbers))
        print(sum(even) * len(numbers))


odd_or_even(input(), [int(x) for x in input().split()])
