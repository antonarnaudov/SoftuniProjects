words = input().split(', ')
length = [f'{word} -> {len(word)}' for word in words]
for word in length:
    if word == length[-1]:
        print(word)
        break
    print(word, end=', ')
