def letter_position(letter):
    letter = letter.upper()
    return ord(letter) - 64


tokens = input().split()
result = 0
for i in tokens:
    current = 0
    first = i[0]
    last = i[-1]
    num = int(i[1:-1])

    if first.isupper():
        current = num / letter_position(first)
    else:
        current = num * letter_position(first)

    if last.isupper():
        current -= letter_position(last)
    else:
        current += letter_position(last)
    result += current

print(f'{result:.2f}')
