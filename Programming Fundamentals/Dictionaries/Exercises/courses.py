data = {}

while True:
    tokens = input()
    if tokens == 'end':
        break
    else:
        tokens = tokens.split(' : ')
    course = tokens[0]
    names = tokens[1]
    if course not in data:
        data[course] = [names]
    else:
        data[course] += [names]

data = dict(sorted(data.items(), key=lambda x: -len(x[1])))
data = {x: sorted(data[x]) for x in data.keys()}

for x, y in data.items():
    print(f'{x}: {len(y)}')
    for i in y:
        print(f'-- {i}')
