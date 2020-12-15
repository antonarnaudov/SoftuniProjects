def result(elements):
    bakery = {}

    for i in range(0, len(elements), 2):
        key = elements[i]
        value = elements[i + 1]
        bakery[key] = int(value)
    return bakery


tokens = input().split(' ')

print(result(tokens))