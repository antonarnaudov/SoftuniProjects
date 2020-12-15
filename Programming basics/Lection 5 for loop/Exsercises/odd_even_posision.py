from sys import maxsize
numbers_count = int(input())

odd_sum = 0
odd_max = -maxsize - 1
odd_min = maxsize

even_sum = 0
even_max = -maxsize - 1
even_min = maxsize

for position in range(1, numbers_count + 1):
    current_num = float(input())
    if position % 2 == 0:
        even_sum += current_num
        if current_num > even_max:
            even_max = current_num
        if current_num < even_min:
            even_min = current_num
    else:
        odd_sum += current_num

        if current_num > odd_max:
            odd_max = current_num

        if current_num < odd_min:
            odd_min = current_num

print(f'OddSum={odd_sum:.2f},')
if odd_min == maxsize:
    print(f'OddMin=No,')
    print(f'OddMax=No,')
else:
    print(f'OddMin={odd_min:.2f},')
    print(f'OddMax={odd_max:.2f},')

print(f'EvenSum={even_sum:.2f},')
if even_min == maxsize:
    print('EvenMin=No,')
    print('EvenMax=No')
else:
    print(f'EvenMin={even_min:.2f},')
    print(f'EvenMax={even_max:.2f}')