banned = input().split(', ')
text = input()

for word in banned:
    while word in text:
        length = len(word)
        asterisk = '*' * length
        text = text.replace(word, asterisk)
print(text)
