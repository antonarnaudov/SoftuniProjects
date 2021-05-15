n = int(input())
m = int(input())
prime = []


def is_prime(x):
    if x <= 1:
        return False
    else:
        for i in range(2, x):
            # checking for factor
            if x % i == 0:
                # return False
                return False
        # returning True
    return True


for x in range(n, m + 1):
    if is_prime(x):
        prime.append(x)

print(' '.join([str(x) for x in prime]))
print(f"The total number of prime numbers between {n} to {m} is {len(prime)}")
