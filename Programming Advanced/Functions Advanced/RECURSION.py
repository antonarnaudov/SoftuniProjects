print('RECURSION')


def func(n):
    # base case
    if n == 0:
        return
    print(n)

    # recursive call
    func(n - 1)


func(5)

print()
print('FIBONACCI')


def fib(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fib(n - 1) + fib(n - 2)


[print(fib(x)) for x in range(10)]
