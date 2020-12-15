text = input()
sum_non_prime = 0
sum_prime = 0
while text != 'stop':
    current_num = int(text)
    if current_num < 0:
        print('Number is negative.')
        text = input()
        continue
    is_prime = True
    for i in range(2, current_num // 2 + 1):
# If num is divisible by any number between
# 2 and n / 2, it is not prime
        if (current_num % i) == 0:
            is_prime = False
            break
    if is_prime:
        sum_prime += current_num
    else:
        sum_non_prime += current_num
    text = input()
print(f"Sum of all prime numbers is: {sum_prime}")
print(f"Sum of all non prime numbers is: {sum_non_prime}")