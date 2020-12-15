a = input()

length = len(a) - 1
power = 2 ** length
result = 0

for i in a:
    result += int(i) * power
    length -= 1
    power = 2 ** length
print(result)
