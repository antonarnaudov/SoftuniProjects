dictionary = {}
one_bool = True
two_bool = True
one = ''
two = ''
while True:
    tokens = input()
    if tokens == 'Lumpawaroo':
        break
    elif '|' in tokens:
        tokens = tokens.split(' | ')
        force_side = tokens[0]
        force_user = tokens[1]
        if force_side not in dictionary:
            dictionary[force_side] = [force_user]
            if one_bool:
                one = force_side
                one_bool = False
            elif two_bool:
                two = force_side
                two_bool = False
        else:
            if force_user not in dictionary[force_side]:
                dictionary[force_side] += [force_user]

    elif '->' in tokens:
        tokens = tokens.split(' -> ')
        force_user = tokens[0]
        force_side = tokens[1]

        if force_side == one:
            if force_user in dictionary[two]:
                dictionary[two].remove(force_user)
                dictionary[one] += [force_user]
                print(f'{force_user} joins the {one} side!')
            else:
                dictionary[one] += [force_user]
                print(f'{force_user} joins the {force_side} side!')

        elif force_side == two:
            if force_user in dictionary[one]:
                dictionary[one].remove(force_user)
                dictionary[two] += [force_user]
                print(f'{force_user} joins the {two} side!')
            else:
                dictionary[two] += [force_user]
                print(f'{force_user} joins the {force_side} side!')

if len(dictionary[one]) == 0:
    del dictionary[one]
if len(dictionary[two]) == 0:
    del dictionary[two]
# dictionary = dict(sorted(dictionary.items(), key=lambda x: (-len(x[0]), -x[1])))

dictionary = dict(sorted(dictionary.items(), key=lambda x: -len(x[1])))
dictionary = {x: sorted(dictionary[x]) for x in dictionary.keys()}

for x, y in dictionary.items():
    print(f'Side: {x}, Members: {len(y)}')
    for i in y:
        print(f'! {i}')
