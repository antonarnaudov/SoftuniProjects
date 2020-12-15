dictionary = {}
while True:
    tokens = input()
    if tokens == 'End':
        break
    tokens = tokens.split(' -> ')
    company = tokens[0]
    user_id = tokens[1]

    if company not in dictionary:
        if user_id not in dictionary:
            dictionary[company] = [user_id]
    else:
        if user_id not in dictionary[company]:
            dictionary[company] += [user_id]

dictionary = dict(sorted(dictionary.items(), key=lambda x: x[0]))
for x, y in dictionary.items():
    print(x)
    for i in y:
        print(f'-- {i}')
