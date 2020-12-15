def result(words):
    word_lower = ''
    for word in words:
        word_lower = word.lower()
    if word_lower not in dictionary:
        dictionary[word_lower] = 0
    dictionary[word_lower] += 1
    for (key, value) in dictionary.items():
        if value % 2 != 0:
            print(key, end=' ')


a = input().split(' ')
dictionary = {}
result(a)
# print(list(filter(lambda item: item[1] % 2 != 0, occurrences.items())))
# words = [w.lower() for w in imput.split]
