dicts = {}

while True:
    a = input().split(' ')
    name = a[0]
    if name == 'stop':
        # dicts formatting
        print("\n".join("{} -> {}".format(k, v) for k, v in dicts.items()))
        break
    number = int(a[1])

    if name in dicts:
        # add to dict's values or increase
        dicts[name] += number
    else:
        dicts.update({name: number})

# print("\n".join("{}\t{}".format(k, v) for k, v in dicts.items()))
