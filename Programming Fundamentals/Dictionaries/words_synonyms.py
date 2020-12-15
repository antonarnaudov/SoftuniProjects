from _collections import defaultdict

words_with_synonyms = defaultdict(list)

n = int(input()) * 2

for _ in range(n):
    word = input()
    synonym = input()
    words_with_synonyms[word].append(synonym)

for word in words_with_synonyms.items():
    print(f'{word} - {", ".join(synonym)}')