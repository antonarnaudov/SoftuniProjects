input_num = input()

number_length = len(str(input_num))
number1 = input_num[0]
number2 = input_num[1]
number3 = input_num[2]

for n1 in range(1, int(number3) + 1):
    n1 = int(n1)
    for n2 in range(1, int(number2) + 1):
        n2 = int(n2)
        for n3 in range(1, int(number1) + 1):
            n3 = int(n3)
            sum = n1 * n2 * n3
            print(f'{n1} * {n2} * {n3} = {sum};')