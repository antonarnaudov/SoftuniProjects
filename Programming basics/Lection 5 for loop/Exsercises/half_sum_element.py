from sys import maxsize
numbers_count = int(input())
sum_numbers = 0
max_num = -maxsize
for i in range(numbers_count):
    current_num = int(input())
    if current_num > max_num:
        max_num = current_num
    sum_numbers += current_num
sum_numbers -= max_num
if sum_numbers == max_num:
    print('Yes')
    print(f'Sum = {sum_numbers}')
else:
    print('No')
    print(f'Diff = {abs(max_num - sum_numbers)}')