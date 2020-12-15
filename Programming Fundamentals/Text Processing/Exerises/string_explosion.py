text = list(input())
numbers = 0
i = 0
while i < len(text):
    c = text[i]
    if text[i].isdigit():
        numbers += int(text[i]) - 1
        text.pop(i)
        i -= 1
        continue
    if text[i].isalpha() and text[i - 1] == '>':
        for r in range(numbers):
            text.pop(i)
            numbers = 0
        continue
    i += 1
print(''.join(text))
