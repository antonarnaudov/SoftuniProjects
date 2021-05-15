def multiply(ll):
    # Multiply elements one by one
    res = 1
    for x in ll:
        res *= x
    return res


summary = 0

while True:
    name = input()
    if name == 'stop':
        break

    nums = input().split(', ')
    nums = [int(x) for x in nums]

    result = []
    for x in nums:
        ll = nums.copy()
        ll.remove(x)
        result.append(multiply(ll))
    summary += sum(result)
    print(f'{name} has a bonus of {sum(result)} lv.')

print(f'The amount of all bonuses is {summary} lv.')
