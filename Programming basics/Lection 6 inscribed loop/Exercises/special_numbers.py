n = int(input())

for firstDigit in range(1, 10):
    for secondDigit in range(1, 10):
        for thirdDigit in range(1, 10):
            for fourthDigit in range(1, 10):
                if n % firstDigit == 0 and n % secondDigit == 0 and n % thirdDigit == 0 and n % fourthDigit == 0:
                    print(f"{firstDigit}{secondDigit}{thirdDigit}{fourthDigit} ", end='')