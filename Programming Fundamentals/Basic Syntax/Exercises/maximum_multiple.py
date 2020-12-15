divisor = int(input())
number = int(input())

result = 0

for i in range(1, number + 1):
    if i % divisor == 0:
        result = i

print(result)