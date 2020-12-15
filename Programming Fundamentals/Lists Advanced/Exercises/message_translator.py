import re

number = int(input())
regex = r'![A-Z]{1,}[a-z]{2,}!:\[[a-zA-Z]{8,}\]'

for _ in range(number):
    text = input()
    if re.match(regex, text):
        text = text.split(':')
        command = text[0].strip('!')
        code = text[1].strip('[]')
        print(f'{command}:', end=' ')
        for i in code:
            print(f'{ord(i)}', end=' ')
        print()
    else:
        print('The message is invalid')
