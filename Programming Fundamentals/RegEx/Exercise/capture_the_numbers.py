import re

regex = '[0-9]+'
result = []
while True:
    text = input()
    if not text:  # if text == '':
        break
    result += re.findall(regex, text)
print(' '.join(result))
