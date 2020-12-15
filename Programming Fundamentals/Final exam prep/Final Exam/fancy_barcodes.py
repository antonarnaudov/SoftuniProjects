import re

regex = r"\@+\#+[A-Z]{1}[a-zA-Z0-9]{4,}[A-Z]{1}\@+\#+"
number = int(input())

for _ in range(number):
    product = input()
    product_groups = ''
    match = re.match(regex, product)

    if match is None:
        print('Invalid barcode')
        continue

    for i in product:
        if i.isdigit():
            product_groups += f'{i}'
    if product_groups == '':
        print(f'Product group: 00')
    else:
        print(f'Product group: {product_groups}')
