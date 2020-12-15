info = input().split(' ')

for i in info:
    # first_letter = chr(int(''.join([n for n in i if n.isdigit()])))
    first_letter = [n for n in i if n.isdigit()]
    first_letter = ''.join(first_letter)
    first_letter = int(first_letter)
    first_letter = chr(first_letter)
    letters = [c for c in i if c.isalpha()]
    letters[0], letters[-1] = letters[-1], letters[0]
    letters = ''.join(letters)
    word = first_letter + letters
    print(word, end=' ')
# end='' e za print na edin red
