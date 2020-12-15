def aliquit_sum(n):
    summary = 0
    for i in range(1, n):
        if n % i == 0:
            summary += i
    if summary == n:
        return 'We have a perfect number!'
    else:
        return "It's not so perfect."


number = int(input())
print(aliquit_sum(number))