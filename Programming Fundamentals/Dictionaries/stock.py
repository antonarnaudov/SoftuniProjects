def first(products):
    for i in range(0, len(products), 2):
        key = products[i]
        value = products[i + 1]
        bakery[key] = int(value)
    return bakery


def second(searched):
    for product in searched:
        if product in bakery:
            print(f'We have {bakery[product]} of {product} left')
        else:
            print(f"Sorry, we don't have {product}")


a = input().split(' ')
b = input().split(' ')
bakery = {}
first(a)
second(b)
