text = input()
numbers = ''
letters = ''
chars = ''
for i in text:
    if i.isdigit():
        numbers += i
    elif i.isalpha():
        letters += i
    else:
        chars += i
print(numbers)
print(letters)
print(chars)
