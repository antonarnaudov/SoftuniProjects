nums = [float(x) for x in input().split()]
counter = {}
for n in nums:
    if n not in counter:
        counter[n] = 0
    counter[n] += 1
for key, value in counter.items():
    print(f'{key} - {value} times')
