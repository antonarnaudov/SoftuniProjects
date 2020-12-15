input_num = input()
for digit in reversed(input_num):
    num = int(digit)
    for i in range(num):
        if num != 0:
            symbol = chr(num + 33)
            print(symbol, end='')
    if num == 0:
        print('ZERO')
    else:
        print()