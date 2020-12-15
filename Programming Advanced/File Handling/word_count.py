import re

path = '08-File-Handling-Lab-Resources'
regex = '[a-zA-Z]+'
words_dict = {}

with open(path + '/Words Count/words.txt', 'r') as file:
    words = file.read().split()
    for word in words:
        words_dict[word] = 0

with open(path + '/Words Count/text.txt', 'r') as file:
    text = file.read()
    text = [x.lower() for x in re.findall(regex, text)]

for key in words_dict.keys():
    for word in text:
        if key == word.lower():
            words_dict[key] += 1


words_sorted = sorted(words_dict.items(), key=lambda x: -x[1])

[print(f'{key} - {value}') for (key, value) in words_sorted]
