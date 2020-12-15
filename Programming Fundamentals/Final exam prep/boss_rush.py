import re

number = int(input())
regex = r'\|([A-Z]{4,})\|\:\#([A-Za-z]+[ ][A-Za-z]+)\#'
# the whole regex is index 0
# the first () is index 1
# the second () is index 2

for _ in range(number):
    text = input()
    match = re.match(regex, text)
    if match is None:
        print('Access denied!')
        continue
    print(f'{match[1]}, The {match[2]}')
    print(f'>> Strength: {len(match[1])}')
    print(f'>> Armour: {len(match[2])}')

# text = text.split(':')
# name = text[0].strip('|')
# title = text[1].strip('#')
# print(f'{name}, The {title}')
# print(f'>> Strength: {len(name)}')
# print(f'>> Armour: {len(title)}')
