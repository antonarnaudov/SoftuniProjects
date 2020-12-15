factor = int(input())
count = int(input())

numbers_list = []
counter = 1
result = 0
while counter <= count:
    result = factor * counter
    numbers_list.append(result)
    counter += 1
print(numbers_list)