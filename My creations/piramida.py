# брой редове които ще вкараме

lastNumber = int(input("Please enter the number: "))

if 3 < lastNumber < 20:

    for num in range(1, lastNumber + 1):
        if 2 < num < lastNumber:
            dots_count = num - 2
            dots = '.' * dots_count
            print(f'*{dots}*')
        else:
            stars = '*' * num
            print(stars)
            # for column in range(num):
            #     print("*", end='')  # print number
        # print()
else:
    print("Елемента не премина проверката. Излизаме от програмата")
