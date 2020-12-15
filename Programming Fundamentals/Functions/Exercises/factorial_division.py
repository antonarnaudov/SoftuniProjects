from math import factorial


def result(a, b):
    fact_a = factorial(a)
    fact_b = factorial(b)

    return f'{fact_a / fact_b:.2f}'


first_num = int(input())
second_num = int(input())

print(result(first_num, second_num))

# ================================================================================================================= #

# def result(a, b):
#     def factorial_a(a):
#         fact_a = 1
#         for i in range(1, a + 1):
#             fact_a = fact_a * i
#         return fact_a
#
#     def factorial_b(b):
#         fact_b = 1
#         for e in range(1, b + 1):
#             fact_b = fact_b * e
#         return fact_b
#
#     return f'{factorial_a(a) / factorial_b(b):.2f}'
#
#
# first_num = int(input())
# second_num = int(input())
#
# print(result(first_num, second_num))
