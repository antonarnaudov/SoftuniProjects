name = input()
max_sum = 0
max_name = ''
while name != 'STOP':
    # name = input()
    sum_name = 0
    for letters in name:
        sum_name += ord(letters)
    if sum_name > max_sum:
        max_sum = sum_name
        max_name = name
    name = input()
print(f'Winner is {max_name} - {max_sum}!')