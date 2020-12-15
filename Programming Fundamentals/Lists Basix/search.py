lines_loop = int(input())
key_word = input()
list_words = []

for n in range(lines_loop):
    current_string = input()
    list_words.append(current_string)

print(list_words)

for i in range(len(list_words) - 1, -1, -1):
    element = list_words[i]

    if key_word not in element:
        list_words.remove(element)

print(list_words)