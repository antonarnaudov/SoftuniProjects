text = input().split(' ')
new_text = ''
for word in text:
    length = len(word)
    new_text += word * length
print(new_text)
