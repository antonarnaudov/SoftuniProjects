first_num = int(input())
second_num = int(input())

for num in range(first_num, second_num + 1):
    # 100 000
    current = str(num)

    even_sum = 0
    odd_sum = 0
    for index, digit in enumerate(current):
        if index % 2 == 0:
            odd_sum += int(digit)
        else:
            even_sum += int(digit)
    if odd_sum == even_sum:
        print(f'{current} ', end='')